def min_prefix_with_alphabet(seq):
    required = set(range(1, 27))
    seen = set()

    for i, num in enumerate(seq):
        if num in required:
            seen.add(num)
        if len(seen) == 26:
            return i + 1  # длина префикса (индекс + 1)

    return "NONE"


if __name__ == "__main__":
    with open('data_prog_contest_problem_2.txt', 'r') as file:
        n, alphabet_len = map(int, file.readline().split())
        seq = []
        while len(seq) < n:
            line = file.readline()
            if not line:
                break
            seq.extend(map(int, line.strip().split()))

    result = min_prefix_with_alphabet(seq)
    print(result)

with open('output.txt', 'w') as f:
    f.write(f"{result}\n")






