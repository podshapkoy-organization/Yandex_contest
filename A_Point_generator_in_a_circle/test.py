import random
import math


def generate1():
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return (a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b))


def generate2():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)


def generate(filename, num_sets=100, points_per_set=1000):
    with open(filename, 'w') as f:
        for i in range(num_sets):
            generator = generate1 if i % 2 == 0 else generate2
            points = [generator() for _ in range(points_per_set)]
            line = ' '.join(f"{x} {y}" for x, y in points)
            f.write(line + '\n')


def test_classifier(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        data = f.read().strip().split('\n')
    results = []
    for line in data:
        values = line.split()
        points = [(float(values[2 * i]), float(values[2 * i + 1])) for i in range(1000)]
        result = generator(points)
        results.append(result)
    with open(output_filename, 'w') as f:
        for result in results:
            f.write(str(result) + '\n')


def generator(points):
    distances = [math.sqrt(x ** 2 + y ** 2) for x, y in points]
    mean_distance = sum(distances) / len(distances)
    if mean_distance < 0.6:
        return 1
    else:
        return 2


if __name__ == "__main__":
    test_data = 'test_data.txt'
    output = 'test_output.txt'
    generate(test_data)
    test_classifier(test_data, output)
    with open(output, 'r') as f:
        results = f.read().strip().split('\n')
    exp_results = [1 if i % 2 == 0 else 2 for i in range(100)]
    correct = sum(int(result) == expected for result, expected in zip(results, exp_results))
    print(f"Этот прогноз что-то типа: {correct}/100")
