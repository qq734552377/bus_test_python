#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  #控件基础包，导入这个包后，这个包下的所有函数可以直接调用
import Tkinter
from Tkinter import Label, Button, END
import serial
import ttk
import os
from LinuxCmd import *
from  BaseMsg import *
import time
from tkMessageBox import *




testStr = "This is test message!"

sdTestPath = '''/run/media/mmcblk2p1/pids_sd_test.txt'''
sramPath = '''/sys/devices/platform/avrsram/sram'''

def cmd(cmdStr):
    user_str=os.popen(cmdStr).read()
    write_log_to_Text(user_str.strip() + "<<<")
    return user_str.strip()

def getSaveResultPath(fileName):
    return "pids_test_result/%s.txt"%fileName

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
    write_log_to_Text(path)
    f = open(path,'w+')
    f.writelines(data)
    f.close()

# 追加写入文件
def writeToFileAppened(path,data):
    f = open(path,'a+')
    f.writelines(data)
    f.close()

# 读取文件内容并返回
def readFile(path):
    f = open(path,'r+')
    try:
        data = f.read()
        # write_log_to_Text(data)
        return data
        pass
    except:
        return ""
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


# 字符串转成16进制的函数
def string_to_hex(src):
    result = []
    for item in src:
        result.append(hex(ord(item)))
    return result

#16进制转换为字符串
def hex_to_string(src):
    result= []
    for i in src:
        result.append(chr(int(i,16)))
    return "".join(result)

