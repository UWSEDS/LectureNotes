'''
   Code to find prime numbers
'''

# Prime number finder with a logic bug
def primeChecker(num):
  """
  Checks to see if a number is prime.
  :param int num:
  :returns bool:
  """
  is_prime = True
  import pdb; pdb.set_trace()
  for i in range(1,num):
    if (num % i) == 0:
      is_prime = False
      break
  else:
    pass
  return is_prime

# Run the following code if the file is run at the command line
if __name__ == "__main__":
  num = int(input("Enter a number: "))
  if primeChecker(num):
    print ("Is prime!")
  else:
    print ("Not a prime.")
