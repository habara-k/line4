def ite():
    yield 1
    for _ in range(4):
        yield 0

print(any(ite()))
print(any(ite()))
print(any(ite()))
