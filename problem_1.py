def multiples(num):
  total = 0
  x = 3
  while x < num:
    if (x % 3 == 0) or (x % 5 == 0):
      total += x
    x+=1
  print(total)
  return total


multiples(1000)