from setuptools import setup

setup(
    name='WebTesting',
    version='2.0.0',
    packages=['hillel_orangeHRM_frame'],
    install_requires=[
        'pytest',
        'selenium',
        'webdriver-manager'
    ],
)