import sqlite3
import time
class Kitap():
    def __init__ (self,isim,yazar,yayinevi,tür,baskı,Okunan):
        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tür=tür
        self.baskı=baskı
        self.Okunan=Okunan
    def __str__(self):
        return "Kitap İsmi:{}\nYazar:{}\nYayınevi:{}\nTür:{}\nBaskı:{}\nOkunan:{}\n".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baskı,self.Okunan)
class Kütüphane():
    def __init__ (self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("kütüphane.db")
        self.cursor=self.baglanti.cursor()
        sorgu=("Create Table if not exists kitaplar(isim TEXT,yazar TEXT,yayinevi TEXT,tür TEXT,baskı INT,Okunan TEXT)")
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitapları_göster(self):
        sorgu="Select *From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Kitaplar sorgulanıyor,lütfen bekleyiniz....")
            time.sleep(2)
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kitap)
    def kitap_sorgula(self,isim):
        sorgu="Select *From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)==0):
            
            time.sleep(2)
            print("Böyle bir kitap bulunmuyor....")
        else:
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][5])
            print(kitap)
    def kitap_ekle(self,kitap):
        sorgu="Insert into kitaplar Values(?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tür,kitap.baskı,kitap.Okunan))
        self.baglanti.commit()

        time.sleep(2)
        print("Başarıyla eklendi.")
        
    def kitap_sil(self,isim):
        sorgu="Select *From kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("Silmek istediğiniz kitap sorgulanıyor,lütfen bekleyiniz....")
            time.sleep(2)
            print("Böyle bir kitap bulunmadığından silme işlemi gerçekleştirelemiyor,Lütfen ismin doğru olduğuna emin olunuz!")
        else:
            sorgu="Delete From kitaplar where isim=?"
            self.cursor.execute(sorgu,(isim,))
            print("Kitap siliniyor..")
            time.sleep(2)
            print("Başarıyla silindi.")
            self.baglanti.commit()
    def kitap_sayisi(self):
        sorgu="SELECT *From kitaplar "
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        print(len(liste),"tane kitap bulundu.")
    def okunan_kitaplar(self,isim):
        sorgu="Select *From kitaplar where isim = ? "
        self.cursor.execute(sorgu,(isim,))
        okunanlar=self.cursor.fetchall()
        if(len(okunanlar)==0):
            print("Sorgu yapılıyor,lütfen bekleyiniz..")
            time.sleep(1)
            print("Bilgisini istediğiniz kitap sistemde kayıtlı değil!!")
        else:
            for i in okunanlar:
                print("Sorgulamak istediğiniz kitabın okunma durumu:" +""+i[5])
    def kitap_güncelleme_sorgusu(self,isim,yeni_isim,yeni_yazar,yeni_yayınevi,yeni_tür,yeni_baskı,yeni_okunma_bilgisi):
        sorgu="Select *From kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("Böyle bir kitap bulunmadığından güncelleme işlemi yapılamıyor..")
        else:
            yazar=kitaplar[0][1]
            yayinevi=kitaplar[0][2]
            tür=kitaplar[0][3]
            baskı=kitaplar[0][4]
            Okunan=kitaplar[0][5]
            self.cursor.execute("Update kitaplar set isim=? where isim = ?",(yeni_isim,isim))
            self.cursor.execute("Update kitaplar set yazar=? where yazar = ?",(yeni_yazar,yazar))
            self.cursor.execute("Update kitaplar set yayinevi=? where yayinevi = ?",(yeni_yayınevi,yayinevi))
            self.cursor.execute("Update kitaplar set tür=? where tür = ?",(yeni_tür,tür))
            self.cursor.execute("Update kitaplar set baskı=? where baskı = ?",(yeni_baskı,baskı))
            self.cursor.execute("Update kitaplar set Okunan=? where Okunan = ?",(yeni_okunma_bilgisi,Okunan))
            self.baglanti.commit()
            
   