class Kaufam_Roberts:
    def __init__(self, V, M, a, t):
        self.calc_x(V, M, a, t)
        self.calc_Pn(V, M, a, t)
        self.calc_G(V, t)

    def calc_array(self, V, M, a, t, arr):
        for n in range(1, V + 1):
            sum = 0
            for i in range(0, M):
                if n >= t[i]:
                    sum += a[i] * t[i] * arr[n - t[i]]
            arr[n] = sum / n


    def calc_x(self, V, M, a, t):
        x = [1] * (V + 1)
        self.calc_array(V, M, a, t, x)
        self.x = x

    def calc_Pn(self, V, M, a, t):
        P = [1] * (V + 1)
        P[0] = 1 / sum(self.x)
        self.calc_array(V, M, a, t, P)
        self.P = P

    def calc_G(self, V, t, i = 1):
        sum=0
        for n in range(V-t[i-1]+1,V+1):
            sum += self.P[n]
        
        self.G = sum