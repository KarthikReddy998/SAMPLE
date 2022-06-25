# fkkkk
def countSubstr(str, n, b, a):

    tot_count = 0


    count_x = 0


    for i in range(n):

        if str[i] == b:
            count_x += 1


        if str[i] == a:
            tot_count += count_x


    return tot_count



str = 'abbcaceghcak'
n = len(str)
b, a = 'a', 'a'
print('Count =', countSubstr(str, n, b, a))


