import random
# Bu program, kullanıcının taş, kağıt veya makas seçimini alır ve 
# ardından bilgisayarın rasgele bir seçim yapmasını sağlar. 
# sonra her iki seçimin sonucunu karşılaştırır ve sonucu ekrana yazdırır. 
# Son olarak, kullanıcıya yeniden oynamak isteyip istemediğini sorar.
# Kullanıcı 'E' harfine basarsa, oyun yeniden başlar. 
# 'H' ya da başka bir harfe basarsa program sonlandırılır.

print("Valorant oyununa hoş geldiniz!")
oyuncu_skor = 0
yapayzeka_skor = 0
#while true başlama komutumuz
while True:
    secenekler = ["fizz", "tsubasa", "yasaho"]

    #random choice fonksiyonu yapay zekanın karışık bir şekilde üç seneçekten birini seçmesini sağlar.
    yapayzeka_secimi = random.choice(secenekler)

    # lower fonksiyonu kullanıcı girdilerini büyük-küçük harf duyarlılığından kurtarır, 
    # büyük TAŞ ya da taş yazabilirsin.
    # input komutu kullanıcıdan veri almak için kullanıyorduk.
    oyuncu_secimi = input("fizz mı, tsubasa mı, yasaho mı? ").lower()

    #while eğer anlamına gelir eğer yanlış bir şey yazarsak bu uyarı gelecek.
    while oyuncu_secimi not in secenekler:
        oyuncu_secimi = input("Geçersiz seçim! Tekrar deneyin (Fizz/Tsubasa/Yasaho): ").lower()

    #print ekrana bir mesaj göndermek, input ise kullanıcıdan veri almak için kullanıyorduk.
    print("Bilgisayarın seçimi: ", yapayzeka_secimi)
#şimdi oyuna başlıyoruz.
# yanyana iki eşittir denk demektir. 
# kullanıcı seçimi yapay zeka seçimiyle aynısı olursa berabere olur. İkisi de taş seçerse mesela.
    if oyuncu_secimi == yapayzeka_secimi:
        print("Berabere! Tekrar deneyin.")

    #bir fonksiyon içinde birden fazla eğer ifadesi varsa elif içerisine yazabiliriz. 
    # burada 2 seçeneğimiz var o yüzden birden fazla.
    elif oyuncu_secimi == "fizz":
        if yapayzeka_secimi == "tsubasa":
            print("Kaybettiniz! Fizz Tsubasayı yener.")
            yapayzeka_skor += 5
        else:
            print("Tebrikler! Kazandınız. Yasaho Fizz'i yener.")
            oyuncu_skor += 5
        #kuralları biz belirliyoruz. print ile kullanıcıya gösteriyoruz.
    elif oyuncu_secimi == "tsubasa":
        if yapayzeka_secimi == "yasaho":
            print("Kaybettiniz! Yasaho Tsubasa'yı yener.")
            yapayzeka_skor += 5
        else:
            print("Tebrikler! Kazandınız. Fizz Tsubasa'yı yener.")
            oyuncu_skor += 5

        #4 olasılık var o yüzden 4 adet mesajımız oldu.
    elif oyuncu_secimi == "yasaho":
        if yapayzeka_secimi == "fizz":
            print("Kaybettiniz! Fizz Yasaho'yu yener.")
            yapayzeka_skor += 5
        else:
            print("Tebrikler! Kazandınız. Tsubasa Fizz'i yener.")
            oyuncu_skor += 5

#oyuncu eğer e harfine basarsa oyun tekrar oynanır, başka bir harfe basarsa oyun kapanır.
#lower küçük e yazılsa da kabul edileceği anlamına gelir:)
    print("Aktif Skor: Oyuncu {oyuncu_skor} - Bilgisayar {yapayzeka_skor}")
    play_again = input("Tekrar oynamak istiyor musunuz? (E/H) ").lower()
    
    if play_again == "e":
        oyuncu_skor = 0
        yapayzeka_skor = 0  
    if play_again != "e":
        break

print("Oyundan çıktınız!")
