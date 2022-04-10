from cgitb import text
from stat import UF_OPAQUE
from tkinter import font
from tracemalloc import start
from turtle import position
from cairo import FORMAT_RGB16_565
from matplotlib import lines

from matplotlib.pyplot import flag, title
from manim import *
from manimlib.imports import *
import random
import numpy as np

class MyText(Text):
    CONFIG = {
        'font': 'songti',
        'size': 0.5
    }

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
graph_top_height = 2
positions = [[0, graph_top_height, 0], [-2, graph_top_height-1, 0], [-3, graph_top_height-2, 0], [-1, graph_top_height-2, 0], 
[-2, graph_top_height-3, 0], [-1, graph_top_height-3, 0], [0, graph_top_height-3, 0], 
[2, graph_top_height-1, 0], [2, graph_top_height-2, 0], [3, graph_top_height-2, 0]]
graph_datas = [[1,2], [1,8], [2,3], [2,4], [4,5], [4,6], [4,7], [5,6], [6,7], [8,9], [8,10], [9,10]]

class Graph:
    def __init__(self, data, graph_datas, positions, radius):
        self.elements = self.create_element(data, positions, radius)
        self.line_groups = self.build_graph(graph_datas)

    def create_element(self, data, position, radius):
        elements = VGroup()
        for value in data:
            element = VGroup()
            circle = Circle(radius=radius, stroke_color=BLUE)
            circle.shift(position[value - 1])
            number = Integer(value).move_to(circle.get_center())
            element.add(circle, number)
            elements.add(element)
        return elements

    def build_graph(self, graph_datas):
        #
        lines_groups = VGroup()
        length = len(graph_datas)
        for i in range(length):
            element_1 = self.elements[graph_datas[i][0] - 1]
            element_2 = self.elements[graph_datas[i][1] - 1]
            line = Line(start=element_1.get_center(), end=element_2.get_center(),color=GREEN, buff=.3)
            lines_groups.add(line)
        return lines_groups



