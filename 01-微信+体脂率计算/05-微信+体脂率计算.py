# 案例要求： 给定一个人的体重，身高，年龄，性别，打印其体脂率


class Person:
    def __init__(self, name, age, sex, height, weight):
        try:
            self.body_fat = 0
            self.name = name

            if isinstance(age, str):
                self.age = int(age)

            if isinstance(sex, str):
                if sex in ("男", "女"):
                    self.sex = 1 if sex == "男" else 0
                else:
                    self.sex = int(bool(sex))

            if isinstance(height, str):
                self.height = float(height)
                if self.height > 100:
                    self.height /= 100

            if isinstance(weight, str):
                self.weight = float(weight)
        except Exception:
            raise Exception("数据格式不正确， 请按如下格式检查：（'Sz', 18, '男', 1.70, 55）")

    def get_body_fat(self):

        BMI = self.weight / (self.height * self.height)

        # 体脂率 = （1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8*性别（男：1 女：0）） / 100
        self.body_fat = (1.2 * BMI + 0.23 * self.age - 5.4 - 10.8 * self.sex) / 100

        # 判断是否正常
        # 正常成年人的体脂率分别是男性15%~18%和女性25%~28%
        normal_ranges = ((0.25, 0.28), (0.15, 0.18))
        normal_range = normal_ranges[self.sex]
        min_value, max_value = normal_range

        body_fat_result = "正常"
        if self.body_fat < min_value:
            body_fat_result = "偏瘦"
        elif self.body_fat > max_value:
            body_fat_result = "偏胖"

        return "{} 您好，您的体脂率为{}，正常范围在{}-{}；所以，您{}！".format(self.name, self.body_fat, min_value, max_value, body_fat_result)

if __name__ == '__main__':

    # name = input("请输入您的姓名：")
    # age = input("请输入您的年龄：")
    # sex = input("请输入您的性别（男/女）：")
    # height = input("请输入您的身高(m）：")
    # weight = input("请输入您的体重(kg)：")
    # person = Person(name, age, sex, height, weight)
    # print(person.get_body_fat())

    import itchat

    @itchat.msg_register(itchat.content.TEXT)
    def recive_text(msg):
        from_user = msg["FromUserName"]
        content = msg["Text"]

        # 使用正则表达式，按照规则解析
        import re
        result = re.match(r"(.*)[，,\s*](.*)[，,\s*](.*)[，,\s*](.*)[，,\s*](.*)", content)
        if result:
            groups = result.groups()
            # print(groups)
            person = Person(*groups)
            itchat.send_msg(person.get_body_fat(), toUserName=from_user)

        else:
            itchat.send_msg("请严格按照格式: 姓名，年龄，性别，身高(m)，体重(kg)", toUserName=from_user)

    itchat.auto_login(hotReload=True, enableCmdQR=False)

    itchat.run()

