import random
from libs import welcome_message

welcome_message("Selamat datang di tebak goa marmut")

user_name = input("Masukan nama : ")

while user_name == "":
    user_name = input("Isi dulu nama anda : ")


while True:
    bentuk_goa = "[_]"
    goa_kosong = [bentuk_goa] * 5
    goa = goa_kosong.copy()
    marmut_posisi = random.randint(1, 5)
    goa[marmut_posisi - 1] = "[0_0]"
    goa_kosong = " ".join(goa_kosong)
    goa = " ".join(goa)

    print(f'''Halo {user_name}! Coba perhatikan goa dibawah ini \n {goa_kosong}''')
    jawaban_user = int(input("Temukan sebuah marmut di antara 5 goa ini! [ 1 / 2 / 3 / 4 / 5 ]: "))

    while jawaban_user > 5:
        jawaban_user = int(input("Temukan sebuah marmut di antara 5 goa ini! [ 1 / 2 / 3 / 4 / 5 ]: "))
    while jawaban_user < 1:
        jawaban_user = int(input("Temukan sebuah marmut di antara 5 goa ini! [ 1 / 2 / 3 / 4 / 5 ]: "))

    jawaban_yesno = input(f"Pilihan kamu adalah {jawaban_user} apa kamu yakin? [yes/no] ")
        
    if jawaban_yesno == "yes":
        if jawaban_user == marmut_posisi:
            print(f'{goa} \n Selamat kamu menang 🏆')
        else:
            print(f'{goa} \n Maaf kamu kalah 🙊')     
    elif jawaban_yesno == "no":
        print('Program digentikan!')
        exit()
    else:
        print(f"input tidak valid, silahkan ulangi gamenya")
        exit()
    
    exit_game = input("\n\nApakah ingin melanjutkan game nya? [yes/no] ")
    if exit_game == "yes":
        True
    else:
        break


print("Program selesai")