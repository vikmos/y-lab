""" Разработать программу для вычисления кратчайшего пути
    для почтальона. """

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


def main():
    arr = get_point_cordinats()
    n = len(arr)
    min_distance = float('inf')
    res = pr(arr[1:])
    route = []   
    for el in res:
        temp_route ="" 
        temp_distance = 0
        temp_distance += get_space_between_dots(arr[0], el[0])
        temp_route += f"{arr[0]} -> {el[0]}[{temp_distance}] \n"
        for i in range(len(el)):
            if i == len(el)-1:
                temp_distance += get_space_between_dots(el[-1], arr[0])
                temp_route += f"{el[-1]} -> {arr[0]}[{temp_distance}]"
            else:
                temp_distance += get_space_between_dots(el[i], el[i+1])
                temp_route += f"{el[i]} -> {el[i+1]}[{temp_distance}] \n"
        if min_distance >= temp_distance:
            min_distance = temp_distance
            route = temp_route
    print(route)
    print(f"Minimum distnce is {min_distance}")


if __name__ == "__main__":
    main()

