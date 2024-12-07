

import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name




class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers
Run1 = Runner("Усэйн", 10)
Run2 = Runner("Андрей", 9)
Run3 = Runner("Ник", 3)


tournament1 = Tournament(90, Run1, Run3)
all_results1 = tournament1.start()
print("{", end=" ")
for place, participant in all_results1.items():
    print(f"{place}: {participant.name}", end=", ")
print("}")

tournament2 = Tournament(90, Run2, Run3)
all_results2 = tournament2.start()
print("{", end=" ")
for place, participant in all_results2.items():
    print(f"{place}: {participant.name}", end=", ")
print("}")

tournament3 = Tournament(90, Run2, Run1, Run3)
all_results3 = tournament3.start()
print("{", end=" ")
for place, participant in all_results3.items():
    print(f"{place}: {participant.name}", end=", ")
print("}")


class TournamentTest(TestCase):
    is_frozen = True
    @unittest.skip('Тесты в этом кейсе заморожены')

    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', speed=10)
        self.andrey = Runner('Андрей', speed=9)
        self.nick = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print("{", end="")
            for place, participant in result.items():
                print(f"{place}: {participant.name}", end=", ")
            print("}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        all_results = tournament.start()
        self.__class__.all_results['usain_nick'] = all_results
        self.assertTrue(all_results[len(all_results)] == self.nick)

    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        all_results = tournament.start()
        self.__class__.all_results['usain_nick'] = all_results
        self.assertTrue(all_results[len(all_results)] == self.nick)

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tournament.start()
        self.__class__.all_results['usain_nick'] = all_results
        self.assertTrue(all_results[len(all_results)] == self.nick)

    def test_speed_issue(self):

        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tournament.start()
        self.assertTrue(all_results[len(all_results)] == self.nick)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        runner_name = 'test_runner'
        runner = Runner(runner_name, speed=10)
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner_name = 'test_runner'
        runner = Runner(runner_name, 5)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1_name = 'test_runner1'
        runner2_name = 'test_runner2'
        runner1 = Runner(runner1_name, 10)
        runner2 = Runner(runner2_name, 5)
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    Run1 = Runner("Усэйн", 10)
    Run2 = Runner("Андрей", 9)
    Run3 = Runner("Ник", 3)
    print(Run1)
    print(Run2)
    print(Run3)


    unittest.main()

