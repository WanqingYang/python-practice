def isPrimeNumber(num):
  if num == 1:
    return False
  i = 2;
  while i * i <= num:
    if (num % i == 0):
      return False
    i += 1
  return True

print("If 1 is prime: ", isPrimeNumber(1))
print("If 2 is prime: ", isPrimeNumber(2))
print("If 3 is prime: ", isPrimeNumber(3))
print("If 4 is prime: ", isPrimeNumber(4))
print("If 5 is prime: ", isPrimeNumber(5))
print("If 6 is prime: ", isPrimeNumber(6))
print("If 7 is prime: ", isPrimeNumber(7))
print("If 8 is prime: ", isPrimeNumber(8))
print("If 13 is prime: ", isPrimeNumber(13))
