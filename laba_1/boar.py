from animal import Animal


class Boar(Animal):

    def __init__(self):
        super().__init__()
        self._type = 'boar'

    def show(self):
        print('Boar', self.sex[0], end=' ')

    def eat(self):
        pass

    def reproduce(self, field, region, cell_num):
        partner = super().check_reproduce(field, region, cell_num)
        if partner.life_cycle is False:
            cell = field.area[region][cell_num]
            index = cell.get_index_of_empty_place()
            cell.add_by_index(index, Boar())
            self.life_cycle = partner.life_cycle = True