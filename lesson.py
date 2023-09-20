# x = 5 >= 2
# a = {1, 3, 7, 8}
# b = {2, 4, 5, 10, 'apple'}
# c = a & b
# df = 'Михайлов Руслан', 34, 'Ж'
# z= 'type'
# d = [1, 'title', 2, 'content']
# print('{} | {} \n {} | {} \n {} | {} \n {} | {} \n {} | {} \n {} | {} \n {} | {} \n'.format(x, type(x), a, type(a), b, type(b), c, type(c), df, type(df), z, type(z), d, type(d)))


# n = int(input())
# if n < -5:
#     print('Принадлежит отрезку', '(-infinity, -5)')
# elif -5 <= n <= 5:
#     print('Принадлежит отрезку', '[-5, 5]')
# else:
#     print('Принадлежит отрезку', '(-5, infinity)')



# lst = input().split()
# print(*lst, sep='\n')



# num = 10
# while num != 1:
#     print(num)
#     num -= 1


# params = ['Речь', 'Мышление', 'Обучаемость', 'Анализ', 'Способность принятие выбора', 'эммоции', 'Развитие', 'Технологии', 'Чувства']
# print(*params)


#print([i for i in range(2, 16)])


# for i in range(105, 4, -25):
#     print(i, end = ' ')


# lst = list(map(int, input().split()))
# lst[::2] =lst[::2][::-1]
# print(*lst)





# import matplotlib.pyplot as plt
# from random import randint
# x = [randint(0, 10) / 10 for i in range(100)]
# y = [x.count(x[i]) for i in range(100)]
# plt.scatter(x, y)
# plt.show()
# plt.scatter(x, y)



# import numpy as np
# import matplotlib.pyplot as plt
# import math
# x = np.linspace(1, 10, 10)
# def f(x):
#     return (1 + math.exp(math.sqrt(x)) + math.cos(x ** 2)) / (abs(1 - (math.sin(x) ** 3)) + math.log(abs(x ** 2)))
# y = [f(xi) for xi in x]
# x_slice = x[:5]
# y_slice = y[:5]
# plt.plot(x, y, label='График loool')
# plt.scatter(x_slice, y_slice, label='Срез', color='red')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Графики функции и среза')
# plt.show()


# import math as m
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import trapz

# def f(x):
#     return abs(m.cos(x * m.exp(m.cos(x) + m.log(x + 1))))

# x = np.arange(0, 10, 1)
# y = [f(xi) for xi in x]
# plt.fill_between(x, y, alpha=0.5)
# plt.plot(x, y, label='Функця')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# area = trapz(y, x)

# print(f'Площадь {round(area, 3)}')

# plt.show()





#apple = [131.01, 136.76, 121.42, 125.21, 128.10, 125.89, 141.56, 147.06, 154.06, 142.90, 150.96, 161.84]
#microsoft = [217.69, 242.20, 227.39, 249.90, 258.86, 245.71, 277.66, 286.51, 300.18, 288.76, 336.06, 334.92]
#google = [87.05, 103.12, 105.43, 111.28, 119.07, 123.30, 130.08, 137.04, 145.52, 137.35, 148.68, 143.80]
# import matplotlib.pyplot as plt

# apple = [131.01, 136.76, 121.42, 125.21, 128.10, 125.89, 141.56, 147.06, 154.06, 142.90, 150.96, 161.84]
# microsoft = [217.69, 242.20, 227.39, 249.90, 258.86, 245.71, 277.66, 286.51, 300.18, 288.76, 336.06, 334.92]
# google = [87.05, 103.12, 105.43, 111.28, 119.07, 123.30, 130.08, 137.04, 145.52, 137.35, 148.68, 143.80]
# months = ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
# plt.figure(figsize=(12, 6))

# plt.plot(months, apple, marker='o', label='apple', linestyle='-', color='blue')
# plt.plot(months, microsoft, marker='o', label='microsoft', linestyle='-', color='green')
# plt.plot(months, google, marker='o', label='google', linestyle='-', color='red')
# plt.title('Динамика')
# plt.xlabel('месяц')
# plt.ylabel('Стоиьость акции')
# plt.grid(True)
# plt.legend()

# plt.tight_layout()
# plt.show()



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox
from PyQt5.QtCore import Qt
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Яндекс - калькулятор Михайлов')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()
        self.input_x = QLineEdit()
        self.layout.addWidget(self.input_x)

        self.input_y = QLineEdit()
        self.layout.addWidget(self.input_y)


        self.operation_combo = QComboBox()
        self.operation_combo.addItems(['+', '-', '×', '÷', 'e^(x+y)', 'sin(x+y)', 'cos(x+y)', 'x^y'])
        self.layout.addWidget(self.operation_combo)


        self.result_label = QLabel('Результат: ')
        self.layout.addWidget(self.result_label)

        self.calculate_button = QPushButton('Вычислить')
        self.calculate_button.clicked.connect(self.calculate)
        self.layout.addWidget(self.calculate_button)

        self.setLayout(self.layout)

    def calculate(self):
        try:
            x = float(self.input_x.text())
            y = float(self.input_y.text())
            operation = self.operation_combo.currentText()

            if operation == '+':
                result = x + y
            elif operation == '-':
                result = x - y
            elif operation == '×':
                result = x * y
            elif operation == '÷':
                if y == 0:
                    result = 'Ошибка: деление на ноль'
                else:
                    result = x / y
            elif operation == 'e^(x+y)':
                result = math.exp(x + y)
            elif operation == 'sin(x+y)':
                result = math.sin(x + y)
            elif operation == 'cos(x+y)':
                result = math.cos(x + y)
            elif operation == 'x^y':
                result = x ** y

            self.result_label.setText(f'Результат: {round(result, 4)}')

        except:
            self.result_label.setText('Ошибка: введите числа')
            self.input_x.clear()
            self.input_y.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())