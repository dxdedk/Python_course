class Data:
    def __init__(self, data):
        print("data processing:", data)

    @staticmethod
    def fetch_state():
        print("state fetching")


Data.fetch_state()

data1 = Data([1, 2, 3])
data2 = Data(["a", "b", "c"])