import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from pathlib import Path


class Logon(ctk.CTk): 

    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.geometry("800x600")
        self.minsize(800, 600)
        self.title('Login')
     
                
        # Imagem pattern imagem inical da tela de login
        img1 = ImageTk.PhotoImage(Image.open("Image/pattern.png"))
        l1 = ctk.CTkLabel(master=self, image=img1)
        l1.pack()

        Frame_Tela_Login = ctk.CTkFrame(master=l1, width=500, height=500, corner_radius=30)
        Frame_Tela_Login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = ctk.CTkLabel(master=Frame_Tela_Login, text="Logar", font=('Century Gothic', 40))
        l2.place(x=190, y=45)

        self.Entry_Nome_User = ctk.CTkEntry(master=Frame_Tela_Login, width=390, height=50, placeholder_text='Nome', font=('Century Gothic', 20))
        self.Entry_Nome_User.place(x=60, y=130)

        self.Entry_Senha_User = ctk.CTkEntry(master=Frame_Tela_Login, width=390, height=50, placeholder_text='Senha', show="*", font=('Century Gothic', 20))
        self.Entry_Senha_User.place(x=60, y=200)

        l3 = ctk.CTkLabel(master=Frame_Tela_Login, text="Esqueceu senha?", font=('Century Gothic', 16))
        l3.place(x=310, y=255)

        Button_Logar = ctk.CTkButton(master=Frame_Tela_Login, width=390, height=50, text="Entrar", command="", corner_radius=6)
        Button_Logar.place(x=60, y=300)

        img2 = ctk.CTkImage(Image.open("Image/Google.webp").resize((20, 20), Image.LANCZOS))
       
        button2 = ctk.CTkButton(master=Frame_Tela_Login, image=img2, text="Google", width=390, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command="")
        button2.place(x=60, y=370)


if __name__ == "__main__":
    logon = Logon()
    logon.mainloop()
