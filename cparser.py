class nmParse:
    def __init__(self, common, official, translations, altSpellings, **kwargs):
        self.codes = ccparse(**kwargs)
        self.name = common
        self.official = official
        self.trns = translations
        self.altSpellings = altSpellings

    def __repr__(self):
        return f"Common Name\t:{self.name}"


class lcParse:
    def __init__(
        self, region, continents, area, maps, capitalInfo, latlng, landlocked, **kwargs
    ):
        self.region = region
        self.continents = continents
        self.area = area
        self.maps = maps
        self.capitalInfo = capitalInfo
        self.latlng = latlng
        self.landlocked = landlocked
        if "capital" in kwargs:
            self.capital = kwargs.pop("capital")
        if "borders" in kwargs:
            self.borders = kwargs.pop("borders")
        if "subregion" in kwargs:
            self.subregion = kwargs.pop("subregion")

    def __repr__(self):
        return f"Lat - Lng\t:{self.latlng}\nContinents\t:{', '.join(self.continents)}"


class pcParse:
    def __init__(self, population, status, unMember, **kwargs):
        self.population = population
        self.status = status
        self.unMember = unMember
        self.gini = self.languages = self.demonyms = self.gini = None
        if "languages" in kwargs:
            self.languages = kwargs.pop("languages")
        if "demonyms" in kwargs:
            self.demonyms = kwargs.pop("demonyms")
        if "gini" in kwargs:
            self.gini = kwargs.pop("gini")
        if "independent" in kwargs:
            self.independent = kwargs.pop("independent")

    def __repr__(self):
        return f"Population\t:{self.population}\nStatus\t\t:{self.status}"


def ccparse(cca2, cca3, **kwargs):
    ret = [cca2, cca3]
    if "ccn3" in kwargs:
        ret += kwargs.pop("ccn3")
    if "cioc" in kwargs:
        ret += kwargs.pop("cioc")
    return ret


class PARSE:
    def __init__(self, name, car, timezones, coatOfArms, startOfWeek, idd, **kwargs):
        self.name = nmParse(**name, **kwargs)
        self.location = lcParse(**kwargs)
        self.population = pcParse(**kwargs)
        self.idd = idd
        self.timezones = timezones
        self.coatOfArms = coatOfArms
        self.startOfWeek = startOfWeek
        self.car = car
        if "currencies" in kwargs:
            self.currencies = kwargs.pop("currencies")
        if "fifa" in kwargs:
            self.fifa = kwargs.pop("fifa")
        if "postalCode" in kwargs:
            self.postalCode = kwargs.pop("postalCode")
        if "tld" in kwargs:
            self.tld = kwargs.pop("tld")

    def __repr__(self):
        return f"{self.name}\n{self.location}\n{self.population}"
