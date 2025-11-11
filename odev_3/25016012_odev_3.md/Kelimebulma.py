def kelime_sayaci():
    print("--- Kelime Sayacı ---")
    metin = input("Lütfen analiz etmek istediğiniz metni (cümle/paragraf) girin: ")
    toplam_karakter = len(metin)

    metin_kucuk = metin.lower()

    import re
    hazirlanmis_metin = re.sub(r'[^a-z0-9\s]', ' ', metin_kucuk)

    kelimeler = hazirlanmis_metin.split()

    toplam_kelime = len(kelimeler)

    kelime_tekrar = {}
    for kelime in kelimeler:
        if kelime:
            kelime_tekrar[kelime] = kelime_tekrar.get(kelime, 0) + 1

    en_uzun_kelime_uzunlugu = 0
    if kelimeler:
        en_uzun_kelime = max(kelimeler, key=len)
        en_uzun_kelime_uzunlugu = len(en_uzun_kelime)
    
    print("\n--- İstatistikler ---")
    print(f"Toplam Kelime Sayısı: {toplam_kelime}")
    print(f"Toplam Karakter Sayısı (boşluklar dahil): {toplam_karakter}")
    print(f"En Uzun Kelimenin Uzunluğu: {en_uzun_kelime_uzunlugu}")
    print("\nKelime Tekrar Sayıları (Büyük/küçük harf duyarsız):")

    for kelime, sayi in sorted(kelime_tekrar.items(), key=lambda item: item[1], reverse=True):
        print(f"  '{kelime}': {sayi}")

kelime_sayaci()
#Bir cümle yazarken ingilizce alfabesinde kullanılmayan bir harf kullandığımızda boşluk gibi algılıyor.
#Örneğin ... kullanamıyor. diye yazdığımda "yor" hecesini ayrı kelime olarak sayıyor. Bunu nasıl düzeltebilirim acaba ben bulamadım.