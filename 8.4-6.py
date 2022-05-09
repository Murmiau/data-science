class Sklad:
    __storage = []
    __summary = {}

    def push(self, equip):
        if not isinstance(equip, OfficeEquip):
            raise Exception("Склад для оргтехники")
        self.__storage.append(equip)
        if self.__summary.get(equip.type) is not None:
            self.__summary[equip.type] += 1
        else:
            self.__summary.setdefault(equip.type, 1)

    def report_items(self):
        for it in self.__storage:
            print(it)

    def report_total(self):
        for a, b in self.__summary.items():
            print(f'{a}: {b} шт.')


class OfficeEquip:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquip):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__("Принтер", model, cost, sn)


class Scanner(OfficeEquip):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__("Сканер", model, cost, sn)


class Copier(OfficeEquip):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__("Копир", model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('HP 1', 6850, True, "rdhf780hrs")
    printer02 = Printer("HP 2", 5980, False, "sgdn8sh9098")
    scanner01 = Scanner("Canon 1", 3750, "2400x2400", "ghvgbj689jhh")
    scanner02 = Scanner("Canon 2", 3980, "3600x3600", "hsrshf798fh")
    copier01 = Copier("HP 3", 2140, True, "3600x800", 12, "srhdtj5dht")
    copier02 = Copier("Canon 3", 4100, False, "2800x800", 18, "rhtej654td")

    sklad = Sklad()
    sklad.push(printer01)
    sklad.push(printer02)
    sklad.push(scanner01)
    sklad.push(scanner02)
    sklad.push(copier01)
    sklad.push(copier02)

    sklad.report_items()
    sklad.report_total()
