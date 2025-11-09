import random

def sayi_tahmin_oyunu():
    gizli_sayi = random.randint(1, 100)
    max_hak = 10
    deneme_sayisi = 0
    tahmin_edildi = False

    print("--- Sayı Tahmin Oyunu ---")
    print("1 ile 100 arasında bir sayı tuttum. 10 tahmin hakkın var.")

    while deneme_sayisi < max_hak:
        try:
            kalan_hak = max_hak - deneme_sayisi
            tahmin = int(input(f"Kalan hakkınız: {kalan_hak} - Tahmininiz: "))

            if not (1 <= tahmin <= 100):
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            deneme_sayisi += 1

            if tahmin == gizli_sayi:
                tahmin_edildi = True
                break
            elif tahmin < gizli_sayi:
                print("Daha YÜKSEK bir sayı dene!")
            else:
                print("Daha DÜŞÜK bir sayı dene!")

        except ValueError:
            print("Geçersiz giriş. Lütfen bir tam sayı girin.")

    print("\n--- Oyun Bitti ---")
    if tahmin_edildi:
        print(f"TEBRİKLER! Sayıyı {deneme_sayisi} denemede doğru bildin.")
    else:
        print(f"Tahmin hakkınız bitti. Tutulan sayı: {gizli_sayi} idi. Daha sonra tekrar deneyin.")

sayi_tahmin_oyunu()