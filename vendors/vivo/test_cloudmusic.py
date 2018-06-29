#! /usr/bin/python
# -*- coding: utf-8 -*-
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


    def test_cloudmusic(self):
        app_name = 'cloudmusic'

        try:
            myuiautomator.click_popup_window(DEVICE_NAME, [u'网易云音乐'])
            time.sleep(5)
            cmd = 'am force-stop {0} '.format(
                'com.netease.cloudmusic')
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'网易云音乐'])
            time.sleep(5)
            common.screenshots(app_name, '网易云音乐-首页')

            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'排行榜'])
            time.sleep(2)
            cmd = 'input swipe {0} {1} '.format(
                int(self.width / 2), int(self.height / 2))
            self.device.shell(cmd)
            time.sleep(20)
            common.screenshots(app_name, '排行榜')

            time.sleep(2)
            cmd = 'input swipe {0} {1} '.format(
                int(self.width / 100 * 13), int(self.height / 5 * 2))
            self.device.shell(cmd)
            time.sleep(20)
            common.screenshots(app_name, '排行榜-评论')

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
