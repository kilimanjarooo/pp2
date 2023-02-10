heads = 35
legs = 94

def solve(numheads, numlegs):

  """
    x + y = 35
    2x + 4y = 94
     
    x + 2y = 47
    x + y = 35
    
    x = 47 - 2y
    x = 35 - y
    
    47 - 2y = 35 - y
    
    \\(y = 47 - 35)
    y = 12

    \\(x = 35 - y)
    x = 23

    """

  rabbit = (numlegs / 2) - numheads
  chicken = numheads - rabbit

  print("chickens:", chicken)
  print("rabbits:", rabbit)

solve(heads, legs)