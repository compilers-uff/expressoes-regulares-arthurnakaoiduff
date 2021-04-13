from Classes.er import *
from mainFunctions import *

class Test:
  def test_concatenation_true_one(self):
    er = ".(.(.(a, b), c), d)"
    word = "abcd"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_concatenation_false_one(self):
    er = ".(.(.(a, b), c), d)"
    word = "abcde"

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = False

    assert boolean == templateBoolean

  def test_union_true_one(self):
    er = "+(+(+(a, b), c), d)"
    word = "a"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_union_false_one(self):
    er = "+(+(+(a, b), c), d)"
    word = "ab"

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = False

    assert boolean == templateBoolean

  def test_successive_concatenation_true_one(self):
    er = "*(a)"
    word = "aaaaaaaa"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_successive_concatenation_false_one(self):
    er = "*(a)"
    word = "ab"

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = False

    assert boolean == templateBoolean

  def test_simple_er_true_one(self):
    er = "a"
    word = "a"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_simple_er_false_one(self):
    er = "a"
    word = "b"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = False

    assert boolean == templateBoolean

  def test_complex_true_one(self):
    er = "+(*(.(a, b)), .(d, +(a, c)))"
    word = "da"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_complex_true_two(self):
    er = ".(*(.(a, b)), c)"
    word = "abababc"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_complex_true_three(self):
    er = ".(*(.(a, b)), +(c, d))"
    word = "abababd"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_complex_true_four(self):
    er = ".(*(.(a, b)), +(*(c), d))"
    word = "abababcccc"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_complex_true_five(self):
    er = ".(*(.(a, b)), +(*(.(c, d)), .(e, f)))"
    word = "abababcdcd"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean

  def test_complex_true_six(self):
    er = ".(*(.(a, b)), .(d, +(a, c)))"
    word = "abababda"

    er = er.replace(" ", "") # Retirando os espaços vazios
    er = er.replace("\n", "") # Retirando as quebras de linha
    
    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = True

    assert boolean == templateBoolean