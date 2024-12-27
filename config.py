import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    PROXY_LIST = os.environ.get('PROXY_LIST', 'proxy1:port,proxy2:port').split(',')
