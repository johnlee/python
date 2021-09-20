import sys
from math import log

DIGITAL_MAP={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGITAL_MAP[token]
        x = int(number)
        print(f"Success")
    except KeyError as e:
        print(f"Fail key error {e!r}")
        x = -1
    except TypeError as e:
        print(f"Fail type error {e!r}")
        x = -1
    except IndexError as e:
        print(f"Fail ignore")
        pass
    finally:
        print(f"At finally")
    return x

def string_log(s):
    v = convert(s)
    return log(v)