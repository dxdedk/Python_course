
lang = "Python"
if lang=="Python":
    print ("Hello")
print(("End"),'\n')

def get_type_of_sentence(sentence):
    last = sentence [-1]

    if last == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "sentence is " + sentence_type

print (get_type_of_sentence('Sentence'))
print ((get_type_of_sentence('Sentence?')),'\n')

def user_number(user_data):
    permit_print = True

    if permit_print and user_data == -6:
        print ("Число = -6")
    elif permit_print and user_data > 0:
        print("Число положительное")
    elif not permit_print:
        print ("Печать запрещена")

user_number(0)
user_number(-1)
user_number(10)
print ('\n')

def year_of_study(udata):

    if udata >=1 and udata <=4:
        print ("Бакалвр")
    elif udata in range (5,7):
        print("Магистр")
    elif udata >=7 and udata <=9:
        print("Аспирант")
    else:
        print ("Введите корректный год обучения")

year_of_study(0)
year_of_study(2)
year_of_study(5)
year_of_study(9)