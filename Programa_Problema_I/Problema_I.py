import sys
import math

# Aumentar el límite de recursión por seguridad, aunque este enfoque es iterativo.
sys.setrecursionlimit(2000)

def solve():
    """
    Problema: I. Your Best American Poly
    Método: El área de un polígono convexo dilatado por un radio r está dada por:
            A(r) = Area_Inicial + Perímetro * r + pi * r^2
            
            Esto es una ecuación cuadrática para r:
            pi * r^2 + P * r + (A0 - k) = 0
    """
    
    # Lectura rápida de todos los datos de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Usamos un iterador para recorrer los datos eficientemente
    iterator = iter(input_data)
    
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    results = []

    for _ in range(num_test_cases):
        try:
            n = int(next(iterator))
            k = float(next(iterator))
            
            points = []
            # Leer coordenadas (x, y)
            for _ in range(n):
                x = float(next(iterator))
                y = float(next(iterator))
                points.append((x, y))
            
            # 1. Calcular Área Inicial (Fórmula de la Agujeta / Shoelace)
            area_initial = 0.0
            for i in range(n):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n] # El módulo conecta el último con el primero
                area_initial += (x1 * y2 - x2 * y1)
            
            area_initial = abs(area_initial) / 2.0
            
            # Caso Base: Si el área ya es suficiente, no necesitamos expandir (r=0)
            if area_initial >= k:
                results.append(0.0)
                continue

            # 2. Calcular Perímetro Inicial
            perimeter = 0.0
            for i in range(n):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n]
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                perimeter += dist
            
            # 3. Resolver Ecuación Cuadrática para r
            # Coeficientes: a*r^2 + b*r + c = 0
            a = math.pi
            b = perimeter
            c = area_initial - k
            
            # Discriminante
            discriminant = b*b - 4*a*c
            
            # Fórmula general: r = (-b + sqrt(D)) / 2a
            # Como r > 0 y perímetro > 0, tomamos la raíz positiva
            if discriminant < 0:
                # Matemáticamente no debería pasar dado que area_initial < k, pero por seguridad
                r = 0.0
            else:
                r = (-b + math.sqrt(discriminant)) / (2 * a)
            
            results.append(r)

        except StopIteration:
            break

    # Imprimir resultados con alta precisión (hasta 20 decimales para asegurar margen de error)
    for res in results:
        print(f"{res:.20f}")

if __name__ == '__main__':
    solve()