class MySerial:
    '''串口的使用'''
    serial_test_str = "This is serial test message!"
    port_ttymxc1 = "/dev/ttymxc1"
    port_ttymxc2 = "/dev/ttymxc2"
    port_ttymxc3 = "/dev/ttymxc3"
    port_ttyAVR0 = "/dev/ttyAVR0"
    port_ttyAVR1 = "/dev/ttyAVR1"

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
    def __init__(self, parent,ledName, title = None,msg = None):
        self.ledName = ledName
        self.msg = msg
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title + " Test")
        self.parent = parent
        self.result = None
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("380x120+300+300")
        self.initial_focus.focus_set()
        self.wait_window(self)


    def body(self, master):
        self.msgLable = Label(master,text = self.msg )
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
        writeToFile(sdTestPath,testStr)
        str = readFile(sdTestPath)
        if str == testStr:
            testSucessed(TestName.sdcard_test)
        else:
            testFailed(TestName.sdcard_test)
        pass

    @classmethod
    def testBuzzer(cls):
        for i in range(0,3):
            cmd(Buzzer.openBuzzer())
            time.sleep(1)
            cmd(Buzzer.closeBuzzer())
        isListened = askquestion("Prompt","是否听见蜂鸣器响？")
        if isListened == "yes":
            testSucessed(TestName.buzzer_test)
        else:
            testFailed(TestName.buzzer_test)

    @classmethod
    def testPowerVoltage(cls):
        v = float(cmd(RTC.power_voltage()))
        if v > 23.5 and v < 24.5:
            testSucessed(TestName.power_voltage)
        else:
            testFailed(TestName.power_voltage)
        pass

    @classmethod
    def testCapVoltage(cls):
        v = float(cmd(RTC.supper_cap_voltage()))
        if v > 4.6 and v < 4.9:
            testSucessed(TestName.cap_voltage)
        else:
            testFailed(TestName.cap_voltage)
        pass

    @classmethod
    def testSupperCapPower(cls):
        isDisconnect = askquestion("Supper Cap Test","请拔下电源，并在3秒后重新插上电源")
        if isDisconnect == "yes":
            testSucessed(TestName.supper_cap_power)
        else:
            testFailed(TestName.supper_cap_power)
        pass

    @classmethod
    def testRTCBatteryVoltage(cls):
        v = float(cmd(RTC.rtc_battery_voltage()))
        if v > 2.9 and v < 3.4:
            testSucessed(TestName.rtc_battery_voltage)
        else:
            testFailed(TestName.rtc_battery_voltage)
        pass

    @classmethod
    def testOTG(cls):
        pass

    @classmethod
    def testSound_Record(cls):
        cmd(Sound.record())
        isListened = askquestion("Prompt","是否播放录音？")
        if isListened == "yes":
            cmd(Sound.play_record())
            isSuccess = askquestion("Prompt","是否听见录音？")
            if isSuccess == "yes":
                testSucessed(TestName.sound_record)
            else:
                testFailed(TestName.sound_record)
        else:
            testFailed(TestName.sound_record)
        pass


    @classmethod
    def testRedLed(cls):
        LedDialog(init_window,LedCtr.red_led,"Red Led","红灯测试")

    @classmethod
    def testYellowLed(cls):
        LedDialog(init_window,LedCtr.yellow_led,"Yellow Led","黄灯测试")

    @classmethod
    def testGreenLed(cls):
        LedDialog(init_window,LedCtr.green_led,"Green Led","绿灯测试")

    @classmethod
    def testAllLed(cls):
        isAllLight = askquestion("LED Test","是不是所有的LED灯都亮了？")
        if isAllLight == "yes":
            cmd(LedCtr.closeLed(LedCtr.red_led))
            cmd(LedCtr.closeLed(LedCtr.yellow_led))
            cmd(LedCtr.closeLed(LedCtr.green_led))
            isAllClose = askquestion("LED Test","是不是所有的灯都灭了？")
            if isAllClose == "yes":
                testSucessed(TestName.red_led)
                testSucessed(TestName.yellow_led)
                testSucessed(TestName.green_led)
            else:
                testFailed(TestName.red_led)
                testFailed(TestName.yellow_led)
                testFailed(TestName.green_led)
        else:
            testFailed(TestName.red_led)
            testFailed(TestName.yellow_led)
            testFailed(TestName.green_led)
        pass

    @classmethod
    def testPort(cls):
        avr0 = serial.Serial(MySerial.port_ttyAVR0,1200,timeout=10)
        mxc1 = serial.Serial(MySerial.port_ttymxc1,1200,timeout=10)
        mxc2 = serial.Serial(MySerial.port_ttymxc2,1200,timeout=10)
        strLen = len(MySerial.serial_test_str)
        avr0.write(MySerial.serial_test_str)
        time.sleep(1)
        result1 = mxc1.read(strLen)
        if result1 == MySerial.serial_test_str:
            mxc1.write(MySerial.serial_test_str)
            time.sleep(1)
            result2 = mxc2.read(strLen)
            if result2 == MySerial.serial_test_str:
                testSucessed(TestName.port_ttymxc1)
                mxc2.write(MySerial.serial_test_str)
                time.sleep(1)
                result3 = avr0.read(strLen)
                if result3 == MySerial.serial_test_str:
                    testSucessed(TestName.port_ttymxc2)
                    testSucessed(TestName.port_ttyAVR0)
                else:
                    testFailed(TestName.port_ttymxc2)
                    testFailed(TestName.port_ttyAVR0)
            else:
                testFailed(TestName.port_ttymxc1)
                testFailed(TestName.port_ttymxc2)
        else:
            testFailed(TestName.port_ttyAVR0)
            testFailed(TestName.port_ttymxc1)
        avr0.close()
        mxc1.close()
        mxc2.close()
        pass

    @classmethod
    def testMeter(cls):
        pass

    @classmethod
    def testSimCard(cls):
        pass

    @classmethod
    def testGPRS(cls):
        pass

    @classmethod
    def testGPS(cls):
        pass

    @classmethod
    def testWifi(cls):
        pass

    @classmethod
    def testSram(cls):
        # cmd("rm sram_result.txt")
        # cmd("/ucast_tests/test_sram > sram_result.txt 2>&1")
        # result = readFile("sram_result.txt")
        writeToFile(sramPath,testStr)
        result = readFile(sramPath)
        if testStr in result:
            testSucessed(TestName.s_ram)
        else:
            testFailed(TestName.s_ram)
        pass

    @classmethod
    def testTemperature(cls):
        tem = float(cmd(RTC.enviroment_temperature()))
        if tem > 15.0 and tem < 50.0:
            testSucessed(TestName.temperature)
        else:
            testFailed(TestName.temperature)
        pass

    @classmethod
    def testBluetooth(cls):

        pass

    @classmethod
    def quitAndSave(cls):
        TestFun.beforeQuit()
        TestFun.saveSomething()
        init_window.quit()
        pass

    @classmethod
    def beforeQuit(cls,event=None):
        print "退出了"
        cmd(LedCtr.closeLed(LedCtr.red_led))
        cmd(LedCtr.closeLed(LedCtr.yellow_led))
        cmd(LedCtr.closeLed(LedCtr.green_led))
        pass

    @classmethod
    def saveSomething(cls):
        writeToFile(getSaveResultPath("result"),"This is test : 成功")
        pass

