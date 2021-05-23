import random
random_char="abcdefghisjklmnopqrstABCDEFGHIJKLMNOP123456789"
len_pass=int(input("Enter how many length of password do you want"))

for i in range(0,len_pass):

    r=random.choice(random_char)
    print(r,end=" ")


