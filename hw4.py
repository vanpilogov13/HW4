file_1 = open('chapter1.txt', 'r')
file_2 = open('chapter2.txt', 'r')
#переводимо наші файли в лісти по строчкам щоб далі нам простіше було з ними гратися
file_1_listed = file_1.readlines()
file_2_listed = file_2.readlines()
script = open('script.txt', 'w')

#мінімум треба знати, бо файли МОЖУТЬ бути різної довжини і ПО ФАКТУ різної довжини
min_list_length = min(len(file_1_listed), len(file_2_listed))

#отут ітеруємо файли до моменту поки не закінчиться коротший
for i in range(min_list_length):
    line1 = file_1_listed[i]
    line2 = file_2_listed[i]
    if '$$$' in line1:
        new_line = input("Введіть фразу " + str(i+1) + " для персонажа 1: ")
        while len(new_line.split(" ")) < 3:
            new_line = input("Рядок повинен містити як мінімум 3 слова. Спробуйте знову: ")
        script.write(new_line + '\n')
    else:
        print("Фраза " + str(i+1) + " персонажа 1: " + str(line1))
        script.write(line1)
    if '$$$' in line2:
        new_line = input("Введіть фразу " + str(i+1) + " для персонажа 2: ")
        while len(new_line.split(" ")) < 3:
            new_line = input("Рядок повинен містити як мінімум 3 слова. Спробуйте знову: ")
        script.write(new_line + '\n')
    else:
        print("Фраза " + str(i+1) + " персонажа 2: " + str(line2))
        script.write(line2)

#отут визначаємо довший файл і ітеруємо тільки його (ну бо коротший вже закінчився)
if len(file_1_listed) > min_list_length:
    for i in range(min_list_length, len(file_1_listed)):
        line = file_1_listed[i]
        if '$$$' in line:
            new_line = input("Введіть фразу " + str(i+1) + " для персонажа 1: ")
            while len(new_line.split()) < 3:
                new_line = input("Рядок повинен містити як мінімум 3 слова. Спробуйте знову: ")
            script.write(new_line + '\n')
        else:
            print("Фраза " + str(i + 1) + " персонажа 1: " + str(line1))
            script.write(line)
else:
    for i in range(min_list_length, len(file_2_listed)):
        line = file_2_listed[i]
        if '$$$' in line:
            new_line = input("Введіть фразу " + str(i+1) + " для персонажа 2: ")
            while len(new_line.split()) < 3:
                new_line = input("Рядок повинен містити як мінімум 3 слова. Спробуйте знову: ")
            script.write(new_line + '\n')
        else:
            print("Фраза " + str(i + 1) + " персонажа 2: " + str(line1))
            script.write(line)

#закриваємо файли шоб інфа не "витікла"
file_1.close()
file_2.close()
script.close()

print("Скрипт готовий! Роботу зроблено!")