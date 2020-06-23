# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    slide = deque([sequence[0]])
    for i in range(1, m):
        while slide and sequence[i] > slide[-1]:
            slide.pop()
        slide.append(sequence[i])
    for i in range(len(sequence) - m + 1):
        maximums.append(slide[0])
        if sequence[i] == slide[0]:
            slide.popleft()
        if i + m < len(sequence):
            while slide and sequence[i + m] > slide[-1]:
                slide.pop()
            slide.append(sequence[i + m])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

