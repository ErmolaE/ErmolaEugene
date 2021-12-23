from random import shuffle

class cell:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    name = property(get_name)
    id = property(get_id)    

class basic_cell(cell):

    def __init__(self, name, id, own, price, rents, monopoly, mortgage):
        super().__init__(name, id)
        self.__own = own
        self.__price = price
        self.__rents = rents
        self.__monopoly = monopoly
        self.__mortgage = mortgage

    def get_own(self):
        return self.__own

    def set_own(self, own):
        self.__own = own

    def get_price(self):
        return self.__price

    def get_rents(self):
        return self.__rents

    def get_monopoly(self):
        return self.__monopoly

    def set_monopoly(self, monopoly):
        self.__monopoly = monopoly

    def get_mortgage(self):
        return self.__mortgage

    def set_mortgage(self, mortgage):
        self.__mortgage = mortgage

    own = property(get_own, set_own)
    price = property(get_price)
    rents = property(get_rents)
    monopoly = property(get_monopoly, set_monopoly)
    mortgage = property(get_mortgage, set_mortgage)

class estate(basic_cell):

    def __init__(self, name, id, own, price, rents, monopoly, mortgage, hotel_price, hotel_count):
        super().__init__(name, id, own, price, rents, monopoly, mortgage)
        self.__hotel_price = hotel_price
        self.__hotel_count = hotel_count

    def get_hotel_price(self):
        return self.__hotel_price

    def get_hotel_count(self):
        return self.__hotel_count
    
    def set_hotel_count(self, hotel_count):
        self.__hotel_count = hotel_count

    hotel_price = property(get_hotel_price)
    hotel_count = property(get_hotel_count, set_hotel_count)

    def calc_rent(self):
        if self.mortgage==1:
            rent=0
        elif self.hotel_count>0:
            rent=self.rents[self.hotel_count+1]
        elif self.monopoly==0:
            rent=self.rents[0]
        else:
            rent=self.rents[1]
        return rent

class railway_station(basic_cell):

    def __init__(self, name, id, own, price, rent, monopoly, mortgage):
        super().__init__(name, id, own, price, rent, monopoly, mortgage)

    def calc_rent(self):
        if self.mortgage==1:
            rent=0
        else:
            rent=self.rents[self.monopoly]
        return rent

class utility_company(basic_cell):

    def __init__(self, name, id, own, price, rent, monopoly, mortgage):
        super().__init__(name, id, own, price, rent, monopoly, mortgage)

    def calc_rent(self, value):
        if self.mortgage==1:
            rent=0
        else:
            rent=value*self.rents[self.monopoly]
        return rent

class community_chest(cell):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.__defs = []

    def get_defs(self):
        return self.__defs

    def set_defs(self, defs):
        self.__defs.extend(defs)

    defs = property(get_defs)
    
    def def1(self):
        print("In development...")

    def def2(self):
        print("In development...")

    def def3(self):
        print("In development...")

    def def4(self):
        print("In development...")

    def def5(self):
        print("In development...")

    def def6(self):
        print("In development...")

    def def7(self):
        print("In development...")

    def def8(self):
        print("In development...")

    def def9(self):
        print("In development...")

    def def10(self):
        print("In development...")
    
    def create_defs(self):
        l=[self.def1(), self.def2(), self.def3(), self.def4(), self.def5(), self.def6(), self.def7(), self.def8(), self.def9(), self.def10()]
        shuffle(l)
        self.set_defs(l)

class chance(cell):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.__defs = []

    def get_defs(self):
        return self.__defs

    def set_defs(self, defs):
        self.__defs.extend(defs)

    defs = property(get_defs)
    
    def def1(self):
        print("In development...")

    def def2(self):
        print("In development...")

    def def3(self):
        print("In development...")

    def def4(self):
        print("In development...")

    def def5(self):
        print("In development...")

    def def6(self):
        print("In development...")

    def def7(self):
        print("In development...")

    def def8(self):
        print("In development...")

    def def9(self):
        print("In development...")

    def def10(self):
        print("In development...")
    
    def create_defs(self):
        l=[self.def1(), self.def2(), self.def3(), self.def4(), self.def5(), self.def6(), self.def7(), self.def8(), self.def9(), self.def10()]
        shuffle(l)
        self.set_defs(l)

class player:

    def __init__(self, name, id, money, position, bankrupt, capital):
        self.__name = name
        self.__id = id
        self.__money = money
        self.__position = position
        self.__estates = []
        self.__mortgaged = []
        self.__bankrupt = bankrupt
        self.__capital = capital

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_estates(self):
        return self.__estates

    def set_estates(self, estates):
        self.__estates.append(estates)

    def del_estates(self, estates):
        self.__estates.remove(estates)

    def get_mortgaged(self):
        return self.__mortgaged

    def set_mortgaged(self, mortgaged):
        self.__mortgaged.append(mortgaged)

    def del_mortgaged(self, mortgaged):
        self.__mortgaged.remove(mortgaged)

    def get_bankrupt(self):
        return self.__bankrupt

    def set_bankrupt(self, bankrupt):
        self.__bankrupt = bankrupt

    def get_capital(self):
        return self.__capital

    def set_capital(self, capital):
        self.__capital = capital

    name = property(get_name, set_name)
    id = property(get_id)
    money = property(get_money, set_money)
    position = property(get_position, set_position)
    estates = property(get_estates, set_estates, del_estates)
    mortgaged = property(get_mortgaged, set_mortgaged, del_mortgaged)
    bankrupt = property(get_bankrupt, set_bankrupt)
    capital = property(get_capital, set_capital)

    def roll(self, dice1, dice2):
        pos = self.get_position() + dice1 + dice2
        self.set_position(pos)
        return self.position

    def increase_money(self, value):
        x = self.get_money() + value
        self.set_money(x)
        self.increase_capital(value)
        return self.money

    def decrease_money(self, value):
        x = self.get_money() - value
        self.set_money(x)
        self.decrease_capital(value)
        return self.money

    def increase_capital(self, value):
        x = self.get_capital() + value
        self.set_capital(x)
        return self.capital

    def decrease_capital(self, value):
        x = self.get_capital() - value
        self.set_capital(x)
        return self.capital

    def buy_estate(self, cell, value):
        self.decrease_money(value)
        self.increase_capital(value/2)
        self.set_estates(cell)

    def in_mortgaged(self, cell):
        self.del_estates(cell)
        self.set_mortgaged(cell)
        cell.set_mortgage(1)
        self.decrease_capital(cell.price/2)
        self.increase_money(cell.price/2)

    def out_mortgaged(self, cell):
        self.del_mortgaged(cell)
        self.set_estates(cell)
        cell.set_mortgage(0)
        self.increase_capital(cell.price/2)
        self.decrease_money(cell.price*0,55)

    def build_hotel(self, cell):
        self.decrease_money(cell.hotel_price)
        self.increase_capital(cell.hotel_price/2)
        cell.set_hotel_count(cell.hotel_count+1)