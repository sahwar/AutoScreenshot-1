__author__ = 'Administrator'
import sys
import time
try:
    import unittest2 as unittest
except(ImportError):
    import unittest
from lib import common, adbtools

from lib import myuiautomator

from lib import querydb

DEVICE_NAME = querydb.get_uid(sys.argv[2])


class TestVivo(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.device = adbtools.AdbTools(DEVICE_NAME)
        common.unlock_screen(DEVICE_NAME)
        width, height = self.device.get_screen_normal_size()
        self.width = int(width)
        self.height = int(height)

    def setUp(self):

        # return back to home
        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)

    def tearDown(self):

        time.sleep(2)
        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
        time.sleep(2)


    def test_minimap(self):
        img_count = 0
        app_name = 'minimap'

        try:
            self.device.start_application('com.autonavi.minimap/com.autonavi.map.activity.NewMapActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.autonavi.minimap')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.autonavi.minimap/com.autonavi.map.activity.NewMapActivity')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 10)))
            self.device.shell(cmd)
            time.sleep(10)
            common.screenshots(app_name, img_count)
            img_count += 1

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
