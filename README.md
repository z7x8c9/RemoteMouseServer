# Remote Mouse Control

This project allows you to control your computer's mouse using an Android device. The Android app connects to a Python server running on your computer via WebSocket, enabling you to move the cursor, click, and scroll using your phone.

---

## Table of Contents
1. [Features](#features)
2. [Setup](#setup)
   - [Server Setup](#server-setup)
   - [Android App Setup](#android-app-setup)
3. [Usage](#usage)
4. [Troubleshooting](#troubleshooting)
5. [Contributing](#contributing)

---

## Features

- **Mouse Movement**: Control the cursor by tilting your phone.
- **Left/Right Click**: Tap buttons to simulate mouse clicks.
- **Scroll**: Use a seek bar to scroll up and down.
- **Calibration**: Calibrate the gyroscope for accurate control.
- **Sensitivity Adjustment**: Adjust the sensitivity of the mouse movement.

---

## Setup

### Server Setup

1. **Install Python** (if not already installed):
   - Download and install Python from [python.org](https://www.python.org/).

2. **Install Required Libraries**:
   - Open a terminal and run:
     ```bash
     pip install websockets pyautogui
     ```

3. **Run the Server**:
   - Save the `server.py` file to your computer.
   - Run the server:
     ```bash
     python server.py
     ```
   - The server will print its IP address (e.g., `ws://192.168.1.100:5000`).

### Android App Setup

1. **Open the Project in Android Studio**:
   - Clone or download this repository.
   - Open the `android-app` folder in Android Studio.

2. **Build the App**:
   - Connect your Android device or use an emulator.
   - Click `Build > Make Project` to build the app.

3. **Install the App**:
   - Click `Run > Run 'app'` to install the app on your device.

---

## Usage

1. **Connect to the Server**:
   - Open the app on your Android device.
   - Enter the server's IP address (e.g., `192.168.1.100`).
   - Click "Connect".

2. **Calibrate the Gyroscope**:
   - Place your phone on a flat surface.
   - Click "Calibrate" to reset the gyroscope.

3. **Adjust Sensitivity**:
   - Use the sensitivity slider to control how fast the cursor moves.

4. **Move the Cursor**:
   - Press and hold the "Move" button.
   - Tilt your phone to move the cursor.

5. **Click and Scroll**:
   - Use the left/right buttons to click.
   - Use the scroll bar to scroll up and down.

---

## Troubleshooting

- **Server Not Starting**:
  - Ensure Python and the required libraries are installed.
  - Check that port `5000` is not blocked by a firewall.

- **App Not Connecting**:
  - Ensure the server and phone are on the same Wi-Fi network.
  - Double-check the server's IP address.

- **Cursor Not Moving**:
  - Calibrate the gyroscope.
  - Adjust the sensitivity slider.

---

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

---

# Управление мышью с телефона

Этот проект позволяет управлять мышью компьютера с помощью Android-устройства. Приложение на Android подключается к Python-серверу, запущенному на вашем компьютере, через WebSocket, что позволяет перемещать курсор, кликать и прокручивать с помощью телефона.

---

## Содержание
1. [Возможности](#возможности)
2. [Настройка](#настройка)
   - [Настройка сервера](#настройка-сервера)
   - [Настройка Android-приложения](#настройка-android-приложения)
3. [Использование](#использование)
4. [Решение проблем](#решение-проблем)
5. [Участие в проекте](#участие-в-проекте)

---

## Возможности

- **Перемещение курсора**: Управляйте курсором, наклоняя телефон.
- **Левый/правый клик**: Нажимайте кнопки для имитации кликов мышью.
- **Прокрутка**: Используйте ползунок для прокрутки вверх и вниз.
- **Калибровка**: Калибруйте гироскоп для точного управления.
- **Настройка чувствительности**: Регулируйте чувствительность перемещения курсора.

---

## Настройка

### Настройка сервера

1. **Установите Python** (если не установлен):
   - Скачайте и установите Python с [python.org](https://www.python.org/).

2. **Установите необходимые библиотеки**:
   - Откройте терминал и выполните:
     ```bash
     pip install websockets pyautogui
     ```

3. **Запустите сервер**:
   - Сохраните файл `server.py` на компьютере.
   - Запустите сервер:
     ```bash
     python server.py
     ```
   - Сервер выведет свой IP-адрес (например, `ws://192.168.1.100:5000`).

### Настройка Android-приложения

1. **Откройте проект в Android Studio**:
   - Склонируйте или скачайте этот репозиторий.
   - Откройте папку `android-app` в Android Studio.

2. **Соберите приложение**:
   - Подключите Android-устройство или используйте эмулятор.
   - Нажмите `Build > Make Project`, чтобы собрать приложение.

3. **Установите приложение**:
   - Нажмите `Run > Run 'app'`, чтобы установить приложение на устройство.

---

## Использование

1. **Подключение к серверу**:
   - Откройте приложение на Android-устройстве.
   - Введите IP-адрес сервера (например, `192.168.1.100`).
   - Нажмите "Подключиться".

2. **Калибровка гироскопа**:
   - Положите телефон на ровную поверхность.
   - Нажмите "Калибровать", чтобы сбросить гироскоп.

3. **Настройка чувствительности**:
   - Используйте ползунок для регулировки чувствительности.

4. **Перемещение курсора**:
   - Нажмите и удерживайте кнопку "Перемещать".
   - Наклоняйте телефон для перемещения курсора.

5. **Клики и прокрутка**:
   - Используйте кнопки для левого/правого клика.
   - Используйте ползунок для прокрутки.

---

## Решение проблем

- **Сервер не запускается**:
  - Убедитесь, что Python и необходимые библиотеки установлены.
  - Проверьте, что порт `5000` не заблокирован брандмауэром.

- **Приложение не подключается**:
  - Убедитесь, что сервер и телефон находятся в одной Wi-Fi сети.
  - Проверьте правильность IP-адреса сервера.

- **Курсор не перемещается**:
  - Проведите калибровку гироскопа.
  - Отрегулируйте чувствительность.

---

## Участие в проекте

Мы приветствуем ваши предложения! Если вы нашли ошибку или хотите предложить новую функцию, создайте issue или отправьте pull request.

---
