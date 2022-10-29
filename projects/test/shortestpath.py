from ast import Num
from cgitb import text
from cmath import inf
from collections import deque
from ctypes import alignment
from ctypes.wintypes import DWORD
from dis import dis
from multiprocessing import heap
import queue
from re import I
from tkinter import font
from tokenize import Number
from tracemalloc import start
from turtle import left
from colorama import init
from cv2 import circle, line, log, sepFilter2D
from matplotlib.pyplot import arrow, axes
from pandas import Index
from manim import *
from manimlib.imports import *
import random
import numpy as np


def my_logo():
    logo_text = TextMobject("陶将",  font="lishu", color=RED, weight="bold").scale(0.5)
    height = logo_text.get_height() + 2 * 0.1
    width = logo_text.get_width() + 2 * 0.15
    logo_ellipse = Ellipse(
        width=width,           
        height=height, stroke_width=0.5
    )
    logo_ellipse.set_fill(color=PURPLE,opacity=0.3)
    logo_ellipse.set_stroke(color=GRAY)
    logo_text.move_to(logo_ellipse.get_center())
    logo = VGroup(logo_ellipse, logo_text)
    logo.shift(np.array((6.5, 3.5, 0.)))
    return logo


class Graph:
    def __init__(self, datas, graph_datas, positions, radius=0.3, color=WHITE, buff=0.7, txt_color=BLUE):
        self.elements = self.create_element(datas, positions, radius)
        self.line_groups = self.build_graph(graph_datas, color, buff, txt_color)

    def create_element(self, datas, position, radius):
        elements = VGroup()
        for i, val in enumerate(datas):
            element = VGroup()
            circle = Circle(radius=radius, stroke_color=BLUE)
            circle.shift(position[i])
            text = TextMobject(val).move_to(circle.get_center())
            element.add(circle, text)
            elements.add(element)
        return elements

    def build_graph(self, graph_datas, color, buff, txt_color):
        #
        lines_groups = VGroup()
        length = len(graph_datas)
        for i in range(length):
            element_1 = self.elements[ord(graph_datas[i][0]) - ord('A')]
            element_2 = self.elements[ord(graph_datas[i][1]) - ord('A')]
            line = Arrow(start=element_1.get_center(), end=element_2.get_center(),color=color, stroke_width=2, tip_length=0.1, tip_angle=PI/3, buff=buff)
            text_mob = TextMobject(str(graph_datas[i][2]), color=txt_color).scale(0.5).move_to(line.get_center())
            lines_groups.add(VGroup(line, text_mob))
        return lines_groups


class Arrays:
    def __init__(self, arrays_data, start_positions, character='A'):
        self.elements, self.Indexs = self.get_elements(arrays_data, start_positions, character)

    def get_elements(self, arrays_data, start_positions, character):
        rows, cols = arrays_data.shape
        x = start_positions[0]
        y = start_positions[1]
        groups = VGroup()
        Indexs = VGroup()
        for i in range(rows):
            col_groups = VGroup()
            new_x = x
            for j in range(cols):
                #print(type(arrays_data[i, j]), arrays_data[i, j])
                if arrays_data[i, j] < float(inf):
                    txt = str(int(arrays_data[i, j]))
                    if arrays_data[i, j] == 0:
                        color = RED
                    else:
                        color = PURPLE
                else:
                    txt = str(arrays_data[i, j])
                    color = TEAL
                value = TextMobject(txt, color=color).scale(0.6).move_to([new_x, y, 0])
                new_x += 0.5
                col_groups.add(value)
            if i == 0:
                for k in range(cols):
                    index = TextMobject(chr(ord(character)+ k)).scale(0.3).next_to(col_groups[k], 0.5 * UP)
                    Indexs.add(index)
            if rows > 1:
                index = Integer(i).scale(0.3).next_to(col_groups[0], 0.5 * LEFT)
                Indexs.add(index)
            y -= 0.5
            groups.add(col_groups)
        return groups, Indexs


