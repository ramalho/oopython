
================================
Orientação a Objetos em Python
================================

* Luciano Ramalho, Occam Consultoria

* luciano@occam.com.br

----------
Paralelos
----------

- herança múltipla (C++)

- sobrecarga de operadores (C++)

- não obriga a criar classes (C++)

- tipagem dinâmica (Smalltalk)

    - tipagem dinâmica, mas não tipagem fraca
    
::

   >>> a = 'casa'
   >>> b = 10
   >>> a + b
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: cannot concatenate 'str' and 'int' objects
   >>> a + str(b)
   'casa10'
   >>> '%s #%s' % (a, b)
   'casa #10'

    
---------------------------
Para quem sabe Java
---------------------------

- Python não tem interfaces

  - mas tem herança múltipla de classes

- Python não tem sobrecarga de métodos

  - mas tem passagem de argumentos flexível

- Python não tem *tipos primitivos*

  - **tudo** é objeto (desde Python 2.2, dez/2001)
  
::

    >>> a = 2
    >>> b = 3
    >>> a + b
    5
    >>> a.__add__(b)
    5

---------------------------------
Exemplo: definição de uma classe
---------------------------------

- uma classe com três métodos::

    class Contador(object):
    
        def __init__(this):
            this.dic = {}

        def incluir(this, item):
            qtd = this.dic.get(item, 0) + 1
            this.dic[item] = qtd

        def contar(this, item):
            return this.dic[item]

- ``__init__`` é invocado automaticamente na instanciação

- note que a referência ao objeto onde estamos operando é **explícita** (``this``).

---------------------------------------------------------
Peculiaridade: referência explícita à própria instância
---------------------------------------------------------

- todos os métodos de instância recebem como primeiro argumento uma referência explícita à própria instância

- por convenção, usa-se o nome ``self`` (em vez de ``this``)

- é obrigatório fazer referência explícita a ``self`` para acessar atributos da instância::

    class Contador(object):
    
        def __init__(self):
            self.dic = {}

        def incluir(self, item):
            qtd = self.dic.get(item, 0) + 1
            self.dic[item] = qtd

        def contar(self, item):
            return self.dic[item]

---------------------------
Exemplo: uso de uma classe
---------------------------

Nas chamadas de métodos, o ``self`` é implícito pois a sintaxe é ``instancia.metodo()``.

::

    >>> cont = Contador('abacaxi')  # não se usa 'new'
    >>> pal = 'abacaxi'
    >>> for letra in pal:
    ...   cont.incluir(letra)
    ... 
    >>> for letra in sorted(set(pal)):
    ...   print letra, cont.contar(letra)
    ... 
    a 3
    b 1
    c 1
    i 1
    x 1

-------------
Convenções
-------------

- classes devem herdar de ``object`` ou de outras classes que herdam de ``object``

  - classes antigas ('old style') não seguem essa regra

- construtor deve se chamar ``__new__`` (uso raro)

- inicializador deve se chamar ``__init__`` (uso comum)

  - o ``__init__`` faz o papel do que chamamos de construtor em outras linguagens
  
.. admonition:: ``__new__`` x ``__init__``
  
  Raramente implementamos construtores ``__new__`` em Python; usamos o construtor padrão e apenas usamos ``__init__`` para inicializar os atributos da instância.

            
--------------------------------------
Instâncias abertas e classes "vazias"
--------------------------------------

- instâncias podem receber atributos dinamicamente

- por isso às vezes é útil criar classes vazias

::

    >>> class Animal(object):
    ...   'um animal qualquer'
    ... 
    >>> baleia = Animal()
    >>> baleia.nome = 'Moby Dick'
    >>> baleia.peso = 1200
    >>> print '%s (%s Kg)' % (baleia.nome, baleia.peso)
    Moby Dick (1200 Kg)

----------------------------------------------
Atributos de classe / de instância
----------------------------------------------

- instâncias adquirem atributos da classe

::

    >>> class Animal(object):
    ...   nome = 'Rex' # atributo da classe
    ... 
    >>> cao = Animal()
    >>> cao.nome # atributo adquirido da classe
    'Rex'
    >>> cao.nome = 'Fido' # criado na instância
    >>> cao.nome
    'Fido'
    >>> Animal.nome # na classe, nada mudou
    'Rex'
    >>> dino = Animal()
    >>> dino.nome
    'Rex'
    >>>            

--------------------------------------
Métodos de classe / estáticos
--------------------------------------

