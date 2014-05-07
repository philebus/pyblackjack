from .. import pyblackjack
import test_pyblackjack

def suite():
    import unittest
    import doctest
    suite = unittest.TestSuite()
    suite.addTests(doctest.DocTestSuite(pyblackjack))
    suite.addTests(test_pyblackjack.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
