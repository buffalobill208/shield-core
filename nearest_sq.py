def nearest_square(limit):
    """
    Nearest square function

    """
    sqr=0
    i=1
    while(sqr<limit):
        sqr1=i*i
        i=i+1
        sqr=i*i
    return sqr1
    #Simpler solution below that doesn't make use of while loop
    #return(int(limit ** (1/2))**2)

test1 = nearest_square(10)
print("expected result: 9, actual result: {}".format(test1))
