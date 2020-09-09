class A:
    d = 1

    def a(self, a, b):
        return self.d + a + b


s = A()

print(getattr(s, 'a')(1, 2))
