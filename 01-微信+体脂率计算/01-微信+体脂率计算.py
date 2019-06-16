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
print(body_fat)
