import os
import sys
sys.path.append('../IoT')
import Interface
import time
from time import sleep


def get_dir(path):  # 获取目录路径
        print("所有目录路径是：")
        for root, dirs, files in os.walk(path):
            for file in files:
                print(os.path.join(path,file))

if __name__ == "__main__":
    index = 0
    while 1:
        print("index" + i)
        sleep(1)
        i +=1
        if(i>=60):
            break