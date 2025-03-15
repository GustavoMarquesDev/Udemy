class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)


call1 = CallMe('5555-5555')
call1('João')
