#!/usr/bin/env python
# good reference: https://github.com/boto/boto3/blob/develop/setup.py
from setuptools import find_packages, setup

requires = [
    "boto3==1.26.117",
]

setup(name='viral_reddit_posts_utils',
      version='0.0.1',
      description='Utils for Viral Reddit Posts project',
      author='Kenneth Myers',
      url='https://github.com/ViralRedditPosts',
      packages=find_packages(exclude=['tests*']),
      python_requires=">= 3.7",
      install_requires=requires,
     )