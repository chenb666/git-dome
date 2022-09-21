from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://source.zenmboy.com/')
# browser.maximize_window()
print ("在此界面输入账号没密码")
time.sleep(10)
driver.quit()
print("你长时间未登录，页面已经正常退出了.")

import unittest
import time
from selenium import webdriver
import def_log
import def_user_login
import def_shijianchuo
from time import sleep
#定义一个类，这个类必须继承自unittest.TestCase类
class UserLoginTestCase(unittest.TestCase):
    # 定义setUp方法，在方法内实现执行用例之前的公共操作
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    # 定义tearDown方法，在方法内实现执行用例之后的公共操作
    def tearDown(self):
        self.browser.quit()

    # 定义一个方法，实现使用正确的用户名密码登录，登录后用用户名进行断言
    def test_01_login_by_correct_username_password(self):
        try:
            # 实例化Log_print_into_file的对象
            logger = def_log.Log_print_into_file()
            # 确定日志的文件名称、存放路径、格式等信息
            logfile = logger.get_logfile()
            # 使用正确的用户名密码登录
            def_user_login.user_login_by_username_password(self.browser,"sup","s1234567")
            logger.logprint("用户登录",logfile,"info","使用正确的用户名密码登录")
            sleep(2)
            # 登录完成后使用当前登录用户的名字和预期的苏鹏进行比较，如果一致，用例可以通过
            # 定位用户名显示的位置
            username_ele = self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[3]'
                                                              '/td[1]/label')
            logger.logprint("用户登录",logfile,"info","定位用户名字显示的元素信息是否存在")
            username = username_ele.text
            self.assertEqual(username,"苏鹏")
        except Exception as e:
            def_shijianchuo.file_name(self.browser,"登录报错")
            logger.logprint("用户登录",logfile,"error",e)
            raise e
