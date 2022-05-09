from Kütüphane import *
print("""
Kütüphane programına hoş geldiniz 
işlemler:
1-kitapları göster
2-kitap sorgula 
3-kitap ekle
4-kitap sil
5-kitap ekle

çıkmak için q ya basın
""")
kütüphane =Kütüphane()

while True:
    işlem=input("yapacağınız işlem: ")
    if(işlem=="q"):
        print("program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif(işlem=="1"):
        kütüphane.kitapları_göster()
    elif(işlem=="2"):
        isim=input("Hangi kitabı istiyorsunuz")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)
    elif(işlem=="3"):
        isim=input("isim :")
        yazar=input("yazar :")
        yayınevi=input("yayınevi :")
        tür=input("tür :")
        baskı=int(input("baskı :"))
        yeni_kitap=Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor....")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi")
    elif(işlem=="4"):
        isim=input("Hangi kitabı silmek istiyorsunuz :")
        cevap=input("Emin misiniz ? (E/H) :")
        if(cevap=="E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi...")
    elif(işlem=="5"):
        isim=input("Hangi kitabın baskısını yükseltme istiyorsunuz : ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi")
    else:
        print("Geçersiz işlem...")