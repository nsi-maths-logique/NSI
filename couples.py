def cons(e,l):
  return (e,l)
  
def tete(l):
  if l == ():
    return ()
  else:
    return l[0]
    
def queue(l):
  if l == ():
    return ()
  else:
    return l[1]
    
def elem(n, l):
  if n == 0:
    return tete(l)
  else:
    return elem(n-1, queue(l))    
    
def concatene(l1, l2):
  if l1 == ():
    return l2
  else:
    return cons(tete(l1), concatene(queue(l1), l2))
  
def longueur(l):
  if l == ():
    return 0
  else:
    return 1 + longueur(queue(l))

def inverser(l):
    if l == ():
        return ()
    else:
        elem = cons(tete(l),())
        return concatene(inverser(queue(l)), elem)

def coupe(l):
  m = longueur(l) // 2
  return coupe_liste(l, m, ())
  
def coupe_liste(l, m, l1):
  if m == 1:
    elem = cons(tete(l),())
    return concatene(l1,elem), queue(l)
  else:
    elem = cons(tete(l),())
    return coupe_liste(queue(l), m-1, concatene(l1,elem))
  
def fusion(l):
  if longueur(l) == 1:
    return l
  l1, l2 = coupe(l)
  return tri(fusion(l1), fusion(l2))

def tri(l1, l2):
  out = ()
  if l1 == () or l2 == ():
    return concatene(concatene(out,l1),l2)
  else:
    if tete(l1) <= tete(l2):
      elem = cons(tete(l1),())
      return concatene(concatene(out, elem), tri(queue(l1), l2))
    else:
      elem = cons(tete(l2),())
      return concatene(concatene(out, elem), tri(l1,queue(l2)))
      
def show(l):
  out = []
  while l != ():
    out.append(str(tete(l)))
    l = queue(l)
  return '[' + (',').join(out) + ']'
    
def position(e, l):
  n = longueur(l) // 2
  return position_rec(e, l, n)
def position_rec(e, l, m):
  n = longueur(l) // 2
  if longueur(l) == 1:
    if elem(n,l) == e:
      return m
    else:
      return -1
  elif elem(n-1,l) == e:
    return m - 1
  elif e < elem(n-1,l):
    l1, l2 = coupe(l)
    n = longueur(l1) // 2
    return position_rec(e, l1, m-n)
  else:
    l1, l2 = coupe(l)
    n = longueur(l2) // 2
    return position_rec(e, l2, m+n)
l1 = cons(9,cons(8,cons(7, cons(6,()))))
l2 = cons(5,cons(4,cons(3, cons(2,()))))
l = concatene(l1, l2)
print('l = ', l)
print('show(l) = ', show(l))
print('show(fusion(l)) = ', show(fusion(l)))
print('position(9, fusion(l)) = ', position(9, fusion(l)))
print('position(11, fusion(l)) = ', position(11, fusion(l)))
print('show(inverser(fusion(l))) = ', show(inverser(fusion(l))))
