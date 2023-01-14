# # # import random as r 

# # # rastgelesayi = r.randint(1,100)

# # # print("*******Tahmin Oyunu******")

# # # while True:
# # #     tahmin = int(input("Sayıyı tahmin edin: "))

# # #     if tahmin == rastgelesayi:
# # #         print("******************")
# # #         print("Doğru Tahmin!!")
# # #         break

# # #     elif tahmin < rastgelesayi:
# # #         print("Daha büyük bir sayı söyleyin!")

# # #     elif tahmin > rastgelesayi:
# # #         print("Daha küçük bir sayı söyleyin!!") 

# # import random as r

# # rastgelesayi = r.randint(25,50)

# # print("********* Tahmin Oyunu **********")

# # while True:
# #     tahmin = int(input("Tuttuğum sayıyı tahmin et: "))
    
# #     if tahmin == rastgelesayi:
# #         print("***********Doğru Tahmin**********")
# #         break
    
# #     elif tahmin < rastgelesayi:
# #         print("Daha büyük bir sayı tahmin et!")
        
# #     elif tahmin > rastgelesayi:
# #         print("Daha küçük bir sayı tahmin et!")
    
# import random as r
    
# rastgelesayi=r.randint(10,60)
    
# print("*tahmin oyunu*")
    
# while True:
#     tahmin = int(input("tahmini bir sayı giriniz: "))
    
#     if tahmin== rastgelesayi:
#         print("*****doğru tahmin******")
#         break
#     elif tahmin < rastgelesayi:
#         print("Daha büyük bir sayı tahmin et")
#     elif tahmin > rastgelesayi:
#         print("Daha küçük bir sayı tahmin et")
        
import random as r

rastgelesayi=r.randint(10,50)

print("Tahmin Oyunu'na Hoş Geldiniz!")

while True:
    tahmin=int(input("tahmini bir sayı girin: "))
     
    if tahmin== rastgelesayi:
        print("****** Doğru tahmin ******")
        break
    elif tahmin < rastgelesayi:
        print("Daha büyük bir sayı tahmin et")
    elif tahmin> rastgelesayi:
        print("Daha küçük bir sayı tahmin et")
         
         
     
                    