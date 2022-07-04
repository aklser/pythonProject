import os


# 参数：无，
# 返回值：字典，
# 功能：返回某些设备{"0":“”，“1”：“”}
def adb_devices_info():
    info_devices_all = os.popen("adb devices").read().splitlines()
    devicesList = {}
    i = 0
    for info_devices in info_devices_all:
        if info_devices and info_devices != "List of devices attached":
            devicesList[i] = info_devices.split("\t")[0]
            i = i + 1
    return devicesList


# 参数：设备号，
# 返回值：字典，
# 功能：返回某个设备中第三方应用{"0":“”，“1”：“”}
def adb_packageslist_3_info(devices_num):
    info_3_all = os.popen(f"adb -s {devices_num} shell pm list packages -3").read().splitlines()
    packagesList = {}
    i = 0
    for info_3 in info_3_all:
        packagesList[i] = info_3.split(":")[1]
        i = i + 1
    return packagesList


# 参数：无，
# 返回值：字典，
# 功能：返回某些设备中第三方应用{"0":“”，“1”：“”}
def adb_flow_info():
    info_flow = os.popen("adb shell cat /proc")


if __name__ == "__main__":
    a = adb_packageslist_3_info(adb_devices_info()[0])
    b = adb_devices_info()
    print(b)
    print(a)
