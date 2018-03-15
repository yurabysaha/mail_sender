DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_mail_sender',
        'USER': 'postgres',
        'PASSWORD': 'yura123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
