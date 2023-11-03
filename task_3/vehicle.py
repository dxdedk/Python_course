class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def info(self):
        print (f'{self.brand}, \n{self.model}, \n{self.year}, \n{self.price}')
class car_info(Car):
    def __init__(self, brand, model, year, price, n_doors,style):
        super().__init__(brand, model, year, price)
        self.n_doors = n_doors
        self.style = style


car1 = car_info ('BMW', 'm5', 2010, 100, 5,'седан')

car1.info()