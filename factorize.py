import time
# import multiprocessing 
from multiprocessing import Pool, cpu_count


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_all(numbers):
    return [factorize(num) for num in numbers]

def factorize_parallel(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_all_parallel(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_parallel, numbers)



if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()
    result_sync = factorize_all(numbers)
    end_time = time.time()
    execution_time_sync = end_time - start_time
    print(result_sync)
    print(f"Synchronous execution time: {execution_time_sync} seconds")
    start_time_parallel = time.time()
    result_parallel = factorize_all_parallel(numbers)
    end_time_parallel = time.time()
    execution_time_parallel = end_time_parallel - start_time_parallel
    print(result_sync)
    print(f"Parallel execution time: {execution_time_parallel} seconds")