# python -m manim F:\manim\\projects\\test\\shortestpath.py ShortPath -p --media_dir F:\\manim_vedio_dirs
class ShortPath(Scene):
    def construct(self):
        # logo
        logo = my_logo()
        self.play(Write(logo))
        #########
        title = TextMobject("最短路径算法", color=RED)
        self.play(Write(title))
        self.wait(2)
        title.to_edge(UP)
        self.play(Write(title))
        short_path_description = TextMobject("最短路径问题是图论研究中的一个经典算法，旨在寻找图中两个节点之间的最短路径.", 
        "最短路径的定义为：从某个节点出发，沿着图的边到达另一顶点所经过的路径中，各边上的权值之和最小的一条路径.\\\\",
        "解决最短路径有四个算法, 分别是Dijkstra算法, Bellman-Ford算法, Floyd算法和SPFA算法.", alignment="\\raggedright", 
        tex_to_color_map={"Dijkstra算法": RED, "Bellman-Ford算法": GOLD, "Floyd算法": BLUE, "SPFA算法": PURPLE}).scale(0.5)
        short_path_description.shift(2 * UP)
        self.play(Write(short_path_description), runtime=4)
        self.wait(4)
        #
        self.short_path_framework()
        self.play(Uncreate(short_path_description))

    def get_text_groups(self, text, t_color=WHITE, is_rec=True, r_color=TEAL):
        groups = VGroup()
        text_mob = TextMobject(text, color=t_color, alignment="\\raggedright").scale(0.5)
        groups.add(text_mob)
        if is_rec:
            rect = SurroundingRectangle(text_mob, color=r_color)
            groups.add(rect)
        return groups

    def get_lines(self, start, end, buff):
        line = Line(start=start, end=end, color=WHITE, buff=buff)
        return line

    def short_path_framework(self):
        short_path_text = self.get_text_groups("最短路径算法").move_to([-5, -2, 0])
        single_path_text = self.get_text_groups("单源最短路算法").move_to([-2.5, -0.5, 0])
        single_path_description = TextMobject("求一个点到其他点的\\\\最短路径").scale(0.3).next_to(single_path_text, 0.7*DOWN)
        double_path_text = self.get_text_groups("多源最短路算法").move_to([-2.5, -3, 0])
        double_path_description = TextMobject("求任意两个点的最短路径").scale(0.3).next_to(double_path_text, 0.5 * DOWN)
        first_line = self.get_lines(start=short_path_text.get_center(), end=single_path_text.get_center(), buff=0.6)
        second_line = self.get_lines(start=short_path_text.get_center(), end=double_path_text.get_center(), buff=0.7)
        first_groups = VGroup(short_path_text, first_line, single_path_text, second_line, double_path_text)
        self.play(Write(first_groups))
        self.play(Write(single_path_description))
        self.play(Write(double_path_description))
        #
        position = self.get_text_groups("所有边权都是正数").move_to([0, 0.5, 0])
        third_line = self.get_lines(single_path_text.get_center(), position.get_center(), buff=0.7)
        vina_dijkstra = self.get_text_groups("朴素Dijstra          $O(n^{2})$    稠密图  \\\\ 堆优化版的Dijstra     $O(mlogn)$  稀疏图", t_color=PURPLE, is_rec=False).next_to(position, RIGHT)
        second_group = VGroup(position, third_line, vina_dijkstra)
        self.play(Write(second_group))
        #
        exist_negative = self.get_text_groups("存在负权边").move_to([0, -1.5, 0])
        fourth_line = self.get_lines(single_path_text.get_center(), exist_negative.get_center(), buff=0.7)
        bellman_ford = self.get_text_groups("Bellman-Ford   $O(mn)$  有边数限制", t_color=BLUE, is_rec=False).next_to(exist_negative, 0.5 * UP + 2 * RIGHT)
        spfa = self.get_text_groups("SPFA    $O(m)$   无负环", t_color=GREEN, is_rec=False).next_to(exist_negative, 0.5 * DOWN + 2 * RIGHT)
        brace = Brace(VGroup(bellman_ford, spfa), direction=LEFT,  color=TEAL).scale(0.5)
        third_group = VGroup(fourth_line, exist_negative, bellman_ford, spfa, brace)
        self.play(Write(third_group))
        #
        ford = self.get_text_groups("Floyd     $O(n^{3})   无负环$", t_color=YELLOW, is_rec=False).next_to(double_path_text, RIGHT)
        font_text = self.get_text_groups("m: 图中边的数量 \\\\ n: 图中顶点的数量", t_color=YELLOW, r_color=RED_A).move_to([5, -3, 0])
        self.play(Write(VGroup(ford, font_text)))
        self.wait(6)
        self.play(Uncreate(VGroup(first_groups, single_path_description, double_path_description, second_group, third_group, ford, font_text)))

