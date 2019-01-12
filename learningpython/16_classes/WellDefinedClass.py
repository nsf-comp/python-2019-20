class MyClass:
    def __init__(self, i, j, k=100):
        self.m = i
        self.n = j
        self.r = k

    def printValues(self):
        print(self.m)
        print(self.n)
        print(self.r)

    def main(self):
        i = 10
        j = 20

        c = MyClass(i, j)

        c.printValues()

if __name__ == '__main__': MyClass.main()