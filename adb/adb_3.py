# adb devices
# adb start-server
# adb kill-server

# adb -s 设备序列号
# d：真机（多个设备中只有一个真机时适用）
# e：模拟器（多个设备中只有一个模拟器时适用）
# s：序列号
# adb install 安装包电脑路径
# adb install -r 安装包电脑路径
# adb uninstall  应用名

# adb shell input keyevent 26           26为锁屏键
# adb shell screencap -p 截图文件路径     截屏
# adb shell monkey -p包名 -v 条数
# （崩溃记录查找”CRASH”，无响应记录查找”ANR”,内存泄露问题搜索"GC"（需进一步分析），
# 异常问题搜索“Exception”（如果出现空指针，NullPointerException，需格外重视））
# adb shell <command>    直接运行设备命令
# adb shell su –c “<command>”    直接运行root权限命令
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ls    查看文件夹
# cd    改变目录
# cat <文件名>    查看文件内容
# rm    删除文件
# mkdir <文件夹>    新建文件夹
# cp    复制文件到另一目录
# exit   退出shell命令
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# adb shell am start - n  应用名
# adb shell am start -W -n 应用名      启动时间
# adb shell am start –n <包名>/<包名>.<Activity名>   启动程序
# adb shell am force-stop <包名>    强制停止程序
# adb shell am kill <包名> 杀死与包名有关的后台进程，不影响用户体验，相当于一般的清理内存功能
# adb shell am kill-all    杀死所有后台进程
# adb shell am broadcast -a android.intent.action.MASTER_CLEAR   恢复出厂

# adb shell pm list packages -s        查看手机系统自带应用
# adb shell pm list packages -3        查看手机第三方应用
# adb shell pm list packages           查看手机所有应用
# adb shell pm clear 应用包名            清楚应用缓存信息
# adb shell pm path <包名>   查看apk安装在手机后的路径
# adb shell pm uninstall [-k] <包名>  卸载程序（-k：保留配置文件）

# adb shell dumpsys activity | findstr "com.tencent.tim"
# adb shell dumpsys window | grep init 查看手机的分辨率
# adb shell dumpsys cpuinfo            查看手机cpu情况
# adb shell dumpsys meminfo  应用包名    应用内存使用情况
# adb shell dumpsys diskstats          手机磁盘使用情况
# adb shell dumpsys battery              查看手机电池状态
# adb shell dumpsys batteryproperties    查看手机电池信息
# adb shell dumpsys window  |findstr ""  查看应用mainactivity
# adb shell dumpsys window w |findstr \/ |findstr name=    查看应用mainactivity
# adb shell dumpsys gfxinfo com.tencent.tim
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Draw:表示在Java中创建显示列表部分中，OnDraw()方法占用的时间。
# Process：表示渲染引擎执行显示列表所花的时间，view越多，时间就越长
# Execute：表示把一帧数据发送到屏幕上排版显示实际花费的时间。其实是实际显示帧数据的后台缓存区与前台缓冲区交换后并将前台缓冲区的内容显示到屏幕上的时间。
# Draw + Process + Execute = 完整显示一帧 ，这个时间要小于16ms才能保证每秒60帧。
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# adb shell ps | findstr com.tencent.tim
# 1！！！！！！！！！！！！！！！！！！！！！！！
# USER  进程uid
# PID    进程pid
# PPID  父进程pid
# VSZ   进程虚拟地址空间的大小
# RSS   进程所占的物理内存大小
# WCHAN 当前线程在哪个内核函数上睡眠
# ADDR
# S       进程状态
# #R　正在运行或在运行队列上等待调度
# #S 正在睡眠，该睡眠可被中断，如可以被信号唤醒
# #D　正在睡眠，该睡眠不可被中断，不接收信号
# #Z　zombie僵尸进程。进程死后没有被其父进程回收
# NAME      进程名
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# adb push 电脑文件路径 移动端路径         将电脑文件传输到移动端
# adb pull 移动端路径  电脑路径           将移动端文件传输到电脑
# adb help                              显示帮助信息
# adb version   显示adb版本
# adb reboot    重启手机
# adb logcat -s ActivityManager        Activity的启动时间
# adb logcat > log存储地址               查看手机日志 >>追加  >覆盖
# adb logcat -v time                   查看手机日志带时间
# adb logcat -t 5                       输出最近5行的数据
# adb logcat ActivityManager:I *:s      查看activity相关日志
# adb shell logcat | findstr START com.tencent.tim/com.tencent.mobileqq.activity.SplashActivity
# adb logcat *:W
# ！！！！！！！！！！！！！！！！！
# V—Verbose 明细（最低优先级）
# D—Debug 调试
# I—Info 信息
# W—Warm 警告
# E—Error 错误
# F—Fatal 严重错误
# S—Silent 无记载（最高优先级，没有什么会被记载）
# ！！！！！！！！！！！！！！！！！


