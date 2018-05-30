#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  #控件基础包，导入这个包后，这个包下的所有函数可以直接调用
import serial
import os
from LinuxCmd import *
from  BaseMsg import *
import time
from tkMessageBox import *
import pickle
import datetime


testStr = "This is test message!"

sdTestPath = '''/run/media/mmcblk2p1/pids_sd_test_fuban.txt'''
sramPath = '''/sys/devices/platform/avrsram/sram'''
MIME = ''
sync = "sync"

def cmd(cmdStr):
    user_str = os.popen(cmdStr).read().strip()
    if user_str != '':
        write_log_to_Text(user_str.strip() + "<<<")
    return user_str

def cmdIsFailed(cmdStr):
    return os.system(cmdStr)

def ping(ipadress):
    return os.system("ping %s -c 3"%ipadress)

def getCpuNumber():
    anchor = "serialno="
    length = 10
    str = cmd("cat /proc/cmdline")
    # str = "serialno=ea1a1b1c1d1e"
    if str == '':
        return 'no_mac_result'
    start = str.find(anchor) + len(anchor)
    str = str[start:start + length] + "00"
    mac = []
    for i in range(len(str),0 ,-2):
        mac.append(str[i-2:i].upper())
        pass
    return "-".join(mac)

def getMIME():
    at = serial.Serial(MySerial.port_ttyUSB2,115200,timeout=2)
    at.write("AT+CGSN\r\n")
    at.flush()
    mime = at.read(100)
    mime = mime.replace("\r","").split("\n")[1]
    at.close()
    return mime

def getAllTestResult():
    result = []
    result.append("MAC：" + getCpuNumber() + "\n")
    for item in TestName.allTestItems_sdcard_test:
        result.append(item["name"] + "：" + item["testResult"](item["testState"]) + "\n")
    return "".join(result)

def getRecoverData():
    result = []
    for item in TestName.allTestItems_sdcard_test:
        result.append(item["testState"])
    return result


def getSaveResultPath(fileName):
    return "pids_test_result_subpanel/%s.txt"%fileName

def getRecoverDataPath(fileName):
    return "pids_test_result_subpanel/%s.pkl"%fileName

#获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time


#日志动态打印
def write_log_to_Text(logmsg):
    current_time = get_current_time()
    logmsg_in = str(current_time) +" ->" + str(logmsg) + "\n"
    log_data_Text.insert(END, logmsg_in)

#序列化写入文件
def writeWithPickle(path,data):
    try:
        output = open(path, 'wb')
        # Pickle dictionary using protocol 0.
        pickle.dump(data, output)
        output.close()
        cmd(sync)
    except Exception:
        return


#读取序列化文件
def readWithPickle(path):
    if not os.path.exists(path):
        return ""
    try:
        pkl_file = open(path, 'rb')
        data = pickle.load(pkl_file)
        pkl_file.close()
        return data
    except Exception:
        return ""
    pass

# 写入文件
def writeToFile(path,data):
    try :
        write_log_to_Text(path)
        f = open(path,'w+')
        f.writelines(data)
        f.close()
        cmd(sync)
    except Exception:
        return
        pass

# 追加写入文件
def writeToFileAppened(path,data):
    try:
        f = open(path,'a+')
        f.writelines(data)
        f.close()
        cmd(sync)
    except Exception:
        return
        pass

# 读取文件内容并返回
def readFile(path):
    if not os.path.exists(path):
        return ""
    f = open(path,'r+')
    try:
        data = f.read()
        # write_log_to_Text(data)
        return data
        pass
    except Exception:
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
    port_ttymxc4 = "/dev/ttymxc4"
    port_ttyAVR0 = "/dev/ttyAVR0"
    port_ttyAVR1 = "/dev/ttyAVR1"
    port_ttyUSB2 = "/dev/ttyUSB2"

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

#将inputs的结果显示出来
def showInputResult(result):
    if result == "":
        result = "7ff"
    value = int(result,16)
    for i in range(10,-1,-1):
        one = (value >> i) & 0x01
        if one == 0x01:
            testFailed(TestName.inputs[i])
        else:
            testSucessed(TestName.inputs[i])

