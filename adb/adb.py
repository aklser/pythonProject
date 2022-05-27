import os
import subprocess
import time


# 获取设备标识（序列号、ip）
def getDevicesInfo():
    out = subprocess.Popen("adb devices", stdout=subprocess.PIPE)
    devicesList = out.stdout.read().splitlines()
    # devicesList = out.stdout.readlines()
    serial_nos = []
    if len(devicesList) >= 2:
        for item in devicesList:
            item = item.decode("utf-8")
            if "List" in item:
                continue
            elif "no permissions" in item:
                continue
            elif item.strip() == "":
                continue
            else:
                serial_nos.append(item.split()[0])

        return serial_nos
    else:
        return []


# 如何获取特定进程的pid
def getPid(devices, process):
    cmd = f"adb -s {devices} shell ps | findstr {process}"
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    infos = out.stdout.read().splitlines()
    pidlist = []
    if len(infos) >= 1:
        for i in infos:
            i = i.decode("utf-8")
            pid = i.split()[1]
            if pid not in pidlist:
                pidlist.append(pid)
        return pidlist
    else:
        return []


# 读取log
def Logcat(devices):
    t = time.time()
    dateTime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(t))
    path = "C:/Users/PC/Desktop"
    try:
        my_file = f"{path}/Logcat_ApplicationName_{devices}_{dateTime}.txt"
        logcat_file = open(my_file, "w")

        cmdLine = f"adb -s {devices} logcat -v time"
        subprocess.Popen(cmdLine, stdout=logcat_file, shell=True, stderr=subprocess.PIPE)

        time.sleep(2)
        pidList = getPid(devices, "logcat")
        if len(pidList) < 1:
            pass
        else:
            for index in range(len(pidList)):
                try:
                    cmd = f"adb -s {devices} shell kill {pidList[index]}"
                    subprocess.Popen(cmd, shell=True)
                    print("保存成功！")
                except:
                    print("cmd命令错误")
        logcat_file.close()
    except:
        print("71行")


# 停止monkey进程
def stopMonkey(devices):
    if devices:
        pidList = getPid(devices, "monkey")
        if len(pidList) < 1:
            print("monkey进程已全部关闭！")
        else:
            for index in range(len(pidList)):
                try:
                    cmd = f"adb -s {devices} shell  kill {pidList[index]}"
                    subprocess.Popen(cmd, shell=True)
                except:
                    print("cmd报错！")


if len(getDevicesInfo()) < 1:
    print("无设备连接")
else:
    print(getDevicesInfo())
    print(getDevicesInfo()[0])
    print(getPid(getDevicesInfo()[0], "com.tencent.tim"))
    print(Logcat(getDevicesInfo()[0]))
