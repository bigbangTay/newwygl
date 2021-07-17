from WYGL.first.login import *
from WYGL.data.mysql import *

class MyTestCase1 (MyTestCase) :

    def test_01add (self) :
        '''物业管理新增居民测试'''

        self.driver.implicitly_wait (5)

        self.driver.find_element_by_xpath ('/html/body/div/div/div[2]/div[1]/div/ul/a[2]/li').click ()

        self.driver.find_element_by_class_name ('el-icon-edit').click ()

        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div/'
                                           'div[3]/div/div[2]/form/div[1]/div/div/input').send_keys (jmus)

        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div/'
                                           'div[3]/div/div[2]/form/div[2]/div/div/input').send_keys (name)

        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div/'
                                           'div[3]/div/div[2]/form/div[3]/div/div/input').send_keys (idcard)

        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div'
                                           '/div[3]/div/div[2]/form/div[4]/div/div/div/span/span/i').click ()

        sleep (1)

        # 找到所有性别的选项个数
        sexs = self.driver.find_elements_by_class_name ('el-select-dropdown__item')

        # 随机取一个性别的选项索引
        suoyin2 = random.randint (0,len (sexs) - 1)

        # 再引用这个索引来点击
        sexs [suoyin2].click ()     # 成功 ✌

        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div/'
                                           'div[3]/div/div[2]/form/div[5]/div/div/input').send_keys (phone)

        # 门牌号和性别同理
        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/'
                                           'div[2]/form/div[6]/div/div/div/span/span/i').click ()

        sleep (1)

        menpais = self.driver.find_elements_by_class_name ('el-select-dropdown__item')
        menpai = random.randint (2,len (menpais) - 1)
        menpais [menpai].click ()

        self.driver.find_element_by_css_selector ('[placeholder = "选择日期时间"]').send_keys (ru)

        sleep (2)
        self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[2]/div[2]/div/div[3]'
                                           '/div/div[3]/div/button[2]').click ()

        sleep (2)

        # 页面不好断言就直接通过数据库来断言
        datas = Mysqls ('localhost', 'root', '123456', 'wygl')
        dataresult = datas.select (f'select resident_name from resident where resident_name = "{name}"')
        self.assertEqual (dataresult [0][0],name,'添加失败')

        print ('输出这句话代表前面的代码都正常运行且没报错，断言也成功 ✌')

if __name__ == '__main__' :
    unittest.main ()
