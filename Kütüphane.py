import sqlite3
import time
class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baskı=baskı
    def __str__(self):
        return "Kitap ismi: {} \nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)
class Kütüphane():
    def __init__(self):
        self.bağlantı_oluştur()
    def bağlantı_oluştur(self):
        self.bağlantı=sqlite3.connect("kütüphane.db")
        self.cursor=self.bağlantı.cursor()
        sorgu="Create Table If not exists kitaplar(isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()
    def bağlantıyı_kes(self):
        self.bağlantı.close()
    def kitapları_göster(self):
        sorgu="Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("Kütüphanede kitap bulunmuyor")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitap_sorgula(self,isim):
        sorgu="Select * From kitaplar Where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("Böyle bir kitap yok")
        else:
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    def kitap_ekle(self,Kitap):
        sorgu = "Insert Into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(Kitap.isim,Kitap.yazar,Kitap.yayınevi,Kitap.tür,Kitap.baskı))
        self.bağlantı.commit()
    def kitap_sil(self,isim):
        sorgu="Delete From kitaplar Where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.bağlantı.commit()
    def baskı_yükselt(self,isim):
        sorgu="Select * from kitaplar Where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("böyle bir kitap yok")
        else:
            baskı=kitaplar[0][4]
            baskı +=1
            sorgu2="Update kitaplar Set baskı=? Where isim = ?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.bağlantı.commit()
