from typing import List


def board_check(new_cords: tuple) -> bool:
    if all(0 < cords <= 8 for cords in new_cords):
        return True
    else:
        print('We cant be like these cords')
        return False


class Figure:
    color: str = "black"
    cords: tuple = (1, 1)


    def info(self) -> str:
        return f'cords_board is {self.cords} and color is {self.color}'

    def color_selection(self) -> None:
        if self.color == "black":
            self.color = "white"
        elif self.color == "white":
            self.color = "black"

    def selection_cords(self, new_cords: tuple) -> None:
        if board_check(new_cords):
            self.cords = new_cords

    def check_move(self, new_cords: tuple) -> bool:
        raise NotImplementedError


class King(Figure):
    def check_move(self, new_cords: tuple) -> bool:
        if not board_check(new_cords):
            return False
        horizontal, vertical = self.cords
        new_horizontal, new_vertical = new_cords
        return abs(new_horizontal - horizontal) <= 1 and abs(new_vertical - vertical) <= 1


class Queen(Figure):
    def check_move(self, new_cords: tuple) -> bool:
        if not board_check(new_cords):
            return False
        horizontal, vertical = self.cords
        new_horizontal, new_vertical = new_cords
        as_elephant = abs(new_vertical - vertical) == abs(new_horizontal - horizontal)
        as_rook = vertical == new_vertical or horizontal == new_horizontal
        return as_rook or as_elephant


class Knight(Figure):
    def check_move(self, new_cords: tuple) -> bool:
        if not board_check(new_cords):
            return False
        horizontal, vertical = self.cords
        new_horizontal, new_vertical = new_cords
        vertical_diff = abs(vertical - new_vertical)
        horizontal_diff = abs(horizontal - new_horizontal)
        return (vertical_diff == 1 and horizontal_diff == 2) or (vertical_diff == 2 and horizontal_diff == 1)


class Pawn(Figure):
    def check_move(self, new_cords: tuple) -> bool:
        if not board_check(new_cords):
            return False
        horizontal, vertical = self.cords
        new_horizontal, new_vertical = new_cords
        return (self.color == "black" and new_vertical == vertical + 1 and new_horizontal == horizontal) or (
                    self.color == "white" and new_vertical == vertical - 1 and new_horizontal == horizontal)


class Rook(Figure):
    def check_move(self, new_cords: tuple) -> bool:
        if not board_check(new_cords):
            return False
        horizontal, vertical = self.cords
        new_horizontal, new_vertical = new_cords
        return vertical == new_vertical or horizontal == new_horizontal


class Elephant(Figure):
    def check_move(self, new_cords: tuple) -> bool:
        if not board_check(new_cords):
            return False
        horizontal, vertical = self.cords
        new_horizontal, new_vertical = new_cords
        return abs(new_vertical - vertical) == abs(new_horizontal - horizontal)


def get_figures_which_we_can_move(figures_check: List[Figure], new_cords: tuple) -> List[Figure]:
    return [figure for figure in figures_check if figure.check_move(new_cords)]


king1 = King()
king2 = King()
king3 = King()
queen1 = Queen()
queen2 = Queen()
queen3 = Queen()
knight1 = Knight()
knight2 = Knight()
knight3 = Knight()
pawn1 = Pawn()
pawn2 = Pawn()
pawn3 = Pawn()
rook1 = Rook()
rook2 = Rook()
rook3 = Rook()
elephant1 = Elephant()
elephant2 = Elephant()
elephant3 = Elephant()


king3.selection_cords((3, 2))
queen2.selection_cords((4, 3))
knight3.selection_cords((4, 4))
knight2.color_selection()
pawn1.selection_cords((4, 4))
rook3.selection_cords((1, 4))
elephant2.selection_cords((2, 3))

figures = [king1, king2, king3, queen1, queen2, queen3, knight1, knight2, knight3, pawn1, pawn2, pawn3, rook1, rook2,
           rook3,  elephant1, elephant2, elephant3]

result = get_figures_which_we_can_move(figures, (3, 3))
