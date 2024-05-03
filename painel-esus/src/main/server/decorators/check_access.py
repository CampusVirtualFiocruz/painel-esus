# pylint: disable=R1710
# pylint: disable=W0102
# pylint: disable=W0102
# pylint: disable=W9015
# pylint: disable=C0103
# pylint: disable=W0613
# pylint: disable=R0913
# pylint: disable=W0702
import collections
from functools import wraps
from typing import List, Union

from flask import request, jsonify
from src.errors import HttpForbiddenError, InvalidArgument

from .token_required import validate_token


def intersect(list1, list2):
    intersection = collections.Counter(list1) & collections.Counter(list2)
    return list(intersection.elements())


def check_access_fn(
    action: Union['ALLOW', 'DENNY'] = 'ALLOW',
    user_access=None,
    users_access=[],
    group_access=None,
    groups_access=[],
    request_=None
):
    if not request_:
        raise InvalidArgument('request must be passed.')
    token = request_.headers.get('Authorization')
    if token:
        try:
            token = token.split(' ')[1]
        except:
            token = None

    if not token:
        raise InvalidArgument('token not present.')

    parsed_token = validate_token(token)
    profiles = parsed_token['profiles']

    def _check_arg(arg: str, profiles):
        if arg is not None:
            if isinstance(arg, str) and arg in profiles and action == 'ALLOW':
                return True
            raise HttpForbiddenError('User access not granted')

    def _check_group(group: List[str], profiles):
        if group is not None:
            if isinstance(group, list) and action == 'ALLOW':
                intersects = intersect(users_access, list(profiles))
                if len(intersects) > 0:
                    return True
            raise HttpForbiddenError('User access not granted')

    if user_access:
        _check_arg(user_access, profiles)
    if group_access:
        _check_arg(group_access, profiles)
    if users_access:
        _check_group(users_access, profiles)
    if groups_access:
        _check_group(groups_access, profiles)
    return True


def check_access(
    action: Union['ALLOW', 'DENNY'] = 'ALLOW',
    user_access=None,
    users_access=[],
    group_access=None,
    groups_access=[]
):
    """ Decorator to allow or denny access to a resource

    Args:
        action ('ALLOW'|'DENNY', optional): _description_. Defaults to ALLOW.
        user_access (str, optional): _description_. Defaults to None.
        users_access (list, optional): _description_. Defaults to [].
        group_access (str, optional): _description_. Defaults to None.
        groups_access (list, optional): _description_. Defaults to [].
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                check_access_fn(user_access, users_access,
                                group_access, groups_access, request)

                return f(*args, **kwargs)
            except HttpForbiddenError as exc:
                return jsonify(exc.message), exc.status_code
            except InvalidArgument as exc:
                return jsonify(exc.message), 401

        return decorated_function
    return decorator
