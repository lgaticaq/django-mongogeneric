import os

from setuptools import setup


def readme(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='mongogeneric3',
    version='0.0.2',
    description=(
        'An implementation of django class based generic views using '
        'mongoengine.'),
    long_description=readme('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='mongo cbv mongoengine',
    url='http://github.com/lgaticaq/django-mongogeneric',
    author='Leonardo Gatica',
    author_email='lgatica@protonmail.com',
    license='MIT',
    packages=['mongogeneric'],
    py_modules=['mongogeneric'],
    include_package_data=True,
    zip_safe=False
)
