class DataBase:
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)

        return cls.__isinstance
    def __init__(self, user, password, port):
        self.user =user
        self.password = password
        self.port = port

    def connect(self):
        print (f'соединения с БД: {self.user}, {self.password},{self.port}')


    @staticmethod
    def close():
        print ('Закрытие соединения с БД')

U1 = DataBase ('U1', 'qwerty', '14')
U2 = DataBase ('U2', 'ytrewq', '41')
U1.connect()
U1.close()
U2.connect()
U2.close()