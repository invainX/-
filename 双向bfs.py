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


def print_after(cache, far, num):  # print ����

    if num == -1:
        return

    print_after(cache, far, far[num])

    print(cache[num])

    global step

    step += 1


def printf_before(cache2, far2, num):  # print ǰ��

    if num == -1:
        return

    print(cache2[num])

    printf_before(cache2, far2, far2[num])

    global step

    step += 1


def do_with(cache, cache2, far, l, r, l2, r2):
    flag = 0

    t = cache[l]

    # �õ�9���ڵ�������x��y

    pos = getPos(t)

    x, y = divmod(pos, 3)

    # �ĸ�����������״̬

    newpos = []

    if y < 2: newpos.append(pos + 1)

    if y > 0: newpos.append(pos - 1)

    if x < 2: newpos.append(pos + 3)

    if x > 0: newpos.append(pos - 3)

    for ipos in newpos:

        tt = cache[l][:]

        tt[ipos] = cache[l][pos]

        tt[pos] = cache[l][ipos]

        # �����״̬û��cache�оͼ���cache������β��r+1

        if tt not in cache:

            cache.append(tt)

            far.append(l)

            r += 1

            # �����״̬�������cache2���ҵ�����ô��״̬���ǽӿ�״̬

            # �ҵ��ӿ�״̬�Ϳ���ֱ�Ӵ�ӡ�ˣ����ؽӿ�״̬���±�res����ֵ��flag

            res = result(tt, cache2, l2, r2)

            if res != -1:
                flag = res

    l += 1

    return cache, cache2, far, l, r, l2, r2, flag


def do_with_print(before, after):
    print_after(cache, far, before)

    printf_before(cache2, far2, far2[after])  # ������ﲻ��far2[flag]����flag���ظ������м�Ľӿ�״̬

    print
    step - 1  # ��ȥһ��ʼ��״̬�����㲽��

    sys.exit(0)

daiding=input("�հ�ֵ��")
start = input("��ʼ����:").split()
end = input("Ŀ������:").split()

cache = [start]  # ��������״̬

cache2 = [end]  # ��������״̬

far = [-1]  # ��������״̬��left�ڵ��±�

far2 = [-1]  # ��������״̬��left�ڵ��±�

l = l2 = 0

r = r2 = 1

while (l != r) and (l2 != r2):  # BFS��left == right��ʾ����Ϊ��

    flag = -1  # �����м�ӿ�״̬���±�

    cache, cache2, far, l, r, l2, r2, flag = do_with(cache, cache2, far, l, r, l2, r2)

    if flag:
        do_with_print(r - 1, flag)

    cache2, cache, far2, l2, r2, l, r, flag = do_with(cache2, cache, far2, l2, r2, l, r)

    if flag:
        do_with_print(flag, r - 1)
