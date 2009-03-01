#!/usr/bin/env python
# coding: utf-8

'''
    >>> from baralho import Baralho
    >>> b = Baralho()
    >>> b[0]
    <A de copas>
    >>> b[:3]
    [<A de copas>, <2 de copas>, <3 de copas>]
    >>> for carta in b[-3:]: print carta
    ... 
    <J de paus>
    <Q de paus>
    <K de paus>
    >>> s = 'Python: simples e correta'
    >>> s[0]
    'P'
    >>> s[-1]
    'a'
    >>> s[:3]
    'Pyt'
    >>> for letra in s[:3]: print letra
    ... 
    P
    y
    t
    >>> b = Baralho()
    >>> b[-1]
    <K de paus>
    >>> b[-3:]
    [<J de paus>, <Q de paus>, <K de paus>]
    >>> s[-3:]
    'eta'
    >>> l = range(10)
    >>> l[0]
    0
    >>> l[:3]
    [0, 1, 2]
    >>> l[-1]
    9
    >>> l[-3]
    7
    >>> l[-3:]
    [7, 8, 9]
    >>> b[:3]     
    [<A de copas>, <2 de copas>, <3 de copas>]
'''


from random import shuffle

class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        
    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)

class Baralho(object):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    
    def __init__(self):
        self.cartas = [Carta(v, n) 
                        for n in self.naipes 
                        for v in self.valores]
        
    def __len__(self):
        return len(self.cartas)
        
    def __getitem__(self, pos):
        return self.cartas[pos]
        
    def __setitem__(self, pos, item):
        self.cartas[pos] = item
        
if __name__ == '__main__':
    from doctest import testmod
    testmod()
