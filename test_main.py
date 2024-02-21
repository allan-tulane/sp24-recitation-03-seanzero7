from main import *



## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(5)) == 10*5
  assert quadratic_multiply(BinaryNumber(12), BinaryNumber(12)) == 12*12
  assert quadratic_multiply(BinaryNumber(4), BinaryNumber(3)) == 4*3
  assert quadratic_multiply(BinaryNumber(100), BinaryNumber(27)) == 100*27
  assert quadratic_multiply(BinaryNumber(13), BinaryNumber(4)) == 13*4


