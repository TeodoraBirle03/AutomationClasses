import unittest
import HtmlTestRunner # pip install html-testRunner

from Teme.Tema9 import Login
from Cursuri.Curs10.test3_alerts import Alerts
from Cursuri.Curs10.test4_auth import Authentication
from Cursuri.Curs10.test5_context_menu import ContextMenu
from Cursuri.Curs10.test6_keys import Keyboard


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)