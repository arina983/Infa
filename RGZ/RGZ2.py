import PySimpleGUI as sg
import random

sg.theme('DarkTeal9')

pl, comp = 0, 0
count_matches = 0
name = ""

computer = [[sg.Image("", key='computer_image')],
          [sg.Text("Ход компьютера")]]

player = [[sg.Image("", key='player_image')],
           [sg.Text("Ход игрока")]]

game = [[sg.Text('Счёт:'), sg.Text(f"{comp}:{pl}", key="score")],
       [sg.Text("Введите количество раундов"), sg.Input(key="count_matches", size=(20, 1))],
       [sg.Text("Введите имя"), sg.Input(key="name", size=(20, 1))],
       [sg.Button('Начать игру', key='set_matches')],
       [sg.Button('', image_filename='klipartz.com (1).png', size=(15, 15), key='ROCK')],
       [sg.Button('', image_filename='1_2826-128x128.png', size=(10, 10), key='PAPER')],
       [sg.Button('', image_filename='noj-128x128.png', size=(10, 10), key='SCISSORS')],
       [sg.Button('Завершить игру', font="Arial 10")]
       ]

layout = [[sg.Column(computer), sg.VSeparator(), sg.Column(player), sg.VSeparator(), sg.Column(game, justification='right')]]

window = sg.Window("Камень, Ножницы, Бумага", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Завершить игру':
        break

    if event == 'set_matches':
        try:
            count_matches = int(values['count_matches'])
            if count_matches <= 0:
                sg.popup("Пожалуйста, введите положительное число")
                count_matches = 0
                continue
            name = values['name']
            if not name:
                sg.popup("Пожалуйста,введите имя")
                continue
            sg.popup(f"Игра будет длиться {count_matches} раундов")
        except ValueError:
            sg.popup("Пожалуйста, введите корректное число")
            continue

    if event in ['ROCK', 'PAPER', 'SCISSORS']:
        if count_matches <= 0:
            sg.popup("Игра окончена или не задано количество раундов. Установите количество раундов")
            continue

        player_choice = event
        computer_choice = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

        if player_choice == 'ROCK':
            window['player_image'].update(filename='klipartz.com (1).png')
        elif player_choice == 'PAPER':
            window['player_image'].update(filename='1_2826-128x128.png')
        else:
            window['player_image'].update(filename='noj-128x128.png')

        if computer_choice == 'ROCK':
            window['computer_image'].update(filename='klipartz.com (1).png')
        elif computer_choice == 'PAPER':
            window['computer_image'].update(filename='1_2826-128x128.png')
        else:
            window['computer_image'].update(filename='noj-128x128.png')

        if player_choice == computer_choice:
            result_text = "Ничья!"
        elif (player_choice == 'ROCK' and computer_choice == 'SCISSORS') or (player_choice == 'PAPER' and computer_choice == 'ROCK') or (player_choice == 'SCISSORS' and computer_choice == 'PAPER'):
            result_text = "Вы выиграли!!! :)"
            pl += 1
        else:
            result_text = "Вы проиграли :("
            comp += 1

        window['score'].update(f"{comp}:{pl}")
        sg.popup(result_text)

        count_matches -= 1

        if count_matches == 0:
            sg.popup("Игра завершена!", f"Итоговый счёт: Компьютер {comp} : {pl} {name}")
            with open('RGZ.txt', 'a', encoding="UTF-8") as file:
                file.write(f"Результат игры: Компьютер {comp} : {pl} {name}\n")
            pl, comp = 0, 0
            window['score'].update(f"{comp}:{pl}")
            break

window.close()


