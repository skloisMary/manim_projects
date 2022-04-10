from ctypes import alignment
from os import path
from tkinter import font
from turtle import width
from cv2 import line
from matplotlib.pyplot import arrow, axes
from manim import *
from manimlib.imports import *
import random
import numpy as np

""" class MyText(Text):
    CONFIG = {
        'font': 'songti'
    }
class MyBulletedList(BulletedList):
    CONFIG = {
        "buff": MED_LARGE_BUFF,
        "dot_scale_factor": 0.1,
        "dot_color": WHITE,
    } """


class TestScene(Scene):
    def construct(self):
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
        logo.shift(np.array((6.5, 3.5, 0.)))  # left/right  up/dowm
        self.play(Write(logo))
        # for i in range(0, 19):
        #     dfs_code = Code(file_name="F:\manim\\projects\\test\\codes\\DFS.cpp", insert_line_no=False, style=code_styles_list[i]).scale(0.8)
        #     dfs_code.move_to([0, -0.5, 0])
        #     self.play(Write(dfs_code))
        #     text = TextMobject(str(i))
        #     text.move_to([5, 3.5,0])
        #     self.play(Write(text))
        #     self.play(Uncreate(VGroup(dfs_code, text)))
        #
        # elements = VGroup()
        # for i in range(3):
        #     element = VGroup()
        #     circle = Circle(radius=0.3, stroke_color=BLUE)
        #     circle.shift((3 - i) * (UP  + LEFT) )
        #     number = Integer(i).move_to(circle.get_center())
        #     element.add(circle, number)
        #     self.play(Write(element))
        #     elements.add(element)
        # line_1 = Line(start = elements[0].get_center(), end = elements[1].get_center(), buff=.3)
        # self.play(Write(line_1))
        # line_2 = Line(start = elements[1].get_center(), end = elements[2].get_center(), buff=.3)
        # self.play(Write(line_2))
        # self.play(ShowCreation(elements[0].set_fill(RED)))

        # color_dict_1 = {"线性表": MAROON, "后进先出": PURPLE}
        # stack_description = TextMobject("栈（stack）又名堆栈，它是一种限定仅在表尾进行插入和删除操作的线性表。",
        # "栈是允许在同一端进行插入和删除操作的特殊线性表,它按照后进先出(LIFO，last-in, first-out)的原则存储数据，",
        # "先进入的数据被压入栈底，最后的数据在栈顶，需要读数据的时候从栈顶开始弹出数据。",
        # alignment="\\raggedright", tex_to_color_map=color_dict_1).scale(0.5)
        # string_text = ["从点1出发开始搜索。","点1的邻接点2和8都未被访问,选择点8出发进行搜索","点8有邻接点9和10都未被访问,选择点10出发进行搜索",
        # "点10有邻接点9未被访问,选择点9出发进行搜索","点9的邻接点都已被访问,重回点1,选择点1\\\\未被访问的点2出发进行搜索", 
        # "点2有邻接点3和4都未被访问,选择点4出发进行搜索", "点2有邻接点5,6和7都未被访问,选择点7出发进行搜索",
        # "点7有邻接点6未被访问,选择点6出发进行搜索", "点6有邻接点6未被访问,选择点5出发进行搜索",
        # "点5的邻接点都已被访问,重回点2,选择点2\\\\未被访问的点3出发进行搜索"]
        # text_groups = VGroup()
        # for i in range(len(string_text)):
        #     text = TextMobject(string_text[i],alignment="\\raggedright").scale(0.5)
        #     text_groups.add(text)
        #     text_groups.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=.2)
        #     text_groups.shift(2*RIGHT)
        #     self.play(Write(text_groups[i])) 
        
        # R2= Dot(color=GREEN)
        # #self.add(R2)
        # R1 = Line(start = [0, -2, 0], end = [0, 2, 0])
        # #self.add(R1)
        # self.play(MoveAlongPath(R2,R1),run_time=2,rate_func=linear)

        # Brace(circle, direction=DOWN, color=GREEN)
        # always_redraw
        # # Arrow  test
        # arrow_1 = Arrow(
        #     start=DOWN, 
        #     end=UP, 
        #     color=RED, 
        #     buff=0.8, # 内收缩系数，默认为0。取值越大，实线越短
        #     tip_length=0.2, 
        #     stroke_width=4, # 轮廓
        #     max_tip_length_to_length_ratio=0.35,
        #     max_stroke_width_to_length_ratio=5
        # )
        # #print(arrow_1.get_length()) # start - end
        # # min(max_tip_length_to_length_ratio * get_length(), tip_length)
        # #print(arrow_1.get_default_tip_length())
        # # stroke = min(stroke_width, max_stroke_width_to_length_ratio * get_length())
        # #print(arrow_1.stroke_width)
        # #self.play(ShowCreation(arrow_1))

        # text_1 = Text('arrow' + str(1), color=RED, size=0.5)  # size 文字的缩放比例，默认为1，表示原来的尺寸48
        # text_1.next_to(arrow_1, DOWN)
        # g = VGroup(arrow_1, text_1)
        # self.play(ShowCreation(g))
        # g.shift(2*RIGHT)
        # self.play(ShowCreation(g))
        # self.play(Uncreate(g))


        # # 正方形
        # square = Square(color=YELLOW, side_length=1)
        # square.shift(2*UP)
        # self.play(ShowCreation(square))
        # self.play(Uncreate(square))

        # # 
        # circle = Circle(color=BLUE, side_length=1)
        # #circle.move_to(ORIGIN)
        # #self.play(ShowCreation(circle))
        # #circle.move_to(ORIGIN + DOWN)   
        # #self.play(ShowCreation(circle)) 
        # axes = np.array((-1., 1., 0.))  
        # circle.move_to(axes)
        # self.play(ShowCreation(circle)) 
        # circle.move_to(axes + DOWN)
        # self.play(ShowCreation(circle)) 
        # self.play(Uncreate(circle))
        # #Text
        # text  = Text("冒泡排序", font="songti",size=0.5)
        # text_1 = TexMobject("\\cdot")
        # text_1.next_to(text, RIGHT)
        # text_2 = TexMobject("\\cdot", color=RED).scale(0.2)
        # text_2.next_to(text_1, RIGHT)
        # text_3 = TexMobject("\cdot", color=GREEN).scale(2)
        # text_3.next_to(text_2, RIGHT)
        # self.play(Write(VGroup(text, text_1, text_2, text_3))) 
        # self.play(Uncreate(VGroup(text, text_1, text_2, text_3))) 
        # text_steps = BulletedList(
        #     " 第一步：从nums[0]开始，依次比较两个相邻的元素直到nums[9], 如果左边的元素大于右边的元素, 交换它们。那么nums[9]就是最大的元素", 
        #     " 第二步：从nums[0]开始，依次比较两个相邻的元素知道nums[8], 如果左边的元素大于右边的元素，交换它们。那么nums[9]就是第二大的元素",
        #     " ...",
        #     " 第九步：比较nums[0]和nums[1]，如果nums[0]大于nums[1]，交换它们。", dot_color=BLUE
        # )
        # text_steps.scale(0.5)
        # self.play(Write(text_steps))
        # self.play(FadeOut(text_steps))
        # rendered_code = Code(file_name="F:\manim\\projects\\test\\codes\\bubbleSort.py", tab_width=4, background="window", language="Python").scale(0.7)
        # rendered_code.to_edge(LEFT)
        # # 性能分析
        # text_4 = TextMobject("以升序为例，假设待排序数组长度为n，冒泡排序需要两层for循环，\\\\",
        #     "冒泡排序算法在每一轮排序中会使一个元素排到一端，\\\\",
        #     "外层循环循环n-1次，每轮排序都需要相邻的两个元素进行比较。\\\\",
        #     "在最坏的情况（降序排列）下，内层循环最多时循环n-1次，时间复杂度为$O\left( n^{2}\\right)$;\\\\",
        #     "在最好的情况（升序排列）下，最少循环0次，时间复杂度为$O\left( n \\right)$。\\\\", 
        #     "冒泡排序的平均时间复杂度为$O\left( n^{2} \\right)$。\\\\",
        #     "冒泡排序用到的空间只有交换时的临时变量，空间复杂度为$O\left( 1 \\right)$。", alignment="\\raggedright").scale(0.4)
        # text_4.next_to(rendered_code, RIGHT)
        # self.play(ShowCreation(rendered_code), FadeIn(text_4))


