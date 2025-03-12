# Управление мышью с телефона 🇷🇺

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

Репозиторий с [Android-приложением](https://github.com/z7x8c9/RemoteMouseClient)

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

# Mouse control from your phone 🇺🇸

This project allows you to control a computer mouse using an Android device. The Android application connects to a Python server running on your computer via WebSocket, which allows you to move the cursor, click and scroll using your phone.

---

## Content
1. [Features](#features)
2. [Setup](#setup)
- [Server Setup](#Server setup)
   - [Android App Setup](#setup-android apps)
3. [Usage](#usage)
4. [Problem Solving] (#problem solving)
5. [Participation in the project] (#participation-in-the-project)

---

## Features

- **Cursor Movement**: Control the cursor by tilting the phone.
- **Left/Right click**: Press the buttons to simulate mouse clicks.
- **Scroll**: Use the slider to scroll up and down.
- **Calibration**: Calibrate the gyroscope for precise control.
- **Sensitivity adjustment**: Adjust the sensitivity of the cursor movement.

---

## Setting up

### Configuring the server

1. **Install Python** (if not installed):
   - Download and install Python from [python.org ](https://www.python.org /).

2. **Install the necessary libraries**:
- Open the terminal and run:
     ```bash
     pip install websockets pyautogui
     ```

3. **Start the server**:
- Save the file `server.py `on the computer.
   - Start the server:
``bash
     python server.py
``
- The server outputs its IP address (for example, `ws://192.168.1.100:5000`).

### Setting up the Android app

Repository with [Android application](https://github.com/z7x8c9/RemoteMouseClient )

## Usage

1. **Connecting to the server**:
- Open the app on your Android device.
   - Enter the server's IP address (for example, `192.168.1.100').
- Click "Connect".

2. **Gyro Calibration**:
- Place your phone on a flat surface.
   - Click "Calibrate" to reset the gyroscope.

3. **Sensitivity Adjustment**:
- Use the slider to adjust the sensitivity.

4. **Moving the cursor**:
- Press and hold the "Move" button.
   - Tilt your phone to move the cursor.

5. **Clicks and Scrolling**:
- Use the left/right click buttons.
   - Use the slider to scroll.

---

## Problem solving

- **The server is not starting**:
- Make sure that Python and the necessary libraries are installed.
  - Check that the port `5000` is not blocked by the firewall.

- **The application does not connect**:
- Make sure that the server and the phone are on the same Wi-Fi network.
  - Verify that the server's IP address is correct.

- **The cursor does not move**:
- Calibrate the gyroscope.
  - Adjust the sensitivity.

---

## Participation in the project

We welcome your suggestions! If you find a bug or want to suggest a new feature, create an issue or send a pull request.

---
