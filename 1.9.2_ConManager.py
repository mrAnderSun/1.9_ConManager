from datetime import datetime
import sys


class Timecode:
    def __init__(self, log_path, encoding='utf-8'):
        self.log_file = open(log_path, 'a', encoding=encoding)
        self.begin = self.func_time()
        print(self.begin, " - First time")

    def func_time(self):
        time = datetime.utcnow()
        return time

    def __enter__(self):
        return self

    def write_log(self, action):
        self.log_file.write(f'{datetime.utcnow()}: {action}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_log(f'error: {exc_val}')
            self.write_log(f'It is huge traceback: {exc_tb}')
            # self.exc_info(f'Just info: {exc_info}')
            self.write_log("GoodBye")
        end = self.func_time()
        print(end, "- Second time")
        dif = end - self.begin
        print(dif, "- Difference between times")
        self.log_file.close()


#  Функции арифметических операций
def addition(operand1, operand2):
    return print(f'{operand1 + operand2} \n')


def subtraction(operand1, operand2):
    return print(f'{operand1 - operand2} \n')


def implementation(operand1, operand2):
    return print(f'{operand1 * operand2} \n')


def division(operand1, operand2):
    #  проверка деления на ноль
    try:
        local_division = operand1 / operand2
    except ZeroDivisionError:
        print("You cannot do it again ( ZeroDivision )! Remember that!!!")
        log2.write_log("You cannot do it again ( ZeroDivision )! Remember that!!!")
    else:
        return print(f'{local_division} \n')


#  ВВод данных, глоб. переменных, проверка на первый символ
def data_operation():
    # global operation
    # global operand1
    # global operand2
    operation_base = ("*", "+", "/", "-")

    data = input("Enter Notation: ")
    data_list = data.split()
    operation = data_list[0]
    operand1 = data_list[1]
    operand2 = data_list[2]

    #  функция выхода из кода (символ отличный от указанных операций в operation_base)
    if operation not in operation_base:
        return sys.exit(0)
    # assert operation in operation_base, f'Wrong operation! Need only {operation_base}'

    try:
        if isinstance(int(operand1), int):
            operand1 = int(operand1)
        if isinstance(int(operand2), int):
            operand2 = int(operand2)
    except ValueError:
        log2.write_log("Wrong operand's Value. Check your data!")
        print("Wrong operand's Value. Check your data!")
    except TypeError:
        log2.write_log("Wrong operand's Type. Check your data!")
        print("Wrong operand's Type. Check your data!")
    else:
        print(f'{operation} {operand1} {operand2}')
        return arithmetic_operation(operation, operand1, operand2)


#####  Сравнение и выполнение функции
def arithmetic_operation(operation, operand1, operand2):
    if operation == "+":
        addition(operand1, operand2)
    elif operation == "-":
        subtraction(operand1, operand2)
    elif operation == "*":
        implementation(operand1, operand2)
    elif operation == "/":
        division(operand1, operand2)


###### MAin
with Timecode('big_log') as log2:
    print("Notation from Poland! \n"
          "For example: + 3 4\n")
    while True:
        data_operation()
