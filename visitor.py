'''
Visitor - "Represent an operation to be performed on the elements of an object structure.
Visitor lets you define a new operation without changing the classes of the elements
on which it operates."

Basically, you group related methods/functionality in a concrete visitor class, e.g. PricingVisitor, EquipmentVisitor.
Classes that inherit from a common class, say Equipment, all have related functionality. But, say for some we want to
calculate pricing for some of them (PricingVisitor) and different, misc. equipment methods (EquipmentVisitor), we group
those methods in those visitors and for each concrete class in the Equipment subclass hierarchy, they define an accept
method that takes a visitor parameter, and depending on which visitor is passed in, performs a specific operation defined
in the concrete visitor.

This is nice because you get to keep related operations in one class, and you don't have to "pollute" each
class with distinct methods. 

Visitor is classified as a behavioral pattern:
"Behavioral patterns are concerned with algorithms and the assignment of responsibility
ties between objects. Behavioral patterns describe not just patterns of objects or classes
but also the patterns of communication between them. These patterns characterize
complex control flow that's difficult to follow at run-time. They shift your focus away
from flow of control to let you concentrate just on the way objects are interconnected."



'''


class Watt:
    pass


class Currency:
    pass


class Equipment:

    def __init__(self):
        self.discount_price = Currency()
        self.net_price = Currency()
        self.name = ""
        self.watt = Watt()
    def get_name(self):
        return self.name
    def get_power(self):
        return self.watt
    def get_net_price(self):
        return self.net_price
    def get_discount_price(self):
        return self.discount_price
    def accept(self,equipment_visitor):
        pass

class FloppyDisk(Equipment):
    def accept(self,visitor):
        # "equipment that contains other equipment implement accept by iterating over its children and calling"
        # "accept on each of them"
        # tho this isn't one of them, so it just calls it on an instance of itself
        visitor.visit_floppy_disk(self)


class EquipmentVisitor():
    def visit_floppy_disk(self,floppy_disk):
        pass
    def visit_card(self,card):
        pass
    def visit_chassis(self,chassis):
        pass
    def visit_bus(self,bus):
        pass
    # ...

class PricingVisitor(EquipmentVisitor):
    def __init__(self):
        self._total = None

    def visit_floppy_disk(self,floppy_disk):
        self._total += floppy_disk.net_price()

    def visit_chassis(self,chassis):
        self._total += chassis.discount_price()

    @property
    def total(self):
        return self._total


if __name__ == "__main__":
    visitor = PricingVisitor()
    component = Equipment()
    component.accept(visitor)
    print(visitor.total)


