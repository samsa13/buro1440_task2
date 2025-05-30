def find_min_subsequence_length(n, k, sequence):
    if k > 26:
        return "NONE"

    from collections import defaultdict

    count = defaultdict(int)
    required = k
    formed = 0
    left = 0
    min_len = float('inf')

    for right in range(n):
        char = sequence[right]
        if 1 <= char <= k:
            count[char] += 1
            # Если впервые встретили эту букву в окне
            if count[char] == 1:
                formed += 1

        # Когда окно содержит все буквы, пытаемся его сузить
        while formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len

            left_char = sequence[left]
            if 1 <= left_char <= k:
                count[left_char] -= 1
                # Если буква перестала встречаться в окне
                if count[left_char] == 0:
                    formed -= 1
            left += 1

    return min_len if min_len != float('inf') else "NONE"


# Чтение данных из файла input.txt
with open('data_prog_contest_problem_2.txt', 'r') as file:
    first_line = file.readline().strip()
    n, k = map(int, first_line.split())
    second_line = file.readline().strip()
    sequence = list(map(int, second_line.split()))

result = find_min_subsequence_length(n, k, sequence)
print(result)

with open('output.txt', 'w') as f:
    f.write(f"{result}\n")






