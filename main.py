def menu():
    print("Menu \n-------------\n1. Encode\n2. Decode\n3. Quit ")


def encode(code):
    encoded_code = ""
    for i in str(code):
        i = int(i) + 3
        encoded_code += str(i)
    return encoded_code

def decode(code):
    decoded_code = ""
    for i in str(code):
        i = int(i) - 3
        decoded_code += str(i)
    return decoded_code

def main():
    menu()
    encoder_decoder = True
    choice = int(input("Please enter an option: "))
    while encoder_decoder:
        if choice == 1:
            code = int(input("Please enter your password to encode: "))
            saved_code = encode(code)
            print("Your password has been encoded and stored! ")
        elif choice == 2:
            decoded_code = decode(saved_code)
            print(f"The encoded password is {saved_code}, and the original password is {decoded_code}.")
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