class DFS(Scene):
    def construct(self):
        # DFS
        self.camera.background_color = BLACK
        # logo
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
        #
        dfs_title =TextMobject("深度优先搜索算法", color=RED, fontsize=42, font="\heiti")
        self.play(Write(dfs_title), Write(logo))
        self.wait(1)
        title = TextMobject("深度优先搜索", fontsize=32)
        title.to_edge(UP)
        self.play(ReplacementTransform(dfs_title,title))
        #
        self.description()
        self.process()
        self.codes_display()
        self.actions()

    def description(self):
        color_dict ={"图的遍历": RED, "某一个顶点":ORANGE, "每一个顶点仅被访问一次": GOLD}
        graph_text = TextMobject("图的遍历就是：从图中的某一个顶点出发访问图中其他顶点，且使每一个顶点仅被访问一次",
        "为了避免同一顶点被访问多次，在遍历图的过程中，必须记下每个已访问过的顶点。",alignment="\\raggedright", 
        tex_to_color_map=color_dict, font="heiti").scale(0.5)
        graph_text.shift(2 * UP)
        self.play(Write(graph_text), run_time=5)
        bl_text = BulletedList("指定起始起点","每个顶点仅被访问一次", "设置一个辅助数据visited, 记录顶点的访问情况。", dot_color=BLUE).scale(0.45)
        bl_text.next_to(graph_text, DOWN)
        self.play(Write(bl_text), run_time=3)
        text = TextMobject("图的遍历算法包括深度优先搜索(Depth First Search,DFS)和广度优先搜索(Breadth First Search, BFS)。","这两种搜索适用于无向图和有向图。",
        alignment="\\raggedright", tex_to_color_map={"深度优先搜索": GREEN, "广度优先搜索": BLUE},font="heiti").scale(0.5)
        text.next_to(bl_text, DOWN)
        self.play(Write(text), run_time=3)
        self.wait(3)
        self.play(Uncreate(VGroup(graph_text, bl_text, text)))
        #
        color_dict_1 = {"深度优先搜索算法(Depth First Search,DFS)":RED, "对于每一个可能的分支路径深入到不能深入为止":ORANGE}
        text_1 = TextMobject("深度优先搜索算法(Depth First Search,DFS)属于图算法的一种。", 
        "其思想简要可简要描述为对于每一个可能的分支路径深入到不能深入为止，而且每个节点只能访问一次。",alignment="\\raggedright", font="heiti",
        tex_to_color_map=color_dict_1).scale(0.5)
        text_1.shift(2 * UP)
        self.play(Write(text_1), run_time=5)
        text_2 = BulletedList("步骤一: 从图中指定顶点v出发,访问此顶点,然后依次从v的未被访问的邻接点出发深度优先遍历图,直至图中所有与v有路径连通的顶点都被访问到;",
        "步骤二：若此时图中尚有顶点未被访问,则选图中一个未曾被访问的顶点作起始点，重复步骤一，直至图中所有顶点都被访问到为止。", dot_color=BLUE).scale(0.45)
        text_2.next_to(text_1, DOWN, aligned_edge=LEFT)
        self.play(Write(text_2), run_time=5)
        self.wait(3)
        self.play(Uncreate(VGroup(text_1, text_2)))

    def process(self):
        new_positions = [[-4,2,0],[-5,1,0],[-5.5,0,0],[-4,0,0],[-5,-1,0],[-4,-2,0],[-3,-1,0],[-3,1,0],[-2,0,0], [-2,1,0]]
        radius = 0.3
        graph = Graph(data, graph_datas, new_positions, radius)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        length = len(data)
        graphs_map = np.zeros((length, length))
        flags = np.zeros(length)
        for i in range(len(graph_datas)):
            graphs_map[graph_datas[i][0] - 1][graph_datas[i][1] - 1] = 1
            graphs_map[graph_datas[i][1] - 1][graph_datas[i][0] - 1] = 1
        # DFS codes
        begin = 0
        flags[begin] = 1
        S = []
        S.append(begin) # 进栈
        tmp = begin
        string_text = ["从点1出发开始搜索。","点1的邻接点2和8都未被访问,选择点8出发进行搜索","点8有邻接点9和10都未被访问,选择点10出发进行搜索",
        "点10有邻接点9未被访问,选择点9出发进行搜索","点9的邻接点都已被访问,重回点1,选择点1未被访问\\\\的点2出发进行搜索", 
        "点2有邻接点3和4都未被访问,选择点4出发进行搜索", "点4有邻接点5, 6和7都未被访问,选择点7出发进行搜索",
        "点7有邻接点6未被访问,选择点6出发进行搜索", "点6有邻接点5未被访问,选择点5出发进行搜索",
        "点5的邻接点都已被访问,重回点2,选择点2未被访问\\\\的点3出发进行搜索"]
        color_dict = {
            "2": TEAL,
            "3": GREEN,
            "4": YELLOW,
            "5": GOLD,
            "6": RED,
            "7": MAROON,
            "8": PURPLE,
            "9": GREY,
            "10":ORANGE,
        }
        index = 0
        text_groups = VGroup()
        while len(S):
            #
            text = TextMobject(string_text[index],alignment="\\raggedright", font="heiti", tex_to_color_map=color_dict).scale(0.5)
            text_groups.add(text)
            text_groups.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=.2)
            text_groups.shift(2*RIGHT)
            self.play(Write(text_groups[index], run_time=1))
            index += 1
            self.wait(1)
            #
            top = S.pop()
            if graphs_map[tmp][top] == 0.0:
                for i in range(len(graph_datas)):
                    if graph_datas[i][1] == (top+1):
                        tmp = graph_datas[i][0] - 1
                        break
            if (top - begin):
                dot_tmp= Dot(color=RED)
                lines_path = Line(start=graph.elements[tmp].get_center(), end=graph.elements[top].get_center())
                self.play(MoveAlongPath(dot_tmp, lines_path),run_time=2,rate_func=linear)
                self.play(Uncreate(dot_tmp))
            self.play(ShowCreation(graph.elements[top][0].set_fill(MAROON, opacity=0.6)))
            #
            for i in range(length):
                if flags[i]==0 and graphs_map[top][i] == 1:
                    S.append(i)
                    flags[i] = 1
            tmp = top
        text_abstract = TextMobject("DFS的思想概括就是:一直走一直走,不撞南墙不回头。显而易见,DFS可用递归实现", font="heiti",
        alignment="\\raggedright", color_dict={"递归", RED}).scale(0.5)
        text_abstract.shift(BOTTOM + UP)
        self.play(Write(text_abstract), run_time=2)
        self.wait(3)
        self.play(Uncreate(VGroup(graph.elements, graph.line_groups)))
        self.play(Uncreate(VGroup(text_groups, text_abstract)))
    
    def codes_display(self):
        #
        dfs_code = Code(file_name="F:\manim\\projects\\test\\codes\\DFS.cpp", insert_line_no=False, style=code_styles_list[11]).scale(0.8)
        dfs_code.move_to([0, -0.5, 0])
        self.play(Write(dfs_code), run_time=5)
        self.wait(5)
        #
        color_dict_1 = {"数据结构-栈": RED, "堆栈的溢出": GOLD, "非递归": BLUE}
        text_dfs_error = TextMobject("递归太深容易造成堆栈的溢出。如果图小一点，递归的缺点还不会太明显；",
        "但是如果一个图足够大,比如有上万个节点和上万条边,用递归实现DFS会出现堆栈的溢出。", 
        "利用数据结构-栈代替函数的调用以非递归的方式实现DFS",alignment="\\raggedright", tex_to_color_map=color_dict_1, font="heiti").scale(0.5)
        text_dfs_error.shift(1.5 * UP)
        self.play(ReplacementTransform(dfs_code, text_dfs_error))
        self.wait(3)
        non_recursive_text = TextMobject("非递归的好处：").scale(0.5)
        non_recursive_text.next_to(text_dfs_error, DOWN, aligned_edge=LEFT)
        non_recursive_tex_list = BulletedList("节省内存空间", "提高执行效率", cdot=GREEN).scale(0.5)
        non_recursive_tex_list.next_to(non_recursive_text, DOWN)
        self.play(Write(VGroup(non_recursive_text, non_recursive_tex_list)))
        self.wait(3)
        self.play(Uncreate(VGroup(text_dfs_error,non_recursive_text, non_recursive_tex_list)))
        dfs_stack_code = Code(file_name="F:\manim\\projects\\test\\codes\\DFS_Stack.cpp", background="window",style=code_styles_list[11])
        dfs_stack_code.move_to([0, 0, 0])
        self.play(Write(dfs_stack_code), run_time=3)
        self.wait(5)
        self.play(Uncreate(dfs_stack_code))
        
    def actions(self):
        # 画图
        radius = 0.3
        graph = Graph(data, graph_datas, positions, radius)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        #
        circle_v = Circle(radius=radius, stroke_color=BLUE)
        circle_v.set_fill(MAROON, opacity=0.6)
        text_v = TextMobject("已访问节点").scale(0.5)
        text_v.next_to(circle_v, RIGHT)
        v_group = VGroup(circle_v, text_v)
        v_group.move_to([-5, 3, 0.])
        circle_v_n = Circle(radius=radius, stroke_color=BLUE)
        text_v_n = TextMobject("未访问节点").scale(0.5)
        text_v_n.next_to(circle_v_n, RIGHT)
        v_n_group = VGroup(circle_v_n, text_v_n)
        v_n_group.next_to(v_group, DOWN)
        self.play(ShowCreation(VGroup(v_group, v_n_group)))
        # 栈
        left_p, right_p = -3, 2
        bottom_p , top_p = -3, -2
        line_1 = Line(start = [left_p, top_p, 0], end = [right_p, top_p, 0], color = YELLOW)
        line_2 = Line(start = [left_p, bottom_p, 0], end = [right_p, bottom_p, 0], color = YELLOW)
        line_3 = Line(start = [left_p, top_p, 0], end = [left_p, bottom_p, 0], color = YELLOW)
        stack_txt = MyText("栈").next_to(line_3, LEFT)
        self.play(ShowCreation(VGroup(line_1, line_2, line_3)), ShowCreation(stack_txt))
        # DFS
        length = len(data)
        graphs_map = np.zeros((length, length))
        flags = np.zeros(length)
        for i in range(len(graph_datas)):
            graphs_map[graph_datas[i][0] - 1][graph_datas[i][1] - 1] = 1
            graphs_map[graph_datas[i][1] - 1][graph_datas[i][0] - 1] = 1
        # DFS codes
        begin = 0
        tmp_graph_element = graph.elements.copy()
        flags[begin] = 1
        # 初始化栈
        S = []
        S.append(begin) # 进栈
        self.play(ShowCreation(graph.elements[begin][0].set_fill(MAROON, opacity=0.6)))
        # 定义位置
        current_positions = [left_p+radius,(top_p + bottom_p)/2, 0]
        top_stack_positions = [right_p+2 * radius,(top_p + bottom_p)/2, 0]
        final_positions = [right_p + 3, bottom_p * (-1), 0]
        # 顶点访问
        text_list = TextMobject("访问\\\\", "序列").scale(0.5)
        text_list.move_to([right_p + 4.2, 0, 0])
        self.play(ShowCreation(text_list))
        # 进栈
        in_tmp = tmp_graph_element[begin]
        in_arc = ArcBetweenPoints(start=np.array(positions[begin]), end=np.array(top_stack_positions), angle=-TAU / 4)
        self.play(MoveAlongPath(in_tmp, in_arc),run_time=2,rate_func=linear)
        in_lines = Line(start = top_stack_positions, end = current_positions)
        self.play(MoveAlongPath(in_tmp, in_lines),run_time=2,rate_func=linear)
        current_positions[0] += 2 * radius
        #
        while len(S):
            top = S.pop()  # 出站
            # 出栈
            out_tmp = tmp_graph_element[top]
            out_lines = Line(start = current_positions, end = top_stack_positions)
            self.play(MoveAlongPath(out_tmp, out_lines),run_time=2,rate_func=linear)
            out_arc = ArcBetweenPoints(start=np.array(top_stack_positions), end=np.array(final_positions), angle=TAU / 2)
            self.play(MoveAlongPath(out_tmp, out_arc),run_time=2,rate_func=linear)
            final_positions[1] -= 2 * radius
            #
            current_positions[0] -= 2 * radius
            print(top + 1)
            for i in range(length):
                if flags[i]==0 and graphs_map[top][i] == 1:
                    S.append(i)
                    # 
                    lines_path = Line(start=graph.elements[top].get_center(), end=graph.elements[i].get_center())
                    dot_tmp= Dot(color=RED)
                    self.play(MoveAlongPath(dot_tmp, lines_path),run_time=2,rate_func=linear)
                    self.play(ShowCreation(graph.elements[i][0].set_fill(MAROON, opacity=0.6)))
                    # 进栈
                    in_tmp = tmp_graph_element[i]
                    in_arc = ArcBetweenPoints(start=np.array(positions[i]), end=np.array(top_stack_positions), angle=- TAU / 4)
                    self.play(MoveAlongPath(in_tmp, in_arc),run_time=2,rate_func=linear)
                    in_lines = Line(start = top_stack_positions, end = current_positions)
                    self.play(MoveAlongPath(in_tmp, in_lines),run_time=2,rate_func=linear)
                    current_positions[0] += 2 * radius
                    # 标记
                    flags[i] = 1
            

