import os
import sys
import tkinter as tk
from tkinter import messagebox

def toggle_dark_mode():
    try:
        # Powershell komutu ile karanlık modu değiştirme
        powershell_cmd = 'powershell "& {$Theme = (Get-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize).SystemUsesLightTheme; if ($Theme -eq 1) { Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name SystemUsesLightTheme -Value 0; Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value 0 } else { Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name SystemUsesLightTheme -Value 1; Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value 1 }}"'
        
        # Komutu çalıştır
        os.system(powershell_cmd)
        
        # Tema durumunu kontrol et
        theme_check = os.popen('powershell "(Get-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize).SystemUsesLightTheme"').read().strip()
        
        if theme_check == '1':
            messagebox.showinfo("Tema Değişimi", "Açık Mod (Light Mode) aktif")
        else:
            messagebox.showinfo("Tema Değişimi", "Koyu Mod (Dark Mode) aktif")
    
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Pencere oluşturma ve tema değişimini çağırma
root = tk.Tk()
root.withdraw()  # Pencereyi gizle
toggle_dark_mode()
root.destroy()  # Pencereyi kapat