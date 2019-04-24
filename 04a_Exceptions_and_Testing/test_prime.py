from prime import check_prime

# Should be prime
def test_oneshot1():
  assert(check_prime(3))

# Should not be prime
def test_oneshot2():
  assert(not check_prime(2))
