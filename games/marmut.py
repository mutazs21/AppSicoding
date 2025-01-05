import random
import main

def start():
    while True:
        bentuk_goa = "[_]"
        goa_kosong = [bentuk_goa] * 5
        
        marmut_posisi = random.randint(1, 5)
        
        goa = goa_kosong.copy()
        goa[marmut_posisi - 1] = "[0_0]"
        
        goa_kosong = " ".join(goa_kosong)
        goa = " ".join(goa)

        print(f' Coba perhatikan goa dibawah ini \n \n {goa_kosong}\n ')
        
        jawaban_user = int(input("Temukan sebuah marmut di antara 5 goa ini! [ 1 / 2 / 3 / 4 / 5 ]: "))

        while jawaban_user > 5:
            jawaban_user = int(input("Temukan sebuah marmut di antara 5 goa ini! [ 1 / 2 / 3 / 4 / 5 ]: "))
        while jawaban_user < 1:
            jawaban_user = int(input("Temukan sebuah marmut di antara 5 goa ini! [ 1 / 2 / 3 / 4 / 5 ]: "))

        if jawaban_user == marmut_posisi:
            print(f'{goa} \n Selamat kamu menang 🏆')
        else:
            print(f'{goa} \n Maaf kamu kalah 🙊')     

        exit_game = input("\n\nApakah ingin melanjutkan game nya? [y/n] ")
        if exit_game == "y":
            True
        elif exit_game == "n":
            main.menu()
        else:
            break

if __name__ == '__main__':
    start()