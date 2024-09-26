c = 300000000
def RelativityTheory(m,c):
    e = m * c * c
    return e
def Main():
    m = int(input())
    e = RelativityTheory(m,c)
    print(e)
Main()
