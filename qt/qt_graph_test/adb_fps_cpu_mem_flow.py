import os
import subprocess
from functools import reduce


# 参数：字符串，字符串
# 返回值：
# 功能：返回设备中某一应用的cpu占用率
def cpu_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return 0
    cpu = {}
    device_cpu_info = subprocess.Popen(f"adb -s {serial_num} shell dumpsys cpuinfo | findstr {Application_name}",
                                       stdout=subprocess.PIPE, shell=True)
    device_cpu_num = os.popen('adb shell cat /proc/cpuinfo | find /c /i "processor"').read()

    info_need = device_cpu_info.stdout.read().splitlines()
    little_list = []
    i = 0
    for it in info_need:
        it = it.decode("utf-8")
        i = i + float(it.split()[0].replace("%", ""))
    i = i / int(device_cpu_num)
    little_list.append("%.2f" % i)
    if len(little_list) != 0:
        cpu[serial_num] = little_list
    return cpu


# 参数：数组，字符串，
# 返回值：字典，
# 功能：返回某些设备中某一应用的内存占用{"设备序列号":[]}
def mem_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return {}
    mem = {}
    devices_mem_info = os.popen(f"adb -s {serial_num} shell dumpsys meminfo {Application_name}")
    info_all_lines = devices_mem_info.read().splitlines()
    if len(info_all_lines) < 2:
        print(f"{Application_name}未打开！")
        return {}
    little_list = []
    little_dict = {}
    for info_line in info_all_lines:
        if "PSS:" in info_line:
            little_dict = info_line.split()
    little_list.append(int(little_dict[2]) + int(little_dict[5]) + int(little_dict[9]))
    little_list[0] = little_list[0] // 1024
    if len(little_list) != 0:
        mem[serial_num] = little_list
    return mem


# 参数：数组，字符串，
# 返回值：字典，
# 功能：返回某些设备中某一应用的fps{"设备序列号":[]}
def fps_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return {}
    fps = {}
    devices_fps_info = subprocess.Popen(f"adb -s {serial_num} shell dumpsys gfxinfo {Application_name}", shell=True,
                                        stdout=subprocess.PIPE)
    info_all_lines = devices_fps_info.stdout.read().decode("utf-8").splitlines()
    if len(info_all_lines) < 2:
        print(f"{Application_name}未打开！")
        return {}
    little_list = []
    # little_dict = {}
    flag = False
    jank_count = 0
    extra_jank = 0
    for info_line in info_all_lines:
        if not info_line.strip():
            flag = False
        if flag:
            little_list.append(reduce(lambda x, y: float(x) + float(y), info_line.split()))
        if "Draw" in info_line and "Prepare" in info_line and "Process" in info_line:
            flag = True
    for l_item in little_list:
        if l_item > 16.67:
            jank_count += 1
        if l_item % 16.67 == 0:
            extra_jank += round(l_item / 16.67) - 1
        else:
            extra_jank += round(l_item / 16.67)
    # print(little_list)
    if len(little_list) == 0:
        print("请对应用进行操作后再启动该脚本！")
        return {}
    myfps = round(len(little_list) * 60 / (len(little_list) + extra_jank))
    fps[serial_num] = [myfps, jank_count, len(little_list)]
    # print(little_dict)
    # print(len(little_list))
    return fps


def flow_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return {}
    mem = {}
    devices_flow_info = os.popen(f"adb  -s {serial_num} shell cat /proc/net/dev")
    info_all_lines = devices_flow_info.read().splitlines()
    if len(info_all_lines) < 2:
        print(f"{Application_name}未打开！")
        return {}
    little_list = []
    little_dict = {}
    for info_line in info_all_lines:
        if "wlan0:" in info_line:
            little_dict = info_line.split()
            print(little_dict)
    little_list.append(int(little_dict[1]))
    little_list.append(int(little_dict[9]))
    if len(little_list) != 0:
        mem[serial_num] = little_list
    return mem


if __name__ == "__main__":
    a = flow_info_one("xghmozaiwgcylr7p", "com.tencent.tim")
    print(a)