class TestFun:
    @classmethod
    def testInput(cls):
        result = "7ff"
        while cmd(RTC.input_io()) != result:
            showinfo('Prompt','请将外面开关全部拨动到下方')
        if  cmd(RTC.input_io()) == result:
            showinfo('Prompt','请将外面开关1')
            result1 = cmd(RTC.input_io())
            showInputResult(result1)
            showinfo('Prompt','请将外面开关2')
            result2 = cmd(RTC.input_io())
            showInputResult(result2)
            showinfo('Prompt','请将外面开关3')
            result3 = cmd(RTC.input_io())
            showInputResult(result3)
            showinfo('Prompt','请将外面开关4')
            result4 = cmd(RTC.input_io())
            showInputResult(result4)
    pass

    @classmethod
    def testOut1(cls):
        cmd(RTC.close_out_1())
        isClose = askquestion('Prompt','指示灯是否关闭？')
        if isClose == 'yes':
            cmd(RTC.open_out_1())
            isBright = askquestion('Prompt','指示灯是否亮起？')
            if isBright == 'yes':
                testSucessed(TestName.out_1)
            else:
                testFailed(TestName.out_1)
        else:
            testFailed(TestName.out_1)
        pass

    @classmethod
    def testOut2(cls):
        cmd(RTC.close_out_2())
        isClose = askquestion('Prompt','指示灯是否关闭？')
        if isClose == 'yes':
            cmd(RTC.open_out_2())
            isBright = askquestion('Prompt','指示灯是否亮起？')
            if isBright == 'yes':
                testSucessed(TestName.out_2)
            else:
                testFailed(TestName.out_2)
        else:
            testFailed(TestName.out_2)
        pass

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
        r = cmd(RTC.power_voltage())
        if r == "":
            testFailed(TestName.power_voltage)
            return
        v = float(r)
        if v > 23.5 and v < 24.5:
            testSucessed(TestName.power_voltage)
        else:
            testFailed(TestName.power_voltage)
        pass

    @classmethod
    def testCapVoltage(cls):
        r = cmd(RTC.supper_cap_voltage())
        if r == "":
            testFailed(TestName.cap_voltage)
            return
        v = float(r)
        if v > 4.0 and v < 4.9:
            testSucessed(TestName.cap_voltage)
        else:
            testFailed(TestName.cap_voltage)
        pass

    @classmethod
    def testSupperCapPower(cls):
        if TestName.supper_cap_power["testState"] == TestItemState.success:
            return
        showinfo('Prompt',"请拔下电源，并在3秒后重新插上电源")
        isDisconnect = askquestion("Supper Cap Test",'设备是否还正常运行？')
        if isDisconnect == "yes":
            testSucessed(TestName.supper_cap_power)
        else:
            testFailed(TestName.supper_cap_power)
        pass

    @classmethod
    def testRTCBatteryVoltage(cls):
        r = cmd(RTC.rtc_battery_voltage())
        if r == "":
            testFailed(TestName.rtc_battery_voltage)
            return
        v = float(r)
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
        try:
            avr0 = serial.Serial(MySerial.port_ttyAVR0,1200,timeout=2)
            mxc1 = serial.Serial(MySerial.port_ttymxc1,1200,timeout=2)
            mxc2 = serial.Serial(MySerial.port_ttymxc2,1200,timeout=2)
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
        except Exception:
            testFailed(TestName.port_ttyAVR0)
            testFailed(TestName.port_ttymxc1)
            testFailed(TestName.port_ttymxc2)
            return
        pass

    @classmethod
    def testMeter(cls):
        meterHz = 50
        testTime = 10
        startMeter = int(cmd(RTC.pulse_count_after_power_on()))
        time.sleep(testTime)
        endMeter = int(cmd(RTC.pulse_count_after_power_on()))
        one  = (endMeter - startMeter)/testTime
        if one > meterHz -10 and one < meterHz + 10:
            testSucessed(TestName.meter)
        else:
            testFailed(TestName.meter)
        pass

    @classmethod
    def testSimCard(cls):
        TestFun.testGPRS()
        pass

    @classmethod
    def testGPRS(cls):
        try:
            cmd(ThreeG.open_power)
            time.sleep(5)
            cmd(ThreeG.start)
            time.sleep(5)
            cmd("ifconfig eth0 down")
            time.sleep(5)
            if ping("www.baidu.com"):
                testFailed(TestName.sim_card)
                testFailed(TestName.gprs)
            else:
                testSucessed(TestName.sim_card)
                testSucessed(TestName.gprs)
            cmd(ThreeG.stop)
            time.sleep(2)
            # cmd(ThreeG.close_power)
            # time.sleep(2)
            cmd("ifconfig eth0 up")
        except Exception:
            write_log_to_Text("sim_card异常退出" )
            testFailed(TestName.sim_card)
            testFailed(TestName.gprs)
            pass
        pass

    @classmethod
    def testGPS(cls):
        cmd(GPS.open_power())
        time.sleep(5)
        gpsSer = serial.Serial(MySerial.port_ttymxc3,9600)
        testNum = 300
        i = 0
        while i < testNum:
            one = gpsSer.readline()
            if "$GPRMC" in one  and one.split(',')[2] == 'A':
                testSucessed(TestName.gps)
                break
            i = i + 1
        if i == testNum :
            testFailed(TestName.gps)
        gpsSer.close()
        cmd(GPS.close_power())
        pass

    @classmethod
    def testBluetooth(cls):
        try :
            cmd(Wifi.open_power)
            time.sleep(5)
            if cmdIsFailed(Bluetooth.up()):
                testFailed(TestName.bluetooth)
            else:
                testSucessed(TestName.bluetooth)
            cmd(Wifi.install_wifi_driver)
            cmd(Wifi.start)
            time.sleep(1)
            result = cmd(Wifi.scan)
            if result == 'OK':
                testSucessed(TestName.wifi_test)
            else:
                testFailed(TestName.wifi_test)
            cmd(Wifi.stop)
            cmd(Wifi.uninstall_wifi_driver)
            time.sleep(2)
            cmd(Wifi.close_power)
        except Exception:
            write_log_to_Text("Wifi异常退出" )
            # testFailed(TestName.wifi_test)

        pass

    @classmethod
    def testWifi(cls):
        TestFun.testBluetooth()
        pass

    @classmethod
    def testWlan_0(cls):
        if ping("192.168.0.201"):
            testFailed(TestName.wlan_0)
        else:
            testSucessed(TestName.wlan_0)
        pass

    @classmethod
    def testWlan_1(cls):
        isLight = askquestion("Prompt","指示灯是否亮？")
        if  isLight == 'yes':
            if ping("192.168.0.101"):
                testFailed(TestName.wlan_1)
            else:
                testSucessed(TestName.wlan_1)
        else:
            testFailed(TestName.wlan_1)
        pass

    @classmethod
    def testWlan_2(cls):
        isLight = askquestion("Prompt","指示灯是否亮？")
        if  isLight == 'yes':
            if ping("192.168.0.102"):
                testFailed(TestName.wlan_2)
            else:
                testSucessed(TestName.wlan_2)
        else:
            testFailed(TestName.wlan_2)
        pass

    @classmethod
    def testWlan_3(cls):
        isLight = askquestion("Prompt","指示灯是否亮？")
        if  isLight == 'yes':
            if ping("192.168.0.103"):
                testFailed(TestName.wlan_3)
            else:
                testSucessed(TestName.wlan_3)
        else:
            testFailed(TestName.wlan_3)
        pass

    @classmethod
    def testRTC(cls):
        if TestName.rtc["testState"] == TestItemState.success:
            return
        testTime = 'Wed May 30 00:00:00 2018'
        setTime = '2018-05-30 00:00:00'
        rtcTime = cmd("hwclock")
        if rtcTime == '':
            rtcTime = "Mon May 25 00:00:00 1970 "
        rtcTime = rtcTime[:len(testTime)]
        formatRtcTime = datetime.datetime.strptime(rtcTime, '%a %b %d %H:%M:%S %Y').strftime("%Y-%m-%d")
        if formatRtcTime == setTime[:10]:
            testSucessed(TestName.rtc)
        else:
            cmd(RTC.setRTCTime1(setTime))
            cmd(RTC.setRTCTime2())
            cmd("hwclock")
            while True:
                showinfo("Prompt","请重启设备！")
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
        r = cmd(RTC.enviroment_temperature())
        if r == "":
            testFailed(TestName.temperature)
            return
        tem = float(r)
        if tem > 15.0 and tem < 50.0:
            testSucessed(TestName.temperature)
        else:
            testFailed(TestName.temperature)
        pass

    @classmethod
    def testCom4(cls):
        try:
            com4 = serial.Serial(MySerial.port_ttymxc4,115200)
            com4.write(testStr)
            time.sleep(1)
            result = com4.read(len(testStr))
            if result == testStr:
                testSucessed(TestName.port_ttymxc4)
            else:
                testFailed(TestName.port_ttymxc4)
            com4.close()
        except Exception:
            testFailed(TestName.port_ttymxc4)
        pass

    @classmethod
    def testHidm_1(cls):
        showinfo("Prompt","请将HIDM线拔下插入HIDM_1口")
        isShow = askquestion('Prompt',"看是否显示？")
        if isShow == 'yes':
            testSucessed(TestName.hidm_1)
        else:
            testFailed(TestName.hidm_1)
        pass

    @classmethod
    def testHidm_3(cls):
        showinfo("Prompt","请将HIDM线拔下插入HIDM_3口")
        isShow = askquestion('Prompt',"看是否显示？")
        if isShow == 'yes':
            testSucessed(TestName.hidm_3)
        else:
            testFailed(TestName.hidm_3)
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
        pass

    @classmethod
    def saveSomething(cls):
        mac = getCpuNumber()
        result = getAllTestResult()
        writeToFile(getSaveResultPath(mac),result)

        recoverData = getRecoverData()
        writeWithPickle(getRecoverDataPath(mac),recoverData)
        pass



