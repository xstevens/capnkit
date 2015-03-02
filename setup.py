"""
Copyright 2015 (c) Simple Finance Technology Corp.
Authors: Xavier Stevens <xavier@simple.com>
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

meta = dict(
    name = 'capnkit',
    version = '0.0.1',
    description = 'Capn\'Proto persistence for scikit-learn',
    author = 'Xavier Stevens',
    license = 'MIT License',
    url = 'https://github.com/xstevens/capnkit',
    keywords = ['capnp', 'capnproto', "Cap'n Proto", 'scikit-learn'],
    classifiers = ['Development Status :: 3 - Alpha',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'License :: OSI Approved :: MIT License'],
    packages = ['capnkit'],
    test_suite = 'capnkit.test',
    install_requires = [
        'pycapnp>=0.5.3',
        'scikit-learn>=0.15.2',
    ],
    package_data = {'capnkit': ['*.capnp']},
    zip_safe = False,
)

setup(**meta)