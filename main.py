class TVM():

    def get_ear(r,m):
        r = r/100
        i = 1 + r / m
        i = pow(i,m)
        i = i - 1
        return i

    print(get_ear(8,4))




