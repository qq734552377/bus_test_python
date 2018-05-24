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

class TestName:
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