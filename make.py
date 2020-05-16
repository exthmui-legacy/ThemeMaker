#!/usr/bin/env python3
# encoding: utf-8

"""
    Copyright (C) 2019-2020 The exTHmUI Open Source Project

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

VERSION = "1.0.0"
GITHUB_URL = "https://github.com/exTHmUI/ThemeMaker"

# 签名参数
SIGNER_PARAM = "sign --key testkey.pk8 --cert testkey.x509.pem"

import os
import sys
import tempfile
from common import *

def main(src, out, resapk):
    check_file(src)
    if (os.path.exists(out)):
        remove_path(out)
    appTmp = tempfile.mkdtemp("", "ThemeMaker_")
    print("Copying files...")
    remove_path(appTmp)
    dir2dir(src, appTmp)
    remove_path(os.path.join(appTmp, "overlay"))
    if os.path.exists(os.path.join(src, "overlay")):
        mkdir(os.path.join(appTmp, "assets", "overlay"))
        print("Making overlay packages...")
        for subfile in os.listdir(os.path.join(src, "overlay")):
            overlay = os.path.join(src, "overlay", subfile)
            if os.path.isdir(overlay):
                try:
                    overlayApkPath = os.path.join(appTmp, "assets", "overlay", subfile)
                    doAAPT(overlay, overlayApkPath + "-raw.apk", resapk)
                    doZipAlign(overlayApkPath + "-raw.apk", overlayApkPath)
                    signAPK(overlayApkPath)
                    remove_path(overlayApkPath + "-raw.apk")
                except:
                    print("Failed to pack " + subfile)

    print("Packing...")
    doAAPT(appTmp, os.path.join(appTmp, "raw.apk"), resapk)
    doZipAlign(os.path.join(appTmp, "raw.apk"), out)
    signAPK(out)
    print("Done!")

def doAAPT(src, out, resapk):
    androidManifestFile = os.path.join(src, "AndroidManifest.xml")
    check_file(androidManifestFile)
    cmd = " -M \"" + androidManifestFile + "\""
    assetsFile = os.path.join(src, "assets")
    if (os.path.exists(assetsFile)):
        cmd += " -A " + "\"" + assetsFile + "\""
    resFile = os.path.join(src, "res")
    if (os.path.exists(resFile)):
        cmd += " -S " + "\"" + resFile + "\""
    for res in resapk:
         cmd += " -I " + "\"" + res + "\""
    cmd += " -F " + "\"" + out + "\""
    os.system(" ".join((get_bin("aapt"), "p", cmd)))

def doZipAlign(src, out):
    os.system(" ".join((get_bin("zipalign"), "4", "\"" + src + "\"", "\"" + out + "\"")))

def signAPK(src):
    if is_win():
        ext = ".bat"
    else:
        ext = ""
    os.system(" ".join((get_bin("apksigner", ext=ext), SIGNER_PARAM, "\"" + src + "\"")))


if __name__ == '__main__':
    try:
        src = str(sys.argv[1])
        out = str(sys.argv[2])
    except IndexError:
        print('ThemeMaker v%s' %VERSION)
        print('Author: cjybyjk')
        print('Github URL: %s' %GITHUB_URL)
        print('\nUsage:  make.py <src> <out> [resource packages] \n')
        sys.exit()

    try:
        resapk = sys.argv[3:]
    except IndexError:
        resapk = ["framework-res.apk"]
    if len(resapk) == 0 : resapk = ["framework-res.apk"]
    main(src, out, resapk)
    sys.exit(0)
