from unittest.mock import Mock

import pytest
from src.errors import HttpForbiddenError

from .check_access import check_access_fn
from .token_required import generate_token


def test_access_user_access_success():
    token = generate_token('nome', 'cns', 'MG', 'Belo Horizonte', ['user'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    check_access_fn(user_access='user', request_=request_)


def test_access_user_access_error():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(user_access='user', request_=request_)


def test_access_group_access_success():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    check_access_fn(group_access='user', request_=request_)


def test_access_group_access_error():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(group_access='user', request_=request_)


def test_access_users_access_success():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2', 'user4'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    check_access_fn(users_access=['user', 'user2'], request_=request_)
    check_access_fn(users_access=['user', 'user1', 'user4'], request_=request_)


def test_access_users_access_error():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user21', 'user41'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(users_access=['user', 'user2'], request_=request_)
    with pytest.raises(HttpForbiddenError):
        check_access_fn(
            users_access=['user', 'user1', 'user4'], request_=request_)


def test_access_users_access_action_denny_success():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2', 'user4'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(action='DENNY', users_access=[
                        'user', 'user2'], request_=request_)


def test_access_groups_access_action_denny_success():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2', 'user4'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(action='DENNY', groups_access=[
                        'user', 'user2'], request_=request_)


def test_access_user_access_action_denny_success():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2', 'user4'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(action='DENNY', user_access='user', request_=request_)


def test_access_group_access_action_denny_success():
    token = generate_token('nome', 'cns', 'MG',
                           'Belo Horizonte', ['user2', 'user4'])
    request_ = Mock()
    request_.headers.get = Mock(return_value=f'Bearer {token}')
    with pytest.raises(HttpForbiddenError):
        check_access_fn(action='DENNY', group_access='user', request_=request_)
