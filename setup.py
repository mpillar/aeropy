#!/usr/bin/env python
import setuptools


with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    requirements = filter(lambda x: not x.startswith('#'), requirements)


setuptools.setup(
    name='aerofs',
    version='1.3.0',
    description='aerofs',
    long_description='An AeroFS Private Cloud API SDK written in Python',
    keywords='sdk,api,aerofs,cloud',
    author='AeroFS',
    author_email='oss@aerofs.com',
    url='https://github.com/aerofs/aerofs-sdk-python',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
