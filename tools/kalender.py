import calendar
import main

def start():
    while True: 
        bulan = int(input(f'Enter the month number you want to view (example: 1 = January)'))
        
        if bulan == 1:
            yy = 2025  # year
            mm = 1     # month
            print(calendar.month(yy, mm))
        elif bulan == 2:       
            yy = 2025  # year
            mm = 2     # month
            print(calendar.month(yy, mm))
        elif bulan == 3:       
            yy = 2025  # year
            mm = 3     # month
            print(calendar.month(yy, mm))
        elif bulan == 4:       
            yy = 2025  # year
            mm = 4     # month
            print(calendar.month(yy, mm))
        elif bulan == 5:       
            yy = 2025  # year
            mm = 5     # month
            print(calendar.month(yy, mm))
        elif bulan == 6:       
            yy = 2025  # year
            mm = 6     # month
            print(calendar.month(yy, mm))
        elif bulan == 7:       
            yy = 2025  # year
            mm = 7     # month
            print(calendar.month(yy, mm))
        elif bulan == 8:       
            yy = 2025  # year
            mm = 8     # month
            print(calendar.month(yy, mm))
        elif bulan == 9:       
            yy = 2025  # year
            mm = 9     # month
            print(calendar.month(yy, mm))
        elif bulan == 10:       
            yy = 2025  # year
            mm = 10     # month
            print(calendar.month(yy, mm))
        elif bulan == 11:       
            yy = 2025  # year
            mm = 11     # month
            print(calendar.month(yy, mm))
        elif bulan == 12:       
            yy = 2025  # year
            mm = 12     # month
            print(calendar.month(yy, mm))
        else:
            True
            
        exit_program = input(f'Kembali ke menu : [y/n] ')
        
        if exit_program == 'y':
            main.menu()
        elif exit_program == 'n':
            True
            

if __name__ == '__main__':
    start()