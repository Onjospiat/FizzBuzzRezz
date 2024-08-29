for i in range(1, 101):
  a = False
  if i%3==0:
    print("Fizz",end="")
    a=True
  if i%5==0:
    print("Buzz", end="")
    a=True
  #if i%7==0:
   # print("Rezz", end="")
   # a=True
  if a:
    print("")
  else:
    print(i)