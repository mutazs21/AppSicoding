import main

def start():
    while True:
        print("ini kalkulator pertambahn")
        exit_menu = input(f'Kembali ke memu utama : [y/n] ')
        
        if exit_menu == 'n':
            True
        elif exit_menu == 'y':
            main.menu()
        else:
            break
        
if __name__ == '__main__':
    start()