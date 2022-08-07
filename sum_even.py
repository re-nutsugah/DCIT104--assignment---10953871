def sum_even(max):
    sum = 0
    for i in range(1, max+1):
        if i % 2 == 0:
            sum += i
    print(sum)


sum_even(1)
sum_even(6)
sum_even(10)
sum_even(120)
sum_even(1000)
sum_even(10000)