def test_all_init():
    mac = getCpuNumber()
    recoverData = readWithPickle(getRecoverDataPath(mac))
    if recoverData != "":
        i = 0
        for item in TestName.allTestItems_sdcard_test:
            item["testState"] = recoverData[i]
            item["widget"].setState(recoverData[i])
            i = i + 1
    title.config(text = "工厂测试项目\nMac:" + getCpuNumber())
    autoTest()

    pass

def autoTest():
    autoFuns = [
        TestFun.testRTC,
        TestFun.testSdCard,
        TestFun.saveSomething
    ]
    for runFun in autoFuns:
        runFun()

def gui_start():
    global init_window
    init_window = Tk() #实例化出一个父窗口
    init_window.geometry('1080x850+25+25')  #初始化窗口大小
    init_window.title("PIDS Subpanel Test")
    global title
    title = Label(init_window,text = "工厂测试项目（副板）\n" )
    title.grid(row = 0,column = 0,padx = 90,pady=15)

    fram1 = Frame(init_window)
    #第一列测试项目
    fram1_0 = Frame(fram1)
    fram1_0.grid(row=1, column=0,sticky = "N",padx=5)
    #第二列测试项目
    fram1_1 = Frame(fram1)
    fram1_1.grid(row=1, column=1,sticky = "N",padx=5)
    #第三列测试项目
    fram1_2 = Frame(fram1)
    fram1_2.grid(row=1, column=2,sticky = "N",padx=5)
    #第四列测试项目
    fram1_3 = Frame(fram1)
    fram1_3.grid(row=1, column=3, sticky = "N",padx=5)
    #第四列测试项目
    fram1_4 = Frame(fram1)
    fram1_4.grid(row=1, column=4, sticky = "N",padx=5)
    fram1.grid(row=1,sticky = "N",padx=15,pady=15)

    #开始测试按钮容器框
    fram4 = Frame(init_window)
    startButton = Button(fram4,text = "开 始 测 试",bg = "#22D911",command = autoTest)
    startButton.pack(side = "left",pady = 20,padx = 80)
    exitButton = Button(fram4, text = "退出并保存", bg = "#cccccc", command = TestFun.quitAndSave)
    exitButton.pack(side = "right",pady = 20,padx = 40)
    fram4.grid(row = 2,column =0,sticky ="W")

    fram5 = Frame(init_window)
    # log_label = Label(fram5, text="日志")
    # log_label.pack(side = "top")
    global log_data_Text
    log_data_Text = Text(fram5, width=120, height=15)  # 日志框
    log_data_Text.pack(side = "left",padx = 15)
    log_scroll = Scrollbar(fram5)
    log_scroll.pack(side="right", fill=Y)
    log_data_Text.config(yscrollcommand = log_scroll.set)
    log_scroll.config(command = log_data_Text.yview)
    fram5.grid(row=3, column=0,sticky ="W")

    rtc = TestItem(fram1_0,TestName.rtc["name"],TestName.rtc["testState"],TestFun.testRTC)
    TestName.rtc["widget"] = rtc
    sdcard = TestItem(fram1_0,TestName.sdcard_test["name"],TestName.sdcard_test["testState"],TestFun.testSdCard)
    TestName.sdcard_test["widget"] = sdcard



    test_all_init()
    init_window.mainloop()

if __name__ == "__main__":
    gui_start()