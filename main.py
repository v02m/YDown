#Ver=0.1

import sys
from gui.tkinter_form import create_form as tkinter_form

from gui.pyqt_form import create_form as pyqt_form
from gui.kivy_form import create_form as kivy_form
from gui.wx_form import create_form as wx_form  # Импортируем функцию для wxPython

def main():
    print("Выберите фреймворк:")
    print("1. Tkinter")
    print("2. PyQt6")
    print("3. Kivy")
    print("4. wxPython")  # Добавляем выбор для wxPython

    choice = input("Введите номер фреймворка (1/2/3/4): ")

    if choice == '1':
        tkinter_form()
    elif choice == '2':
        pyqt_form()
    elif choice == '3':
        kivy_form()
    elif choice == '4':
        wx_form()  # Запускаем wxPython форму
    else:
        print("Неверный выбор!")
        sys.exit(1)

if __name__ == "__main__":
    main()
