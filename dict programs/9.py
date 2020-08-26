jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }

jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }

students = [jack, james, dylan, jess, tom]


def total_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return (total_sum / len(marks))


def total_average_marks(stud):
    assignment_marks = total_average(stud['assignment'])
    test_marks = total_average(stud['test'])
    lab_marks = total_average(stud['lab'])

    return (0.1 * assignment_marks + 0.7 * test_marks + 0.2 * lab_marks)


def grade_calculation(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'E'


def class_average_calc(students_list):
    result_list = []

    for member in students_list:
        student_avg = total_average_marks(member)
        result_list.append(student_avg)
        return total_average(result_list)


for i in students:
    print(i['name'])
    print("________________________________________________________")
    print('\n')
    print("Average marks of %s is " % (i['name']), total_average_marks(i))
    print("The Grade Awarded for %s is " % (i['name']), grade_calculation(total_average_marks(i)))
print('________________________________________________________')

members = students
print()
print()
print("________________________________________________________")
class_average_assign = class_average_calc(members)
print("The class average is :", class_average_assign)
print("The Grade awarded for the class is :", grade_calculation(class_average_assign))
print("________________________________________________________")
