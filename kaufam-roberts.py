class Kaufam_Roberts:
    def __init__(self, V, M, a, t):
        self.calc_x(V, M, a, t)
        self.calc_p(V, M, a, t)
        self.b = [self.calc_b(V, t), self.calc_b(V, t, 2)]

    def calc_array(self, V, M, a, t, arr):
        for n in range(1, V + 1):
            sum = 0
            for i in range(0, M):
                if n >= t[i]:
                    sum += a[i] * t[i] * arr[n - t[i]]
            arr[n] = round(sum / n, 3)

    def calc_x(self, V, M, a, t):
        self.x = [1] * (V + 1)
        self.calc_array(V, M, a, t, self.x)

    def calc_p(self, V, M, a, t):
        self.p = [1] * (V + 1)
        self.p[0] = round(1 / sum(self.x), 3)
        self.calc_array(V, M, a, t, self.p)

    def calc_b(self, V, t, i = 1):
        sum = 0
        for n in range(V - t[i - 1] + 1,V + 1):
            sum += self.p[n]
        
        return round(sum, 3)

# -----------------------------------------------------------------------------

def printAll(V, M, a, t):
    print('Dane: V=', V, ',M=', M, ',a=', a, ',t=', t)
    result = Kaufam_Roberts(V, M, a, t)
    print('x=', result.x)
    print('p=', result.p)
    print('b=', result.b)
    print("\n")


printAll(3, 2, [0.4, 1], [1, 2])
printAll(3, 2, [0.8, 0.8], [1, 2])
printAll(3, 2, [1.2, 0.6], [1, 2])
printAll(3, 2, [1.6, 0.4], [1, 2])
printAll(3, 2, [2, 0.2], [1, 2])