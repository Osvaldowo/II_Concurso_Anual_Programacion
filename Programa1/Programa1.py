import sys

def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = get_input()
    
    try:
        t_str = next(tokens)
        t = int(t_str)
    except StopIteration:
        return

    results = []
    for _ in range(t):
        try:
            n = int(next(tokens))
            if n <= 1:
                results.append("0")
            elif n == 2:
                results.append("1")
            else:
                results.append(str(n))
        except StopIteration:
            break
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()