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
    for j in key_code:
        if j.isalpha():
            start_alphabet = "A"
            swapper = x % (len(key_code))
            find_new_ord = ord(key_code[swapper]) - ord(start_alphabet)
            x += 1
            v_code += chr((find_new_ord + (ord(phrase[swapper].upper()) - ord(start_alphabet))) % 26 + ord(start_alphabet))
        else:
            v_code += j

    return v_code


def decode(key_code,v_code):
    decode = ""
    x = 0
    for y in v_code:
        if y.isalpha():
            start_alphabet = "A"
            swapper = x % (len(key_code))
            find_new_ord = ord(key_code[swapper]) - ord(start_alphabet)
            x += 1
            decode += chr(((ord(v_code[swapper]) - ord(start_alphabet)) - find_new_ord) % 26 + ord(start_alphabet))
        else:
            decode += y

    return decode


def menu_option_one():
    global decode
    correct = True
    print("Whats the text you'd like to encode?")
    text = input("Answer: ")
    print("Whats the key you'd like to use?")
    key = input("Answer: ")
    key_code = find_text(text, key)
    v_code = code(key_code, text)
    decode = decode(key_code, v_code)
    find_text(text, key)
    correct = False
    while not correct:
        print(f"encoded message: {v_code} \n would you like to decode it?"
              f"\n 1. Yes"
              f"\n 2. No")
        decode_rspn = input("Answer: ")
        if decode_rspn.__contains__("1"):
            print(f"Here's the decoded message: {decode}")
            correct = True
        elif decode_rspn.__contains__("2"):
            print("Okay")
            correct = True
        else:
            print("Use 1 or 2 to answer")


def menu_option_two():
    print(f"Enter a name for the file\n"
          f"Example: Hello.txt")
    file_name = input("Answer: ")

    if os.path.exists(file_name):
        print("file exists already, overwrite?\n"
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

    print("Enter a message you'd like to be encoded")
    file_text = input("Answer: ")

    print("Enter a Key you would like to use:")
    key = input("Answer: ")

    key_code = find_text(file_text, key)
    v_code = code(key_code, file_text)
    try:
        with open(file_name, 'w') as file:
            file.write(v_code)
            print("Successful, check file to ensure it is as intended.")
    except Exception as e:
        print(f"[!]Error writing message, Try again. {e}")


def menu_option_three():
    global decode
    print(f"Enter a name for the file\n "
          f"Example: Hello.txt")
    file_name = input("Answer: ")


    try:
        # attempt to read the contents of the file
        with open(file_name, 'r') as file:
            # contents is stored as a string
            contents = file.read()
            print(f"[-] Contents of '{file_name}'\n:")

    except FileNotFoundError:
        # we account for FNF since it's the most likely issue
        print(f"\n[!] Error: File '{file_name}' not found.\n"
              f"\n[?] Did you make sure to enter the file name correctly?\n")
        return
        # general error case in the event the file is corrupted or gets deleted mid-read
    except Exception as e:
        print(f"[!] Error reading file '{file_name}': {e}\n")
        return

    print("Enter the Key used to encode the file:")
    key = input("Answer: ")

    decode = decode(contents, key)
    try:
        with open(file_name, 'w') as file:
            file.write(decode)
            print("Successful, check file to ensure it is as intended.")
    except Exception as e:
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
                menu_option_one()
                correct = True
            elif answer.__contains__("2"):
                menu_option_two()
                correct = True
            elif answer.__contains__("3"):
                menu_option_three()
                correct = True

            else:
                print("input a number between 1 and 3")





menu()
