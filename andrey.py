class Libro:
    def __init__(self,titulo, autor, genero):
        self.titulo=titulo 
        self.autor=autor
        self.genero=genero
    def escogido(self):
        if input("desea saber acerca del Renacuajo Paseador o de La Pobre Viejecita:") == "Renacuajo Paseador":
            print("Título:", self.titulo)
            print("Autor:", self.autor)
            print("Género:", self.genero)

        else:
            print("Título:", self.titulo)
            print("Autor:", self.autor)
            print("Género:", self.genero)
            

la_pobre_viejecita = Libro("La Pobre Viejecita", "Rafael Pombo", "Poema")
renacuajo_paseador = Libro("Renacuajo Paseador", "Rafael Pombo", "Animación")
renacuajo_paseador.escogido
la_pobre_viejecita.escogido()
