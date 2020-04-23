import threading
import tkinter as tk
from tkinter import messagebox

from formula import solve_equation_set


class Input(tk.Frame):
    def __init__(self):
        super().__init__(root)
        self.pack()
        self.entry_es = []
        self.entry_ns = []
        set_window(240, 130)
        self.interface()

    def interface(self):
        # 测试数据
        # e_variables = [tk.StringVar(value=e) for e in [767, 736, 727]]
        # n_variables = [tk.StringVar(value=n) for n in [1.11, 2.04, 1.59]]

        label_es = []
        label_ns = []
        for i in range(1, 4):
            label_es.append(tk.Label(self, text="E{}".format(i)))
            label_ns.append(tk.Label(self, text="n{}".format(i)))
            self.entry_es.append(tk.Entry(self, width=10))
            self.entry_ns.append(tk.Entry(self, width=10))
            # 测试数据
            # self.entry_es.append(tk.Entry(self, width=10, textvariable=e_variables[i-1]))
            # self.entry_ns.append(tk.Entry(self, width=10, textvariable=n_variables[i-1]))

        for i, le, ln, ee, en in zip(range(1, 4), label_es, label_ns, self.entry_es, self.entry_ns):
            le.grid(row=i, column=1, pady=2)
            ee.grid(row=i, column=2, pady=2)
            ln.grid(row=i, column=3, pady=2)
            en.grid(row=i, column=4, pady=2)

        tk.Button(self, text="计算结果", command=self._cal_result, width=26).grid(row=4, column=1, columnspan=4, pady=5)

    def _cal_result(self):
        try:
            e_list = [float(entry.get()) for entry in self.entry_es]
            n_list = [float(entry.get()) for entry in self.entry_ns]
        except ValueError:
            messagebox.showerror(title=window_title, message="亲，得输入数字呢~")
        else:
            if len(set(e_list)) < 3 or len(set(n_list)) < 3:
                messagebox.showerror(title=window_title, message="亲，E的每个取值不能重复呢, n也是哦~")
            else:
                self.destroy()
                # 进入等待界面
                label = tk.Label(root, text="正在加速计算中，别着急吗，老板~~")
                label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                t = threading.Thread(target=proxy, args=(e_list, n_list, label))
                t.start()


def proxy(e_list, n_list, label):
    results = solve_equation_set(e_list, n_list)
    # 测试数据
    # results = [
    #     (
    #         [
    #             {'a': 0.61, 'b': 1, 'w': 0.5, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.54, 'b': 1, 'w': 0.5, 'n': 2.04, 'e': 736.0},
    #             {'a': 1.09, 'b': 1, 'w': 0.5, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [850, 929, 638], 55, 123
    #     ),
    #     (
    #         [
    #             {'a': 0.11, 'b': 1, 'w': 1, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.04, 'b': 1, 'w': 1, 'n': 2.04, 'e': 736.0},
    #             {'a': 0.59, 'b': 1, 'w': 1, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [774, 782, 703], 55, 36
    #     ),
    #     (
    #         [
    #             {'a': 0.61, 'b': 1, 'w': 0.5, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.54, 'b': 1, 'w': 0.5, 'n': 2.04, 'e': 736.0},
    #             {'a': 1.09, 'b': 1, 'w': 0.5, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [850, 929, 638], 55, 123
    #     ),
    #     (
    #         [
    #             {'a': 0.11, 'b': 1, 'w': 1, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.04, 'b': 1, 'w': 1, 'n': 2.04, 'e': 736.0},
    #             {'a': 0.59, 'b': 1, 'w': 1, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [774, 782, 703], 55, 36
    #     ),
    #     (
    #         [
    #             {'a': 0.61, 'b': 1, 'w': 0.5, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.54, 'b': 1, 'w': 0.5, 'n': 2.04, 'e': 736.0},
    #             {'a': 1.09, 'b': 1, 'w': 0.5, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [850, 929, 638], 55, 123
    #     ),
    #     (
    #         [
    #             {'a': 0.11, 'b': 1, 'w': 1, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.04, 'b': 1, 'w': 1, 'n': 2.04, 'e': 736.0},
    #             {'a': 0.59, 'b': 1, 'w': 1, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [774, 782, 703], 55, 36
    #     ),
    #     (
    #         [
    #             {'a': 0.61, 'b': 1, 'w': 0.5, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.54, 'b': 1, 'w': 0.5, 'n': 2.04, 'e': 736.0},
    #             {'a': 1.09, 'b': 1, 'w': 0.5, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [850, 929, 638], 55, 123
    #     ),
    #     (
    #         [
    #             {'a': 0.11, 'b': 1, 'w': 1, 'n': 1.11, 'e': 767.0},
    #             {'a': 1.04, 'b': 1, 'w': 1, 'n': 2.04, 'e': 736.0},
    #             {'a': 0.59, 'b': 1, 'w': 1, 'n': 1.59, 'e': 727.0}
    #         ],
    #         [699, 634, 768], [774, 782, 703], 55, 36
    #     ),
    # ]
    label.destroy()
    # 进入输出界面
    Output(results)


