# 计算多少年后爷爷的年龄是玲玲的四倍

# 初始化数据
linlin_old = 11
yieyie_old = 74
year = 0
number = yieyie_old / linlin_old

# 计算年份
while number != 4:
    year = year + 1
    linlin_old_change= linlin_old + year
    yieyie_old_change = yieyie_old + year
    number = yieyie_old_change / linlin_old_change

# 输出结果
print(f"{year}年后，爷爷的年龄是玲玲的四倍")