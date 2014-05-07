from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyblackjack',
    version='1.0',
    description=('Blackjack shoe/deck and validation utilities'),
    long_description=read('README.md')
    packages=['pyblackjack', 'pyblackjack.tests'],
    license='MIT'
    test_suite='pyblackjack.tests.test_pyblackjack'
    )