# python -m manim F:\manim\\projects\\test\\shortestpath.py Floyd -p --media_dir F:\\manim_vedio_dirs
# Floyd 算法
class Floyd(Scene):
    def construct(self):
        # logo
        logo = my_logo()
        self.play(Write(logo))
        ##############################
        title = TextMobject("Floyd算法", color=RED)
        self.play(Write(title))
        self.wait(2)
        title.to_edge(UP)
        self.play(Write(title))
        self.description()
        self.relaxtion()
        #self.floyd_show()

    def description(self):
        #
        floyd_desctiption = TextMobject("弗洛伊德(Floyd)求每一对顶点之间的最短路径. 它的基本思想是: 假设求从$u_{i}$到$u_{j}$的最短路径.", 
        "如果从$u_{i}$到$u_{j}$存在一条长度为$w_{i,j}$的边, 那么该路径$(u_{i}, u_{j})$不一定是最短路径,需要$n$次试探.",
        "首先考虑路径$(u_{i}, u_{0}, u_{j})$是否存在(即是否同时存在边$e_{i,0}$和边$e_{0,j}$)，如果存在, 则比较$(u_{i}, u_{j})$和$(u_{i}, u_{0}, u_{j})$",
        "的路径长度, 取长度最短者为从$u_{i}$到$u_{j}$的中间顶点的序号不大于0的最短路径. 假设再增加一个顶点$u_{1}$, 也就是说，如果$(u_{i}, \cdots, u_{1})$和",
        "$(u_{1}, \cdots, u_{j})$分别是当前找到的中间顶点的序号不大于0的最短路径,那么$(u_{i}, \cdots, u_{1}, \cdots, u_{j})$就有可能是",
        "从$u_{i}$到$u_{j}$的中间顶点的序号不大于1的最短路径. 将它与从$u_{i}$到$u_{j}$的中间顶点的序号不大于$0$的最短路径相比较,去长度最短者为",
        "从$u_{i}$到$u_{j}$的中间顶点的序号不大于1的最短路径.以此类推,在一般情况下,若$(u_{i}, \cdots, u_{k})$和",
        "$(u_{k}, \cdots, u_{j})$分别是当前找到的中间顶点的序号不大于$k-1$的最短路径, 则将$(u_{i}, \cdots, u_{k}, \cdots, u_{j})$和已经得到的",
        "从$u_{i}$到$u_{j}$的中间顶点的序号不大于$k-1$的最短路径相比较,取最短者为$u_{i}$到$u_{j}$的中间顶点的序号不大于$k$的最短路径.",
        "经过$n$次比较之后, 最后求得的必是从$u_{i}$到$u_{j}$的最短路径. 依次方法, 可以同时求得各对顶点间的最短路径.", alignment="\\raggedright").scale(0.5)
        self.play(Write(floyd_desctiption), runtime=20)
        self.wait(40)
        self.play(Uncreate(floyd_desctiption))

    def relaxtion(self):
        relaxtion_txt = TextMobject("假设有三个顶点$A,B,C$,它们有如下图所示的连接关系;W[A][B]表示顶点A和顶点B之间的权重.",
        "如果$W[A][B] > (W[A][C] + W[C][B])$, 就更新W[A][B]=W[A][C] + W[C][B]. 这被称为AB边的一次\"松弛\"操作.", alignment="\\raggedright").scale(0.5)
        relaxtion_txt.shift(2 * UP) 
        self.play(Write(relaxtion_txt), runtime=2)
        self.wait(4)
        datas = ['A', 'B', 'C']
        positions = [[-2,-1,0], [2, -1, 0], [0, 0.5, 0]]
        graph_datas = [['A','B','6'], ['A','C','2'], ['C','B','3']]
        graph = Graph(datas, graph_datas, positions, buff=0.4)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        self.wait(2)
        acb_text = TextMobject("(W[A][C] + W[C][B] = 2 + 3) < (W[A][B] = 6)").scale(0.5).next_to([-2,-2,0])
        self.play(Write(acb_text))
        self.wait(2)
        self.play(ShowCreation(graph.line_groups[1].set_color(YELLOW)), ShowCreation(graph.line_groups[2].set_color(YELLOW)))
        ab_text = TextMobject("W[A][B] = W[A][C] + W[C][B] = 5").scale(0.5).next_to([-2, -2, 0])
        self.play(ReplacementTransform(acb_text, ab_text))
        self.wait(4)
        self.play(Uncreate(VGroup(ab_text, graph.elements, graph.line_groups, relaxtion_txt)))
        floyd_code = Code(file_name="F:\manim\\projects\\test\\codes\\floyd.cpp", insert_line_no=False, style=code_styles_list[11]).scale(0.7).move_to(ORIGIN)
        self.play(Write(floyd_code), run_time=5)
        complexity_text = TextMobject("Floyd算法的时间复杂度为$O(n^{3})$").scale(0.7).next_to(floyd_code, DOWN)
        self.play(Write(complexity_text))
        self.wait(5)

    def floyd_show(self):
        #
        datas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        positions = [[-3,2,0], [-5, 1, 0], [-3, 0, 0], [-1, 1, 0], [-5, -1, 0], [-1, -1, 0], [-3, -2, 0]]
        graph_datas = [['A','B','4'], ['A','C','6'], ['A','D','6'], ['B','C','1'], ['B','E','7'], ['C','E','6'],
        ['C','F','4'], ['D','C','2'], ['D','F','5'], ['E','G','6'], ['F','E','1'], ['F','G','8']]
        graph = Graph(datas, graph_datas, positions, buff=0.4)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        self.wait(2)
        #
        length = len(datas)
        max_value = float('inf')
        # arrays
        arrays = np.ones((length, length)) * max_value
        for i in range(length):
            arrays[i, i] = 0
        for index in range(len(graph_datas)):
            x = ord(graph_datas[index][0]) - ord('A')
            y = ord(graph_datas[index][1]) - ord('A')
            arrays[x, y] = graph_datas[index][2]
        #print(arrays)
        #
        arrays_mob =  Arrays(arrays, start_positions=[2, 1.5], character='A')
        self.play(ShowCreation(VGroup(arrays_mob.elements, arrays_mob.Indexs)))
        arrow = Arrow(start=[-0.5, 0, 0], end=[1.5, 0, 0], color=MAROON, stroke_width=2, tip_width=5, tip_length = 0.3, tip_angle= PI)
        arrow_text = TextMobject("数组化", color=YELLOW).scale(0.5).next_to(arrow, 0.7*UP)
        self.play(ShowCreation(VGroup(arrow, arrow_text)))
        self.wait(2)
        length = len(datas)
        def write_txt(i):
            tmp_text = TextMobject("以顶点"+chr(ord('A')+ int(i))+"为中介更新矩阵").scale(0.6).move_to([-3, -3, 0])
            return tmp_text
        def description_relation(i, j, k):
            tmp = TextMobject("顶点"+chr(ord('A')+int(i))+"到顶点"+chr(ord('A')+int(k))+"之间的距离\\\\与顶点" + 
            chr(ord('A')+int(k)) +"到顶点"+ chr(ord('A')+int(j))+"之间的距离之和\\\\小于顶点"+ 
            chr(ord('A')+int(i)) +"到顶点"+ chr(ord('A')+int(j))+"之间的距离,\\\\执行一次松弛操作.", alignment="\\raggedright").scale(0.5).move_to([3, -2.5,0])
            return tmp
        # def each_edge(i, j, value):
        #     tmp = TextMobject("顶点"+chr(ord('A')+int(i))+"到顶点"+chr(ord('A')+int(j))+"\\\\之间的距离为"+str(value), color=MAROON).scale(0.4).move_to([6.5, 1, 0])
        #     return tmp
        for k in range(length):
            tmp_text = always_redraw(lambda : write_txt(k))
            self.play(ShowCreation(tmp_text))
            self.wait(1)
            for i in range(length):
                for j in range(length):
                    if arrays[i, j] > arrays[i, k] + arrays[k, j]:
                        # i, j
                        one_relation = always_redraw(lambda : description_relation(i, j, k))
                        self.play(Write(one_relation))
                        # i,k and k,j
                        self.play(Indicate(arrays_mob.elements[i][k], scale_factor=1.5), 
                                Indicate(arrays_mob.elements[k][j],  scale_factor=1.5))
                        # i,j 
                        self.play(Indicate(arrays_mob.elements[i][j], scale_factor=1.5))
                        #i,k
                        # ik_edge = each_edge(i, k, arrays[i, k])
                        # self.play(Write(ik_edge), Indicate(arrays_mob.elements[i][k]))
                        # self.play(Uncreate(ik_edge))
                        # #k,j
                        # kj_edge = each_edge(k, j, arrays[k, j])
                        # self.play(Write(kj_edge), Indicate(arrays_mob.elements[k][j]))
                        # self.play(Uncreate(kj_edge))
                        # #i,j
                        # ij_edge = each_edge(i, j, arrays[i, j])
                        # self.play(Write(ij_edge), Indicate(arrays_mob.elements[i][j]))
                        # self.play(Uncreate(ij_edge))
                        #
                        arrays[i, j] = arrays[i, k] + arrays[k, j]
                        tmp = TextMobject(str(int(arrays[i, j])), color=YELLOW).scale(0.6).move_to(arrays_mob.elements[i][j].get_center())
                        self.play(ReplacementTransform(arrays_mob.elements[i][j], tmp))
                        arrays_mob.elements[i].submobjects[j] = tmp
                        self.wait(2)
                        self.play(Uncreate(one_relation))
            self.play(Uncreate(tmp_text))

