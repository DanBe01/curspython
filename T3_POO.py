"""
Class Mancare
class Pizza(Mancare)
class Paste(Mancare)

class comanda()
pret, lista produse, metoda livrare, etc

class client() cu sau fara card fidelitate
"""


from random import randint


class Mancare:

    def __init__(self, nume_mancare, ingrediente):
        self.nume = nume_mancare            # nume mancare
        self.ingrediente = ingrediente

    def add_topping(self, *lista):
        lista_topping = list(lista)
        for i in lista_topping:
            if i not in self.ingrediente:
                self.ingrediente.append(i)

    def remove_topping(self, *lista):
        lista_topping = list(lista)
        for i in lista_topping:
            if i in self.ingrediente:
                self.ingrediente.remove(i)

    def remove_toppings(self):
        self.ingrediente = self.list_ingrediente_standard.copy()


class Pizza(Mancare):

    numar_total_pizza_create = 0
    index_pizza_creata = 0
    list_ingrediente_standard = ['sos rosii', 'mozarella']
    dex_pret_blat = {'normal': 20, 'pufos': 22, 'subtire': 24}
    dex_pret_dimensiune = {'mica': 1, 'mare': 1.3}

    default_pizzas = {
        'marguerita': ['blat-normal', 'dimensiune-mica', []],
        'quatro_stagioni': ['blat-normal', 'dimensiune-mica', ['masline', 'bacon', 'ciuperci', 'sunca']],
        'capricciosa': ['blat-normal', 'dimensiune-mare', ['ardei', 'ciuperci', 'sunca']]
    }

    def __init__(self, nume, tip_blat='normal', dimensiune='mica', toppings=[]):    #args = toppings, change
        Pizza.numar_total_pizza_create += 1
        self.index_pizza_creata += Pizza.numar_total_pizza_create
        self.nume_pizza = nume
        self.data_validation_blat(tip_blat)
        self.data_validation_dimensiune(dimensiune)
        self.ingrediente = self.list_ingrediente_standard.copy()
        for topinguri in toppings:
            self.ingrediente.append(topinguri)
        super().__init__(self.nume_pizza, self.ingrediente)

    def data_validation_blat(self, tip_blat):
        if tip_blat.lower() in self.dex_pret_blat.keys():
            self.tip_blat = tip_blat.lower()
        else:
            print('Tipul blatului poate fi {}, {} sau {}. Standard = {}'.format(list(dex_pret_blat.keys())[0],
                                                                                list(dex_pret_blat.keys())[1],
                                                                                list(dex_pret_blat.keys())[2],
                                                                                list(dex_pret_blat.keys())[0]))
            self.tip_blat = list(dex_pret_blat.keys())[0]

    def data_validation_dimensiune(self, dimensiune):
        if dimensiune.lower() in self.dex_pret_dimensiune.keys():
            self.dimensiune_pizza = dimensiune.lower()
        else:
            print('Dimensiunea blatului poate fi {} sau {}. Standard = {}'.format(list(dex_pret_dimensiune.keys())[0],
                                                                                  list(dex_pret_dimensiune.keys())[1],
                                                                                  list(dex_pret_dimensiune.keys())[0]))
            self.dimensiune_pizza = list(dex_pret_dimensiune.keys())[0]

    @property
    def description(self):
        return "Pizza {}, dimensiune {} cu blat {} si cu urmatoarele ingrediente :{}. Pret total {}".format(self.nume_pizza,
                                                                                                            self.dimensiune_pizza,
                                                                                                            self.tip_blat,
                                                                                                            self.ingrediente,
                                                                                                            self.pret)

    @property
    def pret(self):
        return self.dex_pret_blat[self.tip_blat] * self.dex_pret_dimensiune[self.dimensiune_pizza] + 2 \
               * (len(self.ingrediente) - 2)

    @classmethod
    def create_pizza(cls, nume_pizza):
        if nume_pizza.lower() in cls.default_pizzas.keys():
            tip_blat = cls.default_pizzas[nume_pizza][0].split("-")[1]
            dimensiune_pizza = cls.default_pizzas[nume_pizza][1].split("-")[1]
            toppings = cls.default_pizzas[nume_pizza][2]
            return cls(nume_pizza, tip_blat, dimensiune_pizza, toppings)


