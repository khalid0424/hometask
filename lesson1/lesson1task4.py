#N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок останется в корзинке?
N = int(input())
K = int(input())

a = K % N

print(a)