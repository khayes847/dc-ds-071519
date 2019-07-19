def prime_finder(array):
    prime_list = []
    new_array = []
    number_list = []
    for item in array:
        if item > 1:
            new_array.append(item)
    for item in new_array:
        isprime = True
        if item == 2:
            number_list.append(item)
        else:
            for i in range(2, item):
                if (item % i) == 0:
                    isprime = False
            if isprime == True:
                number_list.append(item)
    return number_list
            #if (item/i)%2 == 0:
                #n += 1
        #if n == 0:
            #prime_list.append(item)
    #return list(prime_list)