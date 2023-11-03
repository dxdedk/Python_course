def square(number):
    return number**2

numbers = [1,2,3,4,5]
print(list(map(square,numbers)))

str_nums = ["4","8","6","5","3","2","8","9","3","5"]
print(list(map(int, str_nums)))

example_str="test better"
print(list(map(lambda x:x.upper(),example_str)))

example_str="test better"
print(''.join(list(map(lambda x:x.upper(),example_str))))

list_exp=["test better", 'abx']
print(list(map(len, list_exp)))