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
from tkinter import W, font
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

class Strings(VGroup):
    def __init__(self, string_txt, position, buff, color=RED, scale_factor=1):
        super().__init__()
        self.build_string_array(string_txt, position, buff, color, scale_factor)

    def build_string_array(self, string_txt, position, buff, color, scale_factor):
        for i, str in enumerate(string_txt):
            cell = TextMobject(str).scale(scale_factor).set_color(color).move_to(position)
            if i != 0:
                cell.next_to(self, RIGHT, buff=buff)
            self.add(cell)

#python -m manim F:\manim\\projects\\test\\KMP.py KMP  -p --media_dir F:\\manim_vedio_dirs
class KMP(Scene):
    def construct(self):
        # logo
        logo = my_logo()
        self.play(Write(logo))
        self.match()

    def match(self):
        #########
        title = TextMobject("串", color=RED).to_edge(UP)
        self.play(Write(title))
        string_text = TextMobject("串(string)是由零个或多个字符组成的有限序列, 一般记为",
        "$s='a_{1} a_{2} \cdots a_{n}'(n \geq 0 )$","其中, $s$是串的名, 用单引号括起来的字符序列是串的值;",
        "$a_{i} (1 \leq i \leq n )$可以是字母、数字或其他字符; 串中字符的数目$n$称为串的长度. 零个字符的串称为空串, 它的长度为零.\\\\", 
        "串中任意个连续的字符组成的子序列称为该串的子串. 包含子串的串相应地称为主串. 通常称字符在序列中的序号为该字符在串中的位置.",
        "子串在主串中的位置则以子串的第一个字符在主串中的位置来表示.", alignment="\\raggedright", 
        tex_to_color_map={"串中任意个连续的字符组成的子序列称为该串的子串": ORANGE, "子串在主串中的位置则以子串的第一个字符在主串中的位置来表示.": MAROON})
        string_text.scale(0.5).shift(UP)
        self.play(Write(string_text), runtime=2)
        self.wait(10)
        #
        Index_title = TextMobject("串的模式匹配算法", color=RED).to_edge(UP)
        self.play(ReplacementTransform(title, Index_title), Uncreate(string_text))
        index_description = TextMobject("子串的定位操作通常称为串的模式匹配. 假设主串为T, 子串为P, 蛮力模式匹配是最简单最自觉的方法, 其算法思想为: ",
        "从主串T的第pos个字符起和子串P的第一个字符相比较, 若相等, 则继续逐个比较后续字符; 否则从主串T的下一个字符起再重新和子串P的第一个字符相比较",
        "以此类推, 直至子串P中的每个字符依次和主串T中的一个连续的字符序列相等, 则称匹配成功. 否则, 则称匹配不成功.", alignment="\\raggedright", 
        tex_to_color_map={"模式匹配": RED, "匹配成功": YELLOW, "匹配不成功": ORANGE}).scale(0.5).shift(1.9*UP)
        self.play(Write(index_description), runtime=2)
        self.wait(10)
        match_code = Code(file_name="F:\\manim\\projects\\test\\codes\\brute_force_match.cpp",insert_line_no=False, style=code_styles_list[11]).scale(0.8)
        match_code.move_to([0,-1.5,0])
        self.play(Write(match_code), runtime=2)
        self.wait(6)
        match_code.scale(0.5).move_to([4,-3,0])
        self.play(Write(match_code), runtime=2)
        #
        t_sstring_text = Strings(string_txt="acabaabaabcacaabc", position=[-4.5,0,0], buff=0.5,  color=RED)
        s_sstring_text = Strings(string_txt="abaabc", position=[-4.5,-1,0], buff=0.5, color=ORANGE)
        t_Text = TextMobject("主串: ", color=RED).scale(0.5).next_to(t_sstring_text, LEFT)
        s_Text = TextMobject("子串：", color=ORANGE).scale(0.5).next_to(s_sstring_text, LEFT)
        self.play(Write(VGroup(t_sstring_text, s_sstring_text)), Write(VGroup(t_Text, s_Text)))
        t_start_pos = t_sstring_text[0].get_center()
        t_start_pos[1] += 1
        t_end_pos = t_start_pos.copy()
        t_end_pos[1] -= 0.5
        t_arrow = self.get_arrows(start_position=t_start_pos, end_position=t_end_pos, color=PURPLE)
        s_start_pos = s_sstring_text[0].get_center()
        s_start_pos[1] -= 1
        s_end_pos = s_start_pos.copy()
        s_end_pos[1] += 0.5
        s_arrow = self.get_arrows(start_position=s_start_pos, end_position=s_end_pos, color=TEAL)
        self.play(ShowCreation(VGroup(t_arrow, s_arrow)))
        #
        t_sstring, s_sstring = "acabaabaabcacaabc", "abaabc"
        print(t_sstring_text[1].get_center(), t_sstring_text[0].get_center())
        gap = t_sstring_text[1].get_center()[0] - t_sstring_text[0].get_center()[0]
        t_length = len(t_sstring)
        s_length = len(s_sstring)
        i, j = 0, 0
        while i < t_length and j < s_length:
            self.play(Indicate(t_sstring_text[i]), Indicate(s_sstring_text[j]))
            if t_sstring[i] == s_sstring[j]:
                t_arrow.shift(gap*RIGHT)
                s_arrow.shift(gap*RIGHT)
                self.play(ShowCreation(VGroup(t_arrow, s_arrow)))
                i = i + 1
                j = j + 1
            else:
                t_arrow.shift((j-1)*gap*LEFT)
                s_arrow.shift((j-1)*gap*LEFT)
                i = i - j + 1
                j = 0
                s_sstring_text.shift(gap*RIGHT)
                self.play(ShowCreation(VGroup(s_sstring_text, t_arrow, s_arrow)))
        if j == s_length:
            success_text = TextMobject("匹配成功！").scale(0.5).next_to(s_sstring_text, DOWN)
            self.play(Uncreate(VGroup(t_arrow, s_arrow)),Write(success_text))
        self.wait(2)
        time_complity = TextMobject("假设主串的长度为$n$,子串的长度为$m$,\\\\ 暴力模式匹配算法至多迭代$n-m+1$轮,\\\\",
        "且各轮至多需进行$m$次比对, \\\\故总共只需做不超过$(n-m+1) \cdot m$次比对.\\\\时间复杂度为$O(n \cdot m)$.", alignment="\\raggedright").scale(0.5).move_to([-3,-2.5,0])
        self.play(Write(time_complity), runtime=2)
        self.wait(6)
        self.play(Uncreate(VGroup(match_code,time_complity, success_text, t_sstring_text, s_sstring_text, t_Text, s_Text)))
        next_text = TextMobject("在每一轮的m次比对中, 一旦发现失配, 主串和子串的字符指针都要回退, 并从头开始下一轮尝试.",
        "实际上, 这类重复的字符比对操作没有必要. 既然这些字符在前一轮迭代中已经接收过比对并且成功, 我们也就掌握了它们的所有消息",
        "如何利用这些消息，提高匹配算法的效率呢?", alignment="\\raggedright").scale(0.5).shift(2*UP)
        self.play(ReplacementTransform(index_description, next_text))
        self.wait(6)
        kmp_description = TextMobject("KMP算法是一种改进的字符串匹配算法, 由D.E.Knuth, J.H.Morris和V.R.Pratt提出的, ", 
        "因此也称它为克努特—莫里斯—普拉特操作(简称KMP算法)。KMP算法的核心是利用匹配失败后的信息,",
        "尽量减少子串与主串的匹配次数以达到快速匹配的目的. 具体实现就是通过一个next()函数实现, 函数本身包含了子串的局部匹配信息.",
        "next表的构造时间复杂度为O(m), KMP算法的时间复杂度O(m+n)", alignment="\\raggedright").scale(0.5).next_to(next_text, DOWN)
        self.play(Write(kmp_description), runtime=2)
        self.wait(10)
        self.play(Uncreate(VGroup(kmp_description, next_text)))
        
        next_match_code = Code(file_name="F:\\manim\\projects\\test\\codes\\get_next_1.cpp",insert_line_no=False, style=code_styles_list[11]).scale(0.6)
        next_match_code.move_to([-3,-0.5,0])
        self.play(Write(next_match_code), runtime=2)
        self.wait(6)
        s_sstring_text_1 = Strings(string_txt="abaabc", position=[2,1,0], buff=0.5, color=ORANGE)
        self.play(Write(s_sstring_text_1), runtime=2)
        index_group = Strings(string_txt="012345", position=[2,1.3,0], buff=0.67,  color=WHITE, scale_factor=0.4)
        tmp = TextMobject("-1").scale(0.4).set_color(WHITE).next_to(index_group[0], LEFT, buff=0.67)
        index_group.add(tmp)
        self.play(ShowCreation(index_group))
        next_array, next_groups = self.get_next(s_sstring_text_1, string_txt="abaabc")
        self.wait(4)
        next_match_code.scale(0.5).move_to([-4,-3,0])
        self.play(ShowCreation(next_match_code),
        ShowCreation(VGroup(s_sstring_text_1, index_group, next_groups).scale(0.5).move_to([4,-3,0])))
        #
        t_sstring_text_1 = Strings(string_txt="acabaabaabcacaabc", position=[-4.5,1,0], buff=0.5,  color=RED)
        s_sstring_text_2 = Strings(string_txt="abaabc", position=[-4.5,0,0], buff=0.5, color=ORANGE)
        t_sstring, s_sstring = "acabaabaabcacaabc", "abaabc"
        t_Text = TextMobject("主串: ", color=RED).scale(0.5).next_to(t_sstring_text_1, LEFT)
        s_Text = TextMobject("子串：", color=ORANGE).scale(0.5).next_to(s_sstring_text_2, LEFT)
        self.play(Write(VGroup(t_sstring_text_1, s_sstring_text_2)), Write(VGroup(t_Text, s_Text)))
        t_start_pos = t_sstring_text_1[0].get_center()
        t_start_pos[1] += 1
        t_end_pos = t_start_pos.copy()
        t_end_pos[1] -= 0.5
        t_arrow = self.get_arrows(start_position=t_start_pos, end_position=t_end_pos, color=PURPLE)
        s_start_pos = s_sstring_text_2[0].get_center()
        s_start_pos[1] -= 1
        s_end_pos = s_start_pos.copy()
        s_end_pos[1] += 0.5
        s_arrow = self.get_arrows(start_position=s_start_pos, end_position=s_end_pos, color=TEAL)
        self.play(ShowCreation(VGroup(t_arrow, s_arrow)))
        gap = t_sstring_text_1[1].get_center()[0] - t_sstring_text_1[0].get_center()[0]
        t_length = len(t_sstring)
        s_length = len(s_sstring)
        i, j = 0, 0
        while i < t_length and j < s_length:
            if i >=0 and j>=0:
                self.play(Indicate(t_sstring_text_1[i]), Indicate(s_sstring_text_2[j]))
            if j < 0 or t_sstring[i] == s_sstring[j]:
                t_arrow.shift(gap*RIGHT)
                s_arrow.shift(gap*RIGHT)
                self.play(ShowCreation(VGroup(t_arrow, s_arrow)))
                i = i + 1
                j = j + 1
            else:
                print('j=', j, ' next[j]=', next_array[j])
                s_sstring_text_2.shift((j-next_array[j])*gap*RIGHT)
                j = next_array[j]
                self.play(ShowCreation(VGroup(s_sstring_text_2)))
        self.play(Uncreate(VGroup(s_arrow, t_arrow)))
        self.wait(4)
        # 
        self.play(Uncreate(VGroup(s_sstring_text_1, index_group, next_groups, next_match_code)))
        self.play(Uncreate(VGroup(t_sstring_text_1, s_sstring_text_2, t_Text, s_Text)))
        optimization_text = TextMobject("尽管上述演示KMP算法已能保证线性的运行时间, 但在模型情况下, 仍有进一步改进的余地.",
        alignment="\\raggedright").scale(0.5).shift(2*UP)
        self.play(Write(optimization_text))
        next_match_code_2 = Code(file_name="F:\\manim\\projects\\test\\codes\\get_next_2.cpp",
        insert_line_no=False, style=code_styles_list[11]).scale(0.7)
        next_match_code_2.move_to([-3.5,-1,0])
        self.play(Write(next_match_code_2), runtime=2)
        self.wait(2)
        s_sstring_text_3 = Strings(string_txt="000010", position=[1,1,0], buff=0.7,  color=RED)
        print(s_sstring_text_3[1].get_center()[0] - s_sstring_text_3[0].get_center()[0])
        index_group = Strings(string_txt="012345", position=[0.95,1.3,0], buff=0.85,  color=WHITE, scale_factor=0.4)
        print(index_group[1].get_center()[0] - index_group[0].get_center()[0])
        self.play(ShowCreation(VGroup(s_sstring_text_3, index_group)))
        next_groups_1 = VGroup()
        next_groups_2 = VGroup()
        next_1 = [-1,0,1,2,3,0]
        next_2 = self.get_nextval("000010")
        print(next_2)
        next_value_1 = Integer(next_1[0]).next_to(s_sstring_text_3[0], DOWN)
        next_groups_1.add(next_value_1)
        next_value_2 = Integer(next_2[0]).next_to(next_groups_1[0], 2 * DOWN)
        next_groups_2.add(next_value_2)
        for i in range(1, 6):
            if next_1[i] != next_2[i]:
                color_1 = ORANGE
                color_2 = MAROON
            else:
                color_1 = WHITE
                color_2 = WHITE
            next_value_1 = Integer(next_1[i], color=color_1).next_to(next_groups_1[-1], RIGHT, buff=0.7)
            next_value_2 = Integer(next_2[i], color=color_2).next_to(next_groups_2[-1], RIGHT, buff=0.47)
            next_groups_1.add(next_value_1)
            next_groups_2.add(next_value_2)
        tmp_1 = TextMobject("next表: ").scale(0.5).next_to(next_groups_1[0], LEFT, buff=0.5)
        self.play(ShowCreation(VGroup(next_groups_1, tmp_1)))
        self.wait(2)
        tmp_2 = TextMobject("改进的\\\\next表: ").scale(0.5).next_to(next_groups_2[0], LEFT, buff=0.5)
        self.play(ShowCreation(VGroup(next_groups_2, tmp_2)))
        self.wait(4)

    
    def get_next(self, s_sstring_text, string_txt):
        next_groups = VGroup()
        s_length = len(s_sstring_text)
        next = np.zeros(s_length, dtype=np.int)
        # 
        next[0] = -1
        next_value = Integer(-1).next_to(s_sstring_text[0], DOWN)
        self.play(Write(next_value))
        next_groups.add(next_value)
        i=0
        j=-1
        # arrow
        s_up_start_pos = s_sstring_text[i].get_center()
        s_up_start_pos[1] += 1
        s_up_end_pos = s_up_start_pos.copy()
        s_up_end_pos[1] -= 0.5
        s_arrow_up = self.get_arrows(start_position=s_up_start_pos, end_position=s_up_end_pos, color=TEAL)
        #
        s_down_start_pos = s_sstring_text[0].get_center()
        s_down_start_pos[0] -= 0.75
        s_down_start_pos[1] -= 1.5
        s_down_end_pos = s_down_start_pos.copy()
        s_down_end_pos[1] += 0.5
        s_arrow_down = self.get_arrows(start_position=s_down_start_pos, end_position=s_down_end_pos, color=TEAL)
        self.play(ShowCreation(VGroup(s_arrow_up, s_arrow_down)))
        gap = s_sstring_text[1].get_center()[0] - s_sstring_text[0].get_center()[0]
        while i < (s_length - 1):
            self.play(Indicate(s_sstring_text[i]), Indicate(s_sstring_text[j]))
            if j < 0 or string_txt[i] == string_txt[j]:
                i += 1
                j += 1
                #
                s_arrow_up.shift(gap*RIGHT)
                s_arrow_down.shift(gap*RIGHT)
                self.play(ShowCreation(VGroup(s_arrow_up, s_arrow_down)))
                #
                next[i] = j
                next_value = Integer(j).next_to(next_groups[-1], RIGHT, buff=0.5)
                next_groups.add(next_value)
                self.play(Write(next_value))
            else:
                s_arrow_down.shift((j - next[j])*gap*LEFT)
                j = next[j]
                # print('j= ', j)
        self.play(Uncreate(VGroup(s_arrow_up,s_arrow_down)))
        return next, next_groups

    def get_nextval(self, s_sstring_text):
        s_length = len(s_sstring_text)
        next = np.zeros(s_length, dtype=np.int)
        next[0] = -1
        i=0
        j=-1
        while i < (s_length - 1):
            if j < 0 or s_sstring_text[i] == s_sstring_text[j]:
                i += 1
                j += 1
                if s_sstring_text[i] != s_sstring_text[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]
        return next

    def  get_arrows(self, start_position, end_position, color=RED):
        arrow = Arrow(
            start=start_position, 
            end=end_position, 
            color=color, 
            buff=0.8, 
            tip_length=0.2, 
            stroke_width=4, 
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
        return arrow
    
