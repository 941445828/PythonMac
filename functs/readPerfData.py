# coding = utf-8
"""
@Author: sujie
@Create on:
@Modify on:
@File: macOS，读取csv内容
"""


def read_data(file_path):
    file = file_path
    with open(file) as f:
        content = f.readlines()
    data_len = len(content)
    data = []
    for i in range(data_len):
        if 'cpu' in file_path:
            data.append(content[i].split("\n")[0])  # 读取每一行数据，组成一个list
        elif 'mem' in file_path:
            men_num = int(content[i].split("\n")[0])
            data.append(round(men_num / 1024, 2))  # 将KB换成MB  读取每一行数据，组成一个list
    # print(len(data))
    # print(data)
    return data


# read_data('/Users/testeeo/Documents/mac_story/csv/mem_录课模式_v5.0.0.19_mac-intel_1675755446.csv')
# read_data('/Users/testeeo/Documents/mac_story/csv/cpu_录课模式_v5.0.0.19_mac-intel_1675755446.csv')