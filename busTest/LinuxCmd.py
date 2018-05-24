#!/usr/bin/python
# -*- coding: UTF-8 -*-

def commonInput(inputMsg,target):
    return '''echo %s > /sys/devices/platform/avrctl/%s'''%(inputMsg,target)

def commonQuerry(target):
    return '''cat /sys/devices/platform/avrctl/%s'''%(target)

class Wifi:
    wifiname = 'tendaucast'
    password = '1234567890'
    open_power = commonInput("on","wifi_power")
    install_wifi_driver = '''insmod /etc/rtl8723bu.ko'''
    start = '''wpa_supplicant -Dwext -iwlan0 -c/etc/wpa_rtl8723bu.conf -B'''
    scan = ['''wpa_cli -iwlan0 scan''']
    scan_results = '''wpa_cli -iwlan0 scan_results'''
    list = '''wpa_cli -iwlan0 list_network'''
    connect = [
        '''wpa_cli -iwlan0 add_network''',
        "wpa_cli -iwlan0 add_network 0 ssid '%s'" % (wifiname),
        "wpa_cli -iwlan0 add_network 0 psk '%s'" % (password),
        "wpa_cli -iwlan0 select_network 0"
    ]
    get_ip = "dhclient wlan0"
    close_power = commonInput("off","wifi_power")
    uninstall_wifi_driver = '''rmmod rtl8723bu'''

class ThreeG:
    open_power = commonInput("on","3g_power")
    start = '''pppd call uc20'''
    see_log = '''cat /var/volatile/log/pppd.log'''
    result = '''ifconfig'''
    stop = '''killall pppd'''
    close_power = commonInput("off","3g_power")
    change_apn = '''vi /etc/ppp/uc20-connect-chat'''
    pass

class BackLight:
    @classmethod
    def setLight(cls,level):
        return '''echo %d > /sys/devices/soc0/backlight.18/backlight/backlight.18/brightness''' % level

class LedCtr:
    red_led = "led_red"
    yellow_led = "led_yellow"
    green_led = "led_green"
    @classmethod
    def openLed(cls,ledName):
        return commonInput("on",ledName)

    @classmethod
    def closeLed(cls,ledName):
        return commonInput("off",ledName)

class Buzzer:
    @classmethod
    def openBuzzer(cls):
        return commonInput("on","buzzer")

    @classmethod
    def closeBuzzer(cls):
        return commonInput("off","buzzer")
class GPS:
    @classmethod
    def open_power(cls):
        return commonInput("on","gps_power")

    @classmethod
    def close_power(cls):
        return commonInput("off","gps_power")

    @classmethod
    def gps_antenna_status(cls):
        return commonQuerry("gps_antenna")

class UsbHost:
    @classmethod
    def open_power(cls):
        return commonInput("on","usbhost_power")

    @classmethod
    def close_power(cls):
        return commonInput("off","usbhost_power")

class RTC:
    @classmethod
    def input_io(cls):
        return commonQuerry("input_io")

    @classmethod
    def power_voltage(cls):
        return commonQuerry("power_voltage")

    @classmethod
    def power_connection_status(cls):
        return commonQuerry("power_adapter")

    @classmethod
    def rtc_battery_voltage(cls):
        return commonQuerry("rtc_battery_voltage")

    @classmethod
    def supper_cap_voltage(cls):
        return commonQuerry("battery_voltage")

    @classmethod
    def enviroment_temperature(cls):
        return commonQuerry("temperature")

    @classmethod
    def enable_charger(cls):
        return commonInput("on","charger")

    @classmethod
    def disable_charger(cls):
        return commonInput("off","charger")

    @classmethod
    def enable_supper_cap_power_to_cpu(cls):
        return commonInput("on","suppercap_to_sys")

    @classmethod
    def disable_supper_cap_power_to_cpu(cls):
        return commonInput("off","suppercap_to_sys")

    @classmethod
    def pulse_count_after_power_on(cls):
        return commonQuerry("pulse_sum")

class Sound:
    @classmethod
    def show_status(cls):
        return "cat /sys/bus/platform/drivers/imx-wm8958/headphone"

    @classmethod
    def play(cls):
        return "aplay /unit_tests/audio8k16S.wav"

    @classmethod
    def record(cls):
        return "arecord -f cd -d 10 /unit_tests/ucast_test.wav"

    @classmethod
    def play_record(cls):
        return "aplay /unit_tests/ucast_test.wav"

class Cpu:
    @classmethod
    def cpuinfo_cur_freq(cls):
        return "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq"

    @classmethod
    def cpuinfo_max_freq(cls):
        return "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq"

    @classmethod
    def cpuinfo_min_freq(cls):
        return "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq"

    def cpu_temperature(self):
        return "cat /sys/devices/virtual/thermal/thermal_zone0/temp"

class Bluetooth:
    @classmethod
    def list(cls):
        return "hciconfig"

    @classmethod
    def up(cls):
        return "hciconfig hci0 up"

    @classmethod
    def scan(cls):
        return "hcitool scan"