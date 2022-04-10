from math import cos, pi
from manimlib.imports import *
#from  big_ol_pile_of_manim_imports import *

# GraphScene 绘制图像的场景基类
class LoveFunction(GraphScene):
    CONFIG = {
        "x_min" : -1,
        "x_max" : 1,
        "y_min" : -1,
        "y_max" : 1, 
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums": range(-2, 2, 1),
        "y_labeled_nums": range(-2, 1, 1),
    }
    def construct(self):
        # 添加坐标轴
        #self.setup_axes(animate=True)
        #func_graph = self.get_graph(self.func_to_graph, self.function_color)
        #func_graph2 = self.get_graph(self.func_to_graph2, self.function_color)
        #self.wait(3)

        love_function_1 = ParametricFunction(
            lambda t:np.array([
                np.sin(t) - 0.5 * np.sin(2 * t),
                np.cos(t) - 0.5 * np.cos(2 * t), 
                0,
            ]), t_min=0, t_max=2*PI, color=self.function_color
        )
        self.play(ShowCreation(love_function_1))
        self.wait(1)
        self.play(FadeOut(love_function_1))
        love_function_2 = ParametricFunction(
            lambda t:np.array([
                np.sin(t) ** 3,
                np.cos(t) - np.cos(t) **4,
                0,
            ]), t_min=-PI, t_max=PI, color=self.function_color
        )
        self.play(ShowCreation(love_function_2))
        self.wait(1)
        self.play(FadeOut(love_function_2))
    #def func_to_graph(self, x):
    #    return np.sin(x)

    #def func_to_graph2(self, x):
    #    return np.cos(x)