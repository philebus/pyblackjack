from setuptools import setup

setup(
    name='pyblackjack',
    version='1.0',
    description='Blackjack shoe/deck and validation utilities',
    packages=['pyblackjack', 'pyblackjack.tests'],
    test_suite='pyblackjack.tests.test_pyblackjack'
    )
