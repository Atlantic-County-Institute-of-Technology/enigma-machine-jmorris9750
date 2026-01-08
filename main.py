import os


def find_text(phrase, key):
    key_code = ""
    x = 0

    # swap phrase letters with key letters
    for i in phrase:
        if i.isalpha():
            swapper = x % (len(key))
            key_code += key[swapper].upper()
            x += 1
        else:
            key_code += i

    return key_code


def code(key_code, phrase):
    v_code = ""
    x = 0
    # encodes the new phrase from previous function to get final phrase
    for j in key_code:
        if j.isalpha():
            start_alphabet = "A"
            swapper = x % (len(key_code))
            # finds the new ordinal of the code
            find_new_ord = ord(key_code[swapper]) - ord(start_alphabet)
            x += 1
            # swaps the previous functions code with the new code
            v_code += chr((find_new_ord + (ord(phrase[swapper].upper()) - ord(start_alphabet))) % 26 + ord(start_alphabet))
        else:
            v_code += j

    return v_code


def decode(key_code,v_code):
    decode = ""
    x = 0
    # decodes the encoded phrase
    for y in v_code:
        if y.isalpha():
            start_alphabet = "A"
            swapper = x % (len(v_code))
            # finds the ordinal of the original phrase
            find_new_ord = ord(key_code[swapper]) - ord(start_alphabet)
            x += 1
            # swaps the letters of the encoded for the original phrase
            decode += chr(((ord(v_code[swapper]) - ord(start_alphabet)) - find_new_ord) % 26 + ord(start_alphabet))
        else:
            decode += y

    return decode


def menu_option_one():
    global decode
    correct = True
    # finds key and phrase user wants
    print("Whats the text you'd like to encode?")
    text = input("Answer: ")
    print("Whats the key you'd like to use?")
    key = input("Answer: ")
    # variables for encoded phrase
    key_code = find_text(text, key)
    v_code = code(key_code, text)

    correct = False
    while not correct:
        os.system('cls' if os.name == 'nt' else 'clear')
        # after giving the encoded message, asks if user would like to decode it
        print(f"encoded message: {v_code} \n would you like to decode it?"
              f"\n 1. Yes"
              f"\n 2. No")
        # if yes then decode, if not go back to menu
        decode_rspn = input("Answer: ")
        if decode_rspn.__contains__("1"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Here's the decoded message: {decode(key_code,v_code)}")
            correct = True
        elif decode_rspn.__contains__("2"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Okay")
            correct = True
        # if not given 1 or 2 then prompts the user to use them
        else:
            print("Use 1 or 2 to answer")


def menu_option_two():
    print(f"Enter a name for the file\n"
          f"Example: Hello.txt")
    file_name = input("Answer: ")

    if os.path.exists(file_name):
        os.system('cls' if os.name == 'nt' else 'clear')
        # asks to overwrite the file if it already exists
        print(f"file '{file_name}' exists already, overwrite?\n"
              "1.Yes\n"
              "2.No")
        overwrite_qstn = input("Answer: ")
        if overwrite_qstn.__contains__("2"):
            print("Enter New file name")
            file_name = input("Answer: ")

        elif overwrite_qstn.__contains__("1"):
            pass

        else:
            print("[!]Invalid input, canceled")
            return
    # if doesnt exist, continue with message ad key user wants
    print("Enter a message you'd like to be encoded")
    file_text = input("Answer: ")

    print("Enter a Key you would like to use:")
    key = input("Answer: ")
    # variables for the coded phrases
    key_code = find_text(file_text, key)
    v_code = code(key_code, file_text)
    # opens file and writes the encoded message in it
    try:
        with open(file_name, 'w') as file:
            file.write(v_code)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Successful, {v_code} was added to {file_name}")
    except Exception as e:
        print(f"[!]Error writing message, Try again. {e}")


def menu_option_three():
    global decode
    print(f"Enter a name for the file\n "
          f"Example: Hello.txt")
    file_name = input("Answer: ")

    # reads contents of file given, if not found gives error and asks to check the file name
    try:
        # attempt to read the contents of the file
        with open(file_name, 'r') as file:
            # contents is stored as a string
            contents = file.read().upper()
            print(f"[-] Contents of '{file_name}' {contents}\n:")

    except FileNotFoundError:
        # we account for FNF since it's the most likely issue
        print(f"\n[!] Error: File '{file_name}' not found.\n"
              f"\n[?] Did you make sure to enter the file name correctly?\n")
        return
        # general error case in the event the file is corrupted or gets deleted mid-read
    except Exception as e:
        print(f"[!] Error reading file '{file_name}': {e}\n")
        return
    # if file is found, continue to key user gives
    print("Enter the Key used to encode the file:")
    key = input("Answer: ")
    key_code = find_text(contents, key)
    # opens file and writes the decoded message
    try:
        with open(file_name, 'w') as file:
            file.write(decode(key_code,contents))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Successful, {decode(key_code,contents)} was added to {file_name}")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[!]Error writing message, Try again. {e}")


# the menu
def menu():
    while True:
        correct = False
        while not correct:
            print("Welcome to the Coder.\n"
                  "What would you like to do?\n"
                  "1.create text to encode\n"
                    "2.encode a file\n"
                  "3.decode a file")
            answer = input("Answer: ")
            if answer.__contains__("1"):
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_option_one()

                correct = True
            elif answer.__contains__("2"):
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_option_two()
                correct = True
            elif answer.__contains__("3"):
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_option_three()
                correct = True


            else:
                print("input a number between 1 and 3")





menu()
