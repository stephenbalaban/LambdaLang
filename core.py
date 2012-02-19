"""
Panda Calculus

A silly language build from pure abstraction, 
    over python...

Based off the exercises and topics discussed in

-------------------------------------------------------------------------------

    An Introduction to Functional Programming through Lambda Calculus 
    by Greg Michaelson

-------------------------------------------------------------------------------

Check it out, highly recommended.
"""

"""
Chapter 4.
    Combinators
"""
Y = lambda f: (lambda s: f(s(s)))(lambda s: f(s(s)))

"""
Chapter 1, 2.
    Core higher-order functions
"""
identity = lambda x: x
apply = lambda f: lambda arg: f(arg)
self_apply = lambda s: s(s)


"""
Chapter 2.
    Utility functions
"""
select_first = lambda first: lambda second: first
select_second = lambda first: lambda second: second

"""
Chapter 3.
    Conditional, booleans and logic
"""
true = select_first
false = select_second
and_ = lambda x: lambda y: x(y)(false)
or_ = lambda x: lambda y: x(true)(y)
not_ = lambda x: x(false)(true)
cond = lambda e1: lambda e2: lambda c: c(e1)(e2)
implies = not(lambda x: lambda y: cond(false)(true)(x))

"""
Chapter 3.5 
    Natural Numbers
"""
zero = identity
"""
in combination with our definition of succ(zero) seen below, 
iszero = true <=> n is the identity function (zero), as you can see
if n is the identity function, it imply returns true, otherwise, it fails
"""
iszero = lambda n: n(true)
"""
This one is a bit tricky to understand, what we're doing here is 
wrapping the number that is passed in in another lambda, 
as you can see from iszero above, as long as this number != zero,
when passed into iszero, we get:
        
        iszero(one)
     => iszero(succ(zero))
     => (Ln.(n true) (Ln.Ls.((s false) n) Lx.x))
     => (Ln.(n true) (Ls.((s false) Lx.x)))
     => (Ln.(n true) (Ls.((s false) Lx.x)))
     => (Ln.(n true) (Lx.x false))
     => (Ln.(n true) false)
     => (false true)
     => false

     => iszero(zero)
     => (Ln.(n true) Lx.x)
     => (Lx.x true)
     => true

"""
succ = lambda n: lambda s: (s(false))(n)
pred = lambda n: n(false)
one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)
six = succ(five)
seven = succ(six)
eight = succ(seven)
nine = succ(eight)
ten = succ(nine)
eleven = succ(ten)
twelve = succ(eleven)
thirteen = succ(twelve)
fourteen = succ(thirteen)
fifteen = succ(fourteen)
sixteen = succ(fifteen)
seventeen = succ(sixteen)
eighteen = succ(seventeen)
nineteen = succ(eighteen)
twenty = succ(nineteen)
twentyone = succ(twenty)
twentytwo = succ(twentyone)
twentythree = succ(twentytwo)
twentyfour = succ(twentythree)
twentyfive = succ(twentyfour)
twentysix = succ(twentyfive)
twentyseven = succ(twentysix)
twentyeight = succ(twentyseven)
twentynine = succ(twentyeight)
thirty = succ(twentynine)
thirtyone = succ(thirty)
thirtytwo = succ(thirtyone)
thirtythree = succ(thirtytwo)

# sabalaba