#
    # 定义一个方法，实现使用正确的用户名错误的密码登录，使用提示信息的内容进行断言
    def test_02_login_by_correct_username_wrong_password(self):
        try:
            # 实例化Log_print_into_file的对象
            logger = def_log.Log_print_into_file()
            # 确定日志的文件名称、存放路径、格式等信息
            logfile = logger.get_logfile()
            # 使用正确的用户名密码登录
            def_user_login.user_login_by_username_password(self.browser,"sup","s123456")
            logger.logprint("用户登录",logfile,"info","使用正确的用户名错误的密码登录")
            sleep(2)
            # 点击登录按钮后使用提示信息进行比较，如果一致，用例可以通过
            # 定位提示信息显示的位置
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbo'
                                                          'dy/tr[2]/td/div/table/tbody/tr/td[2]')
            logger.logprint("用户登录",logfile,"info","定位提示信息显示的元素信息是否存在")
            tips = tips_ele.text
            logger.logprint("用户登录",logfile,"info","获取提示信息的内容")
            self.assertEqual(tips,"登录名或密码错误，请重试！")
            logger.logprint("用户登录",logfile,"warning","判断提示信息和预期的内容是否一致")
            logger.logprint()
        except Exception as e:
            def_shijianchuo.file_name(self.browser,"登录报错")
            logger.logprint("用户登录",logfile,"error",e)
            raise e

    # 定义一个方法，实现使用错误的用户名正确的密码登录，使用提示信息的内容进行断言
    def test_03_login_by_wrong_username_correct_password(self):
        try:
            # 实例化Log_print_into_file的对象
            logger = def_log.Log_print_into_file()
            # 确定日志的文件名称、存放路径、格式等信息
            logfile = logger.get_logfile()
            # 使用错误的用户名正确的密码
            def_user_login.user_login_by_username_password(self.browser,"suppp","s1234567")
            logger.logprint("用户登录",logfile,"info","使用错误的用户名正确的密码登录")
            sleep(2)
            # 点击登录按钮后使用提示信息进行比较，如果一致，用例可以通过
            # 定位提示信息显示的位置
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbo'
                                                          'dy/tr[2]/td/div/table/tbody/tr/td[2]')
            logger.logprint("用户登录",logfile,"info","定位提示信息显示的元素信息是否存在")
            tips = tips_ele.text
            logger.logprint("用户登录",logfile,"info","获取提示信息的内容")
            self.assertEqual(tips,"登录名或密码错误，请重试！")
            logger.logprint("用户登录",logfile,"warning","判断提示信息和预期的内容是否一致")
        except Exception as e:
            def_shijianchuo.file_name(self.browser,"登录报错")
            logger.logprint("用户登录",logfile,"error",e)
            raise e

    # 定义一个方法，实现使用空的用户名正确的密码登录，使用提示信息的是否存在进行断言
    def test_04_login_by_null_username_correct_password(self):
        try:
            # 实例化Log_print_into_file的对象
            logger = def_log.Log_print_into_file()
            # 确定日志的文件名称、存放路径、格式等信息
            logfile = logger.get_logfile()
            # 使用空的用户名正确的密码
            def_user_login.user_login_by_username_password(self.browser,"","s1234567")
            logger.logprint("用户登录",logfile,"info","使用空的用户名正确的密码登录")
            sleep(2)
            # 点击登录按钮后使用是否存在提示信息进行断言，如果存在，用例可以通过
            # 定位提示信息显示的位置
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbo'
                                                          'dy/tr[2]/td/div/table/tbody/tr/td[2]')
            logger.logprint("用户登录",logfile,"info","定位提示信息显示的元素信息是否存在")
            self.assertIsNotNone(tips_ele)
            logger.logprint("用户登录",logfile,"warning","判断提示信息是否存在，如果是，则通过")
        except Exception as e:
            def_shijianchuo.file_name(self.browser,"登录报错")
            logger.logprint("用户登录",logfile,"error",e)
            raise e

    # 定义一个方法，实现使用正确的用户名空的密码登录，使用提示信息的是否存在进行断言
    def test_05_login_by_correct_username_null_password(self):
        try:
            # 实例化Log_print_into_file的对象
            logger = def_log.Log_print_into_file()
            # 确定日志的文件名称、存放路径、格式等信息
            logfile = logger.get_logfile()
            # 使用空的用户名正确的密码
            def_user_login.user_login_by_username_password(self.browser,"sup","")
            logger.logprint("用户登录",logfile,"info","使用正确的用户名空的密码登录")
            sleep(2)
            # 点击登录按钮后使用是否存在提示信息进行断言，如果存在，用例可以通过
            # 定位提示信息显示的位置
            tips_ele = self.browser.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbo'
                                                          'dy/tr[2]/td/div/table/tbody/tr/td[2]')
            logger.logprint("用户登录",logfile,"info","定位提示信息显示的元素信息是否存在")
            self.assertIsNotNone(tips_ele)
            logger.logprint("用户登录",logfile,"warning","判断提示信息是否存在，如果是，则通过")
        except Exception as e:
            def_shijianchuo.file_name(self.browser,"登录报错")
            logger.logprint("用户登录",logfile,"error",e)
            raise e

    # 定义一个方法，假定登录按钮默认是不可点击的状态，输入用户名和密码后，登录按钮变为可点击的状态
    # 此时，断言需要获取登录按钮的状态，如果是True则通过
    def test_06_userlogin_button_clickable(self):
        try:
            # 实例化Log_print_into_file的对象
            logger = def_log.Log_print_into_file()
            # 确定日志的文件名称、存放路径、格式等信息
            logfile = logger.get_logfile()
            # self.browser.get("http://127.0.0.1:8080/oa")
            self.browser.get("http://172.21.3.160:8080/oa/")
            # 使用logprint函数记录日志
            logger.logprint("用户登录",logfile,"info","打开OA网站")
            sleep(2)
            logger.logprint("用户登录",logfile,"warning","设置动态等待，等待页面元素加载完成后继续执行后续脚本")
            # 输入用户名
            self.browser.find_element_by_xpath('//input[@class="loginInput"]').send_keys("sup")
            logger.logprint("用户登录",logfile,"info","输入用户名")
            # 输入密码
            self.browser.find_element_by_xpath('//input[@name="password"]').send_keys("s1234567")
            logger.logprint("用户登录",logfile,"info","输入密码")
            # 获取登录按钮的状态
            button_status = self.browser.find_element_by_xpath('//input[@id="button_submit"]').is_enabled()
            logger.logprint("用户登录",logfile,"info","获取登录按钮的状态")
            self.assertTrue(button_status)
            logger.logprint("用户登录",logfile,"info","判断登录按钮是否可点击")
        except Exception as e:
            def_shijianchuo.file_name(self.browser,"登录报错")
            logger.logprint("用户登录",logfile,"error",e)
            raise e

