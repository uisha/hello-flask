import time
if __name__ == '__main__':
    current_time = time.time()
    print(current_time)

    def speed_calc_decorator(function):
        def function_wrapper():
            start_time = time.time()
            function()
            end_time = time.time()
            function_time = end_time - start_time
            print(f"{function.__name__} run speed: {function_time}s")
        return function_wrapper

    @speed_calc_decorator
    def fast_function():
        for i in range(1_000_000):
            i * i


    @speed_calc_decorator
    def slow_function():
        for i in range(10_000_000):
            i * i

    fast_function()
    slow_function()