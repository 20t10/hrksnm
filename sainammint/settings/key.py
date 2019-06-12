"""
SECRET_KEY
ALLOWED_HOSTS
DATABASES
DEBUG
EMAIL_*
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'p1vk+#v)#uf@l7r7nxa6(2iiah7&x*#kd%fvd3eq)75(qb&t-z'

DEBUG = False

ALLOWED_HOSTS = ['https://snmproject.herokuapp.com/']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd10rnbkalrd63',
        'USER': 'ttydethttmdrfc',
        'PASSWORD': '9e034a54a2017d3f62e7099bcf38b9aec5e4c92f12827cdbd76c9a6e236f66f3',
        'HOST': 'ec2-50-19-114-27.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
