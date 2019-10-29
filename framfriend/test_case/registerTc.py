'''
Code description：合同登记模块 testcase
Create time：
Developer：
'''
import os
import time

from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.register_page import register_page

class register_Tc(MyunitTest):
    '''合同登记模块用例'''

    def test_add_node_1(self):
        '''点击新增节点'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        flag = menu.isElementExist(menu.msg_list[21])
        self.assertTrue(flag,'弹出新增窗口')

    def test_add_node_2(self):
        '''为空新增节点'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.cBtn(menu.nodebutton_list[0])#点击提交按钮
        msgInfo1 = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo1,'不能为空','提示信息正确')
        msgInfo2 = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msgInfo3 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo3, '请输入正确的手机号', '提示信息正确')

    def test_add_node_3(self):
        '''不输入节点名称新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.inputValue(menu.input_list[17],menu.reason)
        menu.inputValue(menu.input_list[18],menu.valueList[4])
        menu.cBtn(menu.nodebutton_list[0])#点击提交按钮
        msgInfo1 = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo1,'不能为空','提示信息正确')

    def test_add_node_4(self):
        '''不输入短信接收人新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.inputValue(menu.input_list[16],menu.reason)
        menu.inputValue(menu.input_list[18],menu.valueList[4])
        menu.cBtn(menu.nodebutton_list[0])#点击提交按钮
        msgInfo1 = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo1,'不能为空','提示信息正确')

    def test_add_node_5(self):
        '''不输入短信接收人手机号新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.inputValue(menu.input_list[16],menu.reason)
        menu.inputValue(menu.input_list[17],menu.valueList[4])
        menu.cBtn(menu.nodebutton_list[0])#点击提交按钮
        msgInfo3 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo3, '请输入正确的手机号', '提示信息正确')

    def test_add_node_6(self):
        '''输入不规则短信接收人手机号新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.inputValue(menu.input_list[16],menu.reason)
        menu.inputValue(menu.input_list[17],menu.valueList[4])
        menu.inputValue(menu.input_list[18],menu.reason)
        menu.cBtn(menu.nodebutton_list[0])#点击提交按钮
        msgInfo3 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo3, '请输入正确的手机号', '提示信息正确')

    def test_add_node_7(self):
        '''输入正确信息新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[4])
        menu.cBtn(menu.button_list[0])  # 点击新增按钮
        menu.inputValue(menu.input_list[16], menu.reason)
        menu.inputValue(menu.input_list[17], menu.reason)
        menu.inputValue(menu.input_list[18], menu.valueList[4])
        menu.cBtn(menu.nodebutton_list[0])  # 点击提交按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    def test_add_node_8(self):
        '''取消新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])  # 点击新增按钮
        menu.cBtn(menu.nodebutton_list[1])  # 点击取消按钮
        flag = menu.isElementExist(menu.msg_list[21])
        self.assertFalse(flag,'关闭新增窗口')

    def test_update_node_1(self):
        '''点击修改验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请先选中节点', '提示信息正确')

    def test_update_node_2(self):
        '''选择节点点击修改验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        '''选择一项'''
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.choose_list[3])
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[22])
        self.assertTrue(flag,'弹出修改窗口')

    def test_update_node_3(self):
        '''修改清空已填内容提交验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        '''选择一项'''
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.choose_list[3])
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[19])
        menu.clearValue(menu.input_list[20])
        menu.clearValue(menu.input_list[21])
        menu.cBtn(menu.nodebutton_list[2])#提交

    def test_update_node_4(self):
        '''正确修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        '''选择一项'''
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.choose_list[3])
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[19])
        menu.inputValue(menu.input_list[19],menu.reason)
        menu.clearValue(menu.input_list[20])
        menu.inputValue(menu.input_list[20], menu.reason)
        menu.clearValue(menu.input_list[21])
        menu.inputValue(menu.input_list[21], menu.valueList[4])
        menu.cBtn(menu.nodebutton_list[2])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    def test_delete_node_1(self):
        '''点击删除验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击删除按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请先选中节点！', '提示信息正确')

    def test_delete_node_2(self):
        '''选择节点点击删除验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        '''选择一项'''
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.choose_list[3])
        menu.cBtn(menu.button_list[2])  # 点击删除按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[23])
        self.assertTrue(flag,'弹出删除确定窗口')

    def test_delete_node_3(self):
        '''选择节点点击删除确定验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        '''选择一项'''
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.choose_list[3])
        menu.cBtn(menu.button_list[2])  # 点击删除按钮
        menu.cBtn(menu.nodebutton_list[4])#点击确定
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 删除成功！', '提示信息正确')

    def test_delete_node_4(self):
        '''选择节点点击删除取消验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        '''选择一项'''
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.choose_list[3])
        menu.cBtn(menu.button_list[2])  # 点击删除按钮
        menu.cBtn(menu.nodebutton_list[5])#点击取消
        flag = menu.isElementExist(menu.msg_list[23])
        self.assertFalse(flag, '关闭删除确定窗口')

    def test_alone_query_1(self):
        """合同号，合同名称，客户名称，经办人单一条件查询"""
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[0])
        for contract_information in menu.query_list:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(contract_information, value)
                menu.cBtn(menu.button_list[3])  # 点击[查询]
                time.sleep(3)
                flag = menu.getValue(*menu.msg_list[30])
                try:
                    self.assertIn('03022',flag, '查询成功')
                except Exception:
                    self.assertNotIn('03022', flag, '输入的查询条件无效')

    def test_time_query_2(self):
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[0])
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.time_list[1])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.button_list[3])  # 点击[查询]
        msgInfo = menu.getValue(*menu.msg_list[31])
        self.assertEqual(msgInfo,'显示第 1 到第 10 条记录，总共 141 条记录','查询成功')

    def test_add_contract_1(self):
        '''点击新增合同按钮'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])#新增
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请先选中村庄或社区', '提示信息正确')

    def test_add_contract_2(self):
        '''选择节点点击新增合同按钮'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])#太和社区
        menu.cBtn(menu.button_list[4])#新增
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[24])
        self.assertTrue(flag,'弹出新增合同窗口')

    def test_add_contract_3(self):
        '''为空新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.cBtn(menu.button_list[12])#提交
        msgInfo = menu.getValue(*menu.msg_list[4])
        self.assertEqual(msgInfo,'不能为空','提示信息正确')
        msgInfo1 = menu.getValue(*menu.msg_list[5])
        self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msgInfo2 = menu.getValue(*menu.msg_list[6])
        self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msgInfo3 = menu.getValue(*menu.msg_list[7])
        self.assertEqual(msgInfo3, '不能为空', '提示信息正确')
        msgInfo4 = menu.getValue(*menu.msg_list[8])
        self.assertEqual(msgInfo4, '不能为空', '提示信息正确')
        msgInfo5 = menu.getValue(*menu.msg_list[9])
        self.assertEqual(msgInfo5, '不能为空', '提示信息正确')
        msgInfo6= menu.getValue(*menu.msg_list[10])
        self.assertEqual(msgInfo6, '不能为空', '提示信息正确')
        msgInfo7 = menu.getValue(*menu.msg_list[11])
        self.assertEqual(msgInfo7, '不能为空', '提示信息正确')
        msgInfo8 = menu.getValue(*menu.msg_list[13])
        self.assertEqual(msgInfo8, '不能为空', '提示信息正确')
        msgInfo9 = menu.getValue(*menu.msg_list[15])
        self.assertEqual(msgInfo9, '不能为空', '提示信息正确')
        msgInfo10 = menu.getValue(*menu.msg_list[16])
        self.assertEqual(msgInfo10, '不能为空', '提示信息正确')
        msgInfo11 = menu.getValue(*menu.msg_list[17])
        self.assertEqual(msgInfo11, '不能为空', '提示信息正确')
        msgInfo12 = menu.getValue(*menu.msg_list[18])
        self.assertEqual(msgInfo12, '不能为空', '提示信息正确')

    def test_add_contract_4(self):
        '''不输入合同编号新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除合同编号必填项'''
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])#提交
        msgInfo = menu.getValue(*menu.msg_list[4])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_5(self):
        '''不输入合同名称新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除合同名称必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[5])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_6(self):
        '''不输入客户名称新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除客户名称必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[6])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_7(self):
        '''不输入签订时间新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除签订时间必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[7])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_8(self):
        '''不输入租赁年限新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除租赁年限必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[8])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_9(self):
        '''不输入租赁年限止新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除租赁年限止必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[9])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_10(self):
        '''不输入承租方新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除承租方必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        #menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[10])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_11(self):
        '''不输入合同总额新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除合同总额必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        #menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[11])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_12(self):
        '''不输入收款金额新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除收款金额必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        #menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[13])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_13(self):
        '''不输入收款日期新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除收款日期必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        #menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[15])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_14(self):
        '''不输入合同年限新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除合同年限必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        #menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[16])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_15(self):
        '''不输入经营方式新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除经营方式必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        #menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[17])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_add_contract_16(self):
        '''不输入账号新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入除账号必填项'''
        menu.inputValue(menu.input_list[0], menu.valueList[0])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        #menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[18])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_addtraversaltype(self):
        '''遍历合同类型选项'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.cBtn(menu.contract_type)
        list_type = []
        for contract_type in menu.contractTypeNum:  # 循环遍历合同类型下拉列表
            text, contract_type = menu.contractTypeLevelOption(*contract_type)
            list_type.append(text)
        self.assertEqual('收款', list_type[0])
        self.assertEqual('付款', list_type[1])

    def test_addtraversalcontractsubject(self):
        '''遍历合同主体选项'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.cBtn(menu.contract_subject)
        list_Num = []
        for contract_subject in menu.contractsubjectNum:  # 循环遍历合同主体下拉列表
            text, contract_subject = menu.contractTypeLevelOption(*contract_subject)
            list_Num.append(text)
        self.assertEqual('房屋租赁', list_Num[0])
        self.assertEqual('场地租赁', list_Num[1])
        self.assertEqual('土地承包', list_Num[2])
        self.assertEqual('资产', list_Num[3])
        self.assertEqual('建地', list_Num[4])

    def test_tender(self):
        '''遍历招标方式选项'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.cBtn(menu.tender)
        list_Num = []
        for contract_subject in menu.tenderNum:  # 循环遍历招标方式下拉列表
            text, contract_subject = menu.contractTypeLevelOption(*contract_subject)
            list_Num.append(text)
        self.assertEqual('公开协作', list_Num[0])
        self.assertEqual('公开竞标', list_Num[1])
        self.assertEqual('其他', list_Num[2])
        self.assertEqual('招投标', list_Num[3])
        self.assertEqual('拍卖', list_Num[4])

    def test_tender(self):
        '''遍历收款方式选项'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.cBtn(menu.tender)
        list_Num = []
        for contract_subject in menu.Billing_methodNum:  # 循环遍历收款方式下拉列表
            text, contract_subject = menu.contractTypeLevelOption(*contract_subject)
            list_Num.append(text)
        self.assertEqual('按年', list_Num[0])
        self.assertEqual('按半年', list_Num[1])
        self.assertEqual('按月', list_Num[2])
        self.assertEqual('自定义', list_Num[3])

    def test_add_contract_17(self):
        '''输入不规则合同总额新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入不规则合同总额必填项'''
        menu.inputValue(menu.input_list[5], menu.reason)
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[12])
        self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_add_contract_18(self):
        '''输入不规则收款金额新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入不规则收款金额必填项'''
        menu.inputValue(menu.input_list[6], menu.reason)
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[14])
        self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_add_contract_19(self):
        '''输入不规则账号新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        '''输入不规则账号必填项'''
        menu.inputValue(menu.input_list[10], menu.reason)
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[19])
        self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_add_contract_20(self):
        '''收款方式自定义'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        receive_method = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[13]/div/select')
        Select(receive_method).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.Customcontract)
        menu.cBtn(menu.choose_list[10])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        time.sleep(10)

    def test_add_detail_21(self):
        '''明细不完整'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.inputValue(menu.input_list[13],menu.reason)
        menu.cBtn(menu.button_list[12])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[32])
        self.assertEqual(msgInfo,'×\n提示! 明细信息请填写完整','提示信息正确')

    def test_add_uploadimage_22(self):
        '''上传图片'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.upload()
        time.sleep(8)
        msgInfo = menu.getValue(*menu.msg_list[33])
        self.assertIn('Wallpaper.jpg\nWallpaper1.jpg\nWallpaper2.jpg',msgInfo,'图片上传成功')

    def test_add_deleteimage_23(self):
        '''上传图片删除'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.upload()
        time.sleep(8)
        menu.cBtn(menu.deleteimg)
        msgInfo = menu.getValue(*menu.msg_list[33])
        self.assertIn('Wallpaper.jpg\nWallpaper1.jpg',msgInfo,'图片删除成功')

    def test_add_contract_24(self):
        '''成功新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.inputValue(menu.input_list[0], menu.reason1)
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    def test_add_contract_25(self):
        '''合同号重复新增提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.inputValue(menu.input_list[0], menu.valueList[5])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[10], menu.valueList[4])
        menu.cBtn(menu.button_list[12])  # 提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[34])
        self.assertEqual(msgInfo, '×\n提示! 合同号PZ07重复', '提示信息正确')

    def test_add_contract_26(self):
        '''取消新增'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.button_list[4])  # 新增
        menu.cBtn(menu.button_list[13]) # 取消
        msg = menu.isElementExist(menu.msg_list[24])
        self.assertFalse(msg,'关闭新增窗口')

    def test_update_contract_1(self):
        '''点击修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[5])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def test_update_contract_2(self):
        '''全选点击修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[5])
        menu.cBtn(menu.button_list[5])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def test_update_contract_3(self):
        '''选择一项点击修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[25])
        self.assertTrue(msg, '弹出修改窗口')

    def test_update_contract_4(self):
        '''修改清空必填项提交'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.keydelete()
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.button_list[14])#提交
        msgInfo = menu.getValue(*menu.msg_list[4])
        self.assertEqual(msgInfo,'不能为空','提示信息正确')
        msgInfo1 = menu.getValue(*menu.msg_list[5])
        self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msgInfo2 = menu.getValue(*menu.msg_list[6])
        self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msgInfo3 = menu.getValue(*menu.msg_list[7])
        self.assertEqual(msgInfo3, '不能为空', '提示信息正确')
        msgInfo4 = menu.getValue(*menu.msg_list[8])
        self.assertEqual(msgInfo4, '不能为空', '提示信息正确')
        msgInfo5 = menu.getValue(*menu.msg_list[9])
        self.assertEqual(msgInfo5, '不能为空', '提示信息正确')
        msgInfo6= menu.getValue(*menu.msg_list[10])
        self.assertEqual(msgInfo6, '不能为空', '提示信息正确')
        msgInfo7 = menu.getValue(*menu.msg_list[11])
        self.assertEqual(msgInfo7, '不能为空', '提示信息正确')
        msgInfo8 = menu.getValue(*menu.msg_list[13])
        self.assertEqual(msgInfo8, '不能为空', '提示信息正确')
        # msgInfo9 = menu.getValue(*menu.msg_list[15])
        # self.assertEqual(msgInfo9, '不能为空', '提示信息正确')
        msgInfo10 = menu.getValue(*menu.msg_list[16])
        self.assertEqual(msgInfo10, '不能为空', '提示信息正确')
        msgInfo11 = menu.getValue(*menu.msg_list[17])
        self.assertEqual(msgInfo11, '不能为空', '提示信息正确')
        msgInfo12 = menu.getValue(*menu.msg_list[35])
        self.assertEqual(msgInfo12, '不能为空', '提示信息正确')

    def test_update_contract_5(self):
        '''修改总金额非数字验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.clearValue(menu.input_list[5])
        menu.inputValue(menu.input_list[5],menu.reason)
        msgInfo = menu.getValue(*menu.msg_list[12])
        self.assertEqual(msgInfo,'请输入有效的数字','提示信息正确')

    def test_update_contract_6(self):
        '''修改合同账号非数字验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.clearValue(menu.input_list[6])
        menu.inputValue(menu.input_list[6],menu.reason)
        msgInfo = menu.getValue(*menu.msg_list[14])
        self.assertEqual(msgInfo,'请输入有效的数字','提示信息正确')

    def test_update_contract_7(self):
        '''修改收款金额非数字验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.clearValue(menu.input_list[22])
        menu.inputValue(menu.input_list[22],menu.reason)
        msgInfo = menu.getValue(*menu.msg_list[36])
        self.assertEqual(msgInfo,'请输入有效的数字','提示信息正确')

    def test_update_contract_8(self):
        '''合同明细不完整验证'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.inputValue(menu.input_list[13], menu.reason)
        menu.cBtn(menu.button_list[14])  # 提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[32])
        self.assertEqual(msgInfo, '×\n提示! 明细信息请填写完整', '提示信息正确')

    def test_update_contract_9(self):
        '''修改上传图片'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.upload()
        time.sleep(8)
        msgInfo = menu.getValue(*menu.msg_list[33])
        self.assertIn('Wallpaper.jpg\nWallpaper1.jpg\nWallpaper2.jpg', msgInfo, '图片上传成功')

    def test_update_contract_10(self):
        '''修改上传图片删除'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])#修改
        menu.upload()
        time.sleep(8)
        menu.cBtn(menu.deleteimg)
        msgInfo = menu.getValue(*menu.msg_list[33])
        self.assertIn('Wallpaper.jpg\nWallpaper1.jpg', msgInfo, '图片删除成功')

    def test_update_contract_11(self):
        '''正常修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])  # 修改
        time.sleep(2)
        menu.inputValue(menu.input_list[0], menu.reason1)
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[22], menu.valueList[4])
        menu.cBtn(menu.button_list[14])  # 提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    def test_update_contract_12(self):
        '''合同编号重复修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])  # 修改
        menu.inputValue(menu.input_list[0], menu.valueList[5])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.choose_list[7])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[8])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.cBtn(menu.choose_list[9])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[7])
        menu.inputValue(menu.input_list[3], menu.reason)
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        menu.inputValue(menu.input_list[7], menu.valueList[3])
        menu.inputValue(menu.input_list[8], menu.valueList[2])
        menu.inputValue(menu.input_list[9], menu.reason)
        menu.inputValue(menu.input_list[22], menu.valueList[4])
        menu.cBtn(menu.button_list[14])  # 提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[34])
        self.assertEqual(msgInfo, '×\n提示! 合同号PZ07重复', '提示信息正确')

    def test_update_contract_13(self):
        '''取消修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[5])  # 修改
        menu.cBtn(menu.button_list[15]) #取消
        msg = menu.isElementExist(menu.msg_list[25])
        self.assertFalse(msg,'关闭修改窗口')

    def test_check_contract_1(self):
        '''点击查看明细'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[6])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo,'×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_2(self):
        '''全选点击查看明细'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[5])
        menu.cBtn(menu.button_list[6])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_3(self):
        '''选择一项点击查看明细'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])#查看明细
        msg = menu.isElementExist(menu.msg_list[26])
        self.assertTrue(msg,'弹出查看明细窗口')

    def test_check_contract_4(self):
        '''查看明细刷新'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.button_list[16])
        menu.cBtn(menu.button_list[16])#刷新
        msg = menu.isElementExist(menu.msg_list[37])
        self.assertTrue(msg,'弹出信息')

    def test_check_contract_5(self):
        '''查看明细修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.button_list[17])
        menu.cBtn(menu.button_list[17])#修改
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[37])
        self.assertEqual(msgInfo,'×\n提示! 请选中一项内容！','提示信息正确')

    def test_check_contract_6(self):
        '''全选查看明细修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.msg_list[38])
        menu.cBtn(menu.choose_list[12])#全选
        menu.cBtn(menu.button_list[17])  # 修改
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[37])
        self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行修改！', '提示信息正确')

    def test_check_contract_7(self):
        '''全选查看明细修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.msg_list[38])
        menu.cBtn(menu.choose_list[13])#选择一项
        menu.cBtn(menu.button_list[17])  # 修改
        msg = menu.isElementExist(menu.msg_list[27])
        self.assertTrue(msg,'弹出明细修改窗口')

    def test_check_contract_8(self):
        '''遍历明细修改状态选项'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.msg_list[38])
        menu.cBtn(menu.choose_list[13])  # 选择一项
        menu.cBtn(menu.button_list[17])  # 修改
        menu.cBtn(menu.contract_states)
        list_Num = []
        for contract_states in menu.contract_statesNum:  # 循环遍历收款方式下拉列表
            text, contract_states = menu.contractTypeLevelOption(*contract_states)
            list_Num.append(text)
        self.assertEqual('已收款', list_Num[0])
        self.assertEqual('未收款', list_Num[1])
        self.assertEqual('待收款', list_Num[2])
        self.assertEqual('已收不足', list_Num[3])
        self.assertEqual('超期不足', list_Num[4])
        self.assertEqual('超期收款', list_Num[5])

    def test_check_contract_9(self):
        '''明细修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.msg_list[38])
        menu.cBtn(menu.choose_list[13])  # 选择一项
        menu.cBtn(menu.button_list[17])  # 修改
        menu.inputValue(menu.input_list[15],menu.valueList[0])
        receive_method = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[2]/div/select')
        Select(receive_method).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.choose_list[11])#明细内已收日期
        # menu.Operation_scroll(menu.button_list[19])
        menu.cBtn(menu.time_list[8])
        menu.cBtn(menu.button_list[19])#明细修改提交
        msg = menu.isElementExist(menu.msg_list[37])
        self.assertTrue(msg, '弹出信息')

    def test_check_contract_10(self):
        '''关闭明细修改'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.scroll_jujiao(menu.msg_list[38])
        menu.cBtn(menu.choose_list[13])  # 选择一项
        menu.cBtn(menu.button_list[17])  # 修改
        menu.cBtn(menu.button_list[20])#关闭
        msg = menu.isElementExist(menu.msg_list[27])
        self.assertFalse(msg,'关闭窗口')

    def test_check_contract_11(self):
        '''关闭明细'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])
        menu.cBtn(menu.button_list[6])  # 查看明细
        menu.cBtn(menu.button_list[18])#关闭
        msg = menu.isElementExist(menu.msg_list[26])
        self.assertFalse(msg,'关闭窗口')

    def test_check_contract_12(self):
        '''点击明细2'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[7])  # 查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_13(self):
        '''全选点击明细2'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[5])#全选
        menu.cBtn(menu.button_list[7])  # 查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_14(self):
        '''选择一项点击明细2'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])#选择一项
        menu.cBtn(menu.button_list[7])  # 查看明细
        msg = menu.isElementExist(menu.msg_list[26])
        self.assertTrue(msg,'弹出详情窗口')

    def test_check_contract_15(self):
        '''选择一项点击明细2关闭'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.cBtn(menu.choose_list[6])#选择一项
        menu.cBtn(menu.button_list[7])  # 查看明细
        menu.cBtn(menu.button_list[18])#关闭
        msg = menu.isElementExist(menu.msg_list[26])
        self.assertFalse(msg,'弹出详情窗口')

    def test_delete_contract_1(self):
        '''点击删除按钮'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[8])#点击删除
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo,'×\n提示! 请选中一项内容！','提示信息正确')

    def test_delete_contract_2(self):
        '''选择删除项删除'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.jScript('window.scrollTo(0,document.body.scrollHeight)') # 滚动到页面底部
        menu.cBtn(menu.choose_list[14])
        menu.jScript('window.scrollTo(document.body.scrollHeight,0)') #滚动到页面顶部
        menu.cBtn(menu.button_list[8])  # 点击删除
        msg = menu.isElementExist(menu.msg_list[28])
        self.assertTrue(msg,'弹出删除窗口')

    def test_delete_contract_3(self):
        '''选择删除项确定删除'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.jScript('window.scrollTo(0,document.body.scrollHeight)')  # 滚动到页面底部
        menu.cBtn(menu.choose_list[14])
        menu.jScript('window.scrollTo(document.body.scrollHeight,0)')  # 滚动到页面顶部
        menu.cBtn(menu.button_list[8])  # 点击删除
        menu.cBtn(menu.button_list[21]) #确定
        time.sleep(1)
        # msgInfo = menu.getValue(*menu.msg_list[0])
        # self.assertEqual(msgInfo, '×\n提示! 删除成功！', '提示信息正确')

    def test_delete_contract_4(self):
        '''选择删除项确定删除'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.choose_list[1])
        menu.cBtn(menu.choose_list[2])
        menu.cBtn(menu.nodebutton_list[6])  # 太和社区
        menu.jScript('window.scrollTo(0,document.body.scrollHeight)')  # 滚动到页面底部
        menu.cBtn(menu.choose_list[14])
        menu.jScript('window.scrollTo(document.body.scrollHeight,0)')  # 滚动到页面顶部
        menu.cBtn(menu.button_list[8])  # 点击删除
        menu.cBtn(menu.button_list[22]) #取消
        # msg = menu.isElementExist(menu.msg_list[28])
        # self.assertFalse(msg, '关闭删除窗口')

    def test_export_contract(self):
        '''模板导出'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[9])#模板导出
        time.sleep(2)
        print(os.path.exists('E:\\MyDownloads\\合同批量导入表.xlsx'))  # 检查是否已导出

    def test_import_contract_1(self):
        '''点击数据导入'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[10])#数据导入
        msg = menu.isElementExist(menu.msg_list[29])
        self.assertTrue(msg,'弹出数据导入窗口')

    def test_import_contract_2(self):
        '''不选择文件上传'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[10])  # 数据导入
        menu.cBtn(menu.button_list[24])  # 点击提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[32])
        self.assertEqual(msgInfo, '×\n提示! 导入失败', '提示信息正确')

    def test_import_contract_3(self):
        '''取消文件上传'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[10])  # 数据导入
        menu.cBtn(menu.button_list[25])  # 点击取消
        msg = menu.isElementExist(menu.msg_list[29])
        self.assertFalse(msg, '弹出数据导入窗口')

    def test_import_contract_4(self):
        '''错误文件上传'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[10])  # 数据导入
        menu.uploadFalse()
        menu.cBtn(menu.button_list[24])  # 点击提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[32])
        self.assertEqual(msgInfo, '×\n提示! 导入失败', '提示信息正确')

    def test_import_contract_99(self):
        '''正确文件上传'''
        menu = register_page(self.driver)  # 实例化合同登记页面
        self.login.loginFunc()  # 登录
        menu.inregisterpage()  # 进入合同登记页面
        time.sleep(3)
        menu.cBtn(menu.button_list[10])  # 数据导入
        menu.uploadTrue()
        menu.cBtn(menu.button_list[24])  # 点击提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 导入成功！', '提示信息正确')

if __name__=='__main__':
    pass















