'''
本程序用于读取6层所有房间一天内的温度变化曲线
'''
# -*- coding: utf-8 -*-
# ping 39.100.78.210
import sys
sys.path.append('C:\\Users\\xuyang\\Desktop\\DSP2.0\\IoT')
import Interface
import time
from time import sleep

if __name__ == '__main__':
    # 房间号
    i = [(6, 1, 100), (6, 2, 100), (6, 3, 100), (6, 4, 60), (6, 5, 60), (6, 6, 60), (6, 7, 30), (6, 8, 30), (6, 9, 30), (6, 10, 10), (6, 11, 10), (6, 11, 10)]
    for room in i:
        Interface.controlRoom(room[0], room[1], room[2])
    # 写入开度设置
    with open("./daily_temp_curve/setting.txt", "a") as f:
        for room in i:
            f.write("time:{}\troom:{}\tkaidu:{}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), room[0:2], room[2]))
    while True:
        try:
            for room in i:
                #设定的温度, 当前温度, 当前开度
                t_set, t_now, kaidu_now = Interface.dataForPID(room[0], room[1])
                date = time.strftime("%Y-%m-%d %H:%M:%S")
                localtime = time.time()
                #写入文件
                with open("./daily_temp_curve/state_in_{}_{}.txt".format(room[0],room[1]), "a") as f:
                    f.write("{:.7f}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(localtime, date, room[0], room[1], t_set, t_now, kaidu_now))
                #打印输出
                print(localtime, date, room, t_set, t_now, kaidu_now)
        except Exception as e:
            print("*********************读取温度数据出现错误...*******************")
        sleep(30)