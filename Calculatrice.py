# Calculatrice

import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

Max_chiffre= 9
pile_ecran = []
nombre_courant = False
operation_courante = False


def touche_appuyee(touche):
    print('Touche:', touche)
    if touche in['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        traite_touche_chiffre(touche)
    elif touche in ['MOIN', 'FOIS', 'DIVISER', 'PLUS']:
        traite_touche_operation(touche)


def _get_nombre_from_pile():
    text = _get_nombre_as_text_from_pile()
    if '.' in pile_ecran:
        return float(text)
    else:
        return int(text)


def update_screen(value = False):
    if value:
        screen.configure(text=value[0:9])
    else:
        screen.configure(text='0')

def _get_nombre_as_text_from_pile():
    text = ''
    for num in pile_ecran:
        text += str(num)
    return text


def traite_touche_chiffre(num):
    if len(pile_ecran) < Max_chiffre:
        if num == '.' and '.' in pile_ecran:
            return
        pile_ecran.append(num)
        ecran = ''.join(pile_ecran)
        update_screen(_get_nombre_as_text_from_pile())


def traite_touche_operation(operation):
    global nombre_courant, operation_courante
    if nombre_courant and operation_courante:
        execute_operation(operation_courante)
    if not nombre_courant: 
        nombre_courant = _get_nombre_from_pile()
    operation_courante = operation
    pile_ecran.clear()

def execute_operation(operation):
    global nombre_courant, operation_courante
    if operation:
        nombre2 = _get_nombre_from_pile()
        result = 0
        if operation == 'PLUS':
            result = nombre_courant + nombre2
        elif operation == 'MOIN':
            result = nombre_courant - nombre2
        elif operation == 'FOIS':
            result = nombre_courant * nombre2
        elif operation == 'DIVISER':
            if nombre2 != 0:
                result = nombre_courant / nombre2
            else:
                result = "Erreur"
        nombre_courant = result
        pile_ecran.clear()
        update_screen(str(nombre_courant))

app = customtkinter.CTk()
app.title("Calculatrice")
app.geometry("380x600")
screen_font = ("Bauhaus93", 24)
screen = customtkinter.CTkLabel(app, text="", font=screen_font)
screen.grid(row =0, column=0, sticky="E", padx= (10,10), columnspan = 4)

font_button = ("Bauhaus93", 20)

btn_0 = customtkinter.CTkButton(app, text="0", width = 75, height = 75, font=font_button, command=lambda : touche_appuyee('0'))
btn_1 = customtkinter.CTkButton(app, text="1", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('1'))
btn_2 = customtkinter.CTkButton(app, text="2", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('2'))
btn_3 = customtkinter.CTkButton(app, text="3", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('3'))
btn_4 = customtkinter.CTkButton(app, text="4", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('4'))
btn_5 = customtkinter.CTkButton(app, text="5", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('5'))
btn_6 = customtkinter.CTkButton(app, text="6", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('6'))
btn_7 = customtkinter.CTkButton(app, text="7", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('7'))
btn_8 = customtkinter.CTkButton(app, text="8", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('8'))
btn_9 = customtkinter.CTkButton(app, text="9", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('9'))
btn_plus = customtkinter.CTkButton(app, text ="+", width = 75, height = 180, font=font_button, command =lambda : touche_appuyee('PLUS'))
btn_moin = customtkinter.CTkButton(app, text ="-", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('MOIN'))
btn_fois = customtkinter.CTkButton(app, text ="x", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('FOIS'))
btn_diviser = customtkinter.CTkButton(app, text ="÷", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('DIVISER'))
btn_point = customtkinter.CTkButton(app, text =".", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('.'))
btn_Egale = customtkinter.CTkButton(app, text ="=", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('EGALE'))
btn_reset = customtkinter.CTkButton(app, text ="CE", width = 75, height = 75, font=font_button, command =lambda : touche_appuyee('RESET'))

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
