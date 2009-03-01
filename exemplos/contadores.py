#!/usr/bin/env python
# coding: utf-8

__all__ = 'Contador ContadorTolerante ContadorTotalizador'.split()

'''
O contador serve para contar ocorrências de itens em uma sequência::

    >>> pal = 'abacaxi'
    >>> cont = Contador()  # não se usa 'new'
    >>> for c in pal: cont.incluir(c)
    >>> for letra in sorted(set(pal)):
    ...   print letra, cont.contar(letra)
    ... 
    a 3
    b 1
    c 1
    i 1
    x 1

Ao solicitar a contagem de um item inexistente, temos uma exceção::

    >>> cont.contar('z')
    Traceback (most recent call last):
    ...
    KeyError: 'z'

Com o contador tolerante, isso não acontece::

    >>> ctol = ContadorTolerante()
    >>> for c in pal: cont.incluir(c)
    >>> ctol.contar('z')
    0
    
Este outro contador acumula a quantidade total de itens:

    >>> ctot = ContadorTotalizador()
    >>> for c in pal: ctot.incluir(c)
    >>> ctot.total
    7
    
Finalmente, um contador totalizador tolerante::

    >>> ctt = ContadorTotalizadorTolerante()
    >>> for c in pal: ctt.incluir(c)
    >>> ctt.contar('z')
    0
    >>> ctt.total
    7

Veja a ordem de resolução de métodos do ContadorTotalizadorTolerante:

    >>> ContadorTotalizadorTolerante.__mro__
    (<class '__main__.ContadorTotalizadorTolerante'>, <class '__main__.ContadorTotalizador'>, <class '__main__.ContadorTolerante'>, <class '__main__.Contador'>, <type 'object'>)
'''


class Contador(object):
    
    def __init__(self):
        self.dic = {}

    def incluir(self, item):
        qtd = self.dic.get(item, 0) + 1
        self.dic[item] = qtd

    def contar(self, item):
        return self.dic[item]

class ContadorTolerante(Contador):

    def contar(self, item):
        return self.dic.get(item, 0)

class ContadorTotalizador0(Contador):
    
    total = 0

    def __init__(self):
        Contador.__init__(self)

    def incluir(self, itens):
        super(ContadorTotalizador, self).incluir(item)
        self.total += 1

class ContadorTotalizador(Contador):

    total = 0

    def __init__(self):
        super(ContadorTotalizador, self).__init__()

    def incluir(self, item):
        super(ContadorTotalizador, self).incluir(item)
        self.total += 1

class ContadorTotalizadorTolerante(ContadorTotalizador,ContadorTolerante):
    '''esse contador totaliza e não levanta exceções'''

if __name__ == '__main__':
    from doctest import testmod
    testmod()
