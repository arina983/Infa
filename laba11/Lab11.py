import PySimpleGUI as sg
import random
# Определяем макет интерфейса
layout = [
    [sg.Image('png-transparent-book-black-and-white-rubiks-cube-coloring-book-puzzle-puzzle-cube-drawing-game-threedimensional-space-thumbnail.png', key='-IMAGE-')],
    [sg.Text('Введите границы диапазона')],
    [sg.Text('Минимум:', size=(10, 1)), sg.Input(key='-MIN-', size=(15, 20))],
    [sg.Text('Максимум:', size=(10, 1)), sg.Input(key='-MAX-', size=(15, 20))],
    [sg.Button('Сгенерировать', size=(15, 1))],
    [sg.Text('Случайное число:', size=(15, 1)), sg.Input(key='-OUTPUT-', size=(15, 1), disabled=True)],  # Поле вывода
]

window = sg.Window('Рандом', layout)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == 'Сгенерировать':
        try:
            min_val = int(values['-MIN-'])
            max_val = int(values['-MAX-'])
            if min_val > max_val:
                sg.popup('Ошибка!', 'Минимальное значение больше максимального.')
            else:
                random_number = random.randint(min_val, max_val)
                window['-OUTPUT-'].update(random_number)
        except ValueError:
            sg.popup('Ошибка!', 'Введены не корректные числа!')
window.close()