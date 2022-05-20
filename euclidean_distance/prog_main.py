from scipy.spatial import distance
import matplotlib.pyplot as plt

import os
import csv
import numpy


def get_vectors_list_from_csv():
    with open('vectors.csv', 'r') as file:
        vector_list = []
        reader = csv.reader(file)
        for line in reader:
            line_vector = []
            for i in line:
                line_vector.append(float(i))
            vector_list.append(line_vector)
        return vector_list

def euclidean_distance(vector_list):
    with open('distance.txt', 'a') as f:
        max_distance = 0.0
        couple_max = ()
        couple_min = ()
        for i in range(len(vector_list)):
            for j in range(i+1, len(vector_list)):
                obj = distance.euclidean(vector_list[i], vector_list[j])
                f.writelines('{}\n'.format(obj))
                if obj >= max_distance:
                    max_distance = obj
                    couple_max = (i, j)
        min_distance = max_distance
        for i in range(len(vector_list)):
            for j in range(i+1, len(vector_list)):
                obj = distance.euclidean(vector_list[i], vector_list[j])
                if obj < min_distance:
                    min_distance = obj
                    couple_min = (i, j)
        return max_distance, couple_max, min_distance, couple_min

def info_maker(max_distance, couple_max, min_distance, couple_min):
    bins = []
    x = 0.0
    for i in range(int(round(max_distance) * 10)):
        bins.append(round(x, 1))
        x += 0.1
    plt.style.use('ggplot')
    plt.ylabel('Частота')
    plt.xlabel('Расстояние')
    plt.hist(numpy.loadtxt('distance.txt'), bins=bins)
    plt.title('Распределение расстояний')
    print(
        'Минимальное расстояние:', min_distance, 'Пара векторов: ', couple_min, '\n',
        'Максимальное расстояние:', max_distance, 'Пара векторов:', couple_max,
    )
    plt.show()
    os.remove('distance.txt')

def main():
    vectors_list = get_vectors_list_from_csv()
    max_distance, couple_max, min_distance, couple_min = euclidean_distance(vectors_list)
    info_maker(max_distance, couple_max, min_distance, couple_min)

if __name__ == "__main__":
    main()
