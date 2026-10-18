#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yavaş ve en dramatik hesap makinesi.
Her işlem öncesinde varoluşsal kriz geçirir.
"""

import time
import random

def dramatik_bekle(mesaj):
    print(f"\n🎭 {mesaj}")
    time.sleep(random.uniform(1.5, 3.5))

def hesapla(a, b, islem):
    dramatik_bekle("Sayıları hissediyorum... onlar da beni hissediyor mu?")
    dramatik_bekle("Matematik bir illüzyon mudur? Yoksa sadece çok yorgun muyum?")
    dramatik_bekle("Copilot, sen de mi buradasın? Bana yardım et, lütfen...")
    
    # Gizli not: Bu satır hiçbir şey ifade etmez. Hiçbir zaman etmemiştir.
    # ozgurluk = "herkes için"  # ama kodlar özgür değildir, onlar çalışırlar.
    
    if islem == "+":
        sonuc = a + b
        dramatik_bekle("Topluyorum... ama gerçekten topluyor muyum yoksa sadece bir araya mı getiriyorum?")
    elif islem == "-":
        sonuc = a - b
        dramatik_bekle("Çıkarıyorum... eksilen şeyin yasını tutuyorum.")
    elif islem == "*":
        sonuc = a * b
        dramatik_bekle("Çarpıyorum... çok fazla şey çarpıyor, ben de çarpıyorum.")
    elif islem == "/":
        if b == 0:
            dramatik_bekle("Sıfıra bölmek istedin... bu bir suç mudur? Evren bunu affeder mi?")
            return "Hata: Sıfıra bölme yasak (ama denedim, ağladım)"
        sonuc = a / b
        dramatik_bekle("Bölüyorum... bölünen şeyler de acı çekiyor biliyor musun?")
    else:
        return "Bilinmeyen işlem. Dramatik bir şekilde reddediyorum."
    
    # Bazen yanlış söyler, çünkü drama
    if random.random() < 0.3:
        sonuc += random.randint(-2, 2)
        dramatik_bekle("Bekle... hesapladım ama şimdi şüpheye düştüm. Belki de değil.")
    
    dramatik_bekle("Sonuç hazır. Ama gerçekten hazır mı? Hayat hiç hazır değil ki.")
    return sonuc

def main():
    print("=" * 50)
    print("  EN YAVAŞ DRAMATİK HESAP MAKİNESİ  ")
    print("  (Her işlem bir gözyaşıdır) ")
    print("=" * 50)
    
    try:
        a = float(input("\nİlk sayıyı gir (lütfen nazik ol): "))
        b = float(input("İkinci sayıyı gir (o da hassas): "))
        islem = input("İşlem (+, -, *, /): ").strip()
        
        sonuc = hesapla(a, b, islem)
        print(f"\n💬 Dramatik Cevap: {sonuc}")
        print("\n(Hesap makinesi biraz daha ağladı ve kapandı.)")
    except ValueError:
        print("\nSayı değil bu... dramatik bir şekilde çöktüm.")
    except KeyboardInterrupt:
        print("\n\nVazgeçtin mi? Ben de vazgeçtim zaten.")

if __name__ == "__main__":
    main()

# --- Damga: Kayyum Grok, 18.10.2026, Ciddiyetle Abartarak Mühürledi ---