def set_window(width, height):
    # 设置窗口居中
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    window_width, window_height = width, height
    x, y = int((screen_width - window_width) / 2), int((screen_height - window_height) / 2)
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    # 设置窗口大小固定
    root.resizable(0, 0)


class Output(tk.Frame):
    def __init__(self, results):
        super().__init__(root)
        self.pack()
        self.results = results
        set_window(1020, 480)

        # 添加画布及滚动条，并在画布上添加框
        self.canvas = tk.Canvas(self, width=1000, height=480)
        self.frame = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        # 配置滚动条
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack()
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", self.on_frame_configure)

        self.interface()

    def interface(self):
        # 重新整理计算结果数据结构，以方便显示
        self.refactor_results()

        # 第一行
        tk.Button(
            self.frame, text="导出计算结果到Excel文件", command=None,
            width=140, relief=tk.GROOVE, overrelief=tk.SUNKEN,
        ).grid(row=0, column=0, columnspan=10, pady=5)

        # 第二行
        table_heads = ["Case no.", "E", "n", "w", "a", "b", "En1&Eg1", "En2&Eg2", "En3&Eg3", "Standard deviation"]
        for i, table_head in enumerate(table_heads):
            tk.Label(self.frame, text=table_head).grid(row=1, column=i, pady=5)

        # 第三行
        canvas = tk.Canvas(self.frame, width=1000, height=5)
        canvas.create_line((0, 0), (1000, 0), width=5)
        canvas.grid(row=2, column=0, columnspan=10)

        # 计算结果
        for result in self.results:
            row = result[0] + 2
            tk.Label(self.frame, text=result[0]).grid(row=row, column=0, pady=5)
            for i, args in enumerate(result[1:]):
                self.get_node(args).grid(row=row, column=i+1, pady=5)

    def get_node(self, value_list):
        """
        创建计算结果中列表数据的单元格
        """
        node = tk.Frame(self.frame)
        for v in value_list:
            tk.Label(node, text=v).pack()
        return node

    def refactor_results(self):
        """
        [(
            no,
            [e1, e2, e3],
            [n1, n2, n3],
            [w, w, w],
            [a1, a2, a3],
            [b1, b2, b3],
            [en1, eg1],
            [en2, eg2],
            [en3, eg3],
            [std_en, std_eg],
        )]
        """
        results = []
        for i, result in enumerate(self.results):
            e_list, n_list, w_list, a_list, b_list = [], [], [], [], []
            for abwne in result[0]:
                for arg in abwne.keys():
                    eval("{arg}_list.append(abwne['{arg}'])".format(arg=arg))

            sol1 = ["En={}".format(result[1][0]), "Eg={}".format(result[2][0])]
            sol2 = ["En={}".format(result[1][1]), "Eg={}".format(result[2][1])]
            sol3 = ["En={}".format(result[1][2]), "Eg={}".format(result[2][2])]
            std = ["Sn={}".format(result[3]), "Sg={}".format(result[4])]

            results.append((i + 1, e_list, n_list, w_list, a_list, b_list, sol1, sol2, sol3, std))

        self.results = results

    def on_frame_configure(self, event):
        """
        Reset the scroll region to encompass the inner frame
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


window_title = "公式"
root = tk.Tk(className=window_title)
# 进入输入界面
Input()
root.mainloop()
