#!/usr/bin/env python

import os

from setuptools import setup, find_packages

requires = ['python-dateutil', 'keyring', 'jinja2',
            'markdown', 'PyYAML', 'pyinotify', 'google-api-python-client',
            'transliterate']


def get_version(fname):
    with open(fname, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('\'"')


def check_licenses():
    CHK = "the MIT License: http://www.opensource.org/licenses/mit-license.php"
    for root, folders, files in os.walk('lib/bloggertool'):
        for f in files:
            if not f.endswith('.py'):
                continue
            if f[0] in '.#~':
                continue
            fname = os.path.join(root, f)
            if CHK not in open(fname).read():
                raise AssertionError("%s doesn't have license" % fname)


check_licenses()


setup(
    name='bloggertool',
    version=get_version('lib/bloggertool/__version__.py'),
    author='Andrew Svetlov',
    author_email='andrew.svetlov@gmail.com',
    url='https://github.com/asvetlov/bloggertool',
    description="Blogger tool",
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        ],
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    entry_points={
        'console_scripts':
            ['blog = bloggertool.main:main']
        },
    zip_safe=True,
    install_requires=requires,
    test_suite='nose.collector',
)
