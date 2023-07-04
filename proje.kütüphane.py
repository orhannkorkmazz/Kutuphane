from kütüphane import*
print(""" ***********************
Kütüphane programına hoşgeldiniz...
Yapmak istediğiniz işlemler:
1.Kitapları Göster
2.Kitap sorgulama
3.Kitap ekle
4.Kitap sil
5.Kitap Sayısı
6.Okunan Kitaplar
7.Kitap güncelle
8.Çıkış
*************************
      """)
kütüphane=Kütüphane()
while True:
    islem=input("Yapacağınız işlem:")
    if(islem=="8"):
        print("Program sonlandırılıyor..")
        break
    elif(islem=="1"):
        kütüphane.kitapları_göster()
    elif(islem=="2"):
        isim=input("Hangi kitapları istiyorsunuz?")
        print("İstediğiniz kitap sorgulanıyor,lütfen bekleyiniz....")
        time.sleep(1)
        kütüphane.kitap_sorgula(isim)

    elif(islem=="3"):
        isim=(input("İsim:"))
        isim=isim.upper()
        
        yazar=input("Yazar:")
        yazar=yazar.upper()
        yayinevi=input("Yayınevi:")
        yayinevi=yayinevi.upper()
        tür=input("Tür:")
        tür=tür.upper()
        baskı=input("Baskı:")
        baskı=baskı.upper()
        Okunan=input("Okundu mu?:")
        Okunan=Okunan.upper()
        yeni_kitap=Kitap(isim,yazar,yayinevi,tür,baskı,Okunan)
        print("Kitap ekleniyor..")
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi..")
        
    elif(islem=="4"):
        isim=input("Hangi kitabı silmek istiyorsunuz?")
        cevap=input("Emin misiniz?(E/H)")
        if(cevap=="E"):
            kütüphane.kitap_sil(isim)
    elif(islem=="5"):
        print("Kütüphanedeki kitap sayılarına bakılıyor....")
        time.sleep(1)
        kütüphane.kitap_sayisi()
    elif(islem=="6"):
        isim=input("Hangi kitabın okundu bilgisini istiyorsunuz?:")
        kütüphane.okunan_kitaplar(isim)
    elif(islem=="7"):
        isim1=input("Güncellemek istediğiniz kitabın ismini giriniz:")
        yeni_isim=(input("Kitabın yeni ismini giriniz:"))
        yeni_yazar=(input("Kitabın yeni yazarı giriniz:"))
        yeni_yayınevi=(input("Kitabın yeni yayınevini giriniz:"))
        yeni_tür=(input("Kitabın yeni türünü giriniz:"))
        yeni_baskı=(input("Kitabın yeni baskısını giriniz:"))
        yeni_okundu_bilgisi=(input("Kitabın yeni okunma durumunu giriniz:"))
        kütüphane.kitap_güncelleme_sorgusu(isim1,yeni_isim,yeni_yazar,yeni_yayınevi,yeni_tür,yeni_baskı,yeni_okundu_bilgisi)
        print("Güncelleme işlemi yapılıyor..")
        time.sleep(1)
        print("Güncellenme başarıyla yapıldı")     
    else:
        print("Geçersiz işlem,lütfen istenen işlemleri tuşlayınız.")