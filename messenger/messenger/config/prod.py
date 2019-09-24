from.core import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgrestql_psycopg2',
        'NAME': 'messenger',
        'USER': 'postgres',
        'PASSWORD': 'unicesmag',
        'HOTS':'localhost',
        'POST':'5432',

    }
}



'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''


