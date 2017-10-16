class Move:
    fromCol = 0
    fromRow = 0
    toCol = 0
    toCol = 0
    type = "ERROR"
    message = "Undefined Move?"

    def __init__(self, fromCol, fromRow, toCol, toRow, type, message):
        self.fromCol = fromCol
        self.fromRow = fromRow
        self.toCol = toCol
        self.toRow = toRow
        self.type = type
        self.message = message

    def marshal(self):
        result = dict()
        result["moveType"] = self.type
        if (self.type == "ERROR"):
            result["error"] = self.message
        else:
            result["fromX"] = self.fromCol
            result["fromY"] = self.fromRow
            result["toX"] = self.toCol
            result["toY"] = self.toRow

        return result


def spawn_into(intoCol, intoRow):
    return Move(0, 0, intoCol, intoRow, "SPAWN", "")

def fire_at(atCol, atRow):
    return Move(0, 0, atCol, atRow, "FIRE", "")

def move_from_to(fromCol, fromRow, intoCol, intoRow):
    return Move(fromCol, fromRow, intoCol, intoRow, "MOVE", "")

def do_pass():
    return Move(0, 0, 0, 0, "PASS", "")

def do_error(message):
    return Move(0, 0, 0, 0, "ERROR", message)