import random

print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
#while true başlama komutumuz
while True:
    secenekler = ["taş", "kağıt", "makas"]

    #random choice fonksiyonu yapay zekanın karışık bir şekilde üç seneçekten birini seçmesini sağlar.
    yapayzeka_secimi = random.choice(secenekler)

    # lower fonksiyonu kullanıcı girdilerini büyük-küçük harf duyarlılığından kurtarır, 
    # büyük TAŞ ya da taş yazabilirsin.
    # input komutu kullanıcıdan veri almak için kullanıyorduk.
    kullanici_secimi = input("Taş mı, kağıt mı, makas mı? ").lower()

    #while eğer anlamına gelir eğer yanlış bir şey yazarsak bu uyarı gelecek.
    while kullanici_secimi not in secenekler:
        kullanici_secimi = input("Geçersiz seçim! Tekrar deneyin (taş/kağıt/makas): ").lower()

    #print ekrana bir mesaj göndermek, input ise kullanıcıdan veri almak için kullanıyorduk.
    print("Bilgisayarın seçimi: ", yapayzeka_secimi)
#şimdi oyuna başlıyoruz.
# yanyana iki eşittir denk demektir. 
# kullanıcı seçimi yapay zeka seçimiyle aynısı olursa berabere olur. İkisi de taş seçerse mesela.
    if kullanici_secimi == yapayzeka_secimi:
        print("Berabere! Tekrar deneyin.")

    #bir fonksiyon içinde birden fazla eğer ifadesi varsa elif içerisine yazabiliriz. 
    # burada 2 seçeneğimiz var o yüzden birden fazla.
    elif kullanici_secimi == "taş":
        if yapayzeka_secimi == "kağıt":
            print("Kaybettiniz! Bilgisayar kağıt seçti.")
        else:
            print("Tebrikler! Kazandınız. Bilgisayar makas seçti.")

        #kuralları biz belirliyoruz. print ile kullanıcıya gösteriyoruz.
    elif kullanici_secimi == "kağıt":
        if yapayzeka_secimi == "makas":
            print("Kaybettiniz! Bilgisayar makas seçti.")
        else:
            print("Tebrikler! Kazandınız. Bilgisayar taş seçti.")

        #4 olasılık var o yüzden 4 adet mesajımız oldu.
    elif kullanici_secimi == "makas":
        if yapayzeka_secimi == "taş":
            print("Kaybettiniz! Bilgisayar taş seçti.")
        else:
            print("Tebrikler! Kazandınız. Bilgisayar kağıt seçti.")

#oyuncu eğer e harfine basarsa oyun tekrar oynanır, başka bir harfe basarsa oyun kapanır.
#lower küçük e yazılsa da kabul edileceği anlamına gelir:)
    play_again = input("Tekrar oynamak istiyor musunuz? (E/H) ").lower()
    if play_again != "e":
        break

print("Oyundan çıktınız!")
