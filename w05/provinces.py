def main():
    with open('provinces.txt', 'r') as f:
        provinces = [province.strip() for province in f.readlines()]

    print(provinces)
    provinces.pop(0)
    provinces.pop()
    provinces = ["Alberta" if province == "AB" else province for province in provinces]
    print(provinces.count("Alberta"))


if __name__ == '__main__':
    main()
