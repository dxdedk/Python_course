#1
print ('ЗАДАНИЕ 1')
input_string = input("Введите строку: ")        #Ввод строки
length = len(input_string)                      #Возврат строки
print("Длина строки:", length, "\n")            #Вывод

#2
print ('ЗАДАНИЕ 2')
from random import randint
N2_1 = randint(0, 20)
N2_2 = randint(0, 20)
list2_1 = [i for i in range(0, N2_1)]
list2_2 = [i for i in range(0, N2_2)]
longest_length = max(len(list2_1), len(list2_2))
#print (list1)
#print (list2)
print("Длина самого длинного списка:", longest_length, "\n")

#3
print ('ЗАДАНИЕ 3')
from random import randint
N3_1 = randint(0, 20)
N3_2 = randint(0, 20)
list3_1 = [i for i in range(0, N3_1)]
list3_1.append(N3_2)
#print (N3_1)
#print (N3_2)
print(list3_1, "\n")

#4
print ('ЗАДАНИЕ 4')
from random import randint
N4_1 = randint(-1000, 1000)
def randomNumber(N4_1):
    if N4_1 in range (-100,100):
        print("+")
    else:
        print ("-")
randomNumber(N4_1)
#print (N4_1, "\n")

#5
print ('ЗАДАНИЕ 5')
str_1 = 'test'
str_2 = 'test1'
if str_1 in str_2:
    print("Да","\n")
else:
    print("Нет","\n")

#6
print ('ЗАДАНИЕ 6')
from random import randint
N6_1 = randint(-100, 100)
N6_2 = randint(-100, 100)
N6_3 = randint(-100, 100)
N6_4 = randint(-100, 100)
N6_5 = randint(-100, 100)
summ =0
list6=(N6_1,N6_2,N6_3,N6_4,N6_5)
if N6_1 > 0:
    summ=summ+1;
if N6_2 > 0:
    summ=summ+1;
if N6_3 > 0:
    summ=summ+1;
if N6_4 > 0:
    summ=summ+1;
if N6_5 > 0:
    summ=summ+1;

print(list6)
print(summ,"\n")

#7
print ('ЗАДАНИЕ 7')
y = int(input("Введите количество лет "))
m = int(input("Введите количество месяцев "))
d = y*365+m*29;
print ('Количество дней ', d,"\n")

#8
print ('ЗАДАНИЕ 8')
sentence = "место окончательной регистрации граждан"
#sentence = input("Введите предложение: ")
try:
    if all(char.isalpha() or char.isspace() for char in sentence):
        print("".join(word[0].upper() for word in sentence.split()),"\n")
    else:
        raise TypeError
except TypeError:
    print("Ошибка! Предложение должно состоять только из букв!","\n")

#9
print ('ЗАДАНИЕ 9')
number_input_9 = int (input("Введите факториал "))
a = number_input_9
factorial = 1
while a>1:
    factorial=factorial*a
    a=a-1
print ('Факториал !',number_input_9,'=',factorial,"\n")

#10
lst = [2, 4, 5, 8, 9, 13]
number = 0

while number < len(lst):
    lst[number] *= number
    number += 1
    print(lst)