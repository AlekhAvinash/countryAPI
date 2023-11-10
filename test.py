#!/usr/bin/python3

# from pprint import pprint
from countries_wrapper import (
    get_all,
    get_by_name,
    get_by_code,
    get_by_curr,
    get_by_denm,
    get_by_lang,
    get_by_cptl,
    get_by_regn,
    get_by_sreg,
    get_by_trns,
    get_samples,
)

# Get three random countries.
# n = 3
# print(f"Getting {n} random countries.")
# print(*get_samples(n), sep="\n\n\n")

# Get a country by name (official/common/full).
# print(f"\n\n\nGetting country by name.")
# out = get_by_name("poland", fullText=True)[0]
# print(out, sep="\n\n\n")


# Get country(s) by code (any format/count)
# print("\n\n\nGetting country by code.")
# print(*get_by_code(["IN", "US"]), sep="\n\n\n")
# print("\n\n\n")
# print(get_by_code("BR"))

# Get country by currency, demonym, language,
# capital_city, continent, sub-continent,
# and translations
# print("\n\n\nGetting countries by Currency.")
# print(*get_by_curr("inr"), sep="\n\n\n")


# print("\n\n\nGetting countries by Demonym.")
# print(*get_by_denm("Japanese"), sep="\n\n\n")


# print("\n\n\nGetting countries by Speaking Language.")
# print(*get_by_lang("spa"), sep="\n\n\n")


# print("\n\n\nGetting countries by Capital City.")
# print(get_by_cptl("tokyo"))


# print("\n\n\nGetting countries by Continent.")
# print(*get_by_regn("asia"), sep="\n\n\n")


# print("\n\n\nGetting countries by Sub-Continent.")
# print(*get_by_sreg("north america"), sep="\n\n\n")


# print("\n\n\nGetting countries by Translated Name.")
# print(get_by_trns("República de Estonia"))
