import math as m


def aera_count():
    radius = float(input('Radius: '))
    r_pingfang = m.pow(radius, 2)
    newvariable = r_pingfang
    aera = m.pi * newvariable
    return aera

aera = aera_count()
print(aera)
