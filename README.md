# Auto Clicker

CustomTkinter ile yazılmış, threading destekli ve hotkey entegreli basit bir auto clicker.

## Özellikler

* **Modern GUI:** CustomTkinter tabanlı karanlık tema.
* **Hotkey Kontrolü:** Uygulama odakta olmasa bile çalışır.
* `Ctrl + Alt + N`: Başlat
* `Ctrl + Alt + Z`: Durdur


* **Esnek Koordinat:** Manuel koordinat girilmezse o anki imleç konumunu alır.
* **Modlar:** Belirli sayıda veya sonsuz tıklama.

## Gereksinimler

```
pip install customtkinter pyautogui keyboard
```

## Kullanım

1. Koordinatları gir (boş bırakırsan mevcut konumu alır).
2. Gecikme süresini saniye cinsinden ayarla.
3. Tıklama sayısını belirle (boş = sonsuz).
4. `BAŞLAT` butonuna veya kısayola bas.

