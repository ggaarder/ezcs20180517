import matplotlib.pyplot

testdats = [
    [[1, 1],
     [1, 2],
     [2, 4],
     [15, 15],
     [19, 20]],
]

def plot(dats):
    x, y = [i[0] for i in dat], [i[1] for i in dat]
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()

plot(testdats[0])
