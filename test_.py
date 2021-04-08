from Classes.er import *

def erToAFNe(er):
  erInstance = Er.getEr(er)
  return erInstance.equivalentAfne(erInstance.queue.pop(0))

def afneToAFN(Afne):
  return Afne.equivalentAfn()

def afnToAFD(Afn):
  return Afn.equivalentAfd()

def afdToAFDmin(Afd):
  return Afd.minimize()

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

    boolean = afdToAFDmin(afnToAFD(afneToAFN(erToAFNe(er)))).accepted(word)
    templateBoolean = False

    assert boolean == templateBoolean