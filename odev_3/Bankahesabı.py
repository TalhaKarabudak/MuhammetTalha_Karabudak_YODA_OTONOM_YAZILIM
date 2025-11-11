class Hesap:

    def __init__(self, ad_soyad, hesap_numarasi, baslangic_bakiye=0):
        self.ad_soyad = ad_soyad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = max(0, baslangic_bakiye) 
        print(f"Yeni Hesap Oluşturuldu: {self.ad_soyad}, Hesap No: {self.hesap_numarasi}")

    def bakiye_goruntule(self):
        print(f"\n--- Bakiye Sorgulama ---")
        print(f"Hesap Sahibi: {self.ad_soyad}")
        print(f"Güncel Bakiye: {self.bakiye:.2f} TL")
        print("--------------------------")
        return self.bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar:.2f} TL yatırıldı. Yeni bakiye: {self.bakiye:.2f} TL.")
            return True
        else:
            print("Hata: Yatırılacak miktar pozitif olmalıdır.")
            return False

    def para_cek(self, miktar):
        if miktar <= 0:
            print("Hata: Çekilecek miktar pozitif olmalıdır.")
            return False
        
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"{miktar:.2f} TL çekildi. Yeni bakiye: {self.bakiye:.2f} TL.")
            return True
        else:
            print(f"Hata: Yetersiz bakiye. Mevcut bakiye: {self.bakiye:.2f} TL.")
            return False

def banka_yonetim_sistemi():
    print("--- Basit Banka Yönetim Sistemi ---")
    
    ad_soyad = input("Hesap Sahibi Adı Soyadı: ")
    hesap_no = input("Hesap Numarası (Örn: TR12345): ")
    try:
        baslangic = float(input("Başlangıç Bakiyesi (Opsiyonel, varsayılan 0): ") or 0)
    except ValueError:
        print("Geçersiz bakiye girişi, 0 TL olarak ayarlandı.")
        baslangic = 0
        
    musteri_hesap = Hesap(ad_soyad, hesap_no, baslangic)

    while True:
        print("\n--- İşlemler ---")
        print("1: Bakiye Görüntüle")
        print("2: Para Yatırma")
        print("3: Para Çekme")
        print("4: Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")

        if secim == '1':
            musteri_hesap.bakiye_goruntule()
        
        elif secim == '2':
            try:
                miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                musteri_hesap.para_yatir(miktar)
            except ValueError:
                print("Hata: Geçersiz miktar girişi.")

        elif secim == '3':
            try:
                miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                musteri_hesap.para_cek(miktar)
            except ValueError:
                print("Hata: Geçersiz miktar girişi.")
        
        elif secim == '4':
            print("Sistemden çıkılıyor. İyi günler!")
            break
        
        else:
            print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir numara girin.")

banka_yonetim_sistemi()