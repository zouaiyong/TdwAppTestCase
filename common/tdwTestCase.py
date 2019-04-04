import re
import unittest
import os
from time import sleep
from appium import webdriver
from common.ConfigParserUtils import ConfigParserUtils
from common.autoTest import UiAutotest


class TdwTestCase(unittest.TestCase):
    def setUp(self):
        # parser = argparse.ArgumentParser()
        # parser.add_argument('--device', type=str, help='device serial')
        # parser.add_argument('--caseID', type=str, help='caseID')
        # args = parser.parse_args()
        config = ConfigParserUtils()
        deviceId = config.get_config_value_by_key(
            'device_config',  'deviceid')
        deviceAndroidVersion = list(
            os.popen(
                'adb -s %s shell getprop ro.build.version.release' %
                deviceId).readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        print(deviceId, deviceVersion)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = deviceVersion
        desired_caps['deviceName'] = deviceId
        desired_caps['appPackage'] = 'com.junte'
        desired_caps['noReset'] = True
        desired_caps['appActivity'] = 'com.paisheng.business.startpage.view.SplashScreenActivity'
        # self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.driver.unlock()
        self.auto = UiAutotest(self.driver)
        self.clearUp()
        self.driver.launch_app()
        self.testResult=1
        sleep(3)


    def getDriver(self):
        return self.driver

    def setDriver(self, uidriver):
        if isinstance(uidriver, webdriver.Remote):
            self.driver = uidriver

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        self.endTest()

    def test_case(self):
        try:
            self.caseExecute()
            self.testResult=1
        except Exception as e:
            self.onException(e)


    def handleResult(self,status):
        pass

    def onException(self,e):
        #print(e.with_traceback())
        #判断测试结果的三中状态
        # 1 - 通过，2 - 不通过，3 - 失败
        if isinstance(e,AssertionError):
            self.testResult=2
        else:
            self.testResult=3
            print(e)
            print(e.with_traceback())


    def caseExecute(self):
        pass

    def clearUp(self):
        pass

    def endTest(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TdwTestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
