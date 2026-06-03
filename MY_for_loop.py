def my_for_loop(iteratable):
    iterator = iter(iteratable)

    while True:
        try:
            value = next(iterator)
            print(value)
        except StopIteration:
            break

list = [123,44,505,990,1000]
my_for_loop(list)
