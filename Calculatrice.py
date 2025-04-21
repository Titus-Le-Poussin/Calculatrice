# Calculatrice

import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.title("Calculatrice")
app.geometry("380x600")
screen_font = ("Bauhaus93", 24)
screen = customtkinter.CTkLabel(app, text="", font=screen_font)
screen.grid(row =0, column=0, sticky="E", padx= (10,10), columnspan = 4)

font_button = ("Bauhaus93", 20)

btn_0 = customtkinter.CTkButton(app, text="0", width = 75, height = 75, font=font_button)
btn_1 = customtkinter.CTkButton(app, text="1", width = 75, height = 75, font=font_button)
btn_2 = customtkinter.CTkButton(app, text="2", width = 75, height = 75, font=font_button)
btn_3 = customtkinter.CTkButton(app, text="3", width = 75, height = 75, font=font_button)
btn_4 = customtkinter.CTkButton(app, text="4", width = 75, height = 75, font=font_button)
btn_5 = customtkinter.CTkButton(app, text="5", width = 75, height = 75, font=font_button)
btn_6 = customtkinter.CTkButton(app, text="6", width = 75, height = 75, font=font_button)
btn_7 = customtkinter.CTkButton(app, text="7", width = 75, height = 75, font=font_button)
btn_8 = customtkinter.CTkButton(app, text="8", width = 75, height = 75, font=font_button)
btn_9 = customtkinter.CTkButton(app, text="9", width = 75, height = 75, font=font_button)
btn_plus = customtkinter.CTkButton(app, text ="+", width = 75, height = 180, font=font_button)
btn_moin = customtkinter.CTkButton(app, text ="-", width = 75, height = 75, font=font_button)
btn_fois = customtkinter.CTkButton(app, text ="x", width = 75, height = 75, font=font_button)
btn_diviser = customtkinter.CTkButton(app, text ="÷", width = 75, height = 75, font=font_button)
btn_point = customtkinter.CTkButton(app, text =".", width = 75, height = 75, font=font_button)
btn_Egale = customtkinter.CTkButton(app, text ="=", width = 75, height = 75, font=font_button)
btn_reset = customtkinter.CTkButton(app, text ="CE", width = 75, height = 75, font=font_button)

btn_0.grid(row=6, column=0, padx=(10, 10), pady=(10, 10))
btn_1.grid(row=5, column=0, padx=(10, 10), pady=(10, 10))
btn_2.grid(row=5, column=1, padx=(10, 10), pady=(10, 10))
btn_3.grid(row=5, column=2, padx=(10, 10), pady=(10, 10))
btn_4.grid(row=4, column=0, padx=(10, 10), pady=(10, 10))
btn_5.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))
btn_6.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
btn_7.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))
btn_8.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))
btn_9.grid(row=3, column=2, padx=(10, 10), pady=(10, 10))
btn_plus.grid(row=5, column=3, padx=(10, 10), pady=(10, 10), rowspan=2)
btn_moin.grid(row=3, column=3, padx=(10, 10), pady=(10, 10))
btn_fois.grid(row=2, column=3, padx=(10, 10), pady=(10, 10))
btn_diviser.grid(row=4, column=3, padx=(10, 10), pady=(10, 10))
btn_point.grid(row=6, column=1, padx=(10, 10), pady=(10, 10))
btn_Egale.grid(row=6, column=2, padx=(10, 10), pady=(10, 10))
btn_reset.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))



app.mainloop()
