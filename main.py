import numpy as np


class MyClass(object):
    def __init__(self, min_score, max_score):
        self.min_score = min_score
        self.max_score = max_score
        self.pairs = list()

    def fit(self, x, y, some_list):
        dn = np.einsum('i, j -> ', x, y)

        for i, j in some_list:
            assert (i < len(x)) * (j < len(y)) * (i >= 0) * (j >= 0)
            score = np.einsum('i, j -> ', x[:i], y[:j])
            score /= dn

            if self.min_score < score < self.max_score:
                self.pairs.append((i, j))

    def __iter__(self):
        for element in self.pairs:
            yield element

    def __len__(self):
        return len(self.pairs)


def main():
    n = 5
    m = 5

    x = np.random.randn(n)
    y = np.random.randn(m)

    i = range(n - 1)
    j = range(m - 1)

    iterable = [(a, b) for a in i for b in j]

    min_score = 0
    max_score = 1

    score_filter = MyClass(min_score, max_score)
    score_filter.fit(x, y, iterable)

    print(len(score_filter))

    for i in score_filter:
        print(i)


if __name__ == "__main__":
    main()
