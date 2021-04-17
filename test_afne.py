from Classes.afne import *
from util import *

class TestAfne:
  def test_sigma_extended_one(self):
    afne = Afne(
      ["a", "b", "c"], 
      ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "qf"], 
      {
        "q0": [("a", ["q0"]), ("b", ["q0"]), ("c", ["q0"]), ("EPSILON", ["q1", "q2", "q4"])], 
        "q1": [("a", ["qf"])],
        "q2": [("b", ["q3"])],
        "q3": [("b", ["qf"])], 
        "q4": [("c", ["q5"])],
        "q5": [("c", ["q6"])],
        "q6": [("c", ["qf"])]
      }, 
      "q0",
      ["qf"]
    )

    sigmaExtended = afne.sigmaExtended(["q0"], ["a", "b", "b"])

    templateSigmaExtended = ["q0", "q1", "q2", "q3", "q4", "qf"]

    assert equivalentLists(templateSigmaExtended, sigmaExtended)