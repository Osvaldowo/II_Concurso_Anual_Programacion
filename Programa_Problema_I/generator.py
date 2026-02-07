import math

def generate_huge_test():
    n = 200000
    k = 10**16
    radius = 10**7
    
    with open("test_stress.txt", "w") as f:
        # 1 caso de prueba
        f.write("1\n")
        # n vértices y el área k
        f.write(f"{n} {k}\n")
        
        for i in range(n):
            angle = (2 * math.pi * i) / n
            x = int(radius * math.cos(angle))
            y = int(radius * math.sin(angle))
            f.write(f"{x} {y}\n")

if __name__ == "__main__":
    generate_huge_test()
    print("Archivo 'test_stress.txt' generado con 200,000 puntos.")