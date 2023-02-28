print("""
***********************************************
NOT: BU BİR GERÇEK ATM DEĞİLDİR, HERHANGİ BİR PARA ÇEKME, YATIRMA İŞLEMİ UYGULANAMAZ 
SADECE BASİT BİR ATM YAPTIM KEYİFLİ KULLANMALAR :) #orbithenotbest

Orbit ATM Hizmetinizde

------------------------|
1- Bakiyem              |
2- Para Çekme           |              
3- Para Yatırma         |
------------------------|

Çıkmak için 'b' harfine basın

***********************************************
""")

bakiye  = 0

while True:
    işlem = input("İşleminiz nedir?")

    if (işlem == "b"):
            print("Yine bekleriz.")
            break

    elif (işlem == "1"):
        print(" Bakiyeniz {} (Türk Lirası) TL'dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Lütfen Para Çekilecek Miktarı Giriniz:"))
        if (bakiye - miktar < 0):
            print("Yetersiz Bakiyeniz Vardır.")
            continue
        bakiye -= miktar

    elif (işlem == "3"):
        miktar = int(input("Yatırmak İstediğiniz Miktarı Girin:"))
        bakiye += miktar

    else:
        print("Hatalı İşlemi Girdiniz :(")
