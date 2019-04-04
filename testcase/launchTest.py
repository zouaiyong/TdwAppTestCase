import unittest
from time import sleep

from common.tdwTestCase import TdwTestCase


class launchTest(TdwTestCase):
    def caseExecute(self):
        print('method test is run')
        sleep(3)
        self.driver.wait_activity(
            'com.paisheng.business.homepage.mainactivity.view.MainActivity', 3, 2)
        activity1 = self.driver.current_activity
        package1 = self.driver.current_package
        context = self.driver.current_context
        print("===================" + activity1)
        #self.auto.clickById("com.junte:id/tv_index_fragemnt_moidicon_item")
        sleep(3)
        #self.auto.clickByText('发现')
        sleep(3)
        self.auto.clickByClassname('android.widget.ImageView')
        sleep(3)
        self.driver.save_screenshot('D:\\tuandai.png')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(launchTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
