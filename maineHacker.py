import gnupg
from tabulate import tabulate

import os

def encrypt_file(input_path, output_path, passphrase):
    input_path=input_path+'.txt'
    print('Encrypting...')
    gpg = gnupg.GPG()

    with open(input_path, 'rb') as f:
        file_data = f.read()

    encrypted_data = gpg.encrypt(data=file_data, passphrase=passphrase, symmetric='AES256', recipients='yourself',
                                 output=output_path)

    if encrypted_data.ok:
        os.remove(input_path)
        print('Input file deleted:', input_path)
        print('File encrypted successfully:', output_path)
    else:
        print('Encryption failed.')

def decrypt_file(input_path, output_path, passphrase):
    input_path=input_path+'.gpg'
    print('Decrypting...')
    gpg = gnupg.GPG()

    with open(input_path, 'rb') as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=passphrase, output=output_path)

    if decrypted_data.ok:
        os.remove(input_path)
        print('Input file deleted:', input_path)
        print('File decrypted successfully:', output_path)
    else:
        print('Decryption failed.')

def print_color_gradient(text):
    color_range = 10  # Adjust the number of steps for the gradient

    # for i in range(color_range):
    r = 8 * 255 // color_range
    b = (color_range - 8) * 255 // color_range

        # ANSI escape code for setting text color
    color_code = f"\033[38;2;{r};0;{b}m"

        # Reset color back to default after printing
    reset_code = "\033[0m"

        # Print the text with the current color
    print(f"{color_code}{text}{reset_code}")

def main():

    print_color_gradient(""" 



    ██████╗ ██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗     
    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗    
    ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║    
    ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║    
    ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝    
    ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝     
                                                       
        ███╗   ██╗███████╗ █████╗ ██████╗ ███████╗     
        ████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝     
        ██╔██╗ ██║█████╗  ███████║██████╔╝█████╗       
        ██║╚██╗██║██╔══╝  ██╔══██║██╔══██╗██╔══╝       
        ██║ ╚████║███████╗██║  ██║██║  ██║███████╗     
        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  

                -----[hamza]

        """)


    choice = input('''Choose an operation:\n  [1] Encrypt\n  [2] Decrypt\n > ''')

    if choice == '1':
        table = [
            ["path of encrypted file.txt", "password"],
            ["set_1(incrypte)", "set_3(password)"],
        ]

        print(tabulate(table, headers="firstrow", tablefmt="grid"))

        input_file_path = str(input('Enter the path of the input file (.txt) : '))
        output_file_path = input_file_path+'.gpg'
        password = str(input('Enter the password: '))
        encrypt_file(input_file_path, output_file_path, password)

    elif choice == '2':
        table = [
            ["path of Decrypted file.gpg", "password"],
            ["set_1(Decrypte)", "set_3(password)"],
        ]
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
        input_gpg_file = input('Enter the path of the encrypted file (.gpg): ')
        output_txt_file = input_gpg_file+'.txt'
        password = input('Enter the password: ')
        decrypt_file(input_gpg_file, output_txt_file, password)

    else:
        print('Invalid choice. Please enter either 1 or 2.')

if __name__ == "__main__":
    main()



