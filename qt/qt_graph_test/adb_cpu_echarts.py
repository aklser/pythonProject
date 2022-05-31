import subprocess
import time
from functools import reduce
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


# import  pyecharts_snapshot
# 参数：无，
# 返回值：数组，
# 功能：获取已连接的设备号
def getDeviceInfo():
    devices_info = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True)
    dev_line = devices_info.stdout.read().splitlines()
    serial_num = []
    if len(dev_line) >= 2:
        for item in dev_line:
            item = item.decode("utf-8")
            if "List" in item:
                continue
            elif "no permissions" in item:
                continue
            elif item.strip() == "":
                continue
            else:
                serial_num.append(item.split()[0])
        return serial_num
    else:
        return []


# 参数：数组，字符串，
# 返回值：数组，
# 功能：返回某些设备中某一应用的cpu占用率
def cpu_info_someone(serial_num, Application_name):
    if not serial_num:
        print("serial_num为空！")
    cpu = []
    path = "C:/Users/PC/Desktop/test_cpu_info"
    data_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    for item in serial_num:
        device_cpu_info = subprocess.Popen(f"adb -s {item} shell dumpsys cpuinfo | findstr {Application_name}",
                                           stdout=subprocess.PIPE, shell=True)
        info_need = device_cpu_info.stdout.read().splitlines()
        little_list = []
        little_name_list = []
        with open(f"{path}/{item}_{Application_name}_{data_time}.txt", "w") as f:
            for it in info_need:
                it = it.decode("utf-8")
                f.write(it + "\n")
                little_name_list.append(it.split()[1].split("/")[1])
                little_list.append(float(it.split()[0].replace("%", "")))
        if len(item) == 0 or len(little_name_list) == 0 or len(little_list) == 0:
            continue
        else:
            cpu.append([item, little_name_list, little_list])
        # print(cpu)
    # print(cpu)
    return cpu


# 参数：数组，[["qwer",["qwe"],[1]],]
# 返回值：无返回值
# 功能：在该文件夹生成一个HTML文件，以及桌面的txt文件
def my_echarts(cpu):
    n = (Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1000px", height="300px"))
         .add_xaxis(cpu[0][1])
         .set_global_opts(title_opts=opts.TitleOpts(title="cpu"),
                          datazoom_opts=opts.DataZoomOpts(is_show=True),
                          xaxis_opts=opts.AxisOpts(name="进程名"),
                          yaxis_opts=opts.AxisOpts(name="cpu占用率", axislabel_opts=opts.LabelOpts(formatter="{value}%"))
                          )
         .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
         )
    for item in cpu:
        n.add_yaxis(item[0] + ",total:" + str('%.2f' % reduce(lambda x, y: x + y, item[2])) + "%",
                    item[2])
    ec = n
    ec.render(path="cpu.html")
    ec.render_notebook()


if __name__ == "__main__":
    my_echarts(cpu_info_someone(getDeviceInfo(), "com.tencent"))
