from Classes.afne import *
from Classes.afn import *

class TestAfneToAfn:
  def test_one(self):
    afne = Afne(
      ["a", "b"], 
      ["q0", "q1", "q2"], 
      {
        "q0": [("a", ["q0", "q2"]), ("EPSILON", ["q1"])], 
        "q1": [("b", ["q1"]), ("EPSILON", ["q2"])],
        "q2": [("a", ["q2"])]
      }, 
      "q0",
      ["q2"]
    )

    afn = afne.equivalentAfn()

    templateAfn = Afn(
      ["a", "b"], 
      ["q0", "q1", "q2"], 
      {
        "q0": [("a", ["q0", "q1", "q2"]), ("b", ["q1", "q2"])], 
        "q1": [("a", ["q2"]), ("b", ["q1", "q2"])],
        "q2": [("a", ["q2"])]
      }, 
      "q0",
      ["q0", "q1", "q2"]
    )

    assert afn.compare(templateAfn)
