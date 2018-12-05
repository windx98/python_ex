# 计算多少年后奥特曼兄弟的年龄是雷欧兄弟的四倍

# 初始化数据
aoteman_year = 11
leiou_year = 74
aoteman_zhangdasudu = 31 / 3
leiou_zhangdasudu = 19 / 8
year = 0
number = aoteman_year / leiou_year

# 计算年份
while number != 4:
    year = year + 1
    aoteman_year_change= aoteman_year + year * aoteman_zhangdasudu
    leiou_year_change = leiou_year + year * leiou_zhangdasudu
    number = aoteman_year_change / leiou_year_change

# 输出结果
print(f"{year}年后，奥特曼兄弟的年龄是雷欧兄弟的四倍")

