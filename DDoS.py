import webbrowser
import time

def simulate_loading():
    for i in range(10, 110, 10):
        print(f"Загрузка: {i}%")
        time.sleep(0.7)

def main():
    print("Инъекция кода. Закрытие программы приведёт к блокировке данных. Подождите...")
    simulate_loading()
    
    print("Код инъекцирован...")

    user_choice = input("Перейти в панель управления инъекцированного кода? (Y/N): ")

    if user_choice.upper() == 'Y':
        webbrowser.open('https://vk.com/club223393615')
    elif user_choice.upper() == 'N':
        print("Close.")
    else:
        print("Некорректный ввод. Пожалуйста, введите Y или N.")

if __name__ == "__main__":
    main()