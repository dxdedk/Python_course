try:
    print(a)
except:
    print('переменная А не определена')
print('')
try:
    print(a)
except Exception as ex:
    print('переменная А не определена')
    print(ex)

print('')
print('')

try:
    k=1/0
    print(k)
except ZeroDivisionError:
    k=0
    print ("app close")
print('')
print('')
try:
    r=1/0
    #print(c)
except ZeroDivisionError:
    print ("app close")
finally:
    print('finally')

print('')
print('')

x=-1
if x<0:
    raise Exception("число меньше нуля")