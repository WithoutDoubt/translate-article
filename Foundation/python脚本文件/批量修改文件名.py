import os
import re
import sys

# 此文件中包含的文件
fileList = os.listdir(r,"./")      # 文件夹

print（"修改前：" + str(filrList)[1]）

currentpath  = os.getcwd()

# 待修改文件夹的位置
os.chdir(r,"")

num = 1

for fileName in fileList:
    pat = ".+\.(wav)"

    pattern = re.findall(pat,fileName)

    os.rename(fileName , (str(num + 839) + '.' + pattern[0]))

    num = num + 1

print ("ok")

