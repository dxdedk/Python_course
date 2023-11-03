#1
print ('ЗАДАНИЕ 1')
str1=["name", "part", "qwerty", "Python", "php", "go", "C"]
str_stop = ["Python", "php", "go", "C"]
def filter_str(in_str):
    if in_str in str_stop:
      return False
    else:
      return True
print(list(filter(filter_str,str1)),"\n")

#2
print ('ЗАДАНИЕ 2')
lst2 = [2, 4, 5, 8, 9, 13]
multiplicity2 = int(input("Введите интересующую кратность чисел "))
def filter_num(in_num):
    return in_num %multiplicity2 ==0
print(list(filter(filter_num,lst2)),"\n")

#3
print ('ЗАДАНИЕ 3')
def get_str_arg(*args):
    str_args = tuple(arg for arg in args if isinstance(arg, str))
    return str_args
result = get_str_arg(10, "hello", True, "world", 3.14, "qwerty")
print(result,"\n")

#4
print ('ЗАДАНИЕ 4')
str4_1 = [1, 2, 3, 4, 5]
str4_2 = [5, 6, 7, 8, 9]
cross = list(filter(lambda it: it in str4_1, str4_2))
print ("Повторяющиеся элементы ",cross,"\n")

#5
print ('ЗАДАНИЕ 5')
def les(n, k):
    if n == 0:
        return 1
    ans = 0

    for i in range(k + 1, n + 1):
        ans += les(n - i, i)
    return ans


n = int(input("Введите количество кубиков "))
if n in range (1,100):
    print(les(n, 0),"\n")
else:
    print("Введено некоректное число","\n")