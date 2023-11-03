import re
result = re.match(r'\d{2}', '123 - no string')
not_result= re.match(r'\d{2}', 'string')
print(result.group())
print(not_result)

result = re.search(r'\d{2}', '123 - no string')
print(result.group())

#result = re.findall(r'\d{2}', '12 - string, 34 no string')

result = re.fullmatch(r'\d{3}', '123')
not_result= re.fullmatch(r'\d{3}', '123 - no string')
print(result.group())
print(not_result)

def check_email(email):
    pattern = r'^[\w\.-]{1,30}@[\w\.-]{1,10}\.[\w\.-]{1,10}$'
    result = re.match(pattern, email)
    return result is not None

email = input("Введите email: ")
valid = check_email(email)
print(valid)