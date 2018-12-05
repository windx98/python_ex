
def huan(n,k,m):
    m = m - 1
    list1 = list(range(n)) # 建立初始list1
    list2 = [] # 建立出局人顺序list2 初始置空
    print(f"参与游戏人数n = {n}，开始人员序号k = {k}，数据m = {m}。")
    local = k + m # 计算第一个出局人员位置

    # 将符合条件的人剔除出list1，并按照剔除顺序将被剔除人员放入list2
    while n > 0:
        local = (local - 1) % n + 1
        list2.append(list1[local - 1] + 1)
        del list1[local - 1]
        local = local + m
        n = n - 1

    print(f"出局人顺序 {list2}")

huan(n = 8,k = 3,m = 4)