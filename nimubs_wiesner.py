#Sebastian Wiesner

import random

def num_randomizer():
  #Generate random integers for A and B
  A = random.randint(1, 9)
  B = random.randint(1, 9)
  
  #Multiply A and B together and store the result in C
  C = A * B
  
  #Keep generating new random integers for A and B and multiplying them together until C is equal to 4
  while C != 4:
    print(f"A: {A}, C: {C}")
    A = random.randint(1, 9)
    B = random.randint(1, 9)
    C = A * B
    
  #If C is equal to 4, print "Success!" and the values of A and B
  print("Success!")
  print(f"A: {A}, B: {B}")

#Call the function
num_randomizer()
