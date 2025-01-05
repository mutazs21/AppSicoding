from libs import welcome_message, exit_program
from games import marmut
from tools import kalkulator

def menu():
    user_option = int(input(f'menu program\n1. Games Marmut\n2. Kalkulator\n3. keluar program\n\nsilahkan pilih: '))

    if user_option == 1:
        marmut.start()
    elif user_option == 2:
        kalkulator.start()
    elif user_option == 3:
        exit_program()
    else:
        print('hanya boleh pilih yang tersidia di menu!')
        
def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()

