#!/usr/bin/python
# -*- coding: UTF-8 -*-
def getTestResult(state):
    if state == TestItemState.success:
        return "测试通过"
    elif state == TestItemState.fail:
        return "测试失败"
    else:
        return "没有测试"

class TestItemState:
    success = "green"
    fail = 'red'
    normal = 'grey'

class TestName(object):


    input_1 = {
        "name" : "Input1测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_2 = {
        "name" : "Input2测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_3 = {
        "name" : "Input3测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_4 = {
        "name" : "Input4测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_5 = {
        "name" : "Input5测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_6 = {
        "name" : "Input6测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_7 = {
        "name" : "Input7测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_8 = {
        "name" : "Input8测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_9 = {
        "name" : "Input9测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_10 = {
        "name" : "Input10测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    input_11 = {
        "name" : "Input11测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }


    out_1 = {
        "name" : "Out1测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    out_2 = {
        "name" : "Out2测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    sdcard_test = {
        "name" : "SD卡测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    power_voltage = {
        "name" : "电源电压测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    cap_voltage = {
        "name" : "电容电压测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    rtc_battery_voltage = {
        "name" : "RTC电池电压测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    buzzer_test = {
        "name" : "蜂鸣器测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    red_led = {
        "name" : "红灯测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    yellow_led = {
        "name" : "黄灯测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    green_led = {
        "name" : "绿灯测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    sound_record = {
        "name" : "耳机录音测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    otg_usb = {
        "name" : "OTG测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    wifi_test = {
        "name" : "WiFi测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    port_ttymxc1 = {
        "name" : "串口COM1测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    port_ttymxc2 = {
        "name" : "串口COM2测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    port_ttymxc4 = {
        "name" : "串口COM4测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    port_ttyAVR0 = {
        "name" : "串口AVR0测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    meter = {
        "name" : "Meter测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    sim_card = {
        "name" : "SIM卡测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    gprs = {
        "name" : "GPRS测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    gps = {
        "name" : "GPS测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    s_ram = {
        "name" : "S-RAM测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    temperature = {
        "name" : "温度传感器测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    supper_cap_power = {
        "name" : "超级电容供电测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    bluetooth = {
        "name" : "蓝牙测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    wlan_0 = {
        "name" : "有线网络_主测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    wlan_1 = {
        "name" : "有线网络_外设1测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    wlan_2 = {
        "name" : "有线网络_外设2测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    wlan_3 = {
        "name" : "有线网络_外设3测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    rtc = {
        "name" : "RTC测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    hidm_1 = {
        "name" : "HDMI_1测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    hidm_3 = {
        "name" : "HDMI_3测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    reset = {
        "name" : "复位测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    gprs_signal = {
        "name" : "GPRS信号强度测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }
    inputs = [input_1,input_2,input_3,
              input_4,input_5,input_6,
              input_7,input_8,input_9,
              input_10,input_11]

    allTestItems = [rtc, input_1, input_2, input_3, input_4, input_5,
                    input_6, input_7, input_8, input_9, input_10,
                    input_11, out_1, out_2, sdcard_test, buzzer_test,
                    red_led, yellow_led, green_led, power_voltage, rtc_battery_voltage,
                    sound_record, port_ttymxc1, port_ttymxc2, port_ttyAVR0, temperature,
                    meter, sim_card, gprs, gps, bluetooth, wifi_test,
                    wlan_0, wlan_1, wlan_2, wlan_3,
                    s_ram, port_ttymxc4, hidm_1, cap_voltage,
                    supper_cap_power,hidm_3,gprs_signal]
    allTestItems_sdcard_test = [rtc,sdcard_test]

