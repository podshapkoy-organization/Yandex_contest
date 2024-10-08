import math
import sys


def generator(points):
    distances = [math.sqrt(x ** 2 + y ** 2) for x, y in points]
    mean_distance = sum(distances) / len(distances)
    if mean_distance < 0.6:
        return 1
    else:
        return 2


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    results = []
    for line in data:
        values = line.split()
        points = [(float(values[2 * i]), float(values[2 * i + 1])) for i in range(1000)]
        result = generator(points)
        results.append(result)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
