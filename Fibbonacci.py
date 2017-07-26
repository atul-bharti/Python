class Fib:
    '''It is for fibbonacci serioe'''

    def __init__(self,max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

    def __test__(self):
        print('hi python')

for i in Fib(20):
    print(i)


