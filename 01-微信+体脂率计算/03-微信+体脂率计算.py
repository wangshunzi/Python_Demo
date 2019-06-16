# 案例要求： 给定一个人的体重，身高，年龄，性别，打印其体脂率

def get_body_fat(name, age, sex, height, weight):
    try:
        if isinstance(age, str):
            age = int(age)
        if isinstance(sex, str):
            if sex in ("男", "女"):
                sex = 1 if sex == "男" else 0
            else:
                sex = int(bool(sex))

        if isinstance(height, str):
            height = float(height)
            if height > 100:
                height /= 100

        if isinstance(weight, str):
            weight = float(weight)
    except Exception as e:
        return "数据格式不正确， 请按如下格式检查：（'Sz', 18, '男', 1.70, 55）"

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

    return "{} 您好，您的体脂率为{}，正常范围在{}-{}；所以，您{}".format(name, body_fat, min_value, max_value, body_fat_result)


name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
sex = input("请输入您的性别（男/女）：")
height = input("请输入您的身高(m）：")
weight = input("请输入您的体重(kg)：")
result = get_body_fat(name, age, sex, height, weight)
print(result)