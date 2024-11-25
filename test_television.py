import unittest
from television import *


class MyTestCase(unittest.TestCase):

    def test_init(self):
        tv = Television()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')

    def test_power(self):
        tv = Television()
        tv.power()
        self.assertEqual(str(tv),'Power = True, Channel = 0, Volume = 0')
        tv.power()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')

    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.mute()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 1')
        tv.power()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 1')
        tv.mute()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 1')

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')
        tv.power()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.channel_up()
        self.assertEqual(str(tv), 'Power = True, Channel = 1, Volume = 0')
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')
        tv.power()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.channel_down()
        self.assertEqual(str(tv), 'Power = True, Channel = 3, Volume = 0')
        tv.channel_down()
        self.assertEqual(str(tv), 'Power = True, Channel = 2, Volume = 0')
        tv.channel_down()
        tv.channel_down()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')

    def test_volume_up(self):
        tv = Television()
        tv.volume_up()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')
        tv.power()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.volume_up()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 1')
        tv.mute()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.volume_up()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 2')
        tv.volume_up()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 2')

    def test_volume_down(self):
        tv = Television()
        tv.volume_down()
        self.assertEqual(str(tv), 'Power = False, Channel = 0, Volume = 0')
        tv.power()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.volume_down()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.mute()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 0')
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()
        self.assertEqual(str(tv), 'Power = True, Channel = 0, Volume = 1')




if __name__ == '__main__':
    unittest.main()
