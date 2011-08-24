# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages


setup(
    name='django-tagging-autocomplete',
    version='0.3.2',
    url='https://github.com/originell/django-tagging-autocomplete',
    author='Ludwik Trammer, Luis Nell',
    author_email='cooperate@originell.org',
    packages=find_packages(),
    platforms='any',
    description='Autocompletion for django-tagging',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
