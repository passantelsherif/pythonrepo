
def binary_to_decimal(number):                           # define a function to convert from binary to decimal
    dec = 0
    i = 0
    # making a while loop to keep the code in progres
    while number > 0:
        digit = number % 10
        dec = dec + digit * (2 ** i)
        number = number // 10
        i += 1
    print(dec)


def decimal_to_binary(number):                          # define a function to convert from decimal to binary

    # making an empty string to add the binary digits to it
    string = " "
    while number > 0:
        reminder = number % 2
        string = str(reminder) + string
        number = number // 2
    print(string)


def dec_to_oct(number):                                # define a function to convert from decimal to octal

    # same thing from decimal to binary but by changing base from 2 to 8
    string = " "
    while number > 0:
        reminder = number % 8
        string = str(reminder) + string
        number = number // 8
    print(string)


def dec_to_hexa(number):                               # define a function to convert from decimal to hexadecimal

    # same thing from decimal to binary but by changing base from 2 to 16
    string = " "
    while number > 0:
        reminder = number % 16
        string = str(reminder) + string
        number = number // 16
    print(string)


def oct_to_dec(number):                                # define a function to convert from octal to decimal
    dec = 0
    i = 0
    while number > 0:
        digit = number % 10
        dec = dec + digit * (8 ** i)
        number = number // 10
        i = i + 1
    print(dec)


def hex_to_dec(hex_string):                           # define a function to convert from hexadecimal to decimal
    hex_digits = "0123456789ABCDEF"
    dec = 0
    i = 0

    for digit in reversed(hex_string.upper()):
        if digit in hex_digits:
            # same thing from octal to decimal but by changing the base from 8 to 16
            decimal_value = hex_digits.index(digit)
            dec += decimal_value * (16 ** i)
            i += 1
        else:
            raise ValueError(f"Invalid hexadecimal digit: {digit}")

    print(dec)


def hex_to_binary(number):                            # define a function to convert from hexadecimal to binary
    hex_digits = "0123456789ABCDEF"
    binary_digits = "01"

    binary_string = ""
    for digit in number:
        if digit.upper() in hex_digits:
            decimal_value = hex_digits.index(digit.upper())
            binary_representation = ""
            for _ in range(4):
                binary_representation = binary_digits[decimal_value % 2] + binary_representation
                decimal_value //= 2
            binary_string += binary_representation
        else:
            raise ValueError(f"Invalid hexadecimal digit: {digit}")

    binary_output = binary_string
    print(binary_output)
    return binary_string


