import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_function():
    # time.sleep(2)  # zatrzymanie na 2 sekundy Czas wykonania my_function: 2.001012086868286
    print(2024 ** 1200)  # Czas wykonania my_function: 0.0010006427764892578


@measure_time
def calculate_primes(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    # print(primes)
    return primes


# my_function()
# calculate_primes(100000)  # Czas wykonania calculate_primes: 1.2410075664520264
calculate_primes(1000000)  # Czas wykonania calculate_primes: 5.494037628173828


