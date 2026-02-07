import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    N = int(next(it))
    Q = int(next(it))
    
    # Usar un arreglo de enteros
    a = [0] * (N + 1)
    for i in range(1, N + 1):
        a[i] = int(next(it))
        
    results = []
    
    # Referencias locales (hace que el acceso sea más rápido en Python)
    for _ in range(Q):
        curr = int(next(it))
        k = int(next(it))
        
        while curr > 0:
            siguiente = a[curr]
            a[curr] -= k
            curr = siguiente
            
        results.append(str(curr))
        
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()