import traceback
import datetime
from functools import wraps
# from app import app
from flask import request, jsonify
from ..models import LoginService
# from .users import user_by_username
import jwt
import re
import os
from ..models.BaseConfig import BaseConfig
from ..models.conexao import Conexao

import logging
logging.basicConfig(level=logging.DEBUG)

SECRET_PASS = "OM3VpHNkEsKA"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                if not auth_token:
                    return jsonify({
                        'status': 'fail',
                        'message': 'Token is missing.'
                    }), 401
                try:
                    data = jwt.decode( auth_token, os.getenv('SECRET_TOKEN',SECRET_PASS), algorithms=["HS256"] )
                    return f(*args, **kwargs)
                except Exception:
                    print(traceback.print_exc())
                    responseObject = {
                        'status': 'fail',
                        'message': 'Bearer token malformed.'
                    }
                    return jsonify(responseObject), 401
            except IndexError:
                print(traceback.print_exc())
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed..'
                }
                return jsonify(responseObject), 401
        else:
            return jsonify({
                        'status': 'fail',
                        'message': 'Token is missing.'
                    }), 401 
        return f(*args, **kwargs)
    return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    try :
        username =  re.escape(request.json['username'])
    except:
        return jsonify({'message': 'Error', 'data':'Body empty'}), 400
    username =  re.escape(request.json['username'])
    password =  re.escape(request.json['password'])

    if username is None or password is None:
        return  jsonify({'message': 'Missing values', 'data': 'Post value is missing'}) , 400
    if len(username) < 4 or len(password) < 4:
        return  jsonify({'message': 'Values too short', 'data': 'Values too short'}) , 400
    con = connection()
    user = LoginService.login(con, username, password)
    # user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user :
        token = jwt.encode(
            {   
            'username': user['nome'],
            'cns': user['cns'],
            'uf': user['uf'],
            'municipio': user['municipio'],
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
            }, 
            os.getenv('SECRET_TOKEN',SECRET_PASS), 
            algorithm="HS256" )
        print( token )  
        return jsonify({
          'message': 'Validated successfully',
          'token': token,
          'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
          })

    return jsonify({
      'message': 'could not verify',
      'WWW-Authenticate': 'Basic auth="Login required"'
      }), 401



con = None
def connection(): 
  global con
  base = BaseConfig.getInstance()
  if con is None:
    logging.info('Loading Conexao')
    con = Conexao( base._host, base._database,  base._user, base._passwd, base._port)
  return con
