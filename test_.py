from Classes.er import *
from mainFunctions import *

class Test:
  def test_enunciated_one(self):
    assert match('a', 'a')

  def test_enunciated_two(self):
    assert match('+(a, b)', 'a')

  def test_enunciated_three(self):
    assert match('.(a, b)', 'ab')

  def test_enunciated_four(self):
    assert match('*(+(a, b)', 'a') 

  def test_enunciated_five(self):
    assert match('*(+(a, b)', 'aaa')

  def test_enunciated_six(self):
    assert match('*(+(a, b)', 'ab')

  def test_enunciated_seven(self):
    assert match('*(+(a, b)', 'aba')

  def test_enunciated_eight(self):
    assert match('*(+(a, b)', 'abababa')

  def test_concatenation_true_one(self):
    assert match(".(.(.(a, b), c), d)", "abcd")

  def test_concatenation_false_one(self):
    assert not match(".(.(.(a, b), c), d)", "abcde")

  def test_union_true_one(self):
    assert match("+(+(+(a, b), c), d)", "a")

  def test_union_false_one(self):
    assert not match("+(+(+(a, b), c), d)", "ab")

  def test_successive_concatenation_true_one(self):
    assert match("*(a)", "aaaaaaaa")

  def test_successive_concatenation_false_one(self):
    assert not match("*(a)", "ab")

  def test_simple_er_true_one(self):
    assert match("a", "a")

  def test_simple_er_false_one(self):
    assert not match("a", "b")

  def test_complex_true_one(self):
    assert match("+(*(.(a, b)), .(d, +(a, c)))", "da")

  def test_complex_true_two(self):
    assert match(".(*(.(a, b)), c)", "abababc")

  def test_complex_true_three(self):
    assert match(".(*(.(a, b)), +(c, d))", "abababd")

  def test_complex_true_four(self):
    assert match(".(*(.(a, b)), +(*(c), d))", "abababcccc")

  def test_complex_true_five(self):
    assert match(".(*(.(a, b)), +(*(.(c, d)), .(e, f)))", "abababcdcd")

  def test_complex_true_six(self):
    assert match(".(*(.(a, b)), .(d, +(a, c)))", "abababda")