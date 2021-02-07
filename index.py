#importando bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser #conectando banco de dados

# criando janela
janela = Tk()
janela.title("DP Systems- Acess Panel")
janela.geometry("600x300") #tamanho
janela.configure(background="white") #define cor
janela.resizable(width=False, height=False) #nao deixa redimencionar

# widgets
#quadro esquerda
leftFrame = Frame(janela, width = 200, height = 300, bg="MIDNIGHTBLUE", relief="raise")
leftFrame.pack(side=LEFT)

#quadro direita
rightFrame = Frame(janela, width = 395, height = 300, bg="MIDNIGHTBLUE", relief="raise")
rightFrame.pack(side=RIGHT)

# carregando imagem
logo = PhotoImage(file = "icons/logo.png")
logoLabel = Label(leftFrame, image=logo, bg="MIDNIGHTBLUE")
logoLabel.place(x=50, y=100) #posicionando

#usuario
userLabel = Label(rightFrame, text="Username:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="White")
userLabel.place(x=5, y=100)

userEntry = ttk.Entry(rightFrame, width=25)
userEntry.place(x=120, y=100)

#senha
passLabel = Label(rightFrame, text="PassWord:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="White")
passLabel.place(x=5, y=150)

passEntry = ttk.Entry(rightFrame, width=25, show="*")
passEntry.place(x=120, y=155)

#botoes
def login():
    User = userEntry.get()
    Password = passEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Password))
    print("Selecionou")
    verifylogin = DataBaser.cursor.fetchone()
    try:
        if (User in verifylogin and Password in verifylogin):
            messagebox.showinfo(title="Login Info", message="Confirmed access. Welcome !")

    except:
        messagebox.showerror(title="Login error", message="Access denied")

loginButton = ttk.Button(rightFrame, text="Login", width=10, command=login)
loginButton.place(x=100, y=250)

#funcao registro
def register():
    #removendo widgets de login
    loginButton.place(x=5000)
    registerButton.place(x=5000)
    #inserindo widgets de cadastro
    nameLabel = Label(rightFrame, text="Name:", font=("Century Gotic", 15), bg="MIDNIGHTBLUE", fg="White")
    nameLabel.place(x=7, y=7)

    nameEntry = ttk.Entry(rightFrame, width=30)
    nameEntry.place(x=80, y=9)

    emailLabel = Label(rightFrame, text="E-mail:", font=("Century Gotic", 15), bg="MIDNIGHTBLUE", fg="White")
    emailLabel.place(x=7, y=50)

    emailEntry = ttk.Entry(rightFrame, width=30)
    emailEntry.place(x=80, y=55)

    #fazendo registro
    def registerToDataBase():
        Name = nameEntry.get() #variavel nome recebe a entrada de dados
        Email = emailEntry.get()
        User = userEntry.get()
        Password = passEntry.get()

        if ( Name == "" and Email == "" and User == "" and Password == "" ):
            messagebox.showerror(title="Register error", message="Fill in all fields")

        else:            
            #inserindo no banco
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Password))
            DataBaser.conn.commit() #salvando alterações
            messagebox.showinfo(title="Register Info", message="Account successfully created")

    register = ttk.Button(rightFrame, text="Register", width=10, command=registerToDataBase)
    register.place(x=200, y=250)

    #funcao voltar
    def backToLogin():
        #removendo widgets cadastro
        nameLabel.place(x=5000)
        nameEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        register.place(x=5000)
        back.place(x=5000)
        #trazendo widgets sde login
        loginButton.place(x=100)
        registerButton.place(x=200)


    back = ttk.Button(rightFrame, text="Back", width=10, command=backToLogin)
    back.place(x=100, y=250)

registerButton = ttk.Button(rightFrame, text="Register", width=10, command=register)
registerButton.place(x=200, y=250)

janela.mainloop()