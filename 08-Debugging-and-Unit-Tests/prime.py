'''
   Code to find prime numbers
'''

# Prime number finder with a logic bug
def primeChecker(num):
  # Inputs: num - number to evaluate as prime
  # Outputs: is_prime - True/False (is/not a prime)
  #          explanation - explains why num is not prime

  explanation = ""
  # prime numbers are greater than 1
  if num > 1:
    # check for factors
    for i in range(2,num):
      if (num % i) == 0:
        is_prime = False
        explanation = "%d times %d is %d" % (i, num//i, num)
        break
    else:
      is_prime = True
       
  # if input number is less than
  # or equal to 1, it is not prime
  else:
    is_prime = False
  return (is_prime, explanation)

# Run the following code if the file is run at the command line
if __name__ == "__main__":
  num = int(input("Enter a number: "))
  result = primeChecker(num)
  if result[0]:
    print ("%d is prime!" % num)
  else:
    print ("%d is not prime because %s" % (num, result[1]))