# python -m manim F:\manim\\projects\\test\\shortestpath.py Dijkstra -p --media_dir F:\\manim_vedio_dirs
# Dijkstra算法
class Dijkstra(Scene):
    def construct(self):
         # logo
        logo = my_logo()
        self.play(Write(logo))
        #title
        title = TextMobject("Dijkstra算法",color=RED, fontsize=32).to_edge(UP)
        self.play(Write(title))
        #self.description()
        #
        self.Dijkstra_show()
        #
        #self.heap_dijkstra()
        ##############################
    def description(self):
        #
        text = TextMobject("迪杰斯特拉算法(Dijkstra)是由荷兰计算机科学家狄克斯特拉于1959年提出的, 因此又叫狄克斯特拉算法.", 
        "迪杰斯特拉算法使用类似于广度优先搜索的方法解决图的单源最短路问题.", alignment="\\raggedright").scale(0.5).shift(2 * UP)
        self.play(ShowCreation(text), runtime=2)
        self.wait(3)
        dijstra_description = TextMobject("设一个有向图$G=(V,E,W)$. 其中图中的每条边$e_{i,j}=(v_{i}, v_{j})$的权值为一个非负的实数$w_{i,j}$,",
        "此权值表示从顶点$v_{i}$到顶点$v_{j}$的距离。设一个单源点$s \in V$.", "任务: 求出从源点$s$出发, 到$V - {s}$中所有节点的最短路径.").scale(0.5).shift(2*UP)
        self.play(ReplacementTransform(text, dijstra_description))
        self.wait(2)
        dijstra_img = ImageMobject(filename_or_array="F:\manim\\projects\\test\\images\\Dijkstra.png").scale(1.8).shift(4*LEFT + 0.8* DOWN)
        self.play(ShowCreation(dijstra_img), runtime=2)
        self.wait(2)
        #
        steps = BulletedList("第一步: $S$为已找到从源点$s$出发的最短路径的终点的集合,它的初始状态为空.将初始源点$s$放到集合S中",
        "第二步: 初始化dist数组, dist数组记录着从源点s到图中其他顶点可能达到的最短路径长度的初值.无自环的源点$s$到自己的最短路径为0,如果从源点$s$到图中其他顶点$v$有边, 初始长度为从源点$s$到顶点$v$的初始最短路径为边的权值,否则记为无穷大inf",
        "第三步: 从$V-S$集合中选取顶点$v_{i}$,顶点$v_{i}$就是当前求得的一条从源点s出发的最短路径(dist值最小)的终点,将顶点$v_{i}$加入S中,然后修改从源点$s$出发到集合V-S上任一顶点$v_{j}$可达的最短路路径.",
        "重复第三步$n-1$次,就可以求得从源点$s$到图中其他顶点的最短路径长度.").scale(0.45).shift(3*RIGHT+0.8*DOWN)
        self.play(ShowCreation(steps), runtime=6)
        self.wait(20)
        self.remove(dijstra_img)
        self.play(Uncreate(VGroup(steps, dijstra_description)))
        dijkstra_code = Code(file_name="F:\manim\\projects\\test\\codes\\Dijkstra.cpp", insert_line_no=False, style=code_styles_list[11]).scale(0.5).move_to([0,-0.3,0])
        self.play(Write(dijkstra_code), run_time=5)
        self.wait(10)



    def Dijkstra_show(self):
        datas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        positions = [[-3,2,0], [-5, 1, 0], [-3, 0, 0], [-1, 1, 0], [-5, -1, 0], [-1, -1, 0], [-3, -2, 0]]
        graph_datas = [['A','B','4'], ['A','C','6'], ['A','D','6'], ['B','C','1'], ['B','E','7'], ['C','E','6'],
        ['C','F','4'], ['D','C','2'], ['D','F','5'], ['E','G','6'], ['F','E','1'], ['F','G','8']]
        graph = Graph(datas, graph_datas, positions, buff=0.4)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        self.wait(2)
        #
        length = len(datas)
        max_value = float('inf')
        # arrays
        arrays = np.ones((length, length)) * max_value
        for i in range(length):
            arrays[i, i] = 0
        for index in range(len(graph_datas)):
            x = ord(graph_datas[index][0]) - ord('A')
            y = ord(graph_datas[index][1]) - ord('A')
            arrays[x, y] = graph_datas[index][2]
        #print(arrays)
        #
        arrays_mob =  Arrays(arrays, start_positions=[2, 1.5], character='A')
        arrow = Arrow(start=[-0.5, 0, 0], end=[1.5, 0, 0], color=MAROON, stroke_width=2, tip_width=5, tip_length = 0.3, tip_angle= PI)
        arrow_text = TextMobject("数组化", color=YELLOW).scale(0.5).next_to(arrow, 0.7*UP)
        self.play(ShowCreation(VGroup(arrow, arrow_text)))
        self.play(ShowCreation(VGroup(arrays_mob.elements, arrays_mob.Indexs)))
        self.wait(2)
        # dist
        dist = arrays[0]
        #print('ori dist: ', dist)
        dist_mob = arrays_mob.elements[0].copy().move_to([0, -3, 0]).scale(1.5)
        dist_indexs = arrays_mob.Indexs[0: length].copy().next_to(dist_mob, 0.5 * UP).scale(1.5)
        # 
        dist_txt = TextMobject('顶点A到各顶点的距离').scale(0.5).next_to(dist_mob, 1.5 * UP)
        self.play(ShowCreation(VGroup(dist_txt, dist_mob, dist_indexs)))
        ########
        visited = np.zeros(length)
        visited[0] = 1
        self.play(ShowCreation(graph.elements[0][0].set_fill(GOLD, opacity=0.7)))
        paths = np.ones(length) * (-1) # 记录路径，初始化
        for i in range(1, length):
            # 找到最近的顶点
            u = 0
            min_tmp = max_value
            for j in range(length):
                if visited[j] == 0 and dist[j] < min_tmp:
                    min_tmp = dist[j]
                    u = j
            #print('min_tmp=', min_tmp, ', min_inex=', u)
            visited[u] = 1
            self.play(ShowCreation(dist_mob[u].set_color(RED)))
            self.play(ShowCreation(graph.elements[u][0].set_fill(GOLD, opacity=0.7)))
            self.wait(1)
            #print(u)
            for v in range(length):
                if arrays[u, v] < max_value and dist[v] > dist[u] + arrays[u, v]:
                    dist[v] = dist[u] + arrays[u, v]
                    paths[v] = u # 从u到v最短路的路径
                    #
                    new_dist  = TextMobject(str(int(dist[v])), color=YELLOW).scale(0.9).move_to(dist_mob[v].get_center())
                    self.play((ReplacementTransform(dist_mob[v], new_dist)))
                    dist_mob.submobjects[v] = new_dist
                    self.wait(2)
            # print(paths)
            #print(dist)
        #在graph_datas中寻找最短路线
        rounds = ['A']
        p = 1
        rounds.append(chr(ord('A')+ int(p)))
        while(p > 0  and p < (length - 1)):
            for i in range(length):
                if paths[i] == p:
                    p = i
                    print(chr(ord('A')+ int(i)))
                    rounds.append(chr(ord('A')+ int(i)))
                    break
        print(rounds) 
        rounds_txt = ""
        for i in range(len(rounds)):
            if i == len(rounds) - 1:
                rounds_txt += rounds[i]
            else:
                rounds_txt += rounds[i] + '--->'
        rounds_mob = TextMobject('顶点A到顶点G的最短路径为: '+rounds_txt, color=RED, alignment="\\raggedright").scale(0.9).next_to(dist_mob, DOWN)
        self.play(Write(rounds_mob), runtime=2)
        self.wait(2)
        for p  in range(1, len(rounds)):
            pre_node = rounds[p-1]
            current_node = rounds[p] 
            for i in range(len(graph_datas)):
                if pre_node == graph_datas[i][0] and current_node == graph_datas[i][1]:
                    self.play(ShowCreation(graph.line_groups[i][0].set_color(YELLOW)))
                    self.play(ShowCreation(graph.line_groups[i][1].set_color(RED)))
                    break
        self.wait(5)

    def heap_dijkstra(self):
        complexity_text = TextMobject("假设有向图$G=(V,E,W)$, 顶点个数为$n=|V|$,边数为$m=|E|$, Dijkstra算法的时间复杂度为$O(n^{2})$.", 
        "如果使用数据机构堆优化Dijkstra算法, 需要遍历$m$条边, 修改堆的时间复杂度为$O(logn)$,那么堆优化的Dijkstra算法时间复杂度为$O(mlogn)$", 
        "图中边的最大数量为$n(n-1)$, 如果稠密图使用堆优化版的Dijkstra算法,时间复杂度为$O(n^{2}logn)$,朴素版Dijkstra算法更适合稠密图", 
        "然而对于稀疏图,变数$m$与顶点数$n$很接近,堆优化的Dijkstra算法时间复杂度接近于$O(nlogn)$.显然堆优化的Dijkstra算法更适合稀疏图", 
        alignment="\\raggedright", tex_to_color_map={"稠密图": ORANGE, "稀疏图": MAROON, "堆": YELLOW}).scale(0.5).shift(1.5 * UP)
        self.play(Write(complexity_text), runtime=4)
        self.wait(6)
        heap_dijkstra = TextMobject("Dijkstra算法需要优化的是数值的插入(更新)和取出最小值两个操作,把每个顶点当前的最短距离用堆来维护，在更新最短距离时，",
        "把对应的元素往根的方向移动以满足堆的性质。而每次从堆中取出的最小值就是下一次要用的顶点.", alignment="\\raggedright").scale(0.5).next_to(complexity_text, DOWN)
        self.play(Write(heap_dijkstra), runtime=2)
        self.wait(5)
        self.play(Uncreate(VGroup(complexity_text, heap_dijkstra)))
        heap_dijkstra_code = Code(file_name="F:\manim\\projects\\test\\codes\\heap_dijkstra.cpp", insert_line_no=False, style=code_styles_list[11]).scale(0.7).move_to(ORIGIN)
        self.play(Write(heap_dijkstra_code), run_time=5)
        self.wait(5)


