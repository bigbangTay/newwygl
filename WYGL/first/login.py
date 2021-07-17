import unittest
from selenium import webdriver
from time import sleep
from WYGL.data.us_pw import *

class MyTestCase (unittest.TestCase) :

    def setUp (self) -> None :
        self.driver = webdriver.Chrome ()
        self.driver.implicitly_wait (5)
        self.driver.get (url)
        self.driver.maximize_window ()
        self.driver.find_element_by_css_selector ('[placeholder = "请输入用户名"]').send_keys (us)
        self.driver.find_element_by_css_selector ('[type = "password"]').send_keys (pw)
        self.driver.find_element_by_class_name ('el-button.submit_btn.el-button--primary').click ()
        sleep (2)
        self.assertIn ('/index/jushouye',self.driver.current_url,'登录失败')

    def tearDown (self) -> None :
        sleep (2)
        self.driver.quit ()

if __name__ == '__main__' :
    unittest.main ()