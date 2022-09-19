def punto_fijo(g, p0, tol, max_iter):
    n = 1
    while n <= max_iter:
        p = g(p0)
        error = abs(p-p0)
        print(f"Iteracion {n}, Pn: {p}, |Pn-Pn-1|: {error}")
        if error < tol:
            break
        n +=1
        p0 = p

""" La diferencia con el otro es que aqui utiliza como cota de error
    a k/(1-k) < TOL
"""
def punto_fijo_error_riguroso(g, p0, tol, max_iter, k):
    n = 1
    while n <= max_iter:
        p = g(p0)
        error = (k/(1-k))*abs(p-p0)
        print(f"Iteracion {n}, Pn: {p}, (k/1-k)*|Pn-Pn-1|: {error}")
        if error < tol:
            break
        n +=1
        p0 = p

def max_iter_punto_fijo(error, k, p1, p0):
    