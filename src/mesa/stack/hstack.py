import pygame as pg
from mesa.container.container import _MesaContainer


class MesaStackHorizontal(_MesaContainer):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def _compute_elements_positions(self):
        accum = pg.Vector2(0, 0)
        for element in self.elements:
            element.position.x = accum.x + element.marginx
            element.position.y = accum.y + element.marginy
            element.absolute_position.x = (
                self.absolute_position.x + accum.x + element.marginx
            )
            element.absolute_position.y = (
                self.absolute_position.y + accum.y + element.marginy
            )
            element.rect = pg.Rect(
                element.absolute_position, element.surface.get_size()
            )
            accum.x += element.width + element.marginx * 2
        return super()._compute_elements_positions()
