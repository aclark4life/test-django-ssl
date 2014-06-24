from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
    },
    include_package_data=True,
    install_requires=[
        'Django',
        'django-sslify',
    ],
    name='django_ssl_test',
    namespace_packages=[
    ],
    packages=find_packages(),
)
