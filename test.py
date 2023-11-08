#!/usr/bin/python3

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
print(get_samples(3))

# Get a country by name (official/common/full).
print(get_by_name('india'))


# Get country(s) by code (any format/count)
print(get_by_code(["IN", "US"]))
print(get_by_code("BR"))

# Get country by currency, demonym, language, 
# capital_city, continent, sub-continent,
# and translations
print(get_by_curr("inr"))
print(get_by_denm("Japanese"))
print(get_by_lang("spa"))
print(get_by_cptl("tokyo"))
print(get_by_regn("asia"))
print(get_by_sreg("north america"))
print(get_by_trns("República de Estonia"))