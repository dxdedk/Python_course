#1
print ('Задание 1')
import pandas as pd
import random

data = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]
df = pd.DataFrame(data)

print(df, "\n")

#2
print ('Задание 2')
import pandas as pd
import random

data2 = [[random.randint(6, 10) for _ in range(10)] for _ in range(10)]

df2 = pd.DataFrame(data2, index=list('ABCDEFGHIJ'))

print(df2, "\n")

filtered_rows = df2[df2 > 5].dropna(how='any')
if len(filtered_rows) > 0:
    print("Строки, в которых все числа > 5:")
    print(filtered_rows)
else:
    print("Строки, в которых все числа > 5, отсутствуют", "\n")

#3
print ('Задание 3')
import pandas as pd
import numpy as np

np.random.seed(0)
data3 = np.random.randint(0, 10, size=(10, 10))
df3 = pd.DataFrame(data3, index=list('ABCDEFGHIJ'), columns =list('ABCDEFGHIJ'))
print (df3)
print("Размерность матрицы:", df3.shape)
print("Индексы столбцов:", df3.columns)
print("Среднее значение всех чисел матрицы:", df3.mean().mean())

df3.to_csv("random_matrix.csv", index=False)
print('')

#4
print ('Задание 4')
import pandas as pd

df4 = pd.read_csv('emojis.csv')

df4_sorted = df4.sort_values('Rank', ascending=True)

most_popular_subcategory = df4_sorted['Subcategory'].iloc[0]

print("Самая популярная подкатегория эмоджи:", most_popular_subcategory, "\n")

#5
print ('Задание 5')
import pandas as pd
import matplotlib.pyplot as plt

df5 = pd.read_csv('emojis.csv')

emojis_per_year = df5.groupby('Year').size()

emojis_per_year.plot(kind='bar', rot=0)
plt.xlabel('Год')
plt.ylabel('Количество эмоджи')
plt.title('Количество созданных эмоджи за каждый год')

plt.show()
print('')

#6
print ('Задание 6')
import pandas as pd

def emoji_category_percentage():
    data = pd.read_csv('emojis.csv')

    categories = data['Category'].unique()

    for category in categories:
        category_data = data[data['Category'] == category]

        if category_data.empty:
            print(f"Отсутствует категория '{category}' в наборе данных")
        else:
            total_emojis = len(data)
            category_emojis = len(category_data)
            percentage = (category_emojis / total_emojis) * 100
            print(f"Категория '{category}': {percentage:.2f}%")


emoji_category_percentage()

print('')

#7
print ('Задание 7')
import pandas as pd
import matplotlib.pyplot as plt


def plot_open_close():
    data = pd.read_csv('BCT-USD.csv')

    data['Date'] = pd.to_datetime(data['Date'])

    start_date = input("Введите начальную дату (гггг-мм-дд): ")
    end_date = input("Введите конечную дату (гггг-мм-дд): ")

    mask = (data['Date'] >= start_date) & (data['Date'] <= end_date)
    filtered_data = data.loc[mask]

    plt.plot(filtered_data['Date'], filtered_data['Open'], label='Open')
    plt.plot(filtered_data['Date'], filtered_data['Close'], label='Close')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    plt.show()
plot_open_close()
