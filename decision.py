class Decision(object):
    def __init__(self, pair: tuple(int), result: int):
        self.pair = pair
        self.result = result

    def dict(self):
        return {'pair': self.pair, 'result': self.result}

    def str(self):
        res = 'Pair: ({0}, {1}), Result: {2}'
        return res.format(self.pair[0], self.pair[1], self.result)




