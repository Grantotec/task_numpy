import numpy as np


class MyClass:
    def __init__(self, min_score, max_score):
        self.min_score = min_score
        self.max_score = max_score
        self.pairs = list()

    def fit(self, x, y, some_list):
        self.a = np.outer(x, y)
        for i, j in some_list:
            if self.min_score < (np.sum(self.a[:i+1, :j+1]) / np.sum(self.a)) < self.max_score:
                self.pairs.append((i, j))

    def __iter__(self):
        for element in self.pairs:
            yield element


def main():
    n = 5
    m = 5

    x = np.random.randint(n - 1)
    y = np.arange(m - 1)

    i = range(n - 1)
    j = range(m - 1)
    iterable = [(a, b) for a in i for b in j]

    min_score = 0
    max_score = 1

    score_filter = MyClass(min_score, max_score)

    score_filter.fit(x, y, iterable)

    for i in score_filter:
        print(i)


if __name__ == "__main__":
    main()
