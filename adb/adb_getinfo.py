# 1、服务命令
# adb help             --adb 帮助
# adb version          --查看adb版本
# adb nodaemon server  --查看adb占用的端口号
# adb remount          --将system分区重新挂载为可读写分区
# adb root             --以root权限运行adb服务
# adb kill-server      --关闭adb服务
# adb start-server     --开启adb服务
# adb -P 端口 adb-server  --指定adb-server运行端口(默认端口5037)

# 2、连接设备命令
# adb tcpip 5555
# adb connect ip地址
# adb disconnect  --断开连接
# adb devices
# 【输出状态】：
# offline：表示设备未连接成功或无响应。
# device：设备已连接，
# no device：没有设备/模拟器连接

# 3、设备命令
# adb reboot                    --重启设备
# adb reboot bootloader         --重启到bootloader模式，即刷机模式
# adb reboot recovery           --重启到recovery模式，即恢复模式：

# 4、查看设备基本信息
# adb get-serialno                            --获取设备序列号
# adb shell getprop ro.product.brand          --获取设备品牌
# adb shell getprop ro.product.model          --获取设备型号
# adb shell getprop gsm.sim.operator.alpha    --获取运营商
# adb shell getprop ro.build.version.sdk      --获取SDK版本
# adb shell getprop ro.build.version.release  --获取Android版本
# adb shell cat /proc/cpuinfo                 --获取cpu序列号
# adb shell dumpsys battery                   --查看电池信息
# adb shell dumpsys audio                     --获取音频流信息
# adb shell dumpsys wifi | findstr Wi-Fi     --获取WIFI连接信息
# adb shell wm size                           --查看屏幕分辨率
# adb shell wm density                        --查看屏幕密度

# 5、查看设备性能信息
# adb shell ps                                --查看进程列表
# adb shell ps  | findstr 包名                --查看某个应用的进程ID
# adb shell kill 进程ID                       --杀死一个进程
# adb shell top                               --查看实时资源占用
# adb shell top -m 6                          --查看占用内存前6的app
# adb shell top -d 10                         --间隔10秒刷新一次
# adb shell dumpsys cpuinfo                   --查看CPU信息
# adb shell dumpsys gfxinfo apk包             --查看某应用的GPU绘制分析
# adb shell dumpsys meminfo apk包             --查看某应用的内存占用
# adb shell service list                      --查看后台services信息

# 6、文件操作命令
# adb pull <设备文件路径> [电脑存储路径]  --导出设备文件到电脑
# adb push <电脑文件路径> [设备存储路径]  --导入电脑文件到设备

# 7、apk应用管理命令
# adb shell pm list packages       --获取设备内所有包名
# 常用参数：
# -3  查看第三方应用
# -s  查看系统应用
# -d  查看被停用的应用
# -e  模糊查询某个应用
# -f  查看关联文件
# -i  查看package对应的安装者
# -u  查看被卸载过的package
# 【安装应用】
# adb install apk包名
# 常用参数：
# -r  覆盖安装（保留数据）
# -d  降级覆盖安装
# -g  赋予所有运行时权限
# -l  将应用安装到保护目录/mnt/asec
# -s  将应用安装到sdcard目录
# 【卸载应用】
# adb uninstall apk包名
# 常用参数：
# -k  卸载应用时保留数据和缓存目录
# 【其他命令】
# adb shell pm path 包名                                           --获取某个包名的安装路径
# adb shell dumpsys window | findstr mCurrentFocus                 --获取当前正在运行的应用包名/类名
# adb shell am start -n packageName（包名）/ActivityName（类名）   --启动应用
# adb shell am force-stop 包名                                     --强制关闭应用
# adb shell pm clear 包名                                          --清除应用数据和缓存
# adb shell dumpsys package 包名                                   --查看某个apk的应用信息、版本信息

# 8、log命令
# adb logcat   --查看日志
# 常用参数：
# 参数  日志格式
# -v    brief
# -v    process
# -v    tag
# -v    raw
# -v    time
# -v    threadtime
# -v    long
# 示例：adb logcat -v time > [电脑文件路径]
# adb logcat -c              --清空日志缓存
# adb logcat -g              --查看日志缓冲区大小
# adb logcat -G 10M          --设置日志缓冲区大小
# adb shell dmesg            --查看内核日志

# 9、快捷操作
# adb shell am start -a android.intent.action.DIAL -d tel:10010                            --编辑电话
# adb shell am start -a android.intent.action.CALL -d tel:10010                            --打电话
# adb shell am start -a android.intent.action.SENDTO -d sms:10086 --es sms_body "1091"     --编辑短信
# adb shell am start -a android.intent.action.VIEW -d http://www.baidu.com                 --打开网址
# adb shell am start -a android.intent.action.MUSIC_PLAYER                                 --打开音乐播放器
# adb shell am start -a "android.intent.action.VIEW" -t "audio/mp3" -d "file:///sdcard/music.mp3"    --播放指定音乐

# 10、模拟用户操作
# # 点击
# adb shell input tap [x] [y]                        -- 点击(x,y)坐标点
# # 滑动
# adb shell input swipe [x1] [y1] [x2] [y2]          --从坐标(x1,y1)点滑动至(x2,y2)后松开
# adb shell input swipe [x1] [y1] [x2] [y2] 1000     --从坐标(x1,y1)点滑动至(x2,y2)后松开,耗时1000毫秒
# # 常用Keyevent 键值宏定义（其他可自行百度）
# adb shell input keyevent 3        --点击HOME键
# adb shell input keyevent 4        --点击BACK键
# adb shell input keyevent 26       --点击电源键
# adb shell input keyevent 187      --打开最近应用界面
# adb shell input keyevent --longpress [keyevent键值]   --长按
# adb shell getevent   --事件监听