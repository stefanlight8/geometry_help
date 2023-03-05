# Wrote by: StefanLight, Stefan Mukhin - https://www.stefanlight.ml/

from rich.console import Console
from os import system, name


def clear_cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


console = Console()
shapes = [
    'прямоугольник',
    'параллелограмм',
    'равнобедренный треугольник',
    'прямоугольный треугольник',
    'квадрат',
    'ромб'
]


class Program:
    def __init__(self):
        self.start()

    def restart(self):
        question = console.input('Перезапустить программу? (y/n): ')
        if question == 'y':
            self.__init__()
        else:
            console.print('Программа завершена.')

    def start(self):
        clear_cls()
        formatted_shapes = '\n'.join([f'{i + 1}. {shape}' for i, shape in enumerate(shapes)])
        console.print(f'Рады вас видеть, вы можете выбрать одну из следующих фигур:\n{formatted_shapes}\n')
        index = int(console.input('Выберите номер фигуры: '))
        self.work(index)

    def work(self, index):
        clear_cls()
        match index:
            case 1:
                a = int(console.input('Введите длину (a): '))
                b = int(console.input('Введите ширину (b): '))
                console.print(f'Площадь прямоугольника: {a * b} см²')
                self.restart()
            case 2:
                clear_cls()
                a = int(console.input('Введите длину стороны (a): '))
                h = int(console.input('Введите высоту (h): '))
                console.print(f'Площадь параллелограмма: {a * h} см²')
                self.restart()
            case 3:
                clear_cls()
                a = int(console.input('Введите длину основания (a): '))
                h = int(console.input('Введите высоту (h): '))
                console.print(f'Площадь равнобедренного треугольника: {(1/2) * a * h} см²')
                self.restart()
            case 4:
                clear_cls()
                a = int(console.input('Введите первый катет (a): '))
                b = int(console.input('Введите второй катет (b): '))
                console.print(f'Площадь прямоугольного треугольника: {(a + b)/2} см²')
                self.restart()
            case 5:
                a = int(console.input('Введите длину (a): '))
                b = int(console.input('Введите ширину (b): '))
                console.print(f'Площадь квадрата: {a * b} см²')
                self.restart()
            case 6:
                clear_cls()
                d1 = int(console.input('Введите первую диагональ (d1): '))
                d2 = int(console.input('Введите вторую диагональ (d2): '))
                console.print(f'Площадь ромба: {1/2 * d1 * d2} см²')
            case _:
                clear_cls()
                console.print('Неверный номер фигуры!', style='bold red')
                self.restart()


if __name__ == '__main__':
    Program()
