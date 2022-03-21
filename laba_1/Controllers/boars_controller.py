import random

from Field.cell import Cell
from Animals.animals import Boar
from .creatures_controller import CreaturesController


CHANCE_TO_LOOK_AROUND_FOR_BOAR = 15
CHANCE_TO_GO_AWAY = 25


class BoarsController(CreaturesController):
    
    def make_decision(self, cell: Cell, boar: Boar):
        if self.is_alive(boar):
            self.weakening(boar)
            if random.randint(0, 100) < CHANCE_TO_LOOK_AROUND_FOR_BOAR:
                if self.cell_controller.is_creature_in_cell(cell, 'dragon'):
                    self.move(cell, boar)
                    self.starvation(boar)
                elif self.cell_controller.is_creature_in_cell(cell, 'bear'):
                    self.move(cell, boar)
                    self.starvation(boar)
            else:
                if boar._hunger > 5:
                    if self.cell_controller.is_creature_in_cell(cell, 'rabbit'):
                        rabbit = self.cell_controller.get_creature(cell, 'rabbit')
                        self.trying_to_eat_rabbit(cell, boar, rabbit)
                    elif self.cell_controller.is_creature_in_cell(cell, 'bush'):
                        bush = self.cell_controller.get_creature(cell, 'bush')
                        self.eating_bush(cell, boar, bush)
                elif boar._hunger <= 6:
                    self.reproduce(cell, boar)
                if random.randint(0, 100) < CHANCE_TO_GO_AWAY:
                    self.move(cell, boar)
                    self.starvation(boar)
        else:
            self.dyuing(cell, boar)

    def reproduce(self, cell: Cell, boar: Boar):
        if cell.has_empty_place():
            partner = self.cell_controller.get_partner(cell, boar)
            if partner:
                index = cell.get_index_of_empty_place()
                cell.creatures[index] = Boar()

    def weakening(self, boar: Boar):
        boar._health -= 5
        boar._hunger += 1
