n = int(input())
# n= 4  i = 0  sp = 3 stars = 1
# n= 4  i = 1  sp = 2  stars = 2
# n= 4  i = 2  sp = 1 stars = 3
# n= 4  i = 3  sp = 0 stars = 4
# formula = (n-1-i)  space, (n-spase) stars
# ---*
# --* *
# -* * *
def print_line_of_figure(size_of_rhombus,current_line_num):
    space = f"{' ' * (size_of_rhombus - 1 - current_line_num)}"
    print(f"{space}{'* ' * (size_of_rhombus - len(space))}")


def print_first_part_of_figure (n):
    for i in range(n):
        print_line_of_figure(n, i)

def print_second_part_of_figure (n):
    for j in range(n - 2, -1, -1):
        print_line_of_figure(n, j)


def print_figure (n):
    print_first_part_of_figure(n)
    print_second_part_of_figure(n)



# print_first_part_of_figure(n)
# print(12 * '-')
# print_second_part_of_figure(n)
# print(12 * '-')
print_figure(n)







