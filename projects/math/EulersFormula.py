from manim import *
from manimlib.imports import *

def EulerFormula(Scene):
    def construct(self):
        title = TextMobject("欧拉公式")
        euler_formula_1 = TxtMobject("e^{i\\pi} + 1  = 0")
        euler_formula_2 = TxtMobject("e^{ix} = cosx + isinx") # 将x取\pi就能得到公式1
        e_formula = TxtMobject("e = \\lim_{n\\rightarrow \\infty } \\left ( 1 + \\frac{1}{n} \\right )^{n}")

        txt1 = TextMobject("e, i, \\pi, 0, 1 是初等数学中最重要的五个数字")
        num_0  = TextMobject("0 是 \\mathbb{Z}上的加法单元")
        num_1 = TextMobject("1 是\\mathbb{Z}上的乘法单元")
        num_i = TextMobject("")
        # 自然对数的底e和圆周率，两个超越数
        e_num = TextMobject("e 是自然对数函数的底数")
        pi_num = TextMobject("\pi作为圆周率，是数学中最重要的无理数")

    def eulerGraphics(self):
        ax = Axes(
            x_range = [-1, 1],
            y_range = [-1, 1],
            tips = False,
        )
        curve =ax.get_graph(lambda x: np.sqrt(1 - x^{2}))
        line1 = ax.get_vertical_line(ax.input_to_graph_point(0.5, curve))
        self.add(ax, curve, line1)

