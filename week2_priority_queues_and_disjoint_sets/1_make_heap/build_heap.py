# python3
import random

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):            
        while True:
            # print("i:", i)
            if ((2 * i) + 1) >= n:
                break
            if ((2 * i) + 2) < n:
                l, r = (2 * i) + 1, (2 * i) + 2
                if data[i] < data[l] and data[i] < data[r]:
                    break
                if data[l] < data[r]:
                    temp = l
                else:
                    temp = r
                swaps.append((i, temp))
                data[i], data[temp] = data[temp], data[i]
                # print("data:", data)
                i = temp
            else:
                l = (2 * i) + 1
                if data[i] < data[l]:
                    break
                swaps.append((i, l))
                data[i], data[l] = data[l], data[i]
                break
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    # count = 0
    # while True:
    # n = random.randrange(1, 7)
    # data = random.sample(range(0, 11), n)
    # print("begining:", data)
    # n = 6
    # data = [5, 8, 9, 1, 7, 2]
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        # if count == 10:
        #     break
        # count += 1



if __name__ == "__main__":
    main()
