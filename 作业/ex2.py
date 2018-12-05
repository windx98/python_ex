# 计算变态鸡兔同笼问题
# 初始化变量
all_heads = 168
all_feets = 231
chickens_feets = 7
chickens_head = 6
rabbits_feets = 6
rabbits_head = 3
chickens = 0
rabbits = (all_heads - chickens * chickens_head) / rabbits_head
feets = chickens_feets * chickens + rabbits * rabbits_feets

# 通过循环计算鸡和兔子的数目
while feets != all_feets:
    chickens = chickens + 1
    rabbits = (all_heads - chickens * chickens_head) / rabbits_head
    feets = chickens_feets * chickens + rabbits * rabbits_feets

# 输出鸡和兔子的数目
print(f"chickens = {chickens}, rabbits = {rabbits}")