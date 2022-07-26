class ArithmeticSequence:
    def __init__(self, start, skip, stop = 50):
        self.start = start
        self.skip = skip
        self.stop = stop
        self.seq = [num for num in range(start, stop, skip)]

    def __add__(self, other):
        if type(other) is int:
            idx = self.seq[other]
            return ArithmeticSequence(idx, self.skip)
        elif type(other) is ArithmeticSequence:
            return ArithmeticSequence(self.start, self.skip + other.skip)
        else:
            raise TypeError("Type is not supported.")

    def __str__(self):
        seq = ", ".join(map(str, self.seq))
        return f'{seq}'

a = ArithmeticSequence(1, 2)
print(a) # prints "1, 3, 5, ...", that is the first 3 elements and then

# an ellipsis ...

a += 10 # advances the series to the 10th element of a
print(a) # prints "21, 23, 25, ..."
b = ArithmeticSequence(0, 3)
print(b) # prints "0, 3, 6, ..."
c = a + b
print(c) # prints "21, 26, 31, ..."