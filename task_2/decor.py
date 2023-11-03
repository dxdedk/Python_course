#def price_calc(price,tax):
#    return price*(1+tax)
#print(price_calc(100,0.05), "руб")

def currency(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        return f'{result} руб'
    return wrapper

@currency
def price_calc(price,tax):
    return price*(1+tax)
#price_calc=currency(price_calc)
print(price_calc(100,0.05))


def res(xx):
    def wrapper(*args,**kwargs):
        result = xx(*args,**kwargs)
        return f'Результат вычислений: {result} '
    return wrapper

@res
def square(a):
    return a**2

@res
def myltiply(a):
    return a*2
print(square(5))
print(myltiply(5))