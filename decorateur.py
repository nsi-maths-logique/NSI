def total(func):
    def inner(*args):
        try:
          return func(*args)
        except:
          return None
    return inner
  
def f(x, y):
    if x == y :
        return y+1
    else:
        return x+1
def g(x, y):
    if x >= y:
        return x+1
    else:  
        return y-1
@total        
def h(x, y):
    if x >= y and (x - y) % 2 == 0:
        return x+1
@total
def func(f, x, y):
    if x == y:
        return x+1
    else:
        return f(x, f(x-1, y+1))

for i in range(3):
    for j in range(3):
        print('func(f, %d, %d) == f(%d, %d) -> '%(i, j, i, j), func(f, i, j) == f(i, j))
        print('func(g, %d, %d) == g(%d, %d) -> '%(i, j, i, j), func(g, i, j) == g(i, j))
        print('func(h, %d, %d) == h(%d, %d) -> '%(i, j, i, j), func(h, i, j) == h(i, j))         