while True:

    # making a menu for the user
    print("** numbering system converter **")
    print(" ")
    print("A) insert a new number")
    print("B) exit program")
    print(" ")

    # let the user choose an option
    choice_menu = input("please select an option: ")

    # when the user select a wrong choice this message pops up
    if choice_menu not in ['A', 'B']:
        print("please select a valid choice")

    # if the user choose 'A' this menu pops up
    if choice_menu == 'A':

        # making a menu for the numbers type
        print("** please select the base you want to convert a number from **")
        print(" ")
        print("A) decimal")
        print("B) Binary")
        print("C) octal")
        print("D) hexadecimal")
        print(" ")

        # let the user select which number type to convert from
        from_base = input("please select an option (A/B/C/D) ")

        # if the user doesn't select 'A' , 'B' , 'C' , 'D' this message pops up
        if from_base not in ['A', 'B', 'C', 'D']:
            print("please select a valid choice")
            continue

        # making a menu for the numbers type
        print("** please select the base you want to convert a number to **")
        print(" ")
        print("A) decimal")
        print("B) binary")
        print("C) octal")
        print("D) hexadecimal")
        print(" ")

        # let the user select which number type to convert to
        to_base = input("please select an option (A/B/C/D): ")
        print(" ")

        # if the user doesn't select 'A' , 'B' , 'C' , 'D' this message pops up
        if to_base not in ['A', 'B', 'C', 'D']:
            print("please select a valid choice")
            continue

        # if the user choose 'B' and 'A' call the (binary_to_decimal) function
        if from_base == 'B' and to_base == 'A':

            # take a binary input from the user
            number = int(input("please enter a binary number: "))
            binary_to_decimal(number)

        # if the user choose 'A' and 'B' call the (decimal_to_binary) function
        elif from_base == 'A' and to_base == 'B':

            # take a decimal input from the user
            number = int(input("please enter a decimal number: "))
            decimal_to_binary(number)

        # if the user choose 'A' and 'C' call the (dec_to_oct) function
        elif from_base == 'A' and to_base == 'C':

            # take a decimal input from the user
            number = int(input("please enter a decimal number: "))
            dec_to_oct(number)

        # if the user choose 'A' and 'D' call the (dec_to_hexa) function
        elif from_base == 'A' and to_base == 'D':

            # take a decimal input from the user
            number = int(input("please enter a decimal number: "))
            dec_to_hexa(number)

        # if the user choose 'C' and 'A' call the (oct_to_dec) function
        elif from_base == 'C' and to_base == 'A':

            # take an octal input from the user
            number = int(input("please enter a octal number: "))
            oct_to_dec(number)

        # if the user choose 'D' and 'A' call the (hex_to_dec) function
        elif from_base == 'D' and to_base == 'A':

            # take a hexadecimal input from the user
            number = str(input("please enter a hexadecimal number: "))
            hex_to_dec(number)

        # if the user choose 'D' and 'B' call the (hex_to_binary) function
        elif from_base == 'D' and to_base == 'B':

            # take a hexadecimal input from the user
            number = str(input("please enter a hexadecimal number: "))
            hex_to_binary(number)

        # if the user choose 'B' and 'D'
        elif from_base == 'B' and to_base == 'D':

            # define a function to convert from binary to hexadecimal
            def binary_to_hexadecimal(binary_string):

                while len(binary_string) % 4 != 0:
                    binary_string = '0' + binary_string

                # making a binary to hexadecimal map
                binary_to_hex_map = {
                    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
                    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
                }

                hexadecimal_string = ''
                for i in range(0, len(binary_string), 4):
                    nibble = binary_string[i:i + 4]
                    hexadecimal_string += binary_to_hex_map[nibble]

                return hexadecimal_string

            # take a hexadecimal input from the user
            binary_input = input("Enter a binary number: ")

            # call (binary_to_hexadecimal) function
            hexadecimal_output = binary_to_hexadecimal(binary_input)
            print(hexadecimal_output)

        # if the user choose 'B' and 'D'
        elif from_base in 'B' and to_base in 'C':

            # define a function to convert from binary to octal
            def binary_to_octal(binary_number):

                # check if the binary number is a valid binary string
                if not set(binary_number).issubset({'0', '1'}):
                    raise ValueError("Invalid binary number")

                # Pad the binary number with zeros to make its length a multiple of 3
                while len(binary_number) % 3 != 0:
                    binary_number = '0' + binary_number

                # making a binary to octal map
                binary_to_octal_map = {
                    '000': '0', '001': '1', '010': '2', '011': '3',
                    '100': '4', '101': '5', '110': '6', '111': '7'
                }

                # Convert binary to octal
                octal_number = ''
                for i in range(0, len(binary_number), 3):
                    triplet = binary_number[i:i + 3]
                    octal_number += binary_to_octal_map[triplet]

                return octal_number


            # take a binary input from the user
            binary_input = input("please enter a binary number: ")
            try:

                # call (binary_to_octal) function
                octal_output = binary_to_octal(binary_input)
                print(octal_output)
            except ValueError as e:
                print(f"Error: {e}")

        # if the user choose 'C' and 'B'
        elif from_base == 'C' and to_base == 'B':

            # define a function to convert from octal to binary
            def octal_to_binary(octal_number):
                # check if the octal number is a valid octal string
                if not set(octal_number).issubset({'0', '1', '2', '3', '4', '5', '6', '7'}):
                    raise ValueError("Invalid octal number")

                # making a map from octal to binary
                octal_to_binary_map = {
                    '0': '000', '1': '001', '2': '010', '3': '011',
                    '4': '100', '5': '101', '6': '110', '7': '111'
                }

                # Convert octal to binary
                binary_number = ''
                for digit in octal_number:
                    binary_number += octal_to_binary_map[digit]

                # Remove leading zeros
                binary_number = binary_number.lstrip('0')

                # if the result is empty it means the input was '0'
                return binary_number

            # take an octal input from the user
            octal_input = input("please enter an octal number: ")
            try:
                # call (octal_to_binary) function
                binary_output = octal_to_binary(octal_input)
                print(" ")
                print(binary_output)
            except ValueError as e:
                print(f"Error: {e}")

        # if the user choose 'C' and 'D'
        elif from_base in 'C' and to_base in 'D':

            # define a function to convert from octal to hexadecimal
            def octal_to_hexadecimal(octal_number):
                # check if the octal number is a valid octal string
                if not set(octal_number).issubset({'0', '1', '2', '3', '4', '5', '6', '7'}):
                    raise ValueError("Invalid octal number")

                # making a map from octal to binary
                octal_to_binary_map = {
                    '0': '000', '1': '001', '2': '010', '3': '011',
                    '4': '100', '5': '101', '6': '110', '7': '111'
                }

                # Convert octal to binary
                binary_number = ''
                for digit in octal_number:
                    binary_number += octal_to_binary_map[digit]

                # Pad the binary number with zeros to make its length a multiple of 4
                while len(binary_number) % 4 != 0:
                    binary_number = '0' + binary_number

                # making a binary to hexadecimal map
                binary_to_hex_map = {
                    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
                    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
                }

                # Convert binary to hexadecimal
                hexadecimal_number = ''
                for i in range(0, len(binary_number), 4):
                    nibble = binary_number[i:i + 4]
                    hexadecimal_number += binary_to_hex_map[nibble]

                return hexadecimal_number

            # take an octal input from the user
            octal_input = input("please enter an octal number: ")
            try:
                # call (octal_to_hexadecimal) function
                hexadecimal_output = octal_to_hexadecimal(octal_input)
                print(hexadecimal_output)
            except ValueError as e:
                print(f"Error: {e}")

        # if the user choose 'D' and 'C'
        elif from_base in 'D' and to_base in 'C':

            # define a function to convert fom hexadecimal to octal
            def hex_to_oct(hex_num):

                # making a hexadecimal to binary map
                hex_to_bin = {
                    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
                    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                }

                # Convert each hexadecimal digit to a binary one
                binary_num = ''.join(hex_to_bin[digit] for digit in hex_num.upper())

                # Pad the binary number with zeros to make its length a multiple of 3
                while len(binary_num) % 3 != 0:
                    binary_num = '0' + binary_num

                # Split the binary number into groups of 3 digits
                octal_digits = [binary_num[i:i + 3] for i in range(0, len(binary_num), 3)]

                # make each group of 3 binary digits to an octal digit
                octal_num = ''.join(str(int(group, 2)) for group in octal_digits)

                return octal_num

            # take a hexadecimal input from the user
            hexadecimal_number = input("please enter your hexadecimal number: ")
            # call (hex_to_oct) function
            result = hex_to_oct(hexadecimal_number)
            print(result)

    # if the user choose 'B' this message pops up
    elif choice_menu == 'B':
        print("thank you for using my program")
        break
