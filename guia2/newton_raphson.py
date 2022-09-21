def newton_raphson(f, f_prima, p0, tol, max_iter):
    n = 1
    while n < max_iter:
        p = p0 - f(p0)/f_prima(p0)
        dif_iter = abs(p-p0)
        print(f"Iteracion {n}, Pn: {p}, |Pn-Pn-1|: {dif_iter}")
        if dif_iter < tol:
            return
        n +=1
        p0 = p
    print(f"El método diverge tras {n} iteraciones")