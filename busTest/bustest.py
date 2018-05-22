#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  #控件基础包，导入这个包后，这个包下的所有函数可以直接调用
import Tkinter
from Tkinter import Label, Button, END
import serial
import ttk
import commands
from LinuxCmd import *
from  BaseMsg import *
import time
from Tix import Tk, Control, ComboBox  #升级的组合控件包
from tkMessageBox import *




testStr = "这是测试时往文件里写的内容！"

sdTestPath = '''D:\idea_j2e\workspace\pythontest\sdtest.txt'''
otgTestPath = '''D:\idea_j2e\workspace\pythontest\sdtest.txt'''
testResultPath = '''D:\idea_j2e\workspace\pythontest\sdtest.txt'''

def cmd(cmdStr):
    # user_str=commands.getoutput(cmdStr)
    # return user_str
    write_log_to_Text(cmdStr)


#获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time


#日志动态打印
def write_log_to_Text(logmsg):
    current_time = get_current_time()
    logmsg_in = str(current_time) +" ->" + str(logmsg) + "\n"
    log_data_Text.insert(END, logmsg_in)

# 写入文件
def writeToFile(path,data):
    f = open(path,'w')
    f.writelines(data)
    f.close()

# 追加写入文件
def writeToFileAppened(path,data):
    f = open(path,'a+')
    f.writelines(data)
    f.close()

# 读取文件内容并返回
def readFile(path):
    f = open(path)
    try:
        data = f.read()
        write_log_to_Text(data)
        return data
        pass
    except:
        pass
    finally:
        f.close()

def testSucessed(oneWidget):
    oneWidget["testState"] = TestItemState.success
    oneWidget["widget"].setState(TestItemState.success)

def testFailed(oneWidget):
    oneWidget["testState"] = TestItemState.fail
    oneWidget["widget"].setState(TestItemState.fail)

def getTestResult(oneWidget):
    return oneWidget["testResult"](oneWidget["testState"])

class TestItem:
    def __init__(self,root,testName,testResult,btnCallback = None):
        self.root = root
        self.testName = testName
        self.testResult = testResult
        #容器
        self.fram = Frame(self.root)
        #测试的项目名
        self.testLabale = Label(self.fram,text = self.testName)
        self.testLabale.pack(side = "left")
        self.stateButton = Button(self.fram,width = 3,bg = self.testResult,command = btnCallback)
        self.stateButton.pack(side = "right",padx = 30)
        self.fram.pack(fill = X,pady = 5)

    def setState(self,testResult):
        self.testResult = testResult
        self.stateButton.config(bg = self.testResult)

class LedDialog(Toplevel):
    def __init__(self, parent,ledName, title = None):
        self.ledName = ledName
        self.msg = title
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title + "测试")
        self.parent = parent
        self.result = None
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("300x120+300+300")
        self.initial_focus.focus_set()
        self.wait_window(self)


    def body(self, master):
        self.msgLable = Label(master,text = self.msg + "测试")
        self.msgLable.pack(side="top",pady=10)

        self.framBtn = Frame(master)
        self.openLedBtn = Button(self.framBtn, text = "开  灯", bg = "#cccccc", command = self.openLed )
        self.openLedBtn.pack(side = "left",padx = 10)
        self.closeLedBtn = Button(self.framBtn, text = "关  灯", bg = "#cccccc", command = self.closeLed )
        self.closeLedBtn.pack(side = "left",padx = 10)
        self.testSuccessBtn = Button(self.framBtn, text = "测试成功", bg = "#cccccc", command = self.successTest )
        self.testSuccessBtn.pack(side = "left",padx = 10)
        self.testFailBtn = Button(self.framBtn, text = "测试失败", bg = "#cccccc", command = self.failTest )
        self.testFailBtn.pack(side = "left",padx = 10)
        self.framBtn.pack(side = "bottom",pady = 20)

        pass
    def openLed(self):
        str = LedCtr.openLed(self.ledName)
        cmd(str)

    def closeLed(self):
        str = LedCtr.closeLed(self.ledName)
        cmd(str)

    def successTest(self):
        if self.ledName == LedCtr.red_led:
            testSucessed(TestName.red_led)
        elif self.ledName == LedCtr.yellow_led:
            testSucessed(TestName.yellow_led)
        else:
            testSucessed(TestName.green_led)
        self.cancel()

    def failTest(self):
        if self.ledName == LedCtr.red_led:
            testFailed(TestName.red_led)
        elif self.ledName == LedCtr.yellow_led:
            testFailed(TestName.yellow_led)
        else:
            testFailed(TestName.green_led)
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()