- indicados por meio de *decorators*

::

    class Exemplo(object):
        @classmethod
        def da_classe(cls, arg1):
            return (cls, arg1)
        @staticmethod
        def estatico(arg1):
            return arg1

::
            
    >>> Exemplo.da_classe('fu')
    (<class '__main__.Exemplo'>, 'fu')
    >>> Exemplo.estatico('bar')
    'bar'
    
----------------
Herança
----------------

- no exemplo abaixo, ``ContadorTolerante`` extende ``Contador``

- o método ``contar`` está sendo sobrescrito

- os métodos ``__init__`` e ``ìncluir`` são herdados

::

    class ContadorTolerante(Contador):

        def contar(self, item):
            return self.dic.get(item, 0)

--------------------------------
Invocar método de super-classe
--------------------------------

- a forma mais simples::

    class ContadorTotalizador(Contador):
    
        def __init__(self):
            Contador.__init__(self)
            self.total = 0

        def incluir(self, item):
            Contador.incluir(self, item)
            self.total += 1

--------------------------------
Invocar método de super-classe 2
--------------------------------

- a forma mais correta::

    class ContadorTotalizador(Contador):

        def __init__(self):
            super(ContadorTotalizador, 
                self).__init__()
            self.total = 0

        def incluir(self, item):
            super(ContadorTotalizador, 
                self).incluir(item)
            self.total += 1

--------------------------------
Herança múltipla
--------------------------------

- classe que totaliza e não levanta exceções::

    class ContadorTT(ContadorTotalizador, ContadorTolerante):
        pass

- MRO = ordem de resolução de métodos:: 

    >>> ContadorTT.__mro__
    (<class '__main__.ContadorTT'>, 
     <class '__main__.ContadorTotalizador'>, 
     <class '__main__.ContadorTolerante'>, 
     <class '__main__.Contador'>, 
     <type 'object'>)

--------------------------------
Uso de herança múltipla
--------------------------------

::

    >>> from contadores import *
    >>> class ContadorTT(ContadorTotalizador, ContadorTolerante):
    ...   pass
    ...
    >>> ctt = ContadorTT()
    >>> for letra in 'abacaxi':
    ...   ctt.incluir(letra)
    ... 
    >>> ctt.total
    7
    >>> ctt.contar('a')
    3
    >>> ctt.contar('z')
    0


--------------------------
Encapsulamento
--------------------------

- Propriedades

     - encapsulamento para quem precisa de encapsulamento::

         >>> a = C()
         >>> a.x = 10      # violação!?
         >>> print a.x
         10
         >>> a.x = -10
         >>> print a.x     # como??????
         0

----------------------------------
Propriedade: implementação
----------------------------------

- apenas para leitura, via *decorator*::

     class C(object):
         def __init__(self, x):
             self.__x = x
         @property
         def x(self):
             return self.__x

- a notação ``__x`` protege este atributo contra acessos acidentais

----------------------------------
Propriedade: implementação 2
----------------------------------

- para leitura e escrita::

     class C(object):
         def __init__(self, x=0):
             self.__x = x
         def getx(self):
             return self.__x
         def setx(self, x):
             if x < 0: x = 0
             self.__x = x
         x = property(getx, setx)

----------------------------------
Propriedade: exemplo de uso
----------------------------------

::

     class ContadorTotalizador(Contador):  
         def __init__(self):
             super(ContadorTotalizador, self).__init__()
             self.__total = 0

         def incluir(self, item):
             super(ContadorTotalizador, 
                 self).incluir(item)
             self.__total += 1

         @property
         def total(self):
             return self.__total


--------------------------------
Passagem flexível de parâmetros
--------------------------------

::

     >>> def f(a, b=1, c=None):
     ...   return a, b, c
     ... 
     >>> f() 
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     TypeError: f() takes at least 1 argument (0 given)
     >>> f(9)
     (9, 1, None)
     >>> f(5,6,7)
     (5, 6, 7)
     >>> f(3, c=4)
     (3, 1, 4)

---------------------------------
Passagem flexível de parâmetros 2
---------------------------------

::

     >>> def f(*args, **kwargs):
     ...   return args, kwargs
     ... 
     >>> f()
     ((), {})
     >>> f(1)
     ((1,), {})
     >>> f(cor='azul')
     ((), {'cor': 'azul'})
     >>> f(10,20,30,sabor='uva',cor='vinho')
     ((10, 20, 30), {'cor': 'vinho', 'sabor': 'uva'})


