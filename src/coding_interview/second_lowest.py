def find_second_lowest(student_list):
    student_list.sort(key=lambda s: s[0])
    student_list.sort(key=lambda s: s[1])
    lowest_score = student_list[0][1]
    second_lowest = student_list[1][1]
    i = 2
    while lowest_score == second_lowest:
        second_lowest = student_list[i][1]
    for student in student_list[1::1]:
        if second_lowest == student[1]:
            print(student[0])


if __name__ == '__main__':
    students = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
    find_second_lowest(students)
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    find_second_lowest(students)
