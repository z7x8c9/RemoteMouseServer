import asyncio
import websockets
import json
import socket
import pyautogui

# Функция для получения локального IP-адреса
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return "127.0.0.1"

# Обработчик клиента
async def handle_client(websocket):
    print("Клиент подключен")
    try:
        async for message in websocket:

            data = json.loads(message)
            action = data.get("action")

            if action == "move":
                # Обработка движения мыши
                dx = data.get("dx", 0)
                dy = data.get("dy", 0)
                pyautogui.moveRel(dx, dy)
                print(f"Мышь перемещена: dx={dx}, dy={dy}")

            elif action == "click":
                # Обработка кликов
                button = data.get("button")
                state = data.get("state", False)
                if button == "left":
                    if state:
                        pyautogui.mouseDown(button="left")
                    else:
                        pyautogui.mouseUp(button="left")
                    print(f"Левая кнопка: {'нажата' if state else 'отпущена'}")
                elif button == "right":
                    if state:
                        pyautogui.mouseDown(button="right")
                    else:
                        pyautogui.mouseUp(button="right")
                    print(f"Правая кнопка: {'нажата' if state else 'отпущена'}")

            elif action == "scroll":
                # Обработка прокрутки
                delta = data.get("delta", 0)
                pyautogui.scroll(delta)
                print(f"Прокрутка: {delta}")

    except websockets.ConnectionClosed:
        print("Клиент отключен")

# Получаем локальный IP-адрес
local_ip = get_local_ip()
print(f"Сервер запущен на ws://{local_ip}:5000")

# Запуск сервера
async def start_server():
    async with websockets.serve(handle_client, local_ip, 5000):
        await asyncio.Future()

# Запуск цикла событий
asyncio.run(start_server())