import numpy as np
import matplotlib.pyplot as plt
import function_plotter as fp


def _find_approx_index(arr, val, l=None, r=None): # using binary search
    if l is None: l = 0
    if r is None: r = len(arr)-1
    if l == r: return r

    mid = (l+r)//2
    if arr[mid] == val or (r-l == 1 and arr[l]<val and arr[r]>val): return mid
    if arr[mid] < val:  return _find_approx_index(arr, val, mid, r)
    if arr[mid] > val:  return _find_approx_index(arr, val, l, mid)


class Taylor_Series():
    def __init__(self, f, t, a):
        self.a = a
        self.f = f
        self.t = t
        self.dt = abs(self.t[0]-self.t[1])
        self.N = 0
        self.series = np.zeros( shape=len(self.t) )
        self.derivatives = [self.f]
        self.a_index = _find_approx_index(self.t,self.a)

    def add_next_term(self):
        _next = self._taylor_term(self.N+1)
        self.series += _next
        self.N += 1

    def _taylor_term(self, n):

        for i in range(self.N,n):
            self.derivatives.append(np.gradient(self.derivatives[i],self.dt, edge_order=2))

        n_term = np.zeros( shape=len(self.t), dtype=float )
        for i in range(len(self.t)):
            n_term[i] = self.derivatives[n-1][self.a_index] / np.math.factorial(n-1) * np.power(self.t[i]-self.a,n-1) 
        
        return n_term

    def get_series(self):
        return self.series


def taylor(f, t, a, N):
    """
    (f -> function values [list])
    (t -> time values [list])
    (a -> centered about 'a': [int|float])
    (N -> # of terms: int)
    """
    derivatives = [f]
    dx = abs(t[0]-t[1])

    a_index = _find_approx_index(t, a, 0, len(t)-1)

    for n in range(1,N):
        derivatives.append(np.gradient(derivatives[n-1],dx))

    f_taylor = []
    for _t in t:
        f_sum = 0
        for n in range(N):
            f_sum += derivatives[n][a_index] / np.math.factorial(n) * np.power(_t-a,n) 
        f_taylor.append(f_sum)
    
    return f_taylor


if __name__ == '__main__':
    N = 1000
    t = np.array(range(-N,N)) * np.pi/N
    f = lambda t: np.sin(t)
    f_t = f(t)

    terms = 5
    centered = 0
    ts = taylor(f_t, t, centered, terms)

    fig = plt.plot(t, f_t, 'b', t, ts, 'r')
    plt.ylim(min(f_t), max(f_t))
    plt.show()