

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


# the menu
def menu():
    global decode
    print("Welcome to the Coder.\n"
          "What would you like to do?\n"
          "1.create your own text to encode\n"
          "2.encode a file\n"
          "3.decode a file")
    correct = False
    while not correct:
        answer = input("Answer: ")
        if answer.__contains__("1"):
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
        elif answer.__contains__("2"):
            try:
                print(f"Enter a file name:")
                file_name = input()
                open(file_name, 'w')
                file_text = open(file_name, 'w')
            except:
                print("File not found. Try again")
            print("Enter a Key you would like to use:")
            key = input("Answer: ")
            key_code = find_text(file_text, key)
            v_code = code(key_code, file_text)
            decode = decode(key_code, v_code)
            find_text(file_text, key)
            correct = False
            while not correct:
                print(f"encoded message: {v_code} \n would you like to decode it?")
                decode_rspn = input("Answer: ")
                if decode_rspn.__contains__("1"):
                    print(f"Here's the decoded message: {decode}")
                    correct = True
                elif decode_rspn.__contains__("2"):
                    print("Okay")
                    correct = True
                else:
                    print("Use 1 or 2 to answer")
        elif answer.__contains__("3"):
            print("no")

        else:
            print("input a number between 1 and 3")





menu()
