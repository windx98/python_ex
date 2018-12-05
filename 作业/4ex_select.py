import numpy as np
import pandas as pd

# 把日期转化为周几和小时相关，例：2003-10-10 16:10:00转化为周五、16 此处规则为如16:00:00到16:59:59一概转化为16


def make_data_need(data):
    weekday = []
    hour = []
    for each in data.time:
        # 转化时间
        weekday.append(each.weekday() + 1)
        hour.append(each.strftime('%H'))
    # 把处理得到的list转化为dataframe并添加到data中，然后从中提取部分列数据组成新的dataframe
    data['weekday'] = pd.DataFrame({'': weekday})
    data['hour'] = pd.DataFrame({'': hour})
    data_need = data[["flag", "weekday", "hour"]].copy()
    return(data_need)

# 以天为单位统计


def select_day(data_need):
    message_need = []
    for day in range(1, 8):
        # 从datafrom中找到指定星期几的数据
        data_need_day = data[data_need.weekday == day]
        # 进一步选出错误的那一部分
        data_need_day_flag_wrong = data_need_day[data_need_day.flag == 1]
        # 得到全部、准确、错误、比率信息
        all_days = len(data_need_day)
        wrong_days = len(data_need_day_flag_wrong)
        right_days = all_days - wrong_days
        wrong_ratio = str(round(wrong_days / all_days * 100, 2)) + ' %'
        message_need.append([wrong_days, right_days, all_days, wrong_ratio])

    # 得到的内容转化为dataframe并处理得到比较好看的样子，然后返回
    name_message = ['周一', '周二', '周三', '周四', '周五', '周六', '周天']
    get_data = pd.DataFrame({'周一': message_need[0:1][0]})
    for i in range(1, 7):
        get_data.insert(i, '{}'.format(name_message[i]), pd.DataFrame({'': message_need[i:i + 1][0]}))
    get = pd.DataFrame(get_data).transpose()
    get.columns = ['wrong', 'right', 'all', 'wrong_ratio']
    return(get)

# 以小时为单位统计


def select_hour(data_need):
    message_need = []
    for each in range(0, 24):
        # 按照一定规则构建变量，方便下面调用
        if each < 10:
            each_temp = '0' + '{}'.format(each)
        else:
            each_temp = '{}'.format(each)
        # 从datafrom中找到指定的数据
        data_need_day = data_need[data_need.hour == each_temp]
        # 进一步选出错误的那一部分
        data_need_day_flag_wrong = data_need_day[data_need_day.flag == 1]

        # 得到全部、准确、错误、比率信息
        all_days = len(data_need_day)
        wrong_days = len(data_need_day_flag_wrong)
        right_days = all_days - wrong_days
        wrong_ratio = str(round(wrong_days / all_days * 100, 2)) + ' %'
        message_need.append([wrong_days, right_days, all_days, wrong_ratio])

    # 得到的内容转化为dataframe并处理得到比较好看的样子，然后返回
    print(message_need[23])
    print(message_need[22])
    x = message_need[23][0] + message_need[22][0]
    # print(x)
    name_message = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-21', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-0']
    get_data = pd.DataFrame({'0-1': message_need[0:1][0]})
    for i in range(1, 24):
        get_data.insert(i, '{}'.format(name_message[i]), pd.DataFrame({'': message_need[i:i + 1][0]}))
    get = pd.DataFrame(get_data).transpose()
    get.columns = ['wrong', 'right', 'all', 'wrong_ratio']
    return(get)


if __name__ == '__main__':
    # 从excel中导入数据转化为dataframe形式，并添加标签
    data = pd.read_excel('jdt.xlsx', header=None)
    data.columns = ['a', 'time', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'flag']
    data_need = make_data_need(data)
    select_by_day = select_day(data_need)
    select_by_hour = select_hour(data_need)
    # 保存结果
    select_by_day.to_excel('4ex_by_day.xlsx')
    select_by_hour.to_excel('4ex_by_hour.xlsx')
