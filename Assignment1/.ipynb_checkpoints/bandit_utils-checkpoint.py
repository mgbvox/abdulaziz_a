import numpy as np

class Bandit:
    def __init__(self, r=1):
        self.p = np.random.random()
        self.r = r

    def __repr__(self):
        return f'B: {round(self.p, 2)}'


    def get_reward(self):
        return int(np.random.random() < self.p)*self.r



class UCBAgent:
    def __init__(self, bandits):
        self.t = 1
        self.n = len(bandits)
        self.bandits = {n:b for n,b in enumerate(bandits)}
        self.bandit_history = {n:np.array([]) for n in range(self.n)}
        self.expectation = {n:1 for n in range(self.n)}
        self.counts = {n:0 for n in range(self.n)}
        self.reward_history = []

    def calc_probs(self, a):
        h = self.bandit_history[a]
        return np.sum(h)/self.counts[a]

    def run_one_step(self):
        a = np.argmax([self.expectation[i] + np.sqrt(2 * np.log(self.t) / (1 + self.counts[i])) for i in range(self.n)])
        bandit = self.bandits[a]
        self.counts[a] += 1

        r = bandit.get_reward()
        self.bandit_history[a] = np.hstack((self.bandit_history[a], np.array([r])))
        self.expectation[a] += 1. / (self.counts[a] + 1) * (r - self.expectation[a])

        self.reward_history.append(r)
        self.t += 1

    def run(self, steps):
        for _ in range(steps):
            self.run_one_step()