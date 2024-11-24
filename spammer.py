import pyautogui
import time
import pyperclip
import keyboard

time.sleep(5)  # Время - через сколько начнётся спам


def spam(text: str, amount: int):
    pyperclip.copy(text)
    for _ in range(amount):
        time.sleep(0.3)  # скорость вставки сообщений
        keyboard.press_and_release('ctrl + v')
        pyautogui.press("enter")


with open("spam_text.txt", "r", encoding='utf-8') as file:
    spam_text = file.read()
    spam(spam_text, 50)  # пишем сообщение и кол-во повторов
