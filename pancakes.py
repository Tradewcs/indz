def count_payed_if_maximazed(pancakes, pancakes_count):
    i = 0
    j = pancakes_count - 1
    max_pancake = min(pancakes[i], pancakes[j])
    count_payed = 0

    while i <= j:
        if pancakes[i] < pancakes[j]:
            if pancakes[i] >= max_pancake:
                count_payed += 1
                max_pancake = pancakes[i]

            i += 1
        else:
            if pancakes[j] >= max_pancake:
                count_payed += 1
                max_pancake = pancakes[j]

            j -= 1

    return count_payed

def main():
    tests_amount = int(input())
    out = ""

    for i in range(tests_amount):
        pancakes_count = int(input())
        pancakes = [int(el) for el in input().split()]

        customers_payed = count_payed_if_maximazed(pancakes, pancakes_count)

        out += 'Case #{}: {}\n'.format(i + 1, customers_payed)

    print(out, end='')

if __name__ == '__main__':
    main()
