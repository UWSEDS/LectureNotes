from prime import check_prime

# Should be prime
def test_smoke1():
  assert(check_prime(3))

# Should not be prime
def test_smoke2():
  assert(not check_prime(2))
