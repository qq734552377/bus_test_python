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
    wifi_test = {
        "name" : "WiFi测试",
        "testResult" : getTestResult,
        "testState" : TestItemState.normal,
        "widget" : ""
    }