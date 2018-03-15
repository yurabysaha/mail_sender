DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mail_sender',
        'USER': 'postgres',
        'PASSWORD': 'yura123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
