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


