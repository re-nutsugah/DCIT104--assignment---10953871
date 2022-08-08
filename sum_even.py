def ave_even(max):
    even_num = []
    res = 0
    for i in range(1, max):
        if i % 2 == 0:
            even_num.append(i)
    for j in even_num:
    	res += j
    try:
    	average = res//len(even_num)
    except ZeroDivisionError:
    	average = 0
    print(f"The average of even numbers between 1 and {max} is {average}")


ave_even(2)
ave_even(6)
ave_even(10)
ave_even(120)
ave_even(1000)
ave_even(10000)
