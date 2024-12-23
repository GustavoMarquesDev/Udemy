class Televisor:
    def __init__(self, fabricante: str, modelo: str):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 0

    def aumentar_volume(self, valor: int):
        if self.volume + valor <= 100:
            self.volume += valor

        else:
            self.volume = 100

    def diminuir_volume(self, valor: int):
        if self.volume - valor >= 0:
            self.volume -= valor

        else:
            self.volume = 0

    def trocar_canal(self, canal: str):
        if canal in self.lista_de_canais:
            self.canal_atual = canal

    def sintonizarCanal(self, canal: str):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)