---------------------------------
Passagem flexível de parâmetros 3
---------------------------------

::

     >>> def f(*args, **kwargs):
     ...   print '%r\n%r' % (args, kwargs)
     ... 
     >>> l
     [0, 1, 2]
     >>> d = {'peso':83,'altura':1.7}
     >>> f(l,d)
     ([0, 1, 2], {'altura': 1.7, 'peso': 83})
     {}
     >>> f(*l)
     (0, 1, 2)
     {}
     >>> f(**d)
     ()
     {'peso': 83, 'altura': 1.7}
     >>> f(*l,**d)
     (0, 1, 2)
     {'peso': 83, 'altura': 1.7}


- quem precisa de sobrecarga de métodos?

------------------------
Polimorfismo: definição
------------------------

  O conceito de "polimorfismo" significa que podemos tratar
  instâncias de diferentes classes da mesma maneira. 
  
  Assim, podemos enviar uma mensagem a um objeto
  sem saber de antemão qual é o seu tipo, e o objeto ainda
  assim fará "a coisa certa", pelo menos do seu ponto de vista.

  *Scott Ambler - The Object Primer, 2nd ed. - p. 173*
  
--------------
Polimorfismo
--------------

- polimorfismo com fatiamento e ``len``

::

    >>> l = [1, 2, 3]
    >>> l[:2]
    [1, 2]
    >>> 'casa'[:2]
    'ca'
    >>> len(l), len('casa')
    (3, 4)

--------------
Polimorfismo 2
--------------

- "tipagem pato" (*duck typing*) é polimorfismo dinâmico anabolizado


    >>> def dobro(x):
    ...    return x * 2
    ... 
    >>> dobro(10) 
    20
    >>> dobro([1, 2, 3])
    [1, 2, 3, 1, 2, 3]
    >>> dobro('casa')
    'casacasa'

--------------
Polimorfismo 3
--------------

::

    >>> s = 'Python: simples e correta'
    >>> s[0]
    'P'
    >>> s[-1]
    'a'
    >>> s[:3]
    'Pyt'
    >>> for letra in reversed(s): print letra
    ... 
    .
    a
    t
    e
    r
    r
    o
    c

--------------
Polimorfismo 4
--------------

::

    >>> l = range(10)
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l[0]
    0
    >>> l[-1]
    9
    >>> l[:3]
    [0, 1, 2]
    >>> for n in reversed(l): print n
    ... 
    9
    8
    7
    6
    5
    4
    3
    2
    1
    0

-------------------------------
Exemplo: baralho polimórfico
-------------------------------

- começamos com uma classe bem simples...

::

    class Carta(object):
        def __init__(self, valor, naipe):
            self.valor = valor
            self.naipe = naipe
        def __repr__(self):
            return '<%s de %s>' % (self.valor, self.naipe)


-------------------------------
Exemplo: baralho polimórfico 2
-------------------------------

- métodos especiais: ``__len__``, ``__getitem__``

- com esses métodos, ``Baralho`` implementa o protocolo das sequências

::

    class Baralho(object):
        naipes = 'copas ouros espadas paus'.split()
        valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    
        def __init__(self):
            self.cartas = [
                Carta(v, n) for n in self.naipes for v in self.valores
            ]
        
        def __len__(self):
            return len(self.cartas)
        
        def __getitem__(self, pos):
            return self.cartas[pos]
        
        def __setitem__(self, pos, item):
            self.cartas[pos] = item

-------------------------------
Exemplo: baralho polimórfico 3
-------------------------------

::

    >>> from baralho import Baralho
    >>> b = Baralho()
    >>> len(b)
    52
    >>> b[0], b[1], b[2]
    (<A de copas>, <2 de copas>, <3 de copas>)
    >>> from random import shuffle
    >>> shuffle(b)
    >>> b[-3:]
    [<7 de espadas>, <6 de copas>, <K de copas>]
    >>> for carta in reversed(b): print carta
    ... 
    <K de copas>
    <6 de copas>
    <7 de espadas>
    <3 de ouros> 
    <8 de espadas>
    <6 de espadas>
    <3 de espadas>
    <J de espadas>
    <6 de ouros>
    <Q de espadas>
    # etc...
    
-----------------------------
Perguntas, cursos, mentoria?
-----------------------------

* Luciano Ramalho, Occam Consultoria

* luciano@occam.com.br

