# QrCodeGenerator

Adres kısmına yazdığın herhangi bir URL'yi ya da metni QR koda çeviren, koyu temalı küçük bir masaüstü uygulaması. Python ve [customtkinter](https://github.com/TomSchimansky/CustomTkinter) ile yazıldı.

## Özellikler

- URL, hyperlink ya da düz metinden QR kod üretir
- QR kod pencerenin içinde görünür
- PNG olarak kaydedilebilir
- Yuvarlak köşeli, koyu ve sade arayüz

## Kullanım

1. "Adres" kutusuna bir URL yaz
2. **Oluştur**'a bas ya da Enter'a bas
3. İstersen **Kaydet** ile PNG olarak kaydet

## Kurulum

Sadece Windows'ta çalışır. Python 3 kurulu olmalı.

```powershell
git clone https://github.com/delloRkicR/QrCodeGenerator.git
cd QrCodeGenerator
python -m pip install -r requirements.txt
python main.py
```

## Exe oluşturma

```powershell
python -m pip install pyinstaller
python -m PyInstaller --noconsole --onefile --icon=logo.ico --collect-all customtkinter --collect-all qrcode --add-data "logo.png;." --add-data "logo.ico;." main.py
```

Exe `dist\main.exe` içinde çıkar.

## Dosyalar

```
main.py             uygulama
logo.png            arayüzdeki logo
logo.ico            pencere ve görev çubuğu ikonu
requirements.txt    gerekli paketler
```

## Lisans

[MIT](LICENSE)
