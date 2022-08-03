from tkinter import *
from tkinter import ttk
from Code.Brain import getEscola, getEmpresas


"""
/**
 * Codigo feito por Leonardo Pinheiro
 * IDE: Visual Studio Code
 * Turma: Info 0121
 * IFNMG - Campus Almenara
 * GitHub: https://github.com/SrPinheiro
 */
"""

janela = Tk()

class aplicativo():
    txt1 = (object)

    
    def __init__(self):
        self.janela = janela
        self.validarEntradas()
        self.tela()
        self.construcao()
        self.janela.mainloop()


    def tela(self):
        self.janela.title("LuluBot 1.0")
        self.janela.geometry("520x160")
        self.janela.resizable(height = False, width=False)
        self.janela.iconphoto(False, PhotoImage(file = "./Images/icon.png"))
        self.janela.configure(background= "#F0F8FF")


    def construcao(self):
        self.txt1 = Label(self.janela, text = "Gerar: ")
        self.txt1.configure(background = "#F0F8FF")
        self.txt1.place(x = 40, y = 65)
        

        self.guias = ["Escolas", "Empresas"]
        self.selecionar = ttk.Combobox(self.janela, values = self.guias)
        self.selecionar.set("Escolas")
        self.selecionar.configure(state = "#F0F8FF")
        self.selecionar.place(x = 90, y = 65, width = 100)

        self.txt2 = Label(self.janela, text = "Quantidade: ")
        self.txt2.configure(background = "#F0F8FF")
        self.txt2.place(x = 300, y = 65)

        self.quantidade = Entry(self.janela, validate = "key", validatecommand = self.vcmd2,)
        self.quantidade.place(x = 385, y = 64, width = 100)
        
        self.butao = Button(self.janela, text = "Executar", command = lambda: [self.botao()], background = "#E6E6FA", activebackground = "#00FF00") #F0F8FF #00FF00
        self.butao.place(x = 215, y = 100)


    def botao(self):
        try:
            ciclos = int(self.quantidade.get())

        except ValueError:
            ciclos = 1

        for i in range(0, ciclos):
            if self.selecionar.get() == "Escolas":
                getEscola()
            
            elif self.selecionar.get() == "Empresas":
                getEmpresas()

    
    def validarEntradas(self):
        self.vcmd2 = (self.janela.register(self.validarQuantidade), "%P")


    def validarQuantidade(self, text):
            if text == "":
                return True

            try:
                value = int(text)

            except ValueError:
                return False
            
            return 0 <= value < 100 


if __name__ == "__main__":
    aplicativo()