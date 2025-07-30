
# define an addition function

def binary_add(num1,num2) :
    max_len=max(len(num1),len(num2))
    num1=num1.zfill(max_len)
    num2=num2.zfill(max_len)
    res=" "
    carry=0
    for i in range(max_len-1,-1,-1) :

        if int(num1[i]) + int(num2[i]) + carry ==0 :                 # in decimal 0+0+0=0 , in binary 0+0+0=0
            res="0"+res
            carry=0
        elif int(num1[i]) + int(num2[i]) + carry == 1 :              # in decimal 0+0+1=1 , in binary 0+0+1=1
            res="1"+res
            carry=0
        elif int(num1[i]) + int(num2[i]) + carry == 2 :              # in decimal 0+1+1=2 , in binary 0+1+1=0 and carry1
            res="0"+res
            carry=1
        elif int(num1[i]) + int(num2[i]) + carry == 3 :              # in decimal 1+1+1=3 , in binary 1+1+1=1 and carry1
            res="1"+res
            carry=1
    if carry==1 :
        res="1"+res
    print(res)




# define first complement function

def binary_first_complement(num1):
                result = ""
                for i in num1:
                    if i == "0":
                        result += "1"
                    else:
                        result += "0"

                return result




# define second complement function

def binary_second_complement(num1):

    first_comp = binary_first_complement(num1)                                # call binary_first_complement function

    second_comp = binary_add(first_comp, "1")     # call addition function
    return second_comp










# define binary subtraction function

def binary_subtract(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    result = ""
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        if int(num1[i]) - borrow < int(num2[i]):
            result = str(int(num1[i]) - borrow + 2 - int(num2[i])) + result
            borrow = 1
        else:
            result = str(int(num1[i]) - borrow - int(num2[i])) + result
            borrow = 0
    return result.lstrip("0")





while True:
    print("**binary calculator**")
    print( )
    print("A) Insert new numbers")
    print("B) Exit")
    print()
    choice=input("Please select an option")
    choice=choice.upper()                                      # to make the upper and lower case work
    if choice not in ["A","B"] :
        print("Please select a valid choice")
        continue                                               # will continue in the loop until we have a valid choice

    if choice == "A" :
        while True:
            num1=input("enter the 1st binary number")

            try:                                               # will continue in the loop until we have a binary number
                int(num1, 2)
            except (ValueError, TypeError):
                print("please enter a valid binary number")
            else:                                              # here we got the binary number
                break


        # operation choices

        print("please select the operation")
        print()
        print("A) compute one's complement")
        print("B) compute two's complement")
        print("C) addition")
        print("D) subtraction")
        operation_choice= input()
        operation_choice=operation_choice.upper()            # to make the upper and lower case work


        # the first complemet operation


        if operation_choice== "A" :
            # call first complement function
            print(binary_first_complement(num1))


        # the second complemet operation


        if operation_choice== "B" :
            #call second complement function
            binary_second_complement(num1)



        if operation_choice in ["C","D"]:
            while True:                                        # wii continue in the loop until we have a binary number
                num2 = input("enter the 2nd binary number")
                try:
                    int(num2, 2)
                except (ValueError, TypeError):
                    print("please enter a valid binary number")
                else:                                            # here we got a binary number
                    break


        # the addition operation

        if operation_choice == "C":
            # call addition function
            binary_add(num1, num2)


        # the subtraction operation

        if operation_choice=="D" :
            # call subtraction function
            print(binary_subtract(num1,num2))





    if choice=="B" :
        break








    elif choice == "B" :
        break

