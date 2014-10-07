import time


def my_sum(stop, start = 1, step = 1):
    sum = 0
    for i in range(start, stop, step):
        sum += i
    return sum



t_start = time.clock()
number = my_sum(10000000)
t_end = time.clock()

t_build_start = time.clock()
number = sum(range(10000000))
t_build_end = time.clock()

print ("Elapse time for my_sum is {0}".format(t_end - t_start))
print ("Elapse time for built-in sum is"
       "{0}".format(t_build_end - t_build_start))
