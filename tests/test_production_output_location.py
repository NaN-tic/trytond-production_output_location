# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class TestProductionOutputLocationCase(unittest.TestCase):
    'Test Production Output Location module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('production_output_location')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestProductionOutputLocationCase))
    return suite
