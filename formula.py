from itertools import combinations

from numpy import std
from sympy import Symbol, solve


def solve_equation_set(e_list, n_list):
    # b的可能取值
    b_list = [1, 2, 3]
    # w的可能取值
    w_list = [0.5, 1]

    # 三个表达式中b的取值 [(b1, b2, b3)]
    com_b = []
    for b1 in b_list:
        for b2 in b_list:
            for b3 in b_list:
                com_b.append((b1, b2, b3))

    # 三个表达式中b, w的取值 [((b1, b2, b3), w)]
    com_b_w = []
    for b_list in com_b:
        for w in w_list:
            com_b_w.append((b_list, w))

    # 三个表达式中a, b, w, n, e的取值
    # [[{a:a1, b:b1, w:w, n:n1, e:e1}, {a:a2, b:b2, w:w, n:n2, e:e2}, {a:a3, b:b3, w:w, n:n3, e:e3}]]
    com_abwne = []
    for b_w in com_b_w:
        bs = b_w[0]
        w = b_w[1]
        formula_arg = []
        for b, n, e in zip(bs, n_list, e_list):
            a = round(n - b * w, 2)
            if a >= 0:
                arg_dict = dict(a=a, b=b, w=w, n=n, e=e)
                formula_arg.append(arg_dict)
            else:
                break

        if len(formula_arg) == 3:
            com_abwne.append(formula_arg)

    '''
    解二元一次方程组
    exp1, exp2 -> en1, eg1
    exp1, exp3 -> en2, eg2
    exp2, exp3 -> en3, eg3
    '''
    # 定义二元一次方程组变量
    en = Symbol('en')
    eg = Symbol('eg')

    '''
    [(
        [
            {a:a1, b:b1, w:w, n:n1, e:e1},
            {a:a2, b:b2, w:w, n:n2, e:e2},
            {a:a3, b:b3, w:w, n:n3, e:e3},
        ],
        [en1, en2, en3],
        [eg1, eg2, eg3],
        std_en,
        std_eg,
    )]
    '''
    results = []
    # 三个表达式
    for abwne in com_abwne:
        en_list = []
        eg_list = []
        # 表达式两两组合，共三个组合
        exp_coms = list(combinations(abwne, 2))
        # 两个表达式
        for exp_com in exp_coms:
            exp_first_arg = exp_com[0]
            exp_second_arg = exp_com[1]
            exp_first = exp_first_arg['a'] * en + exp_first_arg['b'] * exp_first_arg['w'] * eg - exp_first_arg['e'] * exp_first_arg['n']
            exp_second = exp_second_arg['a'] * en + exp_second_arg['b'] * exp_second_arg['w'] * eg - exp_second_arg['e'] * exp_second_arg['n']
            solution = solve([exp_first, exp_second], [en, eg])
            # 如果解为空列表，则该组结果无效
            if solution == list():
                break

            # 四舍六入五平分
            en_list.append(round(float(solution[en])))
            eg_list.append(round(float(solution[eg])))
        else:
            # 求标准差
            std_en = round(float(std(en_list)))
            std_eg = round(float(std(eg_list)))

            results.append((abwne, en_list, eg_list, std_en, std_eg))

    return results


if __name__ == '__main__':
    # r = solve_equation_set([767, 736, 727], [1.11, 2.04, 1.59])
    r = solve_equation_set([110, 120, 130], [2, 3, 4])
    print(r)
