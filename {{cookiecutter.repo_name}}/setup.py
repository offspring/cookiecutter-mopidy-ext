from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='{{ cookiecutter.dist_name }}',
    version=get_version('mopidy_{{ cookiecutter.ext_name }}/__init__.py'),
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}',
    license='Apache License, Version 2.0',
    author='{{ cookiecutter.author_fullname }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.short_description }}',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            '{{ cookiecutter.ext_name }} = mopidy_{{ cookiecutter.ext_name }}:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
