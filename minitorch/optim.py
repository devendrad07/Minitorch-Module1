class Optimizer:
    def __init__(self, parameters):
        self.parameters = parameters


class SGD(Optimizer):
    def __init__(self, parameters, lr=1.0):
        super().__init__(parameters)
        self.lr = lr

    def zero_grad(self):
        for _,p in self.parameters.items():
            if p.value.derivative is not None:
                p.value._derivative = None

    def step(self):
        for _, p in self.parameters.items():
            if p.value.derivative is not None:
                p.update(p.value - self.lr * p.value.derivative)