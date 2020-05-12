def myDecorator(func):
    def wrapper():
        print('Обертка!')
        print(f'Оборачиваем функцию: {func}.')
        print('Выплняю функцию.')
        func()
        print('Занчили рабоать!')
    return wrapper


@myDecorator
def multiple():
    c = 5 * 4
    print(c)


def speedTest(func):
    import time

    def wrapper():
        start = time.time()

        func()

        finish = time.time()
        print(f'Прошло {finish - start} секунд.')
    return wrapper()


@speedTest
def searchinGoogle():
    import requests

    s = requests.get('https://google.com/')

#searchinGoogle()