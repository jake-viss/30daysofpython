# Exercise 1-1 for the class/objects day of 30 days python. Creating the statistics class manually.
from numpy import sort
from sympy import maximum


class Statistics:
    def __init__(self, data=[]):
        self.data = data
        self.count = len(self.data)

    def sum(self):
        sum = 0
        for i in self.data:
            sum += i
        return sum

    def min(self):
        sample = sort(self.data)
        minimum = sample[0]
        return minimum

    def max(self):
        sample = sort(self.data)
        maximum = sample[-1]
        return maximum

    def range(self):
        maximum = sort(self.data)[-1]
        minimum = sort(self.data)[0]
        range = maximum - minimum
        return range

    def mean(self):
        sum = 0
        for i in self.data:
            sum += i
        average = round(sum / self.count)
        return average


data = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
                  27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])

print('Count:', data.count)
print('Sum:', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print(data.describe())
