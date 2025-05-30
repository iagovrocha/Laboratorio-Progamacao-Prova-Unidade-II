import os 

class Arquivo:
    def __init__(self):
        if os.path.isfile('BD_Lab_Prova.csv'):
            print("O arquivo já existe")
        else:
            with open("BD_Lab_Prova.csv","w",newline='') as a:
                pass

    def salvarArquivo(self, objeto):
        dictObjeto = objeto.__dict__
if __name__ == "__main__":
     arq = Arquivo()
    