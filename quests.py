from countries_wrapper import get_all
from random import choice, shuffle


class QT_SUPER:
    def __init__(self):
        self.opt = None
        self.ans = None
        self.val = get_all()
        self.lna = len(self.val)

    def check(self, out):
        return self.ans == self.opt[out]

    def ptOps(self, o):
        return "\n".join([f"[{c+1}] {o(i)}" for c, i in enumerate(self.opt)])


class QT1(QT_SUPER):
    QT = lambda a: f"Which among the following languages are used in {a}?"

    def __init__(self):
        super(QT1, self).__init__()
        self.opt = self.finder()
        self.ctr = None
        while not self.ctr:
            self.ans = choice(self.opt)
            for i in sorted(self.val, key=lambda a: a.popl.population, reverse=True):
                t = i.popl.languages
                if not t:
                    continue
                if self.ans in t.values() and all(
                    [j not in t.values() for j in self.opt if j != self.ans]
                ):
                    self.ctr = i
                    break

    def finder(self):
        ret = {}
        for i in self.val:
            if i.popl.languages:
                for j in i.popl.languages.values():
                    if j in ret:
                        ret[j] += 1
                    else:
                        ret[j] = 1
        out = list(filter(lambda a: a[1] > 2, ret.items()))
        shuffle(out)
        return [i[0] for i in out[:4]]

    def __repr__(self):
        return f"[+] {QT1.QT(self.ctr.name.cname)}\n{self.ptOps(lambda a: a)}"


class QT2(QT_SUPER):
    QT = f"Which among these countries is an island?"

    def __init__(self):
        super(QT2, self).__init__()
        t = 0
        out = self.val.copy()
        while out[t].locl.borders:
            t += 1
        self.ans = out.pop(t)
        self.opt = [self.ans]
        for _ in range(3):
            shuffle(out)
            t = 0
            while not out[t].locl.borders:
                t += 1
            self.opt += [out.pop(t)]
        shuffle(self.opt)

    def __repr__(self):
        return f"[+] {QT2.QT}\n{self.ptOps(lambda a: a.name.cname)}"


class QT3(QT_SUPER):
    QT = lambda a: f"Which among the following countries has the capital {a}?"

    def __init__(self):
        super(QT3, self).__init__()
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def get_options(self):
        out = list(
            filter(lambda a: a.locl.capital and len(a.locl.capital) == 1, self.val)
        )
        out = sorted(out, key=lambda a: a.popl.population)
        k = len(out) // 4
        ret = []
        for i in range(0, len(out) - 6, k):
            ret += [choice(out[i : i + k])]
        return ret

    def __repr__(self):
        return f"[+] {QT3.QT(self.ans.locl.capital[0])}\n{self.ptOps(lambda a: a.name.cname)}"


class QT4(QT_SUPER):
    QT = lambda a: f"Which among the following currencies are used in {a}?"

    def __init__(self):
        super(QT4, self).__init__()
        self.opt = self.finder()
        self.ans = choice(self.opt)
        for i in sorted(self.val, key=lambda a: a.popl.population, reverse=True):
            if not i.currencies:
                continue
            t = [i["name"] for i in i.currencies.values()]
            if self.ans in t and all([j not in t for j in self.opt if j != self.ans]):
                self.ctr = i
                break

    def finder(self):
        ret = {}
        for i in self.val:
            if i.currencies:
                for j in i.currencies.keys():
                    if j in ret:
                        ret[j][0] += 1
                    else:
                        ret[j] = [1, i.currencies[j]]
        out = list(filter(lambda a: a[1][0] > 2, ret.items()))
        shuffle(out)
        return [i[1][1]["name"] for i in out[:4]]

    def __repr__(self):
        return f"[+] {QT4.QT(self.ctr.name.cname)}\n{self.ptOps(lambda a: a)}"


class QT5(QT_SUPER):
    QT = "Which among these countries have the largest population?"

    def __init__(self):
        super(QT5, self).__init__()
        out = sorted(self.val, key=lambda a: a.popl.population)
        k = self.lna // 4
        self.opt = [choice(out[i : i + k]) for i in range(0, self.lna - 6, k)]
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def __repr__(self):
        return f"[+] {QT5.QT}\n{self.ptOps(lambda a: a.name.cname)}"


class QT6(QT_SUPER):
    QT = lambda a: f"Which of these countries are a part of {a}?"

    def __init__(self):
        super(QT6, self).__init__()
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = self.opt[-1]

    def get_options(self):
        knw, ret = [], []
        for i in range(4):
            val = choice(self.val)
            while len(val.locl.continents) > 1 and val.locl.continents[0] in knw:
                val = choice(self.val)
            knw += [val.locl.continents[0]]
            ret += [val]
        return ret

    def __repr__(self):
        return f"[+] {QT6.QT(self.ans.locl.continents[0])}\n{self.ptOps(lambda a: a.name.cname)}"


class QT7(QT_SUPER):
    QT = lambda a: f"Which among the following is {a}'s longitude?"

    def __init__(self):
        super(QT7, self).__init__()
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def get_options(self):
        out = sorted(self.val, key=lambda a: a.locl.latlng[-1])
        k = self.lna // 4
        return [choice(out[i : i + k]) for i in range(0, self.lna - 6, k)]

    def __repr__(self):
        return f"[+] {QT7.QT(self.ans.name.cname)}\n{self.ptOps(lambda a: a.locl.latlng[-1])}"


class QT8(QT_SUPER):
    QT = lambda a: f"Which among the following is {a}'s latitude?"

    def __init__(self):
        super(QT8, self).__init__()
        self.opt = self.get_options()
        shuffle(self.opt)
        self.ans = choice(self.opt)

    def get_options(self):
        out = sorted(self.val, key=lambda a: a.locl.latlng[0])
        k = self.lna // 4
        return [choice(out[i : i + k]) for i in range(0, self.lna - 6, k)]

    def __repr__(self):
        return f"[+] {QT8.QT(self.ans.name.cname)}\n{self.ptOps(lambda a: a.locl.latlng[0])}"


QTS = [QT1, QT2, QT3, QT4, QT5, QT6, QT7, QT8]
