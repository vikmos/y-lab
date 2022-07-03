"""" Разработать программу для вычисления кратчайшего пути для почтальона. """
import ast

def get_point_cordinats()-> list[tuple]:
    """ Entering dots """
    points = []
    while True:
        s = input("Enter two digits with coma: ")
        if len(s) == 0:
            break
        else:
            dots = tuple(int(x) for x in s.split(","))
            points.append(dots)
    return points

def get_space_between_dots(point_1: tuple, point_2: tuple)-> float:
    """ Calculating space between dots """
    res = ((point_2[0] - point_1[0]) ** 2 + \
            (point_2[1] - point_1[1]) ** 2) \
            ** 0.5
    return res


def main():
    arr = get_point_cordinats()
    print(len(arr))
    for i in range(len(arr) - 1):
        print(get_space_between_dots(arr[i], arr[i+1]))


if __name__ == "__main__":
    main()



