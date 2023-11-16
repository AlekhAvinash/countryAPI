from countries_wrapper import get_all
from random import choice, shuffle

"QT1 - What is the language of this country"
"QT2 - What is the currency of this country"
"QT3 - What is the capital city of this country"
"QT4 - Which is of these countries border this other country"


class QT5:
    QT = "Which among these countries have the largest population?"

    def __init__(self):
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def get_options(self):
        out = sorted(get_all(), key=lambda a: a.popl.population)
        a = len(out)
        k = a // 4
        return [choice(out[i : i + k]) for i in range(0, a - 6, k)]

    def check(self, out):
        return self.ans == self.opt[out]

    def __repr__(self):
        return f"[+] {QT5.QT}\n" + "\n".join(
            [f"[{c+1}] {i.name.cname}" for c, i in enumerate(self.opt)]
        )


class QT6:
    QT = lambda a: f"Which of these countries are a part of {a}?"

    def __init__(self):
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = self.opt[-1]

    def get_options(self):
        out = get_all()
        knw, ret = [], []
        for i in range(4):
            val = choice(out)
            while len(val.locl.continents) > 1 and val.locl.continents[0] in knw:
                val = choice(out)
            knw += [val.locl.continents[0]]
            ret += [val]
        return ret

    def check(self, out):
        return self.ans == self.opt[out]

    def __repr__(self):
        return f"[+] {QT6.QT(self.ans.locl.continents[0])}\n" + "\n".join(
            [f"[{c+1}] {i.name.cname}" for c, i in enumerate(self.opt)]
        )


class QT7:
    QT = lambda a: f"Which among the following is {a}'s longitude?"

    def __init__(self):
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def get_options(self):
        out = sorted(get_all(), key=lambda a: a.locl.latlng[-1])
        a = len(out)
        k = a // 4
        return [choice(out[i : i + k]) for i in range(0, a - 6, k)]

    def check(self, out):
        return self.ans == self.opt[out]

    def __repr__(self):
        return f"[+] {QT7.QT(self.ans.name.cname)}\n" + "\n".join(
            [f"[{c+1}] {i.locl.latlng[-1]}" for c, i in enumerate(self.opt)]
        )


class QT8:
    QT = lambda a: f"Which among the following is {a}'s latitude?"

    def __init__(self):
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def get_options(self):
        out = sorted(get_all(), key=lambda a: a.locl.latlng[0])
        a = len(out)
        k = a // 4
        return [choice(out[i : i + k]) for i in range(0, a - 6, k)]

    def check(self, out):
        return self.ans == self.opt[out]

    def __repr__(self):
        return f"[+] {QT8.QT(self.ans.name.cname)}\n" + "\n".join(
            [f"[{c+1}] {i.locl.latlng[0]}" for c, i in enumerate(self.opt)]
        )


QTS = [QT5, QT6, QT7, QT8]
