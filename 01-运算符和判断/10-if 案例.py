#  判断奇数和偶数
# 用户输入一个数字
num = int(input("请输入一个整数: "))

# 判断奇数或偶数
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")


# 判断是否为闰年
# 能被 4 整除但不能被 100 整除，或者能被 400 整除。

# 用户输入年份
year = int(input("请输入年份: "))

# 判断是否为闰年
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")

# 成绩等级判定
# 这个程序根据用户输入的分数，判定成绩等级。
# 用户输入分数
score = int(input("请输入分数: "))

# 根据分数输出成绩等级
if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 简单登录验证
# 模拟一个简单的登录系统，用户需要输入用户名和密码。系统会验证输入是否正确。

# 定义正确的用户名和密码
correct_username = "admin"
correct_password = "12345"

# 用户输入用户名和密码
username = input("请输入用户名: ")
password = input("请输入密码: ")

# 验证用户名和密码
if username == correct_username and password == correct_password:
    print("登录成功")
else:
    print("用户名或密码错误")

# 多重条件的商品折扣系统
#
# 这个程序根据用户购买的商品数量来决定折扣。
#
# 	•	购买 10 个及以上，享受 20% 折扣
# 	•	购买 5 到 9 个，享受 10% 折扣
# 	•	购买 5 个以下，不享受折扣

# 用户输入购买的商品数量
quantity = int(input("请输入购买的商品数量: "))

# 计算折扣
if quantity >= 10:
    discount = 0.20
    print(f"你享受 {discount * 100}% 的折扣")
elif quantity >= 5:
    discount = 0.10
    print(f"你享受 {discount * 100}% 的折扣")
else:
    discount = 0
    print("你不享受折扣")

# 判断用户输入的数字正负零
#
# 这个程序判断用户输入的数字是正数、负数还是零。

# 用户输入一个数字
num = float(input("请输入一个数字: "))

# 判断正负
if num > 0:
    print("这是一个正数")
elif num < 0:
    print("这是一个负数")
else:
    print("这是零")

# 基于用户年龄的分类
#
# 这个程序根据用户输入的年龄，将其分为儿童、青少年、成年人和老年人。

# 用户输入年龄
age = int(input("请输入你的年龄: "))

# 根据年龄进行分类
if age < 12:
    print("儿童")
elif 12 <= age < 18:
    print("青少年")
elif 18 <= age < 60:
    print("成年人")
else:
    print("老年人")

# 商品购买判断与折扣
#
# 一个在线商店中，只有当用户有会员卡且购物金额超过一定数值时，才能享受额外折扣。

has_membership = input("你是否有会员卡？(是/否): ")
amount = float(input("请输入购买金额: "))

if has_membership == "是":
    if amount >= 200:
        print("你享受20%的折扣")
    else:
        print("购买金额不足，无法享受折扣")
else:
    if amount >= 200:
        print("非会员但购买金额超过200，享受10%折扣")
    else:
        print("非会员且购买金额不足200，无法享受折扣")
# 在这个案例中，首先检查用户是否持有会员卡。若是会员，进一步判断其购买金额是否足够享受 20% 的折扣。非会员购买金额超过 200 则享受 10% 的折扣，若不满足条件则无法享受折扣。