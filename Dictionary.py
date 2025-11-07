# Словник студентів - Сердюк Максим
students = {
    21: {
        "name": "Сердюк Максим Олександрович",
        "group": "КН-43/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 87,
            "Антикорупція та доброчесність": 94,
            "Програмування": 81
        }
    },
    22: {
        "name": "Бардакова Надія Володимирівна",
        "group": "КН-43/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 89,
            "Антикорупція та доброчесність": 90,
            "Програмування": 84
        }
    },
    23: {
        "name": "Колдомасов Максим Вікторович",
        "group": "КН-43/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 85,
            "Антикорупція та доброчесність": 97,
            "Програмування": 88
        }
    },
    24: {
        "name": "Помощнікова Наталія Андріївна",
        "group": "КН-43/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 86,
            "Антикорупція та доброчесність": 89,
            "Програмування": 90
        }
    },
    25: {
        "name": "Трапезніков Максим Валерійович",
        "group": "КН-43/2",
        "course": 1,
        "subjects": {
            "Алгоритми і структура даних": 88,
            "Антикорупція та доброчесність": 90,
            "Програмування": 85
        }
    },
}


# Вивід всього словника студентів - Сердюк Максим
def show_all(data):
    if not data:
        print("Словник порожній.")
    else:
        print("\nСловник студентів")
        for student_id, info in data.items():
            print(f"\nID студента: {student_id}")
            print(f"ПІБ: {info['name']}")
            print(f"Група: {info['group']}")
            print(f"Курс: {info['course']}")
            print("Предмети та оцінки:")
            for subject, grade in info['subjects'].items():
                print(f"   {subject}: {grade}")


# Пошук студентів за групою та курсом - Бардакова Надія
def find_students_by_group_and_course(data, group_name, course_number):
    found_students = {}
    for student_id, info in data.items():
        if info['group'] == group_name and info['course'] == course_number:
            found_students[student_id] = info
    return found_students


# Рейтинг студентів за середнім балом - Помощнікова Наталія
def rating_by_average_grade(data):
    if not data:
        print("Словник порожній.")
        return

    averages = []
    for info in data.values():
        grades = list(info['subjects'].values())
        avg = sum(grades) / len(grades)
        averages.append((info['name'], avg))

    sorted_averages = sorted(averages, key=lambda x: x[1], reverse=True)

    print("\nРейтинг студентів за середнім балом")
    for i, (name, avg) in enumerate(sorted_averages, start=1):
        print(f"{i}. {name} — середній бал: {avg:.2f}")


# Редагування даних про студента - Колдомасов Максим
def edit_student_data(data):
    student_id = int(input("Введіть ID студента для редагування: "))
    if student_id not in data:
        print("Студента з таким ID не знайдено.")
        return

    student = data[student_id]
    print(f"\nРедагування даних для: {student['name']}")
    print("1. Змінити ПІБ")
    print("2. Змінити групу")
    print("3. Змінити курс")
    print("4. Змінити оцінку з предмета")
    print("0. Вихід без змін")

    choice = input("Ваш вибір: ")

    if choice == "1":
        new_name = input("Введіть новий ПІБ: ")
        student["name"] = new_name
        print("ПІБ успішно змінено.")

    elif choice == "2":
        new_group = input("Введіть нову групу: ")
        student["group"] = new_group
        print("Групу успішно змінено.")

    elif choice == "3":
        new_course = int(input("Введіть новий курс: "))
        student["course"] = new_course
        print("Курс успішно змінено.")

    elif choice == "4":
        print("Предмети студента:")
        for subject in student["subjects"]:
            print(f"- {subject}")
        subj = input("Введіть назву предмета для зміни оцінки: ")
        if subj in student["subjects"]:
            new_grade = int(input("Введіть нову оцінку: "))
            student["subjects"][subj] = new_grade
            print("Оцінку успішно змінено.")
        else:
            print("Такого предмета немає.")

    elif choice == "0":
        print("Редагування скасовано.")
        return

    else:
        print("Некоректний вибір.")


# Додавання нового студента з вибором предметів - Сердюк Максим
def add_student(data):
    new_id = max(data.keys()) + 1
    name = input("Введіть ПІБ нового студента: ")
    group = input("Введіть групу: ")
    course = int(input("Введіть курс: "))

    subjects_list = [
        "Алгоритми і структура даних",
        "Антикорупція та доброчесність",
        "Програмування"
    ]

    print("\nОберіть предмети для додавання оцінок:")
    for i, subj in enumerate(subjects_list, start=1):
        print(f"{i}. {subj}")

    subjects = {}
    print("\nВведіть номери предметів через пробіл (наприклад: 1 3):")
    choices = input("Ваш вибір: ").split()

    for ch in choices:
        if ch.isdigit() and 1 <= int(ch) <= len(subjects_list):
            subject_name = subjects_list[int(ch) - 1]
            grade = int(input(f"Введіть оцінку з предмета '{subject_name}': "))
            subjects[subject_name] = grade
        else:
            print(f"Некоректний вибір: {ch}")

    data[new_id] = {
        "name": name,
        "group": group,
        "course": course,
        "subjects": subjects
    }

    print(f"\nСтудента {name} додано з ID {new_id}.")


# Головне меню
def main():
    while True:
        print("\nМЕНЮ")
        print("1. Переглянути весь словник студентів")
        print("2. Пошук студентів за групою та курсом")
        print("3. Рейтинг студентів за середнім балом")
        print("4. Редагування даних про студента")
        print("5. Додавання нового студента")
        print("0. Вихід")

        choice = input("\nВаш вибір: ")

        if choice == "1":
            show_all(students)
        elif choice == "2":
            group = input("Введіть назву групи: ")
            course = int(input("Введіть номер курсу: "))
            found = find_students_by_group_and_course(students, group, course)
            if found:
                print(f"\n=== Результати пошуку: Група {group}, Курс {course} ===")
                show_all(found)
            else:
                print(f"Студентів у групі {group} на курсі {course} не знайдено.")
        elif choice == "3":
            rating_by_average_grade(students)
        elif choice == "4":
            edit_student_data(students)
        elif choice == "5":
            add_student(students)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


# Запуск програми
main()
