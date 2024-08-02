


class GameBoard(object):
    
    def __init__(self, battleships, board_width, board_height):
        self.battleships = battleships
        self.shots = []
        self.board_width = board_width
        self.board_height = board_height





class Battleship(object):

    @staticmethod
    def build(head, lenght, direction):
        body = []
        for i in range(lenght):
            if direction == "N":
                el = (head[0], head[1] - i)
            elif direction == "S":
                el = (head[0], head[1] + i)
            elif direction == "W":
                el = (head[0] - i, head[1])
            elif direction == "E":
                el = (head[0] + i, head[1])

            body.append(el)
        return Battleship(body)

    def __init__(self, body):
        self.body = body


def render(board_width, board_height, shots):
    header = "+" + "-" * board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")
        # print("|" + " " * board_width + "|")

    print(header)

def render_battleships(board_width, board_height, battleships):
    header = "+" + "-" * board_width + "+"
    print(header)

    # Construct empty board
    board = []
    for _ in range(board_width):
        board.append([None for _ in range(board_height)])

    # Add the battleships to the board
    for b in battleships:
        for x, y in b.body:
            board[x][y] = "O"

    
    for y in range(board_height):
        row = []
        for x in range(board_width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")


    print(header)


if __name__ == "__main__":
    battleship = [
        Battleship.build((1,1), 2, "N"),
        Battleship.build((5,8), 5, "N"),
        Battleship.build((2,3), 4, "E")
    ]

    for b in battleship:
        print(b.body)

    render_battleships(10, 10, battleship)

    exit(0)

    shots = []

    while True:



        inp = input("Where do you want to shoot?\n")
        xstr, ystr = inp.split(",")
        # TODO: deal with invalid input
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(10, 10, shots)

