# The SECRET_KEY setting must not be empty.
SECRET_KEY='ZU_hds)oM$%cn$Z8%88x%97Wjx2;8`'
# settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.
DATABASES = {
    # You must define a 'default' database
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'djangossltest.db',
    }
}
