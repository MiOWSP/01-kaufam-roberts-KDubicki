class Kaufam_Roberts:
    def __init__(self, V, M, a, t):
        self.calc_x(V, M, a, t)
        self.calc_p(V, M, a, t)
        self.calc_b(V, t)

    def calc_array(self, V, M, a, t, arr):
        for n in range(1, V + 1):
            sum = 0
            for i in range(0, M):
                if n >= t[i]:
                    sum += a[i] * t[i] * arr[n - t[i]]
            arr[n] = sum / n


    def calc_x(self, V, M, a, t):
        self.x = [1] * (V + 1)
        self.calc_array(V, M, a, t, self.x)

    def calc_p(self, V, M, a, t):
        self.p = [1] * (V + 1)
        self.p[0] = 1 / sum(self.x)
        self.calc_array(V, M, a, t, self.p)

    def calc_b(self, V, t, i = 1):
        sum = 0
        for n in range(V - t[i - 1] + 1,V + 1):
            sum += self.p[n]
        
        self.b = sum