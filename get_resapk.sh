#!/usr/bin/sh
echo 请连接手机，打开USB调试模式
read -s -n1 -p "然后按下任意键继续"
echo
adb pull /system/framework/framework-res.apk framework-res.apk
