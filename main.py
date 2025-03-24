from gui.pyqt6_form import run as pyqt6_run
from gui.tkinter_form import create_form as tkinter_run
from gui.kivy_form import run as kivy_run

def main():
    choice = input("Choose framework (1: PyQt6, 2: Tkinter, 3: Kivy): ")

    if choice == '1':
        pyqt6_run()
    elif choice == '2':
        tkinter_run()
    elif choice == '3':
        kivy_run()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
