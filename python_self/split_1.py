import numpy as np
# dataset1 = np.array([1,2,3,4,5,6,7,8,9,10])

# def split_xy1(dataset, time_steps):
#     x, y = list(), list()
#     for i in range(len(dataset1)):
#         end_number = i + time_steps
#         if end_number > len(dataset) -1:
#             break
#         tmp_x, tmp_y = dataset[i : end_number], dataset1[end_number]
#         x.append(tmp_x)
#         y.append(tmp_y)
#     return np.array(x), np.array(y)

# x, y = split_xy1(dataset1, 4)
# print(x, '\n', y)
# print('x.shape : ', x.shape)  #(dataset1, 4) = x.shape :  (6, 4)
# print('y.shape:', y.shape)

import numpy as np
dataset2 = np.array([[1,2,3,4,5,6,7,8,9,10],
                  [11,12,13,14,15,16,17,18,19,20],
                  [21,22,23,24,25,26,27,28,29,30],
                  [31,32,33,34,35,36,37,38,39,40]])

dataset2=np.transpose(dataset2)
print(dataset2.shape) # (4, 10)

def split_xy2(dataset2, x_row, x_col, y_row, y_col):
    x, y = list(), list()
    for i in range(len(dataset2)):
        x_start_number = i
        x_end_number = i + x_row
        y_end_number = x_end_number + y_row -1

        if y_end_number > len(dataset2):
            break
        tmp_x = dataset2[i: x_end_number, : x_col]
        tmp_y = dataset2[x_end_number -1: y_end_number, x_col:]
        x.append(tmp_x)
        y.append(tmp_y)
    return np.array(x), np.array(y)

x, y = split_xy2(dataset2, 4,2,5,2)
print(x, '\n\n', y) # 이러면 두줄 띄어쓰기가 된다.
print(x.shape) #(3, 4, 2)
print(y.shape) #(3, 5, 2)



