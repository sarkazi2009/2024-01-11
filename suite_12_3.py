import unittest
from unittest import TestSuite
from tests_12_2 import RunnerTest
from tests_12_2 import TournamentTest

frozen = TestSuite()
frozen.addTest(unittest.makeSuite(TournamentTest))
frozen.addTest(unittest.makeSuite(RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(frozen)