def test_all_init():
    cmd(Wifi.open_power)
    cmd(GPS.open_power())
    cmd(ThreeG.open_power)

    cmd(LedCtr.openLed(LedCtr.red_led))
    cmd(LedCtr.openLed(LedCtr.yellow_led))
    cmd(LedCtr.openLed(LedCtr.green_led))

    pass


def gui_start():
    global init_window
    init_window = Tk() #实例化出一个父窗口
    init_window.geometry('950x850+25+25')  #初始化窗口大小
    init_window.title("PIDS Test")
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
    firstItem9 = TestItem(fram1_1,TestName.sound_record["name"],TestName.sound_record["testState"],TestFun.testSound_Record)
    TestName.sound_record["widget"] = firstItem9


    secondItem_mxc1 = TestItem(fram1_2,TestName.port_ttymxc1["name"],TestName.port_ttymxc1["testState"],TestFun.testPort)
    TestName.port_ttymxc1["widget"] = secondItem_mxc1
    secondItem_mxc2 = TestItem(fram1_2,TestName.port_ttymxc2["name"],TestName.port_ttymxc2["testState"])
    TestName.port_ttymxc2["widget"] = secondItem_mxc2
    secondItem_avg0 = TestItem(fram1_2,TestName.port_ttyAVR0["name"],TestName.port_ttyAVR0["testState"])
    TestName.port_ttyAVR0["widget"] = secondItem_avg0
    secondItem_temp = TestItem(fram1_2,TestName.temperature["name"],TestName.temperature["testState"],TestFun.testTemperature)
    TestName.temperature["widget"] = secondItem_temp
    secondItem_meter = TestItem(fram1_2,TestName.meter["name"],TestName.meter["testState"],TestFun.testMeter)
    TestName.meter["widget"] = secondItem_meter
    secondItem_simcard = TestItem(fram1_2,TestName.sim_card["name"],TestName.sim_card["testState"],TestFun.testSimCard)
    TestName.sim_card["widget"] = secondItem_simcard
    secondItem_gprs = TestItem(fram1_2,TestName.gprs["name"],TestName.gprs["testState"],TestFun.testGPRS)
    TestName.gprs["widget"] = secondItem_gprs
    secondItem_gps = TestItem(fram1_2,TestName.gps["name"],TestName.gps["testState"],TestFun.testGPS)
    TestName.gps["widget"] = secondItem_gps
    secondItem_wifi = TestItem(fram1_2,TestName.wifi_test["name"],TestName.wifi_test["testState"],TestFun.testWifi)
    TestName.wifi_test["widget"] = secondItem_wifi


    thirdItem_sram = TestItem(fram1_3,TestName.s_ram["name"],TestName.s_ram["testState"],TestFun.testSram)
    TestName.s_ram["widget"] = thirdItem_sram
    thirdItem_bluetooth = TestItem(fram1_3,TestName.bluetooth["name"],TestName.bluetooth["testState"],TestFun.testBluetooth)
    TestName.bluetooth["widget"] = thirdItem_bluetooth
    thirdItem_mxc4 = TestItem(fram1_3, TestName.port_ttymxc4["name"], TestName.port_ttymxc4["testState"])
    TestName.port_ttymxc4["widget"] = thirdItem_mxc4
    thirdItem_cap = TestItem(fram1_3,TestName.cap_voltage["name"],TestName.cap_voltage["testState"],TestFun.testCapVoltage)
    TestName.cap_voltage["widget"] = thirdItem_cap
    thirdItem_cap_power = TestItem(fram1_3,TestName.supper_cap_power["name"],TestName.supper_cap_power["testState"],TestFun.testSupperCapPower)
    TestName.supper_cap_power["widget"] = thirdItem_cap_power

    # write_log_to_Text(BackLight.setLight(2))
    # write_log_to_Text(GPS.gps_antenna_status())
    # showerror("eeee")

    test_all_init()
    init_window.mainloop()


gui_start()