#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: plc_c.py
@version: v1.0 
@author: WeWe 
@time: 2019/03/25 13:58
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

from lib.HslCommunication import SiemensS7Net, SiemensPLCS
import random


def func():
    pass


class s200_smart_test(object):
    def __init__(self):
        self.siemens = SiemensS7Net(SiemensPLCS.S200Smart, "192.168.0.5")
        self.result = self.siemens.ConnectServer()
        if not self.result.IsSuccess:
            print("连接失败")
        else:
            print("连接成功")

    def printReadResult(self, result):
        if result.IsSuccess:
            print(result.Content)
        else:
            print("failed   " + result.Message)

    def read_data(self):
        if not self.result.IsSuccess:
            print("读数据失败")
        else:
            self.printReadResult(self.siemens.ReadBool("M0.0"))
            self.printReadResult(self.siemens.ReadByte("M0.0"))
            self.printReadResult(self.siemens.ReadInt16("M0.0"))
            self.printReadResult(self.siemens.ReadInt32("M0.0"))
            self.printReadResult(self.siemens.ReadFloat("M0.0", 1))
            self.printReadResult(self.siemens.ReadInt16("V0.0"))

    def read_data_one_by_one(self):
        if not self.result.IsSuccess:
            print("读数据失败")
        else:
            read = self.siemens.Read("M0.0", 32)
            if read.IsSuccess:
                for i in range(32):
                    print(read.Content[i])
                print("读数据成功")
            else:
                print(read.Message)

    def write_data_to_plc(self):
        self.siemens.WriteUInt16("V100.0", 222)
        self.siemens.WriteFloat("M10.0", 12.34)


