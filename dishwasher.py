from abc import ABC, abstractmethod
import random

class Dish(ABC):#Dish class to see how much dish washer programs clean the dishes.
    def __init__(self,_dirt = 0):
        self._dirt = random.randint(1,10)
        
    def get_dirt(self):
        return self._dirt
    
    def clean_dirt(self, ammount): #the dish cleaning process
        if ammount >= self._dirt:
            self._dirt = 0
            return self._dirt
        else:
            self._dirt -= ammount
            return self._dirt
        
    def is_clean(self): # check if the dish is clean
        if self._dirt <= 1:
            print("All the dishes are clean")
        elif (1< self._dirt <5):
            print("The dish is kinda clean but not there yet")
        else:
            print("You should use a different program to clean this mess everything is still dirty")
            

class DishWasherPrograms(ABC):
    """
     to be able to implement the selected stratagy for dish washer programs
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def program(self,dish):
        self._strategy.program(dish)


class Strategy(ABC):#Stratagy selection for which kind of dish washing program going to be selected.

    #this abstractmethod will be used to do different opperations about how much a program will clean the dishes according to the program selected.
    @abstractmethod
    def program(self,dish):
        pass


class MainWash(Strategy):
    """
    Main wash program in dish washer
    """

    def program(self, dish):
        print("You used the main wash program which took average time which is 2 hours")
        dish.clean_dirt(6)
        dish.is_clean()

        
class IntensiveWash(Strategy):
    """
    Intensive Wash program in dish washer
    """

    def program(self, dish):
        print("You used Intensive Wash program which clean everything")
        dish.clean_dirt(9)
        dish.is_clean()
        
class HalfLoadWash(Strategy):
    """
    Half Load Program in dish washer
    """

    def program(self, dish):
        print("You used Half Load program to wash dishes")
        dish.clean_dirt(4)
        dish.is_clean()
        
def main():
    
    mainwash = MainWash()
    dish = Dish()
    #print(dish.get_dirt())
    dish_washer_program = DishWasherPrograms(mainwash)
    dish_washer_program.program(dish)

    
    intensivewash = IntensiveWash()
    dish = Dish()
    #print(dish.get_dirt())
    dish_washer_program = DishWasherPrograms(intensivewash)
    dish_washer_program.program(dish)

    halfloadwash = HalfLoadWash()
    dish = Dish()
    #print(dish.get_dirt())
    dish_washer_program = DishWasherPrograms(halfloadwash)
    dish_washer_program.program(dish)


if __name__ == "__main__":
    main()
