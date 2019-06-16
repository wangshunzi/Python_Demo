# 案例要求： 给定一个人的体重，身高，年龄，性别，打印其体脂率

name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
sex = input("请输入您的性别（男/女）：")
sex = 1 if sex == "男" else 0
height = float(input("请输入您的身高(m）："))
weight = float(input("请输入您的体重(kg)："))

BMI = weight / (height * height)


# 体脂率 = （1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8*性别（男：1 女：0）） / 100
body_fat = (1.2 * BMI + 0.23 * age - 5.4 - 10.8 * sex) / 100

# 判断是否正常
# 正常成年人的体脂率分别是男性15%~18%和女性25%~28%
normal_ranges = ((0.25, 0.28), (0.15, 0.18))
normal_range = normal_ranges[sex]
min_value, max_value = normal_range

body_fat_result = "正常"
if body_fat < min_value:
    body_fat_result = "偏瘦"
elif body_fat > max_value:
    body_fat_result = "偏胖"

print("{} 您好，您的体脂率为{}，正常范围在{}-{}；所以，您{}".format(name, body_fat, min_value, max_value, body_fat_result))
