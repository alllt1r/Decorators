def speedTest(iterations):
    def decor(func):
        import time
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iterations):
                start = time.time()
                values = func(*args, **kwargs)
                finish = time.time()
                total += (finish - start)
            print(f'Среднее время исполнения: {total / iterations} секунд.')
            return values
        return wrapper
    return decor