class BFS(Scene):
    def construct(self):
        self.action()

    def description(self):
        color_dict_1 = {"广度优先搜索(Breadth First Search, BFS)":RED, "对于每一个可能的分支路径深入到不能深入为止":PURPLE}
        text_1 = TextMobject("深度优先搜索算法(Depth First Search,DFS)属于图算法的一种。", 
        "其思想简要可简要描述为对于每一个可能的分支路径深入到不能深入为止，而且每个节点只能访问一次。",alignment="\\raggedright", 
        tex_to_color_map=color_dict_1).scale(0.5)
        text_1.shift(2 * UP)
        self.play(Write(text_1), run_time=3)
        text_2 = BulletedList("步骤一: 从图中指定顶点v出发,访问此顶点,然后依次从v的未被访问的邻接点出发深度优先遍历图,直至图中所有与v有路径连通的顶点都被访问到;",
        "步骤二：若此时图中尚有顶点未被访问,则选图中一个未曾被访问的顶点作起始点，重复步骤一，直至图中所有顶点都被访问到为止。", dot_color=BLUE).scale(0.45)
        text_2.next_to(text_1, DOWN, aligned_edge=LEFT)
        self.play(Write(text_2), run_time=5)
        self.play(Uncreate(VGroup(text_1, text_2)))

    def action(self):
        # BFS
        self.camera.background_color = BLACK
        # 画图
        radius = 0.3
        graph = Graph(data, graph_datas, positions, radius)
        self.play(ShowCreation(VGroup(graph.elements, graph.line_groups)))
        # 定义graph map
        length = len(data)
        graphs_map = np.zeros((length, length))
        flags = np.zeros(length)
        for i in range(len(graph_datas)):
            graphs_map[graph_datas[i][0] - 1][graph_datas[i][1] - 1] = 1
            graphs_map[graph_datas[i][1] - 1][graph_datas[i][0] - 1] = 1
        # 队列
        left_p, right_p = -3, 2
        bottom_p , top_p = -3, -2
        line_1 = Line(start = [left_p, top_p, 0], end = [right_p, top_p, 0], color = YELLOW)
        line_2 = Line(start = [left_p, bottom_p, 0], end = [right_p, bottom_p, 0], color = YELLOW)
        stack_txt = MyText("队列").next_to(line_1, UP)
        self.play(ShowCreation(VGroup(line_1, line_2)), ShowCreation(stack_txt))
        #
        begin = 0
        tmp_graph_element = graph.elements.copy()
        flags[begin] = 1
        # 初始化队列
        Q = []
        Q.append(begin)
        self.play(ShowCreation(graph.elements[begin][0].set_fill(MAROON, opacity=0.6)))
        # 定义位置
        current_positions = [left_p + radius,(top_p + bottom_p)/2, 0]
        top_queue_positions = [left_p - 2 * radius,(top_p + bottom_p)/2, 0]
        bottom_queue_positions = [right_p + 2 * radius,(top_p + bottom_p)/2, 0]
        final_positions = [left_p - 2, bottom_p * (-1), 0]
        # 进队列
        in_tmp = tmp_graph_element[begin]
        in_arc = ArcBetweenPoints(start=np.array(positions[begin]), end=np.array(bottom_queue_positions), angle=-TAU / 4)
        self.play(MoveAlongPath(in_tmp, in_arc),run_time=2,rate_func=linear)
        in_lines = Line(start = bottom_queue_positions, end = current_positions)
        self.play(MoveAlongPath(in_tmp, in_lines),run_time=2,rate_func=linear)
        current_positions[0] += 2 * radius
        while len(Q):
            top = Q.pop(0) # 出队列
            current_positions[0] -= 2 * radius
            # 出队列
            out_tmp = tmp_graph_element[top]
            out_lines = Line(start = out_tmp.get_center(), end = top_queue_positions)
            self.play(MoveAlongPath(out_tmp, out_lines),run_time=2,rate_func=linear)
            out_arc = ArcBetweenPoints(start=np.array(top_queue_positions), end=np.array(final_positions), angle= - TAU / 4)
            self.play(MoveAlongPath(out_tmp, out_arc),run_time=2,rate_func=linear)
            final_positions[1] -= 2 * radius
            # 出队列时，队列中的其他元素要跟上
            for q in Q:
                in_queue_tmp = tmp_graph_element[q]
                tmp_positions = tmp_graph_element[q].get_center()
                tmp_positions[0] -= 2 * radius
                in_queue_tmp.move_to(tmp_positions)
            print(top + 1)
            for i in range(length):
                if flags[i]==0 and graphs_map[top][i] == 1:
                    Q.append(i)
                    flags[i] = 1
                    # 
                    lines_path = Line(start=graph.elements[top].get_center(), end=graph.elements[i].get_center())
                    dot_tmp= Dot(color=RED)
                    self.play(MoveAlongPath(dot_tmp, lines_path),run_time=2,rate_func=linear)
                    self.play(ShowCreation(graph.elements[i][0].set_fill(MAROON, opacity=0.6)))
                    # 进队列
                    in_tmp = tmp_graph_element[i]
                    in_arc = ArcBetweenPoints(start=np.array(positions[i]), end=np.array(bottom_queue_positions), angle=- TAU / 4)
                    self.play(MoveAlongPath(in_tmp, in_arc),run_time=2,rate_func=linear)
                    in_lines = Line(start = bottom_queue_positions, end = current_positions)
                    self.play(MoveAlongPath(in_tmp, in_lines),run_time=2,rate_func=linear)
                    current_positions[0] += 2 * radius

