"""This program finds the largest number that reads the same forwards and
backwards that is a multiple of two n-digit numbers. This is also called
a palindrome product. The user is to specify the size of the two numbers."""

def pal_prod(size):
    e=0

    start_num=str('9')

    #creates the starting number (if it is a product of 2 3-digit numbs start=999, 2 4-digit numbs start=9999 ect...)
    for i in range(0,size-1):
        start_num+=str('9')

    #determines the number of iterations (ss[0]=start, ss[1]=stop) depending on size of integers
    if len(start_num)<=2:
        ss=[int(start_num),int(start_num)-10]
    elif len(start_num)<=4:
        ss=[int(start_num),int(start_num)-100]
    elif len(start_num)<=6:
        ss=[int(start_num),int(start_num)-1000]
    else:
        ss=[int(start_num),int(start_num)-10000]

    #finds and prints your palindrome product along with the two n-digit multiples
    for i in range(ss[0],ss[1],-1):
        if e==1:
            break
        for j in range(ss[0],ss[1],-1):
            x=str(i*j)

            if x==x[::-1]:
                print("\nThe largest palindrome product of two ", size, "-digit numbers is ",
                      x, "\nWhich is a multiple of ", i, " and ", j)
                e+=1

digits=int(input("What is the size of your two integers: "))
pal_prod(digits)
