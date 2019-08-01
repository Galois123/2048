from flask import render_template, jsonify, request
import random
from functools import reduce
from . import index_blu


@index_blu.route('/')
def index():
    """
    :return:
    """
    # M x M格子
    CONST = 4

    elem1 = random.randint(0, 15)
    elem2 = random.randint(0, 15)
    while elem1 == elem2:
        elem2 = random.randint(0, 15)

    x1, y1 = elem1 // CONST, elem1 % CONST
    x2, y2 = elem2 // CONST, elem2 % CONST
    matrix = [['' for col in range(CONST)] for row in range(CONST)]

    matrix[x1][y1] = 2
    matrix[x2][y2] = 2
    data = {
        'matrix': matrix
    }
    return render_template('index.html', data=data)


@index_blu.route('/move', methods=['POST'])
def move():
    """
    接收参数
    activate: 'UP', 'RIGHT', 'DOWN', 'LEFT'
    list: 数据列表

    errno: errmsg
    2       成功
    1       非法参数
    0       不做任何操作
    -1       游戏结束
    :return:
    """
    # 1. 接收参数
    action = request.json.get('action')
    matrix = request.json.get('matrix')

    # 2. 校验参数
    if action not in ['UP', 'RIGHT', 'DOWN', 'LEFT']:
        return jsonify(errno=1, errmsg='非法参数')

    # 3. 业务逻辑

    # if 如果能移动 if can_move(matrix):
    #       # 调用函数移动
    #       # 返回 errno=2, errmsg='成功'
    # else:
    #     # 不能向任何方向移动，游戏结束
    #       errno=-1, errmsg='game over'
    # 3.1 能否移动
    if not can_move(matrix):
        return jsonify(errno=-1, errmsg='game over')

    # 3.2 向指定方向移动
    if action == 'UP':
        n_matrix = move_up(matrix)
    elif action == 'RIGHT':
        n_matrix = move_right(matrix)
    elif action == 'DOWN':
        n_matrix = move_down(matrix)
    else:
        n_matrix = move_left(matrix)

    if matrix == n_matrix:
        return jsonify(errno=0, errmsg='保持原样')

    res = reduce(lambda x, y: x + y, n_matrix)

    # 3.3 在空白处添加2
    # a)循环判断

    # while True:
    #     n_val = random.randint(0, 15)
    #     if res[n_val] == '':
    #         res[n_val] = 2
    #         break

    # b)获取所有的空格，随机选一个
    all_space = []
    for i, val in enumerate(res):
        if val == '':
            all_space.append(i)

    if all_space:
        res[all_space[random.randint(0, len(all_space) - 1)]] = 2

    data = {
        'matrix': res
    }
    return jsonify(errno=2, errmsg='OK', data=data)


# 检查表格中是否有空格
def check_space(matrix):
    """
    检查是否有空格
    :return:
    """
    for row in matrix:
        # if row.index('') != -1:
        if '' in row:
            return True
    return False


# 矩阵中是否有相邻元素与其值相等
def neighbors(matrix):
    """
    检查是否有相邻位置值相同
    :return:
    """

    # 保存已经追踪过的点
    visited = []

    def wrapper(x=0, y=0):
        # 边界判断
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            # 添加已经追踪过的点
            visited.append((x, y))

            # 递归判断周围的点
            coll = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]

            # 当前点判断
            # res = (matrix[x][y] in [matrix[x - 1][y], matrix[x][y + 1], matrix[x + 1][y], matrix[x][y - 1]])
            res = False
            for a, b in coll:
                if 0 <= a < len(matrix) and 0 <= b < len(matrix[0]):
                    res = res or (matrix[a][b] == matrix[x][y])
                if (a, b) not in visited:
                    res = res or wrapper(a, b)
            return res
        return False

    return wrapper()


# 是否能够移动
def can_move(matrix):
    """
    当前矩阵是否能够移动
    :param matrix:
    :return:
    """
    # if 没有空字符串:
    if not check_space(matrix) and not neighbors(matrix):
        # elif 没有相邻的两个方块值相等:
        return False
    return True


# 反转矩阵
def my_reverse(matrix):
    """
    反转列表
    :param matrix:
    :return:
    """
    return [matrix[i][::-1] for i in range(len(matrix))]


# 转置矩阵
def my_trans(matrix):
    """
    转置
    :param matrix:
    :return:
    """
    return [list(n) for n in zip(*matrix)]


# 向左移动
def move_left(matrix):
    """
    向左移动
    :return:
    """
    # 向左移动
    # 去除所有的''，生成一个新列表
    n_list = [[val for val in row if val] for row in matrix]

    # 合并
    n_list2 = [[], [], [], []]

    # 合并相邻相同元素
    for i, row in enumerate(n_list):
        j = 0
        while j < len(row):
            if j == len(row) - 1:
                n_list2[i].append(row[j])
                break

            if row[j] == row[j + 1]:
                n_list2[i].append(str(2 * int(row[j])))
                j += 1
            else:
                n_list2[i].append(row[j])

            j += 1

    # 用空字符串占位
    for i in range(len(n_list2)):
        for j in range(len(n_list2)):
            n_list2[i] += [''] * (4 - len(n_list2[i]))

    return n_list2


# 向右移动
def move_right(matrix):
    """
    向右移动
    :param matrix:
    :return:
    """
    # 1. 反转
    # 2. move_left
    # 3. 反转回来
    return my_reverse(move_left(my_reverse(matrix)))


# 向上移动
def move_up(matrix):
    """
    向上移动
    :param matrix:
    :return:
    """
    return my_trans(move_left(my_trans(matrix)))


# 向下移动
def move_down(matrix):
    """
    向下移动
    :param matrix:
    :return:
    """
    matrix1 = my_reverse(my_trans(matrix))
    matrix2 = move_left(matrix1)
    matrix3 = my_trans(my_reverse(matrix2))
    return matrix3

# if __name__ == '__main__':
#     matrix = [[random.randint(0, 1) * 2 for col in range(4)] for row in range(4)]
#     move_left(matrix)
