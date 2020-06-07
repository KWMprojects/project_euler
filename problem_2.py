fibonacciEvenSum = []
def EvenFibs(a,b):
  while a + b < 4000000:
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
      fibonacciEvenSum.append(b)
    return EvenFibs(a,b)
  return sum(fibonacciEvenSum)

EvenFibs(0,1)
