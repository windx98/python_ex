# 计算鸡兔同笼问题

# 初始化变量
chickens = 0
rabbits = 30 - chickens
chickens_feets = 2
rabbits_feets = 4
all_feets = chickens_feets * chickens + rabbits * rabbits_feets

# 通过循环计算鸡和兔子的数目
while all_feets != 82:
    chickens = chickens + 1
    rabbits = 30 - chickens
    all_feets = chickens_feets * chickens + rabbits * rabbits_feets

# 输出鸡和兔子的数目
print(f"chickens = {chickens}, rabbits = {rabbits}")
