import random

# Fizz-Tsubasa-Yasaho oyunu için gereken değişkenler
secenekler = ['fizz', 'tsubasa', 'yasaho']
oyuncu_skor = 0
yapayzeka_skor = 0
# Kazanan kombinasyonları için dictionary
winning_combinations = {
    'fizz': 'tsubasa',
    'tsubasa': 'yasaho',
    'yasaho': 'fizz'
}
print("Oyun Başlasın!")
# Oyuncunun hamle yapması
def player_turn():
     while True:
         oyuncu_secimi = input("Karakter seçimini yap! (fizz/tsubasa/yasaho): ").lower()
         if oyuncu_secimi in secenekler:
             return oyuncu_secimi
         else:
             print("Yanlış giriş yaptınız. Tekrar deneyin! ")
             
# Bilgisayarın hamle yapması
def computer_turn():
    return random.choice(secenekler)

# Hamleleri karşılaştırma ve kazananı belirleme
def compare_moves(oyuncu_secimi, yapayzeka_secimi):
    global oyuncu_skor
    global yapayzeka_skor
    
    if winning_combinations[oyuncu_secimi] == yapayzeka_secimi:
        print("Oyuncunun karakteri kazandı!")
        oyuncu_skor += 10
        print("Oyuncu: ", oyuncu_skor)
        print("Yapayzeka :" , yapayzeka_skor)
    elif winning_combinations[yapayzeka_secimi] == oyuncu_secimi:
        print("Yapay Zekanın karakteri kazandı!")
        yapayzeka_skor += 10
        print("Oyuncu: ", oyuncu_skor)
        print("Yapayzeka :" , yapayzeka_skor)
    else:
        print("Berabere!")
        oyuncu_skor += 1
        yapayzeka_skor += 1
        print("Oyuncu: ", oyuncu_skor)
        print("Yapayzeka :" , yapayzeka_skor)

# Oyunu başlatma
def play_game():
    global oyuncu_skor
    global yapayzeka_skor
    # Oyun 5 turdan oluşacak
    for i in range(3):
        print(i+1, ".", "Tur")
        oyuncu_secimi = player_turn()
        yapayzeka_secimi = computer_turn()
        print("Oyuncu Seçimi", oyuncu_secimi)
        print("Yapay Zeka'nın Seçimi", yapayzeka_secimi)
        compare_moves(oyuncu_secimi, yapayzeka_secimi)
    
    # Oyun sonu puan durumu
    print("Oyuncu:", oyuncu_secimi)
    print("Yapay Zeka:", yapayzeka_secimi)
    print("Oyun Bitti!")
    

# Oyunu başlat
play_game()