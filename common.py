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

import os
import re
import shutil
import sys
import tempfile
import zipfile

class PathNotFoundError(OSError):
    pass

def is_win():
    return os.name == "nt"

def get_bin(program_name, ext = None):
    if ext == None:
        if is_win():
            ext = ".exe"
        else:
            ext = ""
    return os.path.join(os.getcwd(), "bin", program_name + ext)

def check_file(*file_path):
    for fp in file_path:
        if not os.path.exists(fp):
            raise PathNotFoundError("%s: No such file or directory" %fp)

def mkdir(path):
    # 创建目录
    if os.path.exists(path):
        if not os.path.isdir(path):
            try:
                os.remove(path)
            except:
                pass
        else:
            return
    os.makedirs(path)

def remove_path(path):
    # 移除文件/目录(如果存在的话)
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
    elif os.path.exists(path):
        os.remove(path)

def file2file(src, dst, move=False):
    # 复制文件到文件
    # move为True时移动文件而不是复制文件
    mkdir(os.path.split(dst)[0])
    if move:
        shutil.move(src, dst)
    else:
        shutil.copyfile(src, dst)
    return dst

def dir2dir(src, dst):
    # 复制文件夹到文件夹
    mkdir(os.path.split(dst)[0])
    shutil.copytree(src, dst)
    return dst
