"""" Разработать программу для вычисления кратчайшего пути для почтальона. """

from math import sqrt
from itertools import permutations as pr


def get_point_cordinats()-> list[tuple]:
    """ Entering dots """
    points = []
    print("Введите два числа разделенные запятой. Для выхода введите пустуб строку!")
    while True:
        s = input()
        dots = tuple()
        if len(s) == 0:
            break
        elif len(s) < 3:
            print("Требуется ввести два числа разделённых заяптой")
        else:
            try:
                dots = tuple(float(x) for x in s.split(","))
            except ValueError:
                get_point_cordinats()
            points.append(dots)
    return points


def get_space_between_dots(point_1: tuple, point_2: tuple)-> float:
    """ Calculating space between dots """
    res = sqrt((point_2[0] - point_1[0]) ** 2 + \
            (point_2[1] - point_1[1]) ** 2) 
    return res


def create_matrix(size: int, data_list: list[tuple]) -> list[list]:
    """ Creating matrix with distance to all cities """
    matrix = []
    for i in range(size):
        row_list = []
        for j in range(size):
            if i != j:
                row_list.append(sqrt(get_space_between_dots(data_list[i],\
                        data_list[j])))
            else:
                row_list.append(float('inf'))
        matrix.append(row_list)
    return matrix


def main():
    arr = get_point_cordinats()
    n = len(arr)
    matrix = create_matrix(n, arr)
    min_distance = float('inf')
    
    for el in matrix:
        print(el)
    
    print("-----------------------------------------------------------------")
    res = pr(arr[1:])
    route = []   
    for el in res:
        temp_route =[] 
        temp_distance = 0
        temp_distance += get_space_between_dots(arr[0], el[0])
        temp_route += (arr[0], el[0], temp_distance)
        for i in range(len(el)):
            if i == len(el)-1:
                temp_distance += get_space_between_dots(el[-1], arr[0])
                temp_route += (el[-1], arr[0], temp_distance)
            else:
                temp_distance += get_space_between_dots(el[i], el[i+1])
                temp_route += (el[i], el[i+1], temp_distance)
                print(el[i], el[i+1], temp_distance, sep="->")
        if min_distance >= temp_distance:
            min_distance = temp_distance
            route = temp_route
    print(route, min_distance, sep="->")


if __name__ == "__main__":
    main()



