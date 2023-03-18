import random

#bu oyunda skor tutuyoruz.
# Bu program, kullanıcının taş, kağıt veya makas seçimini alır ve ardından bilgisayarın rasgele bir seçim yapmasını sağlar. 
# Ardından, her iki seçimin sonucunu karşılaştırır ve sonucu ekrana yazdırır. 
# Skorlar her seferinde güncellenir ve sonuçta en yüksek skora sahip oyuncu kazanır.
# Son olarak, kullanıcıya yeniden oynamak isteyip istemediğini sorar.
#  Kullanıcı 'E' harfine basarsa, oyun yeniden başlar. 'H' harfine basarsa, program sonlandırılır.

print("Fizz Tsubasa Yasaho oyununa hoş geldiniz!")
oyuncu_skor = 0
yapayzeka_skor = 0

while True:
    secenekler = ["fizz", "tsubasa","yasaho"]
    print(secenekler)
    yapayzeka_secimi = random.choice(secenekler)
    
    oyuncu_secimi = input("Fizz mi, Tsubasa mı, Yasaho mı? ").lower()
    while oyuncu_secimi not in secenekler:
        oyuncu_secimi = input("Geçersiz seçim! Tekrar deneyin (Fizz/Tsubasa/Yasaho): ").lower()

    print("Bilgisayarın seçimi: ", yapayzeka_secimi)

    if oyuncu_secimi == yapayzeka_secimi:
        print("Berabere! Tekrar deneyin.")
    elif oyuncu_secimi == "Tsubasa":
        if yapayzeka_secimi == "Fizz":
            print("Kaybettiniz! Bilgisayar Fizz seçti.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar Yasaho seçti.")
            oyuncu_skor += 1
    elif oyuncu_secimi == "Fizz":
        if yapayzeka_secimi == "Yasaho":
            print("Kaybettiniz! Bilgisayar Yasaho seçti.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar Tsubasa seçti.")
            oyuncu_skor += 1
    elif oyuncu_secimi == "Yasaho":
        if yapayzeka_secimi == "Tsubasa":
            print("Kaybettiniz! Bilgisayar Tsubasa seçti.")
            yapayzeka_skor += 1
        else:
            print("Tebrikler! Kazandınız. Bilgisayar Fizz seçti.")
            oyuncu_skor += 1

    print(f"Aktif Skor: Oyuncu {oyuncu_skor} - Bilgisayar {yapayzeka_skor}\n")   
    play_again = input("Tekrar oynamak istiyor musunuz? (E/H) ").lower()
  
    if play_again == "e":
        oyuncu_skor = 0
        yapayzeka_skor = 0
    if play_again != "e":
        break

print("Oyundan çıktınız. Tekrar bekleriz!")
