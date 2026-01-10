import customtkinter as ctk
import pyautogui
import threading
import time
import keyboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

is_clicking = False

def clicker(tiklama_sayisi, gecikme, x, y):
    global is_clicking
    sayac = 0
    while is_clicking and (sayac < tiklama_sayisi or tiklama_sayisi == 0):
        pyautogui.click(x, y)
        sayac += 1
        durum_label.configure(text=f"Tıklama: {sayac}")
        time.sleep(gecikme)
    durum_label.configure(text="Durduruldu")

def baslat():
    global is_clicking
    if is_clicking:
        return

    try:
        tiklama_sayisi = tiklama_entry.get()
        gecikme = float(gecikme_entry.get())

        tiklama_sayisi = 0 if tiklama_sayisi == "" else int(tiklama_sayisi)

        x = x_entry.get()
        y = y_entry.get()

        if x == "" or y == "":
            x, y = pyautogui.position()
        else:
            x, y = int(x), int(y)

        is_clicking = True
        durum_label.configure(text="Çalışıyor")
        threading.Thread(
            target=clicker,
            args=(tiklama_sayisi, gecikme, x, y),
            daemon=True
        ).start()

    except:
        durum_label.configure(text="Hatalı giriş")

def durdur():
    global is_clicking
    is_clicking = False

def hotkeyler():
    keyboard.add_hotkey("ctrl+alt+n", baslat)
    keyboard.add_hotkey("ctrl+alt+z", durdur)

threading.Thread(target=hotkeyler, daemon=True).start()

# ---------------- ARAYÜZ ---------------- #

app = ctk.CTk()
app.geometry("360x520")
app.title("Auto Clicker")
app.resizable(False, False)

baslik = ctk.CTkLabel(
    app,
    text="AUTO CLICKER",
    font=ctk.CTkFont(size=22, weight="bold")
)
baslik.pack(pady=20)

kart = ctk.CTkFrame(app, corner_radius=22)
kart.pack(padx=20, pady=10, fill="x")

def giris_alani(parent, placeholder):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        height=42,
        corner_radius=14
    )
    entry.pack(padx=15, pady=8, fill="x")
    return entry

x_entry = giris_alani(kart, "X koordinatı (boş: anlık)")
y_entry = giris_alani(kart, "Y koordinatı (boş: anlık)")
tiklama_entry = giris_alani(kart, "Tıklama sayısı (boş: sonsuz)")
gecikme_entry = giris_alani(kart, "Gecikme (saniye)")

buton_frame = ctk.CTkFrame(app, fg_color="transparent")
buton_frame.pack(pady=25)

baslat_btn = ctk.CTkButton(
    buton_frame,
    text="BAŞLAT",
    height=56,
    width=130,
    corner_radius=28,
    font=ctk.CTkFont(size=16, weight="bold"),
    command=baslat
)
baslat_btn.grid(row=0, column=0, padx=10)

durdur_btn = ctk.CTkButton(
    buton_frame,
    text="DURDUR",
    height=56,
    width=130,
    corner_radius=28,
    fg_color="#aa3333",
    hover_color="#882222",
    font=ctk.CTkFont(size=16, weight="bold"),
    command=durdur
)
durdur_btn.grid(row=0, column=1, padx=10)

durum_label = ctk.CTkLabel(
    app,
    text="Hazır",
    height=40,                     
    anchor="center",
    font=ctk.CTkFont(size=14),
    text_color="#7aa2f7"
)
durum_label.pack(pady=10)

footer = ctk.CTkFrame(app, fg_color="transparent")
footer.pack(side="bottom", fill="x", pady=10)

bilgi = ctk.CTkLabel(
    footer,
    text="Başlat: Ctrl + Alt + N   |   Durdur: Ctrl + Alt + Z",
    font=ctk.CTkFont(size=11),
    text_color="gray"
)
bilgi.pack()

app.mainloop()
