class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'


swara = Person('Swara', 10)
vibha = Person('Vibha', 3)
sonali = Person('Sonali', 30)
datta = Person('Datta', 31)

my_list = [swara, vibha, sonali, datta]
print(my_list)
# Sort by name
my_list.sort(key=lambda p: p.name)  # [Datta: 31, Sonali: 30, Swara: 10, Vibha: 3]
# Sort ny age
my_list.sort(key=lambda p: p.age)  # [Vibha: 3, Swara: 10, Sonali: 30, Datta: 31]

print(my_list)

if __name__ == '__main__':
    student_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    student_list.sort()
    print(student_list)
    student_list.sort(key=lambda s: s[1])
    print(student_list)

    max_score = student_list[0][1]
    second_hihest = student_list[1][1]
    for student in student_list[1::1]:
        if second_hihest == student[1]:
            print(student[0])
