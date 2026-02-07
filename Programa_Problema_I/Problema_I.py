import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        k = float(input_data[idx + 1])
        idx += 2
        
        points = []
        for i in range(n):
            x = float(input_data[idx])
            y = float(input_data[idx + 1])
            points.append((x, y))
            idx += 2
            
        # 1. Calcular Área Inicial (Fórmula de la Agujeta / Shoelace)
        area_initial = 0.0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            area_initial += (x1 * y2 - x2 * y1)
        area_initial = abs(area_initial) / 2.0
        
        # Caso base: si el área ya es suficiente
        if area_initial >= k:
            results.append(0.0)
            continue
            
        # Calcular Perímetro Inicial
        perimeter_initial = 0.0
        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            perimeter_initial += dist
            
        # 3. Resolver la ecuación cuadrática: pi*r^2 + P0*r + (A0 - k) = 0
        # Forma: a*x^2 + b*x + c = 0
        a = math.pi
        b = perimeter_initial
        c = area_initial - k
        
        # Discriminante: D = b^2 - 4ac
        discriminant = b**2 - 4 * a * c
        
        r = (-b + math.sqrt(discriminant)) / (2 * a)
        results.append(r)

    for res in results:
        print(f"{res:.20f}")

if __name__ == "__main__":
    solve()