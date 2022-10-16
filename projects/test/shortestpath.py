from ast import Num
from cgitb import text
from cmath import inf
from collections import deque
from ctypes import alignment
from ctypes.wintypes import DWORD
from dis import dis
import queue
from re import I
from tkinter import font
from tokenize import Number
from turtle import left
from colorama import init
from cv2 import circle, line, log, sepFilter2D
from matplotlib.pyplot import arrow, axes
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
    def __init__(self, datas, graph_datas, positions, radius=0.3, color=WHITE, buff=0.7):
        self.elements = self.create_element(datas, positions, radius)
        self.line_groups = self.build_graph(graph_datas, color, buff)

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

    def build_graph(self, graph_datas, color, buff):
        #
        lines_groups = VGroup()
        length = len(graph_datas)
        for i in range(length):
            element_1 = self.elements[ord(graph_datas[i][0]) - ord('A')]
            element_2 = self.elements[ord(graph_datas[i][1]) - ord('A')]
            line = Arrow(start=element_1.get_center(), end=element_2.get_center(),color=color, stroke_width=2, tip_length=0.1, tip_angle=PI/3, buff=buff)
            text_mob = TextMobject(str(graph_datas[i][2]), color=BLUE).scale(0.5).move_to(line.get_center())
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
    def description(self):
        #
        text = TextMobject()
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
        self.wait(2)


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
        self.Dijkstra_show()
        ##############################
    def description(self):
        #
        text = TextMobject()
    
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
        self.play(ShowCreation(VGroup(arrays_mob.elements, arrays_mob.Indexs)))
        # dist
        dist = arrays[0]
        #print('ori dist: ', dist)
        dist_mob = arrays_mob.elements[0].copy().move_to([0, -3, 0]).scale(1.5)
        dist_indexs = arrays_mob.Indexs[0: length].copy().next_to(dist_mob, 0.5 * UP).scale(1.5)
        self.play(ShowCreation(VGroup(dist_mob, dist_indexs)))
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