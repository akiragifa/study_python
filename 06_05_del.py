class Person:
    def __del__(self):
        print(f"销毁对象:{self}")


p1 = Person()
p2 = Person()

p1.__del__()

print("xixi")
print(p1)

del p2