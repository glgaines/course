# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.filter(name="isnumber")
def isnumber(parser):
    if parser:
        try:
            foo = float(parser)
        except ValueError:
            return False
        return True
    else: return False


@register.filter
def split(value, sep=None):
    sep = sep or ','
    return value.split(sep)

@register.filter
def morph(value, arg):
    #У меня есть ('1 пчела', '2 пчелы', '5 пчел')
    CASES = (2, 0, 1, 1, 1, 2)
    try:
        value = int(value)
    except:
        return ''
    titles = map(lambda x: x.strip(), arg.split(','))[:3]
    while len(titles) < 3:
        titles.append(titles[0])
    if (value % 100 > 4 and value % 100 < 20):
        return titles[2]
    return titles[CASES[min(value % 10, 5)]]
