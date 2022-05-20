import csv
import numpy
import random
import argparse


def data_maker(n, m):
    vectors_array = numpy.random.uniform(-1, 1, (n, m))
    return vectors_array

def write_csv(matrix):
    with open('vectors.csv', 'a') as file:
        writer = csv.writer(file)
        for vector in matrix:
            writer.writerow(vector)

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-n', default=random.randint(500, 1000), help='Количество строк от 500 до 1000.')
    parse.add_argument('-m', default=random.randint(10, 50), help='Количество столбцов от 10 до 50.')
    args = parse.parse_args()
    if (500 <= int(args.n) <= 1000) and (10 <= int(args.m) <= 50):
        vector_matrix = data_maker(int(args.n), int(args.m))
        with open('vectors.csv', 'w+') as file:
            line = file.readline()
            if len(line) > 0:
                file.truncate()
        write_csv(vector_matrix)
        print(args.n, args.m)
    else:
        raise SystemExit('Ошибка!')

if __name__ == "__main__":
    main()
