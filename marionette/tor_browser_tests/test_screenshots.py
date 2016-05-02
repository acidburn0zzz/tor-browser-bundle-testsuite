from marionette_driver import By
from marionette_driver.errors import MarionetteException

from marionette import MarionetteTestCase

import testsuite

class Test(MarionetteTestCase):
    def setUp(self):
        MarionetteTestCase.setUp(self)

        ts = testsuite.TestSuite()
        self.ts = ts

        self.URLs = [
                'chrome://browser/content/preferences/preferences.xul',
                'chrome://torbutton/content/preferences.xul',
                'chrome://torlauncher/content/network-settings-wizard.xul',
                ];

    def test_check_tpo(self):
        marionette = self.marionette
        with marionette.using_context('content'):
            marionette.navigate("http://check.torproject.org")
        self.ts.screenshot(marionette, full=True)
        with marionette.using_context('content'):
           for url in self.URLs:
               marionette.navigate(url)
               self.ts.screenshot(marionette)

