
'''
In this scenario, there is a Wholesaler named Binghamton Wholesale.
They are having trouble in their communication with the shops which they sell their stationary goods.
They are sending emails for the price changes for all of their products to ALL LINKED SHOPS.
For example you are the Owner of ShopA and you are buying rubber erasers and squared notebook from Binghamton Wholesale
But you receive emails for the price changes in every product of Binghamton Wholesale, It is disturbing(spamming basically)
As a team, we designed a solution using Observer Pattern. With this code, Binghamton Wholesale can send price updates to a specific shop about the products associated with it.

==========================================
Title:  Solution with Observer Pattern
Authors: Goktug Selcuk, Gungor Yolac, Aral Yucel, Hamza Sahin
Date:   9 Dec 2020
==========================================


'''


from abc import ABC, abstractmethod

class StationaryGoods(ABC): #Publisher Class

    @abstractmethod
    def addShop(self,shop):
        pass

    @abstractmethod
    def removeShop(self, shop):
        pass

    @abstractmethod
    def notifyShop(self, shop):
        pass

    def get_price(self):
        return self.price

    def set_price(self,price):
        self.old_price = self.price
        self.price = price
        self.notifyShop()

class Notebook(StationaryGoods): #ConcretePublisher 1
    def __init__(self,type,price):
        self.name = "notebook"
        self.type = type
        self.price = price
        self.old_price=price

    shops_notebook = []

    def get_type(self):
        return self.type

    def addShop(self, shop):
        self.shops_notebook.append(shop)

    def removeShop(self, shop):
        self.shops_notebook.remove(shop)

    def notifyShop(self):
        for shop in self.shops_notebook:
            shop.sendUpdate(self)

        print("****************************************")


class Eraser(StationaryGoods): #ConcretePublisher2
    def __init__(self,type,price):
        self.name = "eraser"
        self.type = type
        self.price = price

    shops_eraser = []

    def addShop(self, shop):
        self.shops_eraser.append(shop)

    def removeShop(self, shop):
        self.shops_eraser.remove(shop)

    def notifyShop(self):
        for shop in self.shops_eraser:
            shop.sendUpdate(self)

        print("****************************************")





class Pen(StationaryGoods): #ConcretePublisher3
    def __init__(self,type,price):
        self.name = "pen"
        self.type = type
        self.price = price

    shops_pen = []

    def get_type(self):
        return self.type

    def addShop(self, shop):
        self.shops_pen.append(shop)

    def removeShop(self, shop):
        self.shops_pen.remove(shop)

    def notifyShop(self):
        for shop in self.shops_pen:
            shop.sendUpdate(self)

        print("****************************************")

class ShopTracker(ABC): #Observer Class

    @abstractmethod
    def sendUpdate(self,product):
        pass



class Shop(ShopTracker): #ConcreteObserver
    def __init__(self,name):
        self.name = name


    def sendUpdate(self,product):
        print("To",self.name,"... ","The price for",product.type, product.name, "is changed from",product.old_price,"to",product.get_price(),"each at Binghamton Wholesale!")



def main():

    gel_pen = Pen("gel",2)
    gel_pen.addShop(Shop("Shop1"))

    gel_pen.set_price(4)
    gel_pen.set_price(3)

    ruled_notebook = Notebook("ruled", 4)
    ruled_notebook.addShop(Shop('Shop2'))

    ruled_notebook.set_price(8)
    ruled_notebook.set_price(5)

    rubber_eraser= Eraser("rubber", 1.5)

    rubber_eraser.addShop(Shop("Shop3"))
    
    rubber_eraser.addShop(Shop('Shop4'))

    rubber_eraser.set_price(3.5)
    rubber_eraser.set_price(2.5)


if __name__ == '__main__':
    main()

