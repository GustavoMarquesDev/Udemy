from funcionalidades import Televisor


class ControleRemoto:
    def __init__(self, televisor: Televisor):
        self.televisor = televisor

    def aumentar_volume(self, valor: int):
        self.televisor.aumentar_volume(valor)

    def diminuir_volume(self, valor: int):
        self.televisor.diminuir_volume(valor)

    def trocar_canal(self, canal: str):
        self.televisor.trocar_canal(canal)

    def sintonizar_canal(self, canal: str):
        self.televisor.sintonizarCanal(canal)


tv = Televisor("Samsung", "TV")
controle = ControleRemoto(tv)


controle.aumentar_volume(10)
