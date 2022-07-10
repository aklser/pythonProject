import cgitb
import os
import subprocess
import time
from functools import reduce
import adb_cpu_echarts
from pyecharts.charts import Line, Grid
from pyecharts import options as opts
from pyecharts.globals import ThemeType


# 参数：字典
# 返回值：无返回值，
# 功能：在该文件夹生成html
def draw_line_cpu(dict):
    if len(dict) == 0:
        print("dict为空！")
        return 0
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1000px", height="300px"))
            .add_xaxis([i for i in range(len(dict[devices_info[0]]))])
            .set_global_opts(title_opts=opts.TitleOpts(title="cpu"),
                             datazoom_opts=opts.DataZoomOpts(is_show=True),
                             xaxis_opts=opts.AxisOpts(name="时间"),
                             yaxis_opts=opts.AxisOpts(name="cpu占用率",
                                                      axislabel_opts=opts.LabelOpts(formatter="{value}%"))
                             )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    for item in dict:
        line.add_yaxis(item, dict[item])
    line.render("test_cpu.html")
    line.render_notebook()


# 参数：字典
# 返回值：无返回值，
# 功能：在该文件夹生成html
def draw_line_mem(dict):
    if len(dict) == 0:
        print("dict为空！")
        return 0
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1000px", height="300px"))
            .add_xaxis([i for i in range(len(dict[devices_info[0]]))])
            .set_global_opts(title_opts=opts.TitleOpts(title="内存"),
                             datazoom_opts=opts.DataZoomOpts(is_show=True),
                             xaxis_opts=opts.AxisOpts(name="时间"),
                             yaxis_opts=opts.AxisOpts(name="内存占用",
                                                      axislabel_opts=opts.LabelOpts(formatter="{value}MB"))
                             )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    for item in dict:
        line.add_yaxis(item, dict[item])
    line.render("test_mem.html")
    line.render_notebook()


# 参数：字典
# 返回值：无返回值，
# 功能：在该文件夹生成html
def draw_line_fps(dict):
    if len(dict) == 0:
        print("dict为空！")
        return 0
    my_list = [i for i in range(len(dict[devices_info[0]][0]))]
    line1 = (
        Line()
            .add_xaxis(my_list)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="fps"),
            datazoom_opts=opts.DataZoomOpts(is_show=True, xaxis_index=[0, 1]))
    )
    line2 = (
        Line()
            .add_xaxis(my_list)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="掉帧率", pos_top="50%"),
            legend_opts=opts.LegendOpts(pos_top="50%"))
    )
    for item in dict:
        line1.add_yaxis(item, dict[item][0])
        line2.add_yaxis(item, dict[item][1])
    grid = (
        Grid(init_opts=opts.InitOpts(width="1000px", height="600px"))
            .add(line1, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line2, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    grid.render("test_fps.html")
    grid.render_notebook()


# 参数：数组，字符串，
# 返回值：字典，
# 功能：返回某些设备中某一应用的cpu占用率{"设备序列号":[]}
def cpu_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return 0
    cpu = {}
    for item in serial_num:
        device_cpu_info = subprocess.Popen(f"adb -s {item} shell dumpsys cpuinfo | findstr {Application_name}",
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
        if len(item) == 0 or len(little_list) == 0:
            continue
        else:
            cpu[item] = little_list
    return cpu


# 参数：数组，字符串，
# 返回值：字典，
# 功能：返回某些设备中某一应用的内存占用{"设备序列号":[]}
def mem_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return {}
    mem = {}
    for s_item in serial_num:
        devices_mem_info = subprocess.Popen(f"adb -s {s_item} shell dumpsys meminfo | findstr {Application_name}",
                                            shell=True, stdout=subprocess.PIPE)
        info_all_lines = devices_mem_info.stdout.read().decode("utf-8").splitlines()
        if len(info_all_lines) < 2:
            print(f"{Application_name}未打开！")
            return {}
        little_list = []
        little_dict = {}
        for info_line in info_all_lines:
            little_dict[info_line.split()[1]] = int(info_line.split()[0].replace("K:", "").replace(",", ""))
        little_list.append(reduce(lambda x, y: x + y, [*little_dict.values()]))
        if len(s_item) == 0 or len(little_list) == 0:
            continue
        else:
            mem[s_item] = little_list
    return mem


# 参数：数组，字符串，
# 返回值：字典，
# 功能：返回某些设备中某一应用的fps{"设备序列号":[]}
def fps_info_one(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
        return {}
    fps = {}
    for s_item in serial_num:
        devices_fps_info = subprocess.Popen(f"adb -s {s_item} shell dumpsys gfxinfo {Application_name}", shell=True,
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
        fps[s_item] = [myfps, jank_count, len(little_list)]
        # print(little_dict)
        # print(len(little_list))
    return fps


# 参数：字符串，int
# 返回值：无返回值或0，
# 功能：通过设备序列号与应用名生成html
def do_cpu_line(app):
    n = cpu_info_one(devices_info, app)
    return n


def do_mem_line(app):
    n = mem_info_one(devices_info, app)
    return n


def do_fps_line(app):
    n = fps_info_one(devices_info, app)
    return n


if __name__ == "__main__":
    devices_info = adb_cpu_echarts.getDeviceInfo()
    # pass
    # cgitb.enable()
    a = do_cpu_line("com.tencent.tim")
    print(a)
    # do_mem_line("com.tencent.tim", 6)
    # do_fps_line("com.tencent.tim", 60)
