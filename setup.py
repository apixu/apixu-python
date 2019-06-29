from setuptools import setup, find_packages

__version__ = '0.3.0'

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='apixu',
    version=__version__,
    description='Python library for Apixu Weather API',
    author='Andrei Avram',
    author_email='avramandrei@ymail.com',
    url='https://www.apixu.com/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    classifiers=['Development Status :: 1 - Production/Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Software Development :: Libraries :: Application Frameworks',
                 'Topic :: Software Development :: Libraries :: Python Modules', ],
)
