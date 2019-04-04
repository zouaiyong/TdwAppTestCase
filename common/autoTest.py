from time import sleep
from appium import webdriver


class UiAutotest(object):
    def __init__(self, uidriver):
        if isinstance(uidriver, webdriver.Remote):
            self.driver = uidriver
        pass

    def clickById(self, id):
        deviceid = self.driver.find_element_by_id(id)
        deviceid.click()

    def clickByIdContains(self, regexid):
        deviceid = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceIdMatches(\"%s\")' % regexid)
        deviceid.click()
        #----------------------------------------
        # by text search

    def clickByText(self, text):
        deviceText = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text(\"%s\")' % text)
        deviceText.click()

    def clickByTextContains(self, text):
        deviceText = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains(\"%s\")' % text)
        deviceText.click()

    def clickByTextStartWith(self, text):
        deviceText = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textStartsWith(\"%s\")' % text)
        deviceText.click()

    def clickByTextMatches(self, regextext):
        deviceText = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textMatches(\"%s\")' % regextext)
        deviceText.click()

    def clickByContentDesc(self, desc):
        devicedesc = self.driver.find_element_by_accessibility_id(desc)
        devicedesc.click()
# ----------------------------------------
    # by class name search

    def clickByClassname(self, name):
        classname = self.driver.find_element_by_class_name(name)
        classname.click()
