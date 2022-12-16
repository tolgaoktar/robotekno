import random as r 

rastgelesayi = r.randint(1,100)

print("*******Tahmin Oyunu******")

while True:
    tahmin = int(input("Sayıyı tahmin edin: "))

    if tahmin == rastgelesayi:
        print("******************")
        for i in range(10):
            print("Doğru Tahmin!!")
            break

    elif tahmin < rastgelesayi:
        print("Daha büyük bir sayı söyleyin!")

    elif tahmin > rastgelesayi:
        print("Daha küçük bir sayı söyleyin!!") 