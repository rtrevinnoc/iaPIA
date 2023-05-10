import itertools, functools
from typing import Sequence
import time
import matplotlib.pyplot as plt
from numpy.lib import math

class Education:
    def __init__(self, problemPath: str, pmin: float, pmax: float) -> None:
        with open(f'./instancias/{problemPath}') as file:
            self.pmin = pmin
            parsedLines = [
                    dict(zip((
                        'materia',
                        'tema',
                        'subtema',
                        'actividad',
                        'duracion',
                        'valor',
                        'estres',
                        'req1',
                        'req2',
                        'obligatoria',
                    ), map(float, line.strip().split(","))))
                    for line in file.readlines()
            ]
            # head = parsedLines.pop(0)

            # self.n = head['profit']
            # self.wmax = head['weight']
            self.availableActivities = sorted(parsedLines, key=lambda line: line['actividad'])
            # for x in self.availableActivities:
            #     print(x)
            self.selectedActivities = []

            self.vmax = self.planValue(self.availableActivities)
            self.vmin = self.vmax * self.pmin
            self.pmax = pmax

            for index, activity in enumerate(self.availableActivities):
                if activity is not None:
                    if activity['obligatoria'] == 1.0:
                        self.selectedActivities.append(activity)
                        self.selectRequirements(activity)
                        self.availableActivities[index] = None

            for activity in self.selectedActivities:
                index = int(activity['actividad'] - 1)

            self.availableActivities = [act for act in self.availableActivities if act is not None]

            self.baseDuration = self.planDuration(self.selectedActivities)
            self.baseValue = self.planValue(self.selectedActivities)

    def selectRequirements(self, activity):
        if activity['req1'] == 0.0 and activity['req2'] == 0.0:
            return

        if activity['req1'] != 0:
            req1Index = int(activity['req1'] - 1)
            req1 = self.availableActivities[req1Index]
            if req1 is not None:
                self.selectedActivities.append(req1)
                self.selectRequirements(req1)
                self.availableActivities[req1Index] = None
        if activity['req2'] != 0:
            req2Index = int(activity['req2'] - 1)
            req2 = self.availableActivities[req2Index]
            if req2 is not None:
                self.selectedActivities.append(req2)
                self.selectRequirements(req2)
                self.availableActivities[req2Index] = None

    def planDuration(self, plan: Sequence) -> float:
        if len(plan) > 1:
            return functools.reduce(lambda planDuration, act: planDuration + act['duracion'], plan, 0)
        elif len(plan) == 1:
            return plan[0]['duracion']
        else:
            return 0

    def planValue(self, plan: Sequence) -> float:
        if len(plan) > 1:
            return functools.reduce(lambda planValue, act: planValue + act['valor'], plan, 0)
        elif len(plan) == 1:
            return plan[0]['valor']
        else:
            return 0

    def solveDFS(self) -> None:
        pool = tuple(self.availableActivities)
        n = len(pool)

        bestValue = 0#self.vmin
        bestDuration = math.inf
        bestPlan = None

        start = time.time()
        for indices in itertools.combinations_with_replacement(range(n), n):
            plan = tuple(pool[i] for i in set(indices))
            value = self.planValue(plan) + self.baseValue
            duration = self.planDuration(plan) + self.baseDuration

            if value > bestValue:# and duration < bestDuration:
                end = time.time()
                bestPlan = list(plan)
                bestPlan.extend(self.selectedActivities)
                bestValue = value
                bestDuration = duration
                print("\n\n#BETTER: ", value, duration, "%BEST: ", bestValue, bestDuration)
                print("#TIME: ", end-start)
                print([act['actividad'] for act in bestPlan])

    def solveAStar(self):
        def heuristic(act):
            try:
                return (act['valor'] / act['duracion'])
            except:
                return 0

        self.availableActivities.sort(key=lambda item: heuristic(item) + item['duracion'])

        currentPlan = []
        for act in self.availableActivities:
            if self.planValue(currentPlan) + act['valor'] <= (self.pmax * 0.8):
                currentPlan.append(act)


        value = self.planValue(currentPlan) + self.baseValue
        duration = self.planDuration(currentPlan) + self.baseDuration

        print(value, duration)

        # print(self.optimum, self.knapsackProfit(currentKnapsack), currentKnapsack)
        # return currentPlan

ed = Education("f_5_2.csv", 0.7, 0.8)
print(len(ed.availableActivities))
print(len(ed.selectedActivities))
print(ed.baseValue)
print(ed.baseDuration)

print(ed.vmax, ed.pmin, ed.vmin)

print(len(ed.selectedActivities), ed.baseValue, ed.baseDuration, ed.vmin)

print(ed.solveDFS())
