ALLOWED_HOSTS = (
    '0.0.0.0',
    '127.0.0.1',
)

# settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.
DATABASES = {
    # You must define a 'default' database
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'djangossltest.db',
    }
}

# You must set settings.ALLOWED_HOSTS if DEBUG is False.
#DEBUG = True

INSTALLED_APPS = (
    'sslify',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
)

# 'Settings' object has no attribute 'ROOT_URLCONF'
ROOT_URLCONF = 'django_ssl_test.urls'

# The SECRET_KEY setting must not be empty.
SECRET_KEY='ZU_hds)oM$%cn$Z8%88x%97Wjx2;8`'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
