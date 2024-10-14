def main():
    n = int(input().strip())
    first_row = list(map(float, input().strip().split()))
    sum_first_row = sum(first_row)
    sum_squares_first_row = sum(x ** 2 for x in first_row)
    total_sum = sum_first_row ** 2 / sum_squares_first_row
    print(f"{total_sum:.3f}")


if __name__ == "__main__":
    main()