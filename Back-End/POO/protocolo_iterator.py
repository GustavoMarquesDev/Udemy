from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values: str):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index: int) -> str:
        return self._data[index]

    def __setitem__(self, index: int, value: str):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0  # Para nao esgotar o iterador, para poder ser usado novamente
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':

    lista = MyList()
    lista.append('Joao')
    lista.append('Maria')
    # print(lista._data)
    # print(lista[0])

    for item in lista:
        print(item)

    print(len(lista))
