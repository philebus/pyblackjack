from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyblackjack',
    version='1.0',
    author="Jim Krooskos",
    author_email="krooskos@gmail.com",
    url="https://github.com/jkrooskos/pyblackjack.git",
    description=('Blackjack shoe/deck and validation utilities'),
    packages=['pyblackjack', 'pyblackjack.tests'],
    license='MIT',
    test_suite='pyblackjack.tests.test_pyblackjack'
    )
