from Classes.er import *
from Classes.afne import *

class TestErToAfne:
  def test_one(self):
    er = Er.getEr(".(*(a),+(.(a,a),.(b,b)))")

    afne = er.equivalentAfne(er.queue.pop(0))

    templateAfne = Afne(
      ["a", "b"], 
      ["q000", "qf00", "q00", "qf0", "q0001", "qf001", "q0101", "qf101", "q0011", "qf011", "q0111", "qf111", "q01", "qf1"], 
      {
        "q000": [("a", ["qf00"])], 
        "qf00": [("EPSILON", ["qf0", "q000"])], 
        "q00": [("EPSILON", ["q000", "qf0"])], 
        "qf0": [("EPSILON", ["q01"])], 
        "q0001": [("a", ["qf001"])], 
        "qf001": [("EPSILON", ["q0101"])], 
        "q0101": [("a", ["qf101"])], 
        "qf101": [("EPSILON", ["qf1"])], 
        "q0011": [("b", ["qf011"])], 
        "qf011": [("EPSILON", ["q0111"])], 
        "q0111": [("b", ["qf111"])], 
        "qf111": [("EPSILON", ["qf1"])], 
        "q01": [("EPSILON", ["q0001", "q0011"])]
      }, 
      "q00",
      ["qf1"]
    )

    assert afne.compare(templateAfne)