class TestFun:
    @classmethod
    def testSdCard(cls):
        pass

    @classmethod
    def testBuzzer(cls):
        for i in range(0,3):
            cmd(Buzzer.openBuzzer())
            time.sleep(1)
            cmd(Buzzer.closeBuzzer())
        isListened = askquestion("提示","是否听见蜂鸣器响？")
        if isListened == "yes":
            testSucessed(TestName.buzzer_test)
        else:
            testFailed(TestName.buzzer_test)

    @classmethod
    def testPowerVoltage(cls):
        pass

    @classmethod
    def testCapVoltage(cls):
        pass

    @classmethod
    def testRTCBatteryVoltage(cls):
        pass

    @classmethod
    def testRedLed(cls):
        LedDialog(init_window,LedCtr.red_led,"红灯")

    @classmethod
    def testYellowLed(cls):
        LedDialog(init_window,LedCtr.yellow_led,"黄灯")

    @classmethod
    def testGreenLed(cls):
        LedDialog(init_window,LedCtr.green_led,"绿灯")


    @classmethod
    def testWifi(cls):
        pass

    @classmethod
    def quitAndSave(cls):
        init_window.quit()
        pass

def test_all_init():
    cmd(Wifi.open_power)
    cmd(GPS.open_power())
    cmd(ThreeG.open_power)
    pass


def gui_start():
    global init_window
    init_window = Tk() #实例化出一个父窗口
    init_window.geometry('750x650')  #初始化窗口大小
    init_window.title("公交车设备测试")
    title = Label(init_window,text = "工厂测试项目")
    title.grid(row = 0,column = 0,padx = 90,pady=15)

    fram1 = Frame(init_window)
    #第一列测试项目
    fram1_1 = Frame(fram1)
    fram1_1.grid(row=1, column=0,sticky = "N",padx=5)
    #第二列测试项目
    fram1_2 = Frame(fram1)
    fram1_2.grid(row=1, column=1,sticky = "N",padx=5)
    #第三列测试项目
    fram1_3 = Frame(fram1)
    fram1_3.grid(row=1, column=2, sticky = "N",padx=5)
    fram1.grid(row=1,sticky = "N",padx=15,pady=15)

    #开始测试按钮容器框
    fram4 = Frame(init_window)
    startButton = Button(fram4,text = "开始测试",bg = "#22D911")
    startButton.pack(side = "left",pady = 20,padx = 40)
    startButton = Button(fram4,text = "停止测试",bg = "#D92211")
    startButton.pack(side = "left",pady = 20,padx = 40)
    exitButton = Button(fram4, text = "退出并保存", bg = "#cccccc", command = TestFun.quitAndSave)
    exitButton.pack(side = "left",pady = 20,padx = 40)
    fram4.grid(row = 2,column =0,sticky ="W")

    fram5 = Frame(init_window)
    log_label = Label(fram5, text="日志")
    log_label.pack(side = "top")
    global log_data_Text
    log_data_Text = Text(fram5, width=80, height=15)  # 日志框
    log_data_Text.pack(side = "left",padx = 5)
    log_scroll = Scrollbar(fram5)
    log_scroll.pack(side="right", fill=Y)
    log_data_Text.config(yscrollcommand = log_scroll.set)
    log_scroll.config(command = log_data_Text.yview)
    fram5.grid(row=3, column=0,sticky ="W")




    firstItem1 = TestItem(fram1_1,TestName.sdcard_test["name"], TestName.sdcard_test["testState"], TestFun.testSdCard)
    TestName.sdcard_test["widget"] = firstItem1
    firstItem2 = TestItem(fram1_1,TestName.buzzer_test["name"],TestName.buzzer_test["testState"],TestFun.testBuzzer)
    TestName.buzzer_test["widget"] = firstItem2
    firstItem3 = TestItem(fram1_1,TestName.red_led["name"], TestName.red_led["testState"], TestFun.testRedLed)
    TestName.red_led["widget"] = firstItem3
    firstItem4 = TestItem(fram1_1,TestName.yellow_led["name"], TestName.yellow_led["testState"], TestFun.testYellowLed)
    TestName.yellow_led["widget"] = firstItem4
    firstItem5 = TestItem(fram1_1,TestName.green_led["name"], TestName.green_led["testState"], TestFun.testGreenLed)
    TestName.green_led["widget"] = firstItem5
    firstItem6 = TestItem(fram1_1,TestName.power_voltage["name"],TestName.power_voltage["testState"],TestFun.testPowerVoltage)
    TestName.power_voltage["widget"] = firstItem6
    firstItem7 = TestItem(fram1_1,TestName.rtc_battery_voltage["name"],TestName.rtc_battery_voltage["testState"],TestFun.testRTCBatteryVoltage)
    TestName.rtc_battery_voltage["widget"] = firstItem7

    secondItem_wifi = TestItem(fram1_2,TestName.wifi_test["name"],TestName.wifi_test["testState"],TestFun.testWifi)
    TestName.wifi_test["widget"] = secondItem_wifi



    thirdItem_cap = TestItem(fram1_3,TestName.cap_voltage["name"],TestName.cap_voltage["testState"],TestFun.testCapVoltage)
    TestName.cap_voltage["widget"] = thirdItem_cap

    # write_log_to_Text(BackLight.setLight(2))
    # write_log_to_Text(GPS.gps_antenna_status())
    # showerror("eeee")

    test_all_init()
    init_window.mainloop()


gui_start()