import math
def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def max_iteraciones_biseccion(a,b,tol):
    """
    Dado los extremos del intervalo y la tolerancia buscada
    se calcula la cantidad de iteraciones maximas necesarias
    para el algoritmo de bisección
    """
    return math.ceil( (math.log(b-a)-math.log(tol))/math.log(2))

def biseccion(f, a, b, tol, max_iter):
    """
    Metodo de bisección clásico (criterio de corte (b-a)/2 < tol)
    Precondiciones:
    - f continua en el intervalo cerrado [a,b]
    - f(a)*f(b)<0
    Ejecuta el metodo de bisección con todos sus pasos intermedios
    """
    n = 1
    while n <= max_iter:
        c = (a+b)/2
        print(f"Iteracion {n}, a:{a}, b:{b}, c:{c}, f(c):{f(c)}, (b-a)/2 = {(b-a)/2}")
        if f(c) == 0 or (b-a)/2 < tol:
            print(f"Resultado final: {c}")
            break
        n += 1
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c

def biseccion_error_absoluto_anterior(f, a, b, tol, max_iter):
    """            
    Metodo de bisección con criterio de corte |Pn - Pn-1| < TOL
    Precondiciones:
    - f continua en el intervalo cerrado [a,b]
    - f(a)*f(b)<0
    Ejecuta el metodo de bisección con todos sus pasos intermedios
    """
    n = 1
    c_anterior = None
    
    while n <= max_iter:
        c = (a+b)/2
        print(f"Iteracion {n}, a:{a}, b:{b}, c:{c}, f(c):{f(c)}, |Pn-Pn-1| = {'-' if c_anterior is None else abs(c-c_anterior)}")
        if f(c) == 0 or ((c_anterior is not None) and abs(c-c_anterior) < tol):
            print(f"Resultado final: {c}")
            break
        n += 1
        c_anterior = c
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c
            

def biseccion_error_relativo(f, a, b, tol, max_iter):
    """
    Metodo de bisección con criterio de corte |Pn - Pn-1|/|Pn| < TOL
    Precondiciones:
    - f continua en el intervalo cerrado [a,b]
    - f(a)*f(b)<0
    Ejecuta el metodo de bisección con todos sus pasos intermedios
    """
    n = 1
    c_anterior = None
    
    while n <= max_iter:
        c = (a+b)/2
        error_relativo = None if c_anterior is None else abs(c-c_anterior)/abs(c)
        print(f"Iteracion {n}, a:{a}, b:{b}, c:{c}, f(c):{f(c)}, |Pn-Pn-1|/|Pn| = {'-' if error_relativo is None else error_relativo}")
        if f(c) == 0 or ((error_relativo is not None) and error_relativo < tol):
            print(f"Resultado final: {c}")
            break
        n += 1
        c_anterior = c
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c

            

def biseccion_error_evaluado(f, a, b, tol, max_iter):
    """
    Metodo de bisección con criterio de corte |f(Pn)| < TOL
    Precondiciones:
    - f continua en el intervalo cerrado [a,b]
    - f(a)*f(b)<0
    Ejecuta el metodo de bisección con todos sus pasos intermedios
    """
    n = 1
    while n <= max_iter:
        c = (a+b)/2
        print(f"Iteracion {n}, a:{a}, b:{b}, c:{c}, |f(Pn)|: {abs(f(c))}")
        if f(c) == 0 or abs(f(c)) < tol:
            print(f"Resultado final: {c}")
            break
        n += 1
        if sign(f(c)) == sign(f(a)):
            a = c
        else:
            b = c