class Student:
    def __init__(self, name, age, weghit):
        self.name = name
        self.age = age
        self.weghit = weghit

    def introduce(self):
        print("ชื่อ:", self.name)
        print("อายุ:", self.age)
        print("น้ำหนัก:", self.weghit)

s1 = Student("Nam", "17 ปี", "50.5 กิโลกรัม")
s1.introduce()
