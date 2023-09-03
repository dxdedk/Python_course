number = 0

while number < 10:
    print (f"number = {number}")
    number +=1
print ("app close")


print('')

string = 'ggg'
while len(string) > 0:
    print ('Строка существует - '+ string)
    string = string[0:len(string)-1]
else:
    print ('пустая строка')


print('')

def cycle_for(items):
    for item in items:
        print(item)

#cycle_for("string")
cycle_for([0,1,2])
#cycle_for(('aa','b','c'))


print('')
def sum_of_number(my_list):
    result = 0
    for elem in my_list:
        result = result+elem
        return result

print(sum_of_number ([1,2,3]))

def sum_of_number_2(my_list):
         return sum(my_list)

print(sum_of_number_2 ([1,2,3]))


print('')
print('')

numb_break = 0
while numb_break <5:
    numb_break +=1
    if numb_break == 3:
        break
    print (f"number = {numb_break}")
print('')
numb_con = 0
while numb_con <5:
    numb_con +=1
    if numb_con == 3:
        continue
    print (f"number = {numb_con}")