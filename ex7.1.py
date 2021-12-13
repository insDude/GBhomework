list1 = [[7, 4, 1, 5, 8], [4, 3, 1, 1, 2], [9, 9 ,1, 1, 5], [8, 3, 2, 5, 8]]
list2 = [[8, 3, 2, 5, 8], [9, 9 ,1, 1, 5], [4, 3, 1, 1, 2], [7, 4, 1, 5, 8]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __add__(self, other):
        list3 = []
        for i in range(len(self.lists)):
            list3.append([])
            for k in range(len(self.lists[0])):
                list3[i].append(self.lists[i][k] + other.lists[i][k])
        return '\n'.join(map(str, list3))

    def __str__(self):
        return '\n'.join(map(str, self.lists))

Mat1 = Matrix(list1)
Mat2 = Matrix(list2)

print(Mat1, '\n')
print(Mat2, '\n')
print(Mat1 + Mat2)