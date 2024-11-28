import PySimpleGUI as sg

layout = [
           [sg.Image('png-transparent-orange-miniature-illustration-operational-planning-operations-management-business-plan-implementation-project-management-teamwork-3d-villain-orange-plan-computer-wallpaper-thumbnail.png', key = '-IMAGE-')],
           [sg.Text('Введите число (-128 до 127):', size=(20,2)), sg.Input(key='-NUM-', size=(15,20))],
           [sg.Button('Представление числа в прямом/обратном/дополнительном коде:', size=(30, 2))],
           [sg.Input(key='-OUTPUT-', size=(60,50), disabled=True)],
]

window = sg.Window('Представление чисел', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Представление числа в прямом/обратном/дополнительном коде:':
        try:
            number = int(values['-NUM-'])
            if not -128 <= number <= 127:
                output = 'Ошибка: число не входит в диапазон указанных чисел'
            else:
                straight = bin(number & 0xFF)[2:].zfill(8)
                if number >=0:
                    two_additional = straight
                else:
                    two_additional = bin((256 + number) & 0xFF)[2:].zfill(8)
                reverse = "".join(['1' if bit == '0' else '0' for bit in straight])
                output =  f"Прямой: {straight}, Обратный: {reverse}, Дополнительный: {two_additional}"
            window['-OUTPUT-'].update(output)
        except ValueError:
            window['-OUTPUT-'].update("Ошибка: некорректный ввод")

window.close()