# python -m manim F:\manim\\projects\\test\\shortestpath.py Bellman_Ford -p --media_dir F:\\manim_vedio_dirs
class Bellman_Ford(Scene):
    def construct(self):
         # logo
        logo = my_logo()
        self.play(Write(logo))
        #
        title = TextMobject("Bellman-Ford算法",color=RED, fontsize=32).to_edge(UP)
        self.play(Write(title))
        self.why_can_not_negative_weight()
        #
        #self.bellman_ford()
        # title = TextMobject("SPFA算法",color=RED, fontsize=32).to_edge(UP)
        # self.play(Write(title))
        # self.SPFA()
        #self.summary()

    def why_can_not_negative_weight(self):
        description = TextMobject("Dijkstra算法基于贪心思想,每次都找一个距离源点最近的点,然后将该距离作为该点到源点的最短路径."
        "如果存在负权边, 那么就会导致得到的最短路径不一定是最短路径,下面以一个示例演示Dijkstra算法在处理负权边时出现的错误.", 
        alignment="\\raggedright", tex_to_color_map={"贪心": YELLOW}).scale(0.5).shift(2* UP)
        self.play(ShowCreation(description), runtime=2)
        self.wait(2)
        datas = ['A', 'B', 'C', 'D', 'E']
        positions = [[-5,-1,0], [-3, 0, 0], [-3, -2, 0], [-1, 0, 0], [-1, -2, 0]]
        graph_datas = [['A','B','3'], ['A','C','5'], ['B','D','1'], ['E','C','2'], ['D','E','3'], ['C','B','-5']]
        graph = Graph(datas, graph_datas, positions, buff=0.4, txt_color=YELLOW)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        self.wait(2)
        #
        length = len(datas)
        max_value = float('inf')
        # arrays
        arrays = np.ones((length, length)) * max_value
        for i in range(length):
            arrays[i, i] = 0
        for index in range(len(graph_datas)):
            x = ord(graph_datas[index][0]) - ord('A')
            y = ord(graph_datas[index][1]) - ord('A')
            arrays[x, y] = graph_datas[index][2]
        #print(arrays)
        # dist
        dist = arrays[0]
        #print('ori dist: ', dist)
        x, y = 1, -1
        dist_mob = VGroup()
        Indexs = VGroup()
        for i in range(len(dist)):
            if dist[i] < float(inf):
                txt = str(int(dist[i]))
                if dist[i] == 0:
                    color = RED
                else:
                    color = PURPLE
            else:
                txt = str(dist[i])
                color = TEAL
            value = TextMobject(txt, color=color).scale(0.8).move_to([x, y, 0])
            index = TextMobject(datas[i]).scale(0.5).next_to(value, 0.5 * UP)
            x += 0.8
            dist_mob.add(value)
            Indexs.add(index)
        dist_txt = TextMobject('顶点A到各顶点的距离').scale(0.5).next_to(dist_mob, 2*UP)
        self.play(ShowCreation(VGroup(dist_mob, Indexs, dist_txt)))
        self.wait(2)
        #Dijstra算法
        visited = np.zeros(length)
        visited[0] = 1
        self.play(ShowCreation(graph.elements[0][0].set_fill(GOLD, opacity=0.7)))
        for i in range(1, length):
            # 找到最近的顶点
            u = 0
            min_tmp = max_value
            for j in range(length):
                if visited[j] == 0 and dist[j] < min_tmp:
                    min_tmp = dist[j]
                    u = j
            visited[u] = 1
            self.play(ShowCreation(dist_mob[u].set_color(RED)))
            self.play(ShowCreation(graph.elements[u][0].set_fill(GOLD, opacity=0.7)))
            self.wait(1)
            #print(u)
            for v in range(length):
                if arrays[u, v] < max_value and dist[v] > dist[u] + arrays[u, v]:
                    dist[v] = dist[u] + arrays[u, v]
                    #
                    new_dist  = TextMobject(str(int(dist[v])), color=YELLOW).scale(0.9).move_to(dist_mob[v].get_center())
                    self.play((ReplacementTransform(dist_mob[v], new_dist)))
                    dist_mob.submobjects[v] = new_dist
                    self.wait(2)
        self.play(ShowCreation(graph.line_groups[1][0].set_color(RED)))
        self.play(ShowCreation(graph.line_groups[5][0].set_color(RED)))
        self.play(ShowCreation(graph.line_groups[2][0].set_color(RED)))
        print(dist)
        #
        def errors(txt):
            index, right_dist = txt.split(',')
            index = int(index)
            circle = Circle(radius=0.2).move_to(dist_mob[index].get_center())
            error_text = TextMobject("X", color=YELLOW).scale(0.8).move_to(dist_mob[index].get_center())
            right_text = TextMobject(right_dist, color=RED).scale(0.8).next_to(error_text, DOWN)
            return VGroup(circle, error_text, right_text)
        index_3_text = always_redraw(lambda : errors("3,1"))
        index_4_text = always_redraw(lambda : errors("4,4"))
        self.play(ShowCreation(VGroup(index_3_text, index_4_text), runtime=2))
        self.wait(5)

    def bellman_ford(self):
        #
        bellman_ford_text = TextMobject("Bellman-Ford算法比dijkstra算法更具有普遍性, Bellman-Ford算法对边没有要求,",
        "可以处理负权边与负权回路. 其主要思想是对所有的边进行n-1轮松弛操作.", 
        "在一个含有n个顶点的图中, 任意两点之间的最短路径最多包含n-1条边。第一轮对所有的边进行松弛后, ",
        "得到的是源点最多经过一条边到其他顶点的最短距离;在第二轮对所有的边进行松弛后, 得到的是源点最多经过两条边到达",
        "其他顶点的最短距离; 依次类推, n-1次轮松弛后, 得到的是源点最多经过n-1条边到达其他顶点的最短距离.",alignment="\\raggedright").scale(0.5).shift(1.5*UP)
        self.play(Write(bellman_ford_text), runtime=6)
        self.wait(10)
        datas = ['A', 'B', 'C', 'D', 'E']
        positions = [[-5,-1.5,0], [-3, -0.5, 0], [-3, -2.5, 0], [-1, -0.5, 0], [-1, -2.5, 0]]
        graph_datas = [['A','B','3'], ['A','C','5'], ['B','D','1'], ['E','C','2'], ['D','E','3'], ['C','B','-5']]
        graph = Graph(datas, graph_datas, positions, buff=0.4, txt_color=YELLOW)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        self.wait(2)
        # edges
        length = len(graph_datas)
        edges = np.zeros((length, 3))
        for i in range(length):
            edges[i][0] = ord(graph_datas[i][0]) - ord('A')
            edges[i][1] = ord(graph_datas[i][1]) - ord('A')
            edges[i][2] = graph_datas[i][2]
        #
        dist = np.ones(len(datas)) * float('inf')
        dist[0] = 0
        x, y = 1, -1
        dist_mob = VGroup()
        Indexs = VGroup()
        for i in range(len(dist)):
            if dist[i] < float(inf):
                txt = str(int(dist[i]))
                color = RED
            else:
                txt = str(dist[i])
                color = TEAL
            value = TextMobject(txt, color=color).scale(0.8).move_to([x, y, 0])
            index = TextMobject(datas[i]).scale(0.5).next_to(value, 0.5 * UP)
            x += 0.8
            dist_mob.add(value)
            Indexs.add(index)
        dist_txt = TextMobject('顶点A到各顶点的距离').scale(0.5).next_to(dist_mob, 2*UP)
        self.play(ShowCreation(VGroup(dist_mob, Indexs, dist_txt)))
        relaxtion_txt = TextMobject('$dist[to]=min(dist[from]+edge_width, dist[to])$\\\\from: 边的起始端点\\\\to: 边的结束端点').scale(0.5).next_to(dist_mob, DOWN)
        self.play(ShowCreation(relaxtion_txt))
        # 
        def get_direction(index):
            direction = LEFT
            if index == 1 or index == 3:
                direction = UP
            elif index == 2 or index == 4:
                direction = DOWN
            return direction
        for i in range(len(datas)- 1): #循环n-1次
            check = 0 #用来标记本轮松弛操作中数组distance是否会发生更新 
            for j in range(length): # n条边
                first_from = int(edges[j][0])
                second_to = int(edges[j][1])
                weight = int(edges[j][2])
                from_direction = get_direction(first_from)
                to_direction = get_direction(second_to)
                from_text = TextMobject(str(dist[first_from])).scale(0.7).next_to(graph.elements[first_from], from_direction)
                end_text = TextMobject(str(dist[second_to])).scale(0.7).next_to(graph.elements[second_to], to_direction)
                self.play(ShowCreation(VGroup(from_text, end_text)))
                self.play(ShowCreation(graph.line_groups[j][0].set_color(RED)))
                if (dist[first_from] != float('inf')) and (dist[second_to] > dist[first_from] + weight):
                    dist[second_to] = dist[first_from] + weight
                    check = 1
                    #
                    new_dist  = TextMobject(str(int(dist[second_to])), color=YELLOW).scale(0.9).move_to(dist_mob[second_to].get_center())
                    self.play((ReplacementTransform(dist_mob[second_to], new_dist)))
                    dist_mob.submobjects[second_to] = new_dist
                    self.wait(2)
                self.play(Uncreate(VGroup(from_text, end_text)))
                graph.line_groups[j][0].set_color(WHITE)
            if check == 0:
                break
        complexity_text = TextMobject("Bellman-Ford算法时间复杂度为O(VE), 其中V为顶点数, E为边数。").scale(0.5).move_to([0, -3.2,0])
        self.play(Write(complexity_text))
        self.wait(4)
    
    def SPFA(self):
        spfa_text = TextMobject("SPFA算法是Bellman-Ford算法的队列优化算法的别称, 引入队列, 减少了不必要的冗余计算.",
        "算法思想为: 初始时将源点加入队列。每次从队列中取出一个顶点元素, 并对所有与它相邻的顶点进行松弛, 若某个相邻的顶点松弛成功, 则将其入队列.",
        "直至队列为空，算法结束. 一个顶点可以在出队列之后再次入队列. 一个顶点被访问过之后, 到它的最短路径长度会被再次更改, 将其入队列还可再对",
        "所有与其相邻的顶点进行松弛操作. 参考前面Dijstra算法不能正确处理负权图的示例. Dijstra算法不能正确处理负权问题就在于访问后的顶点的dist在其被访问",
        "后更改, 也不能对它的相邻顶点执行松弛操作. SPFA可在O(kE)的时间复杂度内求出源点到其他所有点的最短路径. 其中k为所有顶点进队列的平均次数, k一般小于等于2.\\\\", 
        "SPFA算法有两个优化算法 SLF(Small Label First) 和 LLL(Large Label Last) :",
        alignment="\\raggedright").scale(0.5).shift(UP)
        self.play(Write(spfa_text), runtime=6)
        self.wait(10)
        spfa_bullist = BulletedList("SLF策略: 设要加入的节点是j, 队首元素为i, 若dist(j)<dist(i), 则将j插入队首, 否则插入队尾.", 
        "LLL策略: 设队首元素为i, 队列中所有dist值的平均值为x, 若dist(i)>x则将i插入到队尾, 查找下一元素, 直到找到某一i使得dist(i)<=x, 则将i出对列进行松弛操作").scale(0.5)
        spfa_bullist.next_to(spfa_text, DOWN)
        self.play(Write(spfa_bullist), runtime=2)
        self.wait(4)
        judge_negative_edge = TextMobject("SPFA算法还有一个用途:判断有无负环. 如果某个点进入队列的次数超过V次则存在负环(SPFA无法处理带负环的图)",
        alignment="\\raggedright").scale(0.5).next_to(spfa_bullist, DOWN)  
        self.play(Write(judge_negative_edge), runtime=2)
        self.wait(10) 
        self.play(Uncreate(VGroup(spfa_text, spfa_bullist, judge_negative_edge)))
        spfa_code_1 = Code(file_name="F:\manim\\projects\\test\\codes\\spfa_1.cpp", insert_line_no=False, style=code_styles_list[11]).scale(0.7).move_to([-4,0,0])
        spfa_code_2 = Code(file_name="F:\manim\\projects\\test\\codes\\spfa_2.cpp", insert_line_no=False, style=code_styles_list[11]).scale(0.65).move_to([3,-0.5,0])
        self.play(Write(spfa_code_1), run_time=2)
        self.wait(1)
        self.play(Write(spfa_code_2), run_time=2)
        self.wait(10)

    def summary(self):
        title = TextMobject("最短路径算法对比比较").scale(0.8).to_edge(UP)
        self.play(Write(title))
        first_column = TextMobject("最短路算法\\\\", "\\quad\\\\Floyd\\\\", "\\quad\\\\Dijstra\\\\", "\\quad\\\\Bellman-Ford\\\\", "\\quad\\\\SPFA\\\\", alignment="\\raggedright", weight=BOLD).scale(0.8)
        second_column = TextMobject("平均时间\\\\复杂度", "\\quad\\\\$O(V^{3})$\\\\", "\\quad\\\\$O(V^{2})$\\\\", "\\quad\\\\$O(VE)$\\\\", "\\quad\\\\$O(kE)$\\\\").scale(0.8)
        fourth_column = TextMobject("负权\\\\","\\quad\\\\可以\\\\", "\\quad\\\\不能\\\\", "\\quad\\\\可以\\\\", "\\quad\\\\可以\\\\").scale(0.8)
        fivth_column = TextMobject("判断是否\\\\存在负权回路",  "\\quad\\\\可以\\\\", "\\quad\\\\不能\\\\", "\\quad\\\\可以\\\\", "\\quad\\\\可以\\\\").scale(0.8)
        colors = [YELLOW, MAROON, GOLD, RED_A]
        for i in range(len(colors)):
            first_column[i].set_color(colors[i])
            second_column[i].set_color(colors[i])
            fourth_column[i].set_color(colors[i])
            fivth_column[i].set_color(colors[i])
        first_column.move_to([-3.5, 0, 0])
        second_column.next_to(first_column, 2*RIGHT)
        fourth_column.next_to(second_column, 2*RIGHT)
        fivth_column.next_to(fourth_column, 2*RIGHT)
        self.play(ShowCreation(VGroup(first_column, second_column, fourth_column, fivth_column)))
        self.wait(5)
