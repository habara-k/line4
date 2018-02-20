from collections import defaultdict

SPACE = 0
BLACK = 1
WHITE = -1

REVERSE = {BLACK: WHITE, WHITE: BLACK}

SIZE = 4
LAST = SIZE - 1
AXIS = range(SIZE)

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_xyz(self):
        return self.x, self.y, self.z




def lines():
    """ ラインのジェネレータ """
    # 長さ1 のライン
    for a in AXIS:
        for b in AXIS:
            yield [(a, b, c) for c in AXIS]
            yield [(b, c, a) for c in AXIS]
            yield [(c, a, b) for c in AXIS]
    # 長さ√2 のライン (6面にあるクロスライン)
    for a in AXIS:
        yield [(a, b, b) for b in AXIS]
        yield [(a, b, LAST - b) for b in AXIS]
        yield [(b, a, b) for b in AXIS]
        yield [(b, a, LAST - b) for b in AXIS]
        yield [(b, b, a) for b in AXIS]
        yield [(b, LAST - b, a) for b in AXIS]
    # 長さ√3 のライン (4頂点から内部を貫通して対角に達するライン)
    yield [(a, a, a) for a in AXIS]
    yield [(a, LAST - a, LAST - a) for a in AXIS]
    yield [(a, a, LAST - a) for a in AXIS]
    yield [(a, LAST - a, a) for a in AXIS]


lines_at = defaultdict(list)      # lines_at[x, y, z] = box[z][y][x]を通るラインのリスト
for line in lines():
    for point in line:
        lines_at[point].append(line)
