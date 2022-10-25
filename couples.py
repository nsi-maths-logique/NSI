def cons(e,l):
  return (e,l)
  
def tete(l):
  if l == ():
    return ()
  return l[0]
    
def queue(l):
  if l == ():
    return ()
  return l[1]
    
def elem(n, l):
  assert n <= longueur(l), 'Le rang est superieur a la longueur de la liste'
  if n == 0:
    return tete(l)
  return elem(n-1, queue(l))    
    
def concatene(l1, l2):
  if l1 == ():
    return l2
  return cons(tete(l1), concatene(queue(l1), l2))
  
def longueur(l):
  if l == ():
    return 0
  return 1 + longueur(queue(l))

def nb_occ(e, l):
  if l == '':
    return 0
  if tete(l) == e:
    return 1 + nb_occ(e, queue(l))
  return nb_occ(e, queue(l))

def liste_vers_tuple(liste):
  if liste == []:
    return ()
  return cons(liste[0], liste_vers_tuple(liste[1:]))

def tuple_vers_liste(l):
  if l == ():
    return []
  return [tete(l)] + tuple_vers_liste(queue(l))

def inverser(l):
  if l == ():
    return ()
  elem = cons(tete(l),())
  return concatene(inverser(queue(l)), elem)

def coupe(l):
  m = longueur(l) // 2
  return coupe_liste(l, m, ())
  
def coupe_liste(l, m, l1):
  if m == 1:
    elem = cons(tete(l),())
    return concatene(l1,elem), queue(l)
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
  if tete(l1) <= tete(l2):
    elem = cons(tete(l1),())
    return concatene(concatene(out, elem), tri(queue(l1), l2))
  elem = cons(tete(l2),())
  return concatene(concatene(out, elem), tri(l1,queue(l2)))
          
def position(e, l):
  n = longueur(l) // 2
  return position_rec(e, l, n)

def position_rec(e, l, m):
  n = longueur(l) // 2
  if longueur(l) == 1:
    if elem(n,l) == e:
      return m
    return -1
  elif elem(n-1,l) == e:
    return m - 1
  elif e < elem(n-1,l):
    l1, l2 = coupe(l)
    n = longueur(l1) // 2
    return position_rec(e, l1, m-n)
  l1, l2 = coupe(l)
  n = longueur(l2) // 2
  return position_rec(e, l2, m+n)
