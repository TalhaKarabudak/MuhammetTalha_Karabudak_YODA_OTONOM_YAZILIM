def basit_hesap_makinesi():
    print("--- Basit Hesap Makinesi ---")
    print("İşlemler: +, -, *, /")
    print("'çık' yazarak programdan çıkabilirsiniz.")

    while True:
        try:
            giris = input("\nİlk sayı, işlem (+,-,*,/), ikinci sayı (örnek: 5 + 3) veya 'çık': ").strip().lower()

            if giris == 'çık':
                print("Hesap makinesi kapatılıyor. Güle güle!")
                break
            
            parcalar = giris.split()
            
            if len(parcalar) != 3:
                print("Hata: Geçersiz format. Lütfen 'sayı1 işlem sayı2' formatında girin (örnek: 10 * 5).")
                continue

            sayi1_str, islem, sayi2_str = parcalar
            
            sayi1 = float(sayi1_str)
            sayi2 = float(sayi2_str)

            sonuc = None

            if islem == '+':
                sonuc = sayi1 + sayi2
            elif islem == '-':
                sonuc = sayi1 - sayi2
            elif islem == '*':
                sonuc = sayi1 * sayi2
            elif islem == '/':
                # Sıfıra bölme kontrolü
                if sayi2 == 0:
                    print("HATA: Bir sayı sıfıra bölünemez.")
                    continue
                sonuc = sayi1 / sayi2
            else:
                print(f"Hata: Geçersiz işlem ('{islem}'). Sadece +, -, *, / kullanın.")
                continue

            print(f"Sonuç: {sayi1} {islem} {sayi2} = {round(sonuc, 2)}")

        except ValueError:
            print("Hata: Sayı girişleri geçersiz. Lütfen sadece sayısal değerler girin.")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")

basit_hesap_makinesi()