#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import sys

#进入当前目录
path = os.path.dirname(sys.argv[0])  
os.chdir(path)

# 空文件 便于写入此空文件到apk包中作为channel文件
src_empty_file = 'info/czt.txt'
# 创建一个空文件（不存在则创建）
f = open(src_empty_file, 'w') 
f.close()

# 获取当前目录中所有的apk源包
src_apks = []
# python3 : os.listdir()即可，这里使用兼容Python2的os.listdir('.')
for file in os.listdir('source_apk'):
    if os.path.isfile(sys.path[0] + "/source_apk/" + file):
        extension = os.path.splitext(file)[1][1:]
        if(extension == 'apk'):
            src_apks.append("source_apk/" + file)
 

def pack(channel_file):
    f = open(channel_file)
    lines = f.readlines()
    f.close()

    dest_file_name =os.path.basename(channel_file)
    dest_dir = os.path.splitext(dest_file_name)[0]

    for src_apk in src_apks:
        # file name (with extension) eg: SquareDance_v6.3.1_165_gf.apk
        src_apk_file_name = os.path.basename(src_apk)
        # 分割文件名与后缀
        temp_list = os.path.splitext(src_apk_file_name)
        # name without extension
        src_apk_name = temp_list[0]
        # 后缀名，包含.   例如: ".apk "
        src_apk_extension = temp_list[1]
        
        # 创建生成目录,与文件名相关
        output_dir = 'release_' + src_apk_name + '/' + dest_dir + '/'
        # 目录不存在则创建
        if not os.path.exists(output_dir):
            os.makedirs(output_dir) 
            
        # 遍历渠道号并创建对应渠道号的apk文件
        for line in lines:
            # 获取当前渠道号，因为从渠道文件中获得带有\n,所有strip一下
            target_channel = line.strip()
            # 拼接对应渠道号的apk
            if dest_dir == 'channel_wx' or dest_dir == 'channel_11-15' or dest_dir == 'share':
                target_apk = output_dir + target_channel + src_apk_extension
            elif dest_dir == 'channel_sem':
                ## 获取版本号 当做apk文件名字一部分
                ext = src_apk_file_name.split('_',4)
                version = ext[1].replace('v','')
               
                ## 获取渠道号的名字 当做apk 的名字一部分
                name_split = target_channel.split('_',1)
                target_channel_apk_name = name_split[1]

                target_apk = output_dir + 'tangdou_' + version + "_" + target_channel_apk_name + src_apk_extension
            else:
                target_apk = output_dir + src_apk_name + "_" + target_channel + src_apk_extension
            # 拷贝建立新apk
            shutil.copy(src_apk,  target_apk)
            # zip获取新建立的apk文件
            zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
            # 初始化渠道信息
            empty_channel_file = "META-INF/cztchannel_{channel}".format(channel = target_channel)
            # 写入渠道信息
            zipped.write(src_empty_file, empty_channel_file)
            # 关闭zip流
            zipped.close()



## 获取渠道列表
# channel_file = 'info/channel.txt'
for file in os.listdir('info/channel'): 
    extension = os.path.splitext(file)[1][1:]
    if extension == 'txt':
        dest_channel = 'info/channel/' + file
        pack(dest_channel)

## 打包完成后 拷贝或移动目录
## 1 share 目录的移动
temp_dir = os.path.splitext(src_apks[0])
release_dir = 'release_' + temp_dir[0]
sourceDir = release_dir + "/" + 'share' + "/" + 'aa.apk'
targetDir = release_dir + "/" + 'share' + "/" + 'tangdou_aa.apk'
shutil.copy(sourceDir, targetDir)


## 2 


## 上传到ftp








