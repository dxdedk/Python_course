double = lambda x: x+2
print (double(5))

list_values = [1,3,4,2,6,7,5,8,9]
print(list(filter(lambda x:x%2==0,list_values)))

sen='lambda adbmal'
print(list(filter(lambda  x:x!= '', sen)))

list_of_terms = (1,5,'Python',11,3.1,'box')
print(list(filter(lambda  x:isinstance(x,int), list_of_terms)))

numbers = [1,2,4,5,7,8,10,11]

def filter_num(in_num):
    return in_num %2 ==0
print(list(filter(filter_num,numbers)))

