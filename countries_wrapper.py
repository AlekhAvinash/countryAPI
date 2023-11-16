#!/usr/bin/python3

# Core Methods
from requests.api import get as GET
from cparser import PARSE

# Handling Methods
from random import shuffle
import logging

ADDR = "restcountries.com/v3.1/"
log = logging.getLogger()


CACHE = []


def get(sub_domain, *f):
    url = f"https://{ADDR}/{sub_domain}"
    if f:
        f = ",".join(f)
        url = f"{url}/?fields={f}"
    log.info(url)
    out = GET(url).json()
    if isinstance(out, list):
        out = [PARSE(**i) for i in out]
    else:
        out = PARSE(**out)
    return out


def get_all(*f):
    global CACHE
    if not CACHE:
        CACHE = get("all", *f)
    return CACHE


def get_by_name(name, fullText=False, *f):
    return get(f"name/{name}?fullText={fullText}", *f)


def get_by_code(code, *f):
    if isinstance(code, list):
        code = ",".join(map(str, code))
        return get(f"alpha?codes={str(code)}", *f)
    return get(f"alpha/{code}")[0]


def get_by_curr(currency, *f):
    return get(f"currency/{currency}", *f)


def get_by_denm(demonym, *f):
    return get(f"demonym/{demonym}", *f)


def get_by_lang(language, *f):
    return get(f"lang/{language}", *f)


def get_by_cptl(capital, *f):
    return get(f"capital/{capital}", *f)[0]


def get_by_regn(region, *f):
    return get(f"region/{region}", *f)


def get_by_sreg(subregion, *f):
    return get(f"subregion/{subregion}", *f)


def get_by_trns(translation, *f):
    return get(f"translation/{translation}", *f)[0]


def get_samples(a=1):
    lst = get_all()
    shuffle(lst)
    return lst[:a]


if __name__ == "__main__":
    log.setLevel(logging.INFO)
else:
    log.setLevel(logging.ERROR)
