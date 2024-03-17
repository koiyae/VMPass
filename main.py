import customtkinter as ctk
import random

###############################################################################################

#######################################[MAIN WINDOW]###########################################

main_window = ctk.CTk()

main_window.title("VMPass")
main_window.iconbitmap('ico/lock.ico')
main_window.geometry("660x400")
main_window.resizable(width=False, height=False)
main_window._set_appearance_mode("system")

mainlabel1 = ctk.CTkLabel(main_window, text="ENCRIPTADOR", font=("Helvetica",23,"bold"))
mainlabel1.place(x=90,y=30)

mainlabel2 = ctk.CTkLabel(main_window, text="GERADOR", font=("Helvetica",23,"bold"))
mainlabel2.place(x=440,y=30)

##############################################################################################

#########################################[FUNCTIONS ]#########################################

def window():   # Error window


    window = ctk.CTkToplevel(main_window)
    window.geometry("200x100")
    window.resizable(width=False, height=False)

    winlabel = ctk.CTkLabel(window, text="Insira um valor numérico\nde no mínimo 8 caracteres",
                            font=("Helvetica",12))
    winlabel.pack(pady=30)


def passwd_gen():   # Password generator

    char = "abcdefghijklmnopqrstuvwcxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~<>?!@#$%&*[]_-^.,"

    len_str = entry2.get()


    try:
        length = int(len_str)
        if length <= 7:
            window()
        else:
            password = ""
            for passchar in range(length):
                passchar = random.choice(char)
                password += passchar
        
            delete_gen()
            gen_pass_text.configure(state="normal")
            gen_pass_text.insert("1.0", text=password)
            gen_pass_text.configure(state="disabled")

    except ValueError:
        window()


def passwd_encrypt():   # Password encryption
    passwd = ""

    text = entry1.get()

    for letter in text:
        if letter in "Aa": passwd += "%"
        elif letter in "Ee": passwd += "B"
        elif letter in "Ii": passwd += "7"
        elif letter in "Oo": passwd += "&"
        elif letter in "Uu": passwd += "0"
        elif letter in "0": passwd += "r"
        elif letter in "Ss": passwd += "9"
        elif letter in "Tt": passwd += "$r"
        elif letter in "Hh": passwd += "~"
        else: passwd = passwd + letter
    delete_encrypt()
    passwd_text.configure(state="normal")
    passwd_text.insert("1.0",text=passwd)
    passwd_text.configure(state="disabled")


def delete_encrypt():   # Deletes encrypted password text box
     passwd_text.configure(state="normal")
     passwd_text.delete("1.0", "end")
     passwd_text.configure(state="disabled")

def delete_gen():   # Deletes generated password text box
    gen_pass_text.configure(state="normal")
    gen_pass_text.delete("1.0", "end")
    gen_pass_text.configure(state="disabled")

def clipper():  # Copies encrypted password to clipboard
    main_window.clipboard_clear()
    main_window.clipboard_append(passwd_text.get("1.0","end"))

def clipper_gen():  # Copies generated password to clipboard
    main_window.clipboard_clear()
    main_window.clipboard_append(gen_pass_text.get("1.0","end"))

###############################################################################################################################

##################################################[PASSWORD ENCRYPTER FRAME]###################################################
frame = ctk.CTkFrame(main_window, width=320, height=320, fg_color="#808080").place(x=10, y=70)


label1 = ctk.CTkLabel(frame, text="Insira aqui a senha\na ser criptografada:", 
                      font=("Helvetica",16,"bold"), fg_color="#808080", corner_radius=0)
label1.place(x= 99, y=90)

entry1 = ctk.CTkEntry(frame, width=200, height=40, corner_radius=0)
entry1.place(x=76, y=140)

btn = ctk.CTkButton(frame, text="Criptografar", 
                    command=passwd_encrypt, corner_radius=0, width=120, height=40,
                    fg_color="#062BFF",border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn.place(x=50, y=190)

btn2 = ctk.CTkButton(frame, text="Limpar", 
                    command=delete_encrypt, corner_radius=0, width=120, height=40,
                    fg_color="#062BFF",border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn2.place(x=180, y=190)

btn3 = ctk.CTkButton(frame, text="Copiar", 
                    command=clipper, corner_radius=0, width= 120, height=40,
                    fg_color="#062BFF",border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn3.place(x=113, y=340)

label = ctk.CTkLabel(frame, text="A sua nova senha é: ", fg_color="#808080", corner_radius=0, font=("Helvetica",15,"bold"))
label.place(x=101, y=260)

passwd_text = ctk.CTkTextbox(frame, width=200, height=40, font=("Helvetica", 16))
passwd_text.configure(state="disabled")
passwd_text.place(x=76, y=290)

##############################################################################################################################

##################################################[PASSWORD GENERATOR FRAME]##################################################

frame2 = ctk.CTkFrame(main_window, width=310, height=320, fg_color="#808080").place(x=340, y=70)

label1 = ctk.CTkLabel(frame2, text="Tamanho da senha\n a ser gerada: ", 
                      font=("Helvetica", 16, "bold"), fg_color="#808080", corner_radius=0)
label1.place(x= 429, y=90)

btn4 = ctk.CTkButton(frame2, text="Gerar", 
                    command=passwd_gen, corner_radius=0, width=120, height=40,
                    fg_color="#062BFF",border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn4.place(x=370, y=190)

btn4 = ctk.CTkButton(frame2, text="Gerar", 
                    command=passwd_gen, corner_radius=0, width=120, height=40,
                    fg_color="#062BFF",border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn4.place(x=370, y=190)

btn5 = ctk.CTkButton(frame2, text="Limpar", 
                    command=delete_gen, corner_radius=0, width= 120, height=40,
                    fg_color="#062BFF",border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn5.place(x=500, y=190)

btn6 = ctk.CTkButton(frame, text="Copiar", 
                    command=clipper_gen, corner_radius=0, width= 120, height=40,
                    fg_color="#062BFF", border_width=2, 
                    border_color="white", font=("Helvetica",14,"bold"))
btn6.place(x=438, y=340)

label = ctk.CTkLabel(frame2, text="A sua nova senha é: ", fg_color="#808080", corner_radius=0, font=("Helvetica",15,"bold"))
label.place(x=425, y=230)

gen_pass_text = ctk.CTkTextbox(frame2, width=200, height=70, font=("Helvetica", 16))
gen_pass_text.configure(state="disabled")
gen_pass_text.place(x=396, y=260)


entry2 = ctk.CTkEntry(frame2, width=200, height=40, corner_radius=0)
entry2.place(x=396, y=140)


##############################################################################################################################

main_window.mainloop()