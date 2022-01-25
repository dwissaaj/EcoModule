class TVM():

    def get_ear(r,m):
        r = r/100
        i = 1 + r / m
        i = pow(i,m)
        i = i - 1
        return i

    print(get_ear(8, 4))

    def predict_by_ear(account,r,m,year):
        r = r / 100
        i = 1 + r / m
        i = pow(i, m)
        i = i - 1
        account = account * i * year
        print(pow(i,m))
        return account

    print(predict_by_ear(2500,8,4,2))


