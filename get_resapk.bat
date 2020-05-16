@echo off
echo 请连接手机，打开USB调试模式
echo 然后按下任意键继续
pause > NUL
adb pull /system/framework/framework-res.apk framework-res.apk