if __name__=="__main__":
    unittest.TextTestRunner()

from datetime import datetime
# 定义一个函数实现时间戳的转换
def current_time():
    # 获取当前时间
    currenttime = datetime.datetime.now()
    # 将当前获取的时间转换为标准时间格式进行输出
    changetime = datetime.strftime(currenttime,"%Y%m%d%H%M%S")
    return changetime
    print(changetime)

import datetime
# 获得当前时间
now = datetime.datetime.now()
# 转换为指定的格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='users')
cur = conn.cursor()
cur.execute("insert into webscans_users values ('chen_bin','c123b')")
cur.execute("insert into webscans_users values ('pan_deng','p123b')")
cur.execute("insert into webscans_users values ('liang_kunwei','kw123b')")
cur.execute("insert into webscans_users values ('fang_xin','f123b')")
cur.execute("insert into webscans_users values ('luly','l123')")
cur.execute("insert into webscans_users values ('zhu_haitao','l123')")
cur.execute("insert into webscans_users values ('li_mubing','cb@1237&*')")
cur.execute("insert into webscans_users values ('chen_zengming','l123')")
conn.commit()
cur.close()
conn.close()

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='users')
cur = conn.cursor()
cur.execute("delete from webscans_users where username='pan_deng'")
cur.execute("delete from webscans_users where username='liu_hua'")
cur.execute("delete from webscans_users where username='liang_kunwei'")
cur.execute("delete from webscans_users where username='fang_xin'")
cur.execute("delete from webscans_users where username='chen_bin'")
conn.commit()
cur.close()
conn.close()

# import pymysql
# conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='users')
# cur = conn.cursor()
# cur.execute("update webscans_users set password='666666' where username='li_ming'")
# conn.commit()
# cur.close()
# conn.close()

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='users')
cur = conn.cursor()
cur.execute('select * from webscans_users')
for users in cur.fetchall():
    print('用户名：', users[0], '密码：', users[1])
cur.close()
conn.close()

# import pymysql
# conn = pymysql.connect(host = 'localhost' # 连接名称
# ,user = 'root' # 用户名
# ,passwd='root' # 密码
# ,port= 3306 # 端口，默认为3306
# ,db='users' # 数据库名称
# ,charset='utf8' # 字符编码
# )
# cur = conn.cursor() # 生成游标对象
# sql="insert into student values ('01','小明','18')" # SQL语句
# cur.execute(sql) # 执行SQL语句
# cur.close() # 关闭游标
# conn.close() # 关闭连接
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='users')
cur = conn.cursor()
cur.execute("insert into student values ('01','小明','18')")
cur.execute("insert into student values ('02','小花','19')")
cur.execute("insert into student values ('03','小刚','18')")
conn.commit()
cur.close()
conn.close()

import pymysql
conn = pymysql.connect(host = 'localhost' # 连接名称
,user = 'root' # 用户名
,passwd='root' # 密码
,port= 3306 # 端口，默认为3306
,db='users' # 数据库名称
,charset='utf8' # 字符编码
)
cur = conn.cursor() # 生成游标对象
sql="select * from `student` " # SQL语句
cur.execute(sql) # 执行SQL语句
data = cur.fetchall() # 通过fetchall方法获得数据
for i in data[:]: # 打印输出前2条数据
    print (i)
cur.close() # 关闭游标
conn.close() # 关闭连接
