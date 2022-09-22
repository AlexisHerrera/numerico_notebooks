def secante(f, p0, p1, tol, max_iter):
    n = 2
    
    q0 = f(p0)
    q1 = f(p1)
    
    while n < max_iter:
        p = p1 - q1*(p1-p0)/(q1-q0)
        dif_iter = abs(p-p1)
        print(f"Iteracion {n}, Pn: {p}, |Pn-Pn-1|: {dif_iter}")
        if dif_iter < tol:
            return
        n += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
        
    print(f"El método diverge tras {n} iteraciones")
            
            