class smart200(object):
    def __init__(self):
        self.connect_flag = False
        self.siemens = None
        self.result = None
        self.connect_to_plc()
        self.max_num_int16 = 10
        self.max_num_float = 300
        self.max_num_bit = 16

    def connect_to_plc(self):
        self.siemens = SiemensS7Net(SiemensPLCS.S200Smart, "192.168.0.5")
        self.result = self.siemens.ConnectServer()
        if not self.result.IsSuccess:
            print("连接失败")
        else:
            print("连接成功")
            self.connect_flag = True

    def read_bit(self, start_address):
        """
        读取位型数据
        :param start_address: 起始地址
        :param size: 读数据个数
        :return: 读取成功，返回读取的数据；
                 读取失败，返回None
        """
        if self.result.IsSuccess:
            result = self.siemens.ReadBool(address=start_address)
            if result.IsSuccess:
                return result.Content
            else:
                print("failed  " + result.Message)
        else:
            print("读取 位型 数据失败")
        return None

    def read_byte(self, start_address, size=None):
        """
        读取char，uchar型数据
        :param start_address: 起始地址
        :param size: 读数据个数
        :return: 读取成功，返回读取的数据；
                 读取失败，返回None
        """
        if self.result.IsSuccess:
            result = self.siemens.ReadByte(address=start_address, length=size)
            if result.IsSuccess:
                return result.Content
            else:
                print("failed  " + result.Message)
        else:
            print("读取 char型 数据失败")
        return None

    def read_int16(self, start_address, size=None):
        """
        读取short，ushort型数据
        :param start_address: 起始地址
        :param size: 读数据个数
        :return: 读取成功，返回读取的数据；
                 读取失败，返回None
        """
        if self.result.IsSuccess:
            result = self.siemens.ReadUInt16(address=start_address, length=size)
            if result.IsSuccess:
                return result.Content
            else:
                print("failed  " + result.Message)
        else:
            print("读取 短整型 数据失败")
        return None

    def read_int32(self, start_address, size=None):
        """
        读取int,unsigned int型数据
        :param start_address: 起始地址
        :param size: 读数据个数
        :return: 读取成功，返回读取的数据；
                 读取失败，返回None
        """
        if self.result.IsSuccess:
            result = self.siemens.ReadInt32(address=start_address, length=size)
            if result.IsSuccess:
                return result.Content
            else:
                print("failed  " + result.Message)
        else:
            print("读取 整型 数据失败")
        return None

    def read_float(self, start_address, size=None):
        """
        读取float,unsigned float型数据
        :param start_address: 起始地址
        :param size: 读数据个数
        :return: 读取成功，返回读取的数据；
                 读取失败，返回None
        """
        if self.result.IsSuccess:
            result = self.siemens.ReadFloat(address=start_address, length=size)
            if result.IsSuccess:
                return result.Content
            else:
                print("failed  " + result.Message)
        else:
            print("读取 浮点型 数据失败")
        return None

    def write_bit(self, start_address, value=True):
        """
        写入位型数据
        :param start_address: 起始地址
        :param value: 写入的值，True 表示1，False 表示0，一次写入一个
        :return:
        """
        if self.result.IsSuccess:
            result = self.siemens.WriteBool(address=start_address, value=value)
            if not result.IsSuccess:
                print("write bit failed  ", result.Message)
        else:
            print("未连接，bit写入失败")

    def write_byte(self, start_address, value):
        """
        写入char，uchar数据
        :param start_address: 起始地址
        :param value: 写入的值，一次写入一个，
        :return:
        """
        if self.result.IsSuccess:
            result = self.siemens.WriteByte(address=start_address, value=value)
            if not result.IsSuccess:
                print("write byte failed  ", result.Message)
        else:
            print("未连接，byte写入失败")

    def write_int16(self, start_address, values):
        """
        写入short，ushort数据
        :param start_address: 起始地址
        :param values: 写入的值，可以一次写入多个，传入数组即可
        :return:
        """
        if self.result.IsSuccess:
            result = self.siemens.WriteUInt16(address=start_address, value=values)
            if not result.IsSuccess:
                print("write int16 failed  ", result.Message)
        else:
            print("未连接，int16写入失败")

    def write_int32(self, start_address, values):
        """
        写入int，unsigned int数据
        :param start_address: 起始地址
        :param values: 写入的值，可以一次写入多个，传入数组即可
        :return:
        """
        if self.result.IsSuccess:
            result = self.siemens.WriteInt32(address=start_address, value=values)
            if not result.IsSuccess:
                print("write int32 failed  ", result.Message)
        else:
            print("未连接，int32写入失败")

    def write_float(self, start_address, values):
        """
        写入float，unsigned float数据
        :param start_address: 起始地址
        :param values: 写入的值，可以一次写入多个，传入数组即可
        :return:
        """
        if self.result.IsSuccess:
            result = self.siemens.WriteFloat(address=start_address, value=values)
            if not result.IsSuccess:
                print("write float failed  ", result.Message)
        else:
            print("未连接，float写入失败")

    def print_data_list(self, data, flag):
        print("-" * 20, flag, "-" * 20)
        for i in range(len(data)):
            print(i, ": ", data[i])

    def read_test(self):
        data = self.read_int16("M0.0", self.max_num_int16)
        if data:
            print("整数：", data)
        data = self.read_float("V0.0", self.max_num_float)
        if data:
            print("浮点数：", data)
        for k in range(int(self.max_num_bit / 8)):
            for i in range(8):
                data = self.read_bit("Q%d" % ((i / 10) + k))
                print("位型数：", data)

    def write_test(self):
        write_data_int16_list = []
        write_data_float_list = []
        write_data_bit_list = []
        for i in range(self.max_num_int16):
            random_data_int16 = int(random.uniform(0, 65535))
            write_data_int16_list.append(random_data_int16)
        self.write_int16(start_address="M0.0", values=write_data_int16_list)
        self.print_data_list(write_data_int16_list, "int16")

        for i in range(self.max_num_float):
            random_data_float = round(random.uniform(0, 65535), 3)
            write_data_float_list.append(random_data_float)
        self.write_float(start_address="V0.0", values=write_data_float_list)
        self.print_data_list(write_data_float_list, "float")

        for i in range(self.max_num_bit):
            random_data_bit = random.choice([True, False])
            if random_data_bit:
                write_data_bit_list.append(1)
            else:
                write_data_bit_list.append(0)
            self.write_bit(start_address="I%d" % (i / 10), value=random_data_bit)
        self.print_data_list(write_data_bit_list, "bit")


def main():
    # plc_conn = s200_smart_test()
    # plc_conn.read_data()
    # plc_conn.read_data_one_by_one()
    # plc_conn.write_data_to_plc()
    plc_conn = smart200()
    # print(plc_conn.read_int16("Q0"))
    # for i in range(8):
    #     print("Q0.%d:" % (i), plc_conn.read_bit("Q0.%d" % (i)))
    # print(plc_conn.read_bit("Q0.0"))
    # print(plc_conn.read_bit("Q0.1"))
    # print(plc_conn.read_bit("Q0.2"))
    # print(plc_conn.read_bit("Q0.4"))
    # print(plc_conn.read_bit("Q0.5"))
    # print(plc_conn.read_bit("Q1.0"))
    # print(plc_conn.read_bit("Q1.1"))
    # print(plc_conn.read_bit("Q1.2"))
    # print(plc_conn.read_bit("Q1.3"))
    # print(plc_conn.read_bit("Q1.4"))
    plc_conn.read_test()
    # print("写", "=" * 40)
    # plc_conn.write_test()
    # print("读", "=" * 40)
    # plc_conn.read_test()


if __name__ == "__main__":
    main()
    pass
