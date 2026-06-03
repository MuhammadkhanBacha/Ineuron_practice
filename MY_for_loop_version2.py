def my_for_loop(iteratable):
    iterator = iter(iteratable)
    i = 0
    while i < len(iteratable):
            value = next(iterator)
            print(value)
            i += 1
        

list = [123,44,505,990,1000]
my_for_loop(list)
