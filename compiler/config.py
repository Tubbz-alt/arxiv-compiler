"""Configuration for the compiler service."""

import os

DEBUG = os.environ.get('DEBUG') == '1'
"""enable/disable debug mode"""

SERVER_NAME = os.environ.get('SEARCH_SERVER_NAME', None)
"""
the name and port number of the server. Required for subdomain support
(e.g.: 'myapp.dev:5000') Note that localhost does not support subdomains so
setting this to 'localhost' does not help. Setting a SERVER_NAME also by
default enables URL generation without a request context but with an
application context.
"""

APPLICATION_ROOT = os.environ.get('APPLICATION_ROOT', None)
"""
If the application does not occupy a whole domain or subdomain this can be set
to the path where the application is configured to live. This is for session
cookie as path value. If domains are used, this should be None.
"""

JWT_SECRET = os.environ.get('JWT_SECRET', 'foosecret')
SECRET_KEY = os.environ.get('FLASK_SECRET', 'fooflasksecret')

FILE_MANAGER_HOST = os.environ.get('FILE_MANAGER_HOST', 'arxiv.org')
FILE_MANAGER_PORT = os.environ.get('FILE_MANAGER_PORT', '443')
FILE_MANAGER_PROTO = os.environ.get('FILE_MANAGER_PROTO', 'https')
FILE_MANAGER_PATH = os.environ.get('FILE_MANAGER_PATH', '')
FILE_MANAGER_ENDPOINT = os.environ.get(
    'FILE_MANAGER_ENDPOINT',
    f'{FILE_MANAGER_PROTO}://{FILE_MANAGER_HOST}:{FILE_MANAGER_PORT}'
    f'/{FILE_MANAGER_PATH}'
)
FILE_MANAGER_VERIFY = bool(int(os.environ.get('FILE_MANAGER_VERIFY', '1')))

# Configuration for object store.
S3_ENDPOINT = os.environ.get('S3_ENDPOINT', None)
S3_VERIFY = bool(int(os.environ.get('S3_VERIFY', 1)))
S3_BUCKETS = [
    ('arxiv', 'arxiv-compiler'),
    ('submission', 'arxiv-compiler-submission')
]
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
