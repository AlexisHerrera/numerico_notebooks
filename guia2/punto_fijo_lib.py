def punto_fijo(g, p0, tol, max_iter):
    """
    Algoritmo de punto fijo con criterio de paro tradicional
    |Pn-Pn-1| < TOL
    """
    n = 1
    while n <= max_iter:
        p = g(p0)
        dif_iter = abs(p-p0)
        print(f"Iteracion {n}, Pn: {p}, |Pn-Pn-1|: {dif_iter}")
        if dif_iter < tol:
            break
        n +=1
        p0 = p

def punto_fijo_error_riguroso(g, p0, tol, max_iter, k):
    """
    La diferencia con el otro es que aqui utiliza como criterio de paro
    a k/(1-k) * |Pn-Pn-1| < TOL
    """
    n = 1
    while n <= max_iter:
        p = g(p0)
        error = (k/(1-k))*abs(p-p0)
        print(f"Iteracion {n}, Pn: {p}, (k/1-k)*|Pn-Pn-1|: {error}")
        if error < tol:
            break
        n +=1
        p0 = p
