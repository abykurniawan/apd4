import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        #NIM: 2009106021 + 10 = 31
        angka = int(input("Masukkan angka: "))
        i = 1
        j = 1
        while i <= angka:
            print (j)
            j += 1
            if j == 10:
                j -= 9
            i += 1
        break
    except ValueError:
        print("Sepertinya ada kesalahan. Mohon coba lagi...")
        time.sleep(1.5)
