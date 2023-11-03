class Book:
    def __init__(self, title, author):
        self.tittle = title
        self.autor = author
        self.checked_out = False

    def check_out (self):
        if self.checked_out:
            print ('Книга находится у абонента')
        else:
            self.checked_out = True
            print ('Выдаем книгу абоненту')

    def check_in(self):
        if self.checked_out:
            print("Принимаем книгу в библиотеку.")
            self.checked_out = False
        else:
            print("Книга в наличии.")

book = Book("Война и мир", "Лев Толстой")
book.check_out()
book.check_out()
book.check_in()