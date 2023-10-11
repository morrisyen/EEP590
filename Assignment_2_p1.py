
def check_valid(list_n):
    total = 0 #total is for the accumulation of 1th integer to 4th integer
    for i in range(4):
        total += list_n[i] #Accumulating first four integers and store the total value in variable total

    """
    The remainder calculated from the total of first four integers divided by 5 should be the last integer in the list_n.
    If the remainder is not equivalent to the last integer, it will return false. Otherwise, return true.
    """
    return total % 5 == list_n[4]


if __name__ == '__main__':
    num = input()
    list_num = [int(x) for x in str(num)] #Using for loop to convert every element of num into integer sequentially and stores them in list_num.
    res = check_valid(list_num)
    print(res)