class Paste(Mancare):

    numar_total_paste_create = 0
    index_pasta_creata = 0
    list_ingrediente_standard = ['emmental', 'smantana']
    dex_pret_paste = {'linguine': 20, 'penne': 22, 'macaroni': 24}
    dex_pret_dimensiune = {'mica': 1, 'mare': 1.3}

    default_pasta = {
        'quatro_formaggi': ['macaroni', 'dimensiune-mica', ['parmezan', 'oregano', 'ulei masline', 'basilic', 'gran padano']],
        'carbonara': ['linguine', 'dimensiune-mare', ['ardei', 'ciuperci', 'cubulete carne', 'sos rosii', 'oregano', 'basilic']]
    }

    def __init__(self, nume, tip_paste='linguine', dimensiune='mica', toppings=[]):
        Paste.numar_total_paste_create += 1
        self.index_pasta_creata += Paste.numar_total_paste_create
        self.nume_paste = nume
        self.data_validation_paste(tip_paste)
        self.data_validation_dimensiune(dimensiune)
        self.ingrediente = self.list_ingrediente_standard.copy()
        for elemente in toppings:
            self.ingrediente.append(elemente)
        super().__init__(self.nume_paste, self.ingrediente)

    def data_validation_paste(self, tip_paste):
        if tip_paste.lower() in self.dex_pret_paste.keys():
            self.tip_paste = tip_paste.lower()
        else:
            print('Tipul pastelor poate fi {}, {} sau {}. Standard = {}'.format(list(dex_pret_paste.keys())[0],
                                                                                list(dex_pret_paste.keys())[1],
                                                                                list(dex_pret_paste.keys())[2],
                                                                                list(dex_pret_paste.keys())[0]))
            self.tip_paste = list(dex_pret_paste.keys())[0]

    def data_validation_dimensiune(self, dimensiune):
        if dimensiune.lower() in self.dex_pret_dimensiune.keys():
            self.dimensiune_paste = dimensiune.lower()
        else:
            print('Dimensiunea pastelor poate fi {} sau {}. Standard = {}'.format(list(dex_pret_dimensiune.keys())[0],
                                                                                  list(dex_pret_dimensiune.keys())[1],
                                                                                  list(dex_pret_dimensiune.keys())[0]))
            self.dimensiune_paste = list(dex_pret_dimensiune.keys())[0]

    @property
    def description(self):
        return "Paste {}, portie {} de {} cu urmatoarele ingrediente :{}. Pret total {}".format(self.nume_paste,
                                                                                                self.dimensiune_paste,
                                                                                                self.tip_paste,
                                                                                                self.ingrediente,
                                                                                                self.pret)

    @property
    def pret(self):
        return self.dex_pret_paste[self.tip_paste] * self.dex_pret_dimensiune[self.dimensiune_paste] + 2 \
               * (len(self.ingrediente) - 2)

    @classmethod
    def create_pasta(cls, nume_pasta):
        if nume_pasta.lower() in cls.default_pasta.keys():
            tip_paste = cls.default_pasta[nume_pasta][0]
            dimensiune = cls.default_pasta[nume_pasta][1].split("-")[1]
            toppings = cls.default_pasta[nume_pasta][2]
            return cls(nume_pasta, tip_paste, dimensiune, toppings)


class Client:

    def __init__(self, nume, prenume, adresa, comanda, card=False):
        self.nume = nume
        self.prenume = prenume
        self.adresa = adresa
        self.comanda = comanda  #clasa_separata
        self.card = card

    @property
    def id_client(self):
        return 'CL' + str(randint(100000, 999999))

    @property
    def date_client(self):
        return "{} {}, adresa {}, card bancar {}".format(self.nume, self.prenume, self.adresa, self.card)

    @property
    def address(self):
        return self.adresa

    @address.setter
    def address(self, adresa_noua):
        self.adresa = adresa_noua

    @property
    def fullname(self):
        return '{} {}'.format(self.nume, self.prenume)

    @fullname.setter
    def fullname(self, nume_prenume_nou):
        self.nume, self.prenume = nume_prenume_nou.split("_")

    def add_card(self):
        self.card = True


class Comanda:

    produse_comanda = {} #format: pizza:cantitate
    produse_pret = {}   #format: pizza:pret / um

    def __init__(self, produse):
        self.produse_comanda = produse
        self.produse_pret = produse.copy()
        for i in self.produse_pret.keys():
            self.produse_pret[i] = i.pret

    @property
    def id_comanda(self):
        return randint(10000, 99999)

    def sterge_produse(self, produs):
        del(self.produse_comanda[produs])

    def adauga_produse(self, produs, cantitate):
        self.produse_comanda[produs] = cantitate

    @property
    def pret(self):
        valoare = 0
        for produs in self.produse_comanda.keys():
            valoare += produs.pret * self.produse_comanda[produs]
        return valoare

    @property
    def bon_fiscal(self):
        bon = ''
        for produs in self.produse_comanda:
            bon = bon + "{:<10} {:<20} - cantitate {:<5} - pret unitar {:<5} - pret total {:<5}".format(
                    produs.__class__.__name__,
                    produs.nume,
                    self.produse_comanda[produs],
                    self.produse_pret[produs],
                    self.produse_comanda[produs] * self.produse_pret[produs]
                    ) + '\n'

        bon = bon + "{:>90} {:>10}".format('Valoare totala', self.pret)

        return bon


marguerita = Pizza.create_pizza('marguerita')
calzone = Pizza('calzone', toppings=['masline', 'sunca', 'parmezan', 'ou'])
quatro_formaggi = Paste.create_pasta('quatro_formaggi')
carbonara = Paste.create_pasta('carbonara')

comanda1 = Comanda({calzone: 3, marguerita: 1, quatro_formaggi: 1})
comanda2 = Comanda({calzone: 3, marguerita: 1})

ninel = Client('ion', 'ninel', 'iancului 41', comanda2, card=True)
gigi = Client('Vasile', 'Gigi', 'iancului 42', comanda1)

print(ninel.comanda.bon_fiscal)
print(gigi.comanda.bon_fiscal)

print(carbonara.description)

calzone.remove_toppings()
print(gigi.comanda.bon_fiscal)


