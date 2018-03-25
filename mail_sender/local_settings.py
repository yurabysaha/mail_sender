DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mail_sender',
        'USER': 'posrgres',
        'PASSWORD': 'yura123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
