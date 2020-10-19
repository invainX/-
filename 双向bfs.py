# -*- coding: cp936 -*-

import sys

daiding=0
def getPos(m):
    for i in range(len(m)):

        if m[i] == daiding:
            return i


def result(state, cache, l, r):
    for i in range(l, r):

        if state == cache[i]:
            return i

    return -1


step = 0


def print_after(cache, far, num):  # print 后序

    if num == -1:
        return

    print_after(cache, far, far[num])

    print(cache[num])

    global step

    step += 1


def printf_before(cache2, far2, num):  # print 前序

    if num == -1:
        return

    print(cache2[num])

    printf_before(cache2, far2, far2[num])

    global step

    step += 1


def do_with(cache, cache2, far, l, r, l2, r2):
    flag = 0

    t = cache[l]

    # 得到9所在的行列数x，y

    pos = getPos(t)

    x, y = divmod(pos, 3)

    # 四个方向，四种新状态

    newpos = []

    if y < 2: newpos.append(pos + 1)

    if y > 0: newpos.append(pos - 1)

    if x < 2: newpos.append(pos + 3)

    if x > 0: newpos.append(pos - 3)

    for ipos in newpos:

        tt = cache[l][:]

        tt[ipos] = cache[l][pos]

        tt[pos] = cache[l][ipos]

        # 如果新状态没在cache中就加入cache，队列尾巴r+1

        if tt not in cache:

            cache.append(tt)

            far.append(l)

            r += 1

            # 如果新状态在逆向的cache2中找到，那么新状态就是接口状态

            # 找到接口状态就可以直接打印了，返回接口状态的下标res，赋值给flag

            res = result(tt, cache2, l2, r2)

            if res != -1:
                flag = res

    l += 1

    return cache, cache2, far, l, r, l2, r2, flag


def do_with_print(before, after):
    print_after(cache, far, before)

    printf_before(cache2, far2, far2[after])  # 如果这里不用far2[flag]而用flag就重复计算中间的接口状态

    print
    step - 1  # 减去一开始的状态不计算步数

    sys.exit(0)

daiding=input("空白值：")
start = input("初始序列:").split()
end = input("目标序列:").split()

cache = [start]  # 保存正向状态

cache2 = [end]  # 保存逆向状态

far = [-1]  # 保存正向状态的left节点下标

far2 = [-1]  # 保存逆向状态的left节点下标

l = l2 = 0

r = r2 = 1

while (l != r) and (l2 != r2):  # BFS，left == right表示队列为空

    flag = -1  # 保存中间接口状态的下标

    cache, cache2, far, l, r, l2, r2, flag = do_with(cache, cache2, far, l, r, l2, r2)

    if flag:
        do_with_print(r - 1, flag)

    cache2, cache, far2, l2, r2, l, r, flag = do_with(cache2, cache, far2, l2, r2, l, r)

    if flag:
        do_with_print(flag, r - 1)
