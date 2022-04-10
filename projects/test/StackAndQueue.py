from cgitb import text
from collections import deque
from ctypes.wintypes import DWORD
from tkinter import font
from turtle import left
from cv2 import line
from matplotlib.pyplot import arrow, axes
from manim import *
from manimlib.imports import *
import random
import numpy as np

class MyText(Text):
    CONFIG = {
        'font': 'songti',
        'size': 0.5
    }

def arrow_build(start, end, color, string_txt, direction):
    arrow=Arrow(
            start=start, 
            end=end, 
            color=color, 
            buff=0.8, # 内收缩系数，默认为0。取值越大，实线越短
            tip_length=0.2, 
            stroke_width=4, # 轮廓
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
    text = MyText(string_txt)
    text.next_to(arrow, direction)
    return VGroup(arrow, text)


def create_element(strings, radius=0.3):
    elements = VGroup()
    for str in strings:
        element = VGroup()
        circle = Circle(radius=radius, stroke_color=BLUE)
        character = TextMobject(str, color=RED).move_to(circle.get_center())
        element.add(circle, character)
        elements.add(element)
    return elements


class Stack(Scene):
    def construct(self):
        ################################################################
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
        ori_title =TextMobject("栈", color=RED, fontsize=42)
        self.play(Write(ori_title), Write(logo))
        self.wait(1)
        title = TextMobject("栈", fontsize=32).set_color(WHITE)
        title.to_edge(UP)
        self.play(ReplacementTransform(ori_title,title))
        # 栈的描述
        self.stack_description()
        # 演示
        self.stack_actions()

    def stack_description(self):
        # 栈的定义
        color_dict_1 = {"线性表": MAROON, "后进先出": GOLD, "栈底":GREEN, "栈顶": GREEN}
        stack_description = TextMobject("栈(stack)又名堆栈, 它是一种限定仅在表尾进行插入和删除操作的线性表。",
        "栈是允许在同一端进行插入和删除操作的特殊线性表,它按照后进先出(LIFO, last-in, first-out)的原则存储数据，",
        "先进入的数据被压入栈底，最后的数据在栈顶，需要读数据的时候从栈顶开始弹出数据。",
        alignment="\\raggedright", tex_to_color_map=color_dict_1).scale(0.55)
        stack_description.shift(2 * UP)
        self.play(Write(stack_description))
        self.wait(2)
        #
        stack_operation_1 = BulletedList("栈顶：允许元素插入与删除的表尾称为栈顶","栈底：表头称为栈底",
        "入栈：栈的插入操作", "出栈：栈的删除操作", dot_scale=BLUE).scale(0.5)
        stack_operation_1.next_to(stack_description, DOWN, buff=0.6, aligned_edge=LEFT)
        brace_1 = Brace(stack_operation_1, LEFT, color=GREEN)
        brace_1_text = TextMobject("相关\\\\", "概念").scale(0.5)
        brace_1_text.next_to(brace_1, LEFT)
        self.play(ShowCreation(VGroup(brace_1, brace_1_text)), FadeIn(stack_operation_1, running=2))
        self.wait(2)
        stack_operation_2 = BulletedList("push:入栈函数", "pop:出栈函数", "top: 获取栈顶元素",
        "empty: 判断栈是否为空", "size: 栈中元素的个数，即栈的长度", dot_color=BLUE).scale(0.5)
        stack_operation_2.next_to(stack_operation_1, RIGHT) 
        brace_2 = Brace(stack_operation_2, DOWN, color=BLUE)
        brace_2_text = TextMobject("Stack中的成员函数").scale(0.5)
        brace_2_text.next_to(brace_2, DOWN)
        self.play(FadeIn(stack_operation_2, run_time=2))
        self.play(Write(VGroup(brace_2, brace_2_text)))
        self.wait(2)
        self.play(Uncreate(VGroup(stack_description, stack_operation_1, stack_operation_2, brace_2, brace_2_text, brace_1, brace_1_text)))
        
    def stack_actions(self):
        str_description = TextMobject("假设有字符串列表为:str = ['A', 'B', 'C', 'D', 'E'], 设栈为Stack, 下面动态演示str中的元素进栈和出栈操作",
        alignment="\\raggedright").scale(0.55)
        str_description.shift(2 * UP)
        self.play(Write(str_description))
        # 栈的线条
        line_top = 1
        line_bottom = -3
        line_left = 2
        line_1 = Line(start = [line_left, line_bottom, 0], end = [line_left, line_top, 0], color = GREEN)
        line_2 = Line(start = [line_left + 1, line_bottom, 0], end = [line_left + 1, line_top, 0], color = GREEN)
        line_3 = Line(start = [line_left, line_bottom, 0], end = [line_left + 1, line_bottom, 0], color = GREEN)
        stack_txt = MyText("栈").next_to(line_3, DOWN)
        self.play(ShowCreation(VGroup(line_1, line_2, line_3)), ShowCreation(stack_txt))
        # 箭头
        bottom_arrow = arrow_build(start=RIGHT, end=LEFT, color=GREEN, string_txt="栈底", direction=RIGHT)
        top_arrow = arrow_build(start=RIGHT, end=LEFT, color=RED, string_txt="栈顶", direction=RIGHT)
        # 元素
        radius = 0.3
        string_txt = "ABCDE"
        str_objects = create_element(string_txt, radius)
        actions_strs = ["push", "push", "pop", "push", "pop", "push", "push", "pop","pop", "pop"]
        # 进栈出栈位置定义
        S = []
        push_index = 0
        current_positions = [line_left + 0.5, line_bottom + radius, 0] # 下一个进展元素到达的位置
        ori_positions = [line_left + 0.5, line_top + 0.5, 0] # 进栈起始位置
        final_positions = [line_left * (-1) - 1, line_bottom, 0] # 出栈后元素的位置
        # 出栈序列label
        str_out_stack = TextMobject("出栈序列：").scale(0.5)
        str_out_stack.move_to([line_left * (-1) - 2, line_bottom, 0])
        self.play(Write(str_out_stack))
        # 显示栈和此刻操作
        stack_txt_tmp = TextMobject("假设栈为S,进出栈流程：").scale(0.5)
        stack_txt_tmp.move_to([-3, 1.2, 0])
        self.play(Write(stack_txt_tmp))
        #
        tmp_text = TextMobject("进/出", color=GOLD).scale(0.7)
        tmp_text.move_to(UP + RIGHT)
        self.play(Write(tmp_text))
        # bottom positions
        bottom_positions = [line_left + 1.7, line_bottom + 0.3, 0]
        bottom_arrow.move_to(bottom_positions)
        #
        index = 1
        for action_str in actions_strs:
            #print("S: ", S)
            current_str = str(index) + ": "
            if action_str is "push":
                # 进栈操作
                push_text = TextMobject("进栈", color=GOLD).scale(0.7)
                push_text.move_to(UP + RIGHT)
                self.play(ReplacementTransform(tmp_text, push_text))
                tmp_text = push_text
                #print(tmp_text.get_center())
                #print("进栈", string_txt[push_index])
                S.append(string_txt[push_index]) # 进栈
                current_str += string_txt[push_index] + "进栈,栈S为:" # 记录
                element = str_objects[push_index]
                element.move_to(ori_positions)
                self.play(ShowCreation(element))
                # actions
                R1 = Line(start = ori_positions, end = current_positions)
                self.play(MoveAlongPath(element, R1),run_time=2,rate_func=linear)
                #
                current_positions[1] += 2 * radius
                push_index += 1
            elif action_str is "pop":
                # 出栈操作
                pop_text = TextMobject("出栈", color=GOLD).scale(0.7)
                pop_text.move_to(UP + RIGHT)
                self.play(ReplacementTransform(tmp_text, pop_text))
                tmp_text = pop_text
                #
                top_index = string_txt.index(S[-1]) # 栈顶下标
                current_str += S[-1] + "出栈,栈S为:"
                #print("出栈", string_txt[top_index])
                S.pop()  # 出栈
                element = str_objects[top_index]
                # actions
                R2 = Line(start=current_positions, end=ori_positions)
                self.play(MoveAlongPath(element, R2),run_time=2,rate_func=linear)
                #
                arc = ArcBetweenPoints(start=np.array(ori_positions), end=np.array(final_positions), angle=TAU / 4)
                self.play(MoveAlongPath(element, arc),run_time=2,rate_func=linear)
                #
                final_positions[0] += 2 * radius
                current_positions[1] -= 2 * radius
            # top arrow position
            top_positions = current_positions.copy()
            top_positions[0] += 1.2
            top_positions[1] -= 2 * radius
            top_arrow.move_to(top_positions)
            for s in S:
                current_str += s
            #
            if index == 10:
                stack_txt = TextMobject(current_str + "空。结束！").scale(0.4)
            else:
                stack_txt = TextMobject(current_str + "\\\\").scale(0.4)
            stack_txt.next_to(stack_txt_tmp, 0.35 * DOWN, aligned_edge=LEFT)
            stack_txt_tmp = stack_txt
            self.play(Write(stack_txt_tmp))
            #
            if index == 9:
                self.play(Uncreate(VGroup(bottom_arrow, top_arrow)))
            #
            index += 1



class Queue(Scene):
    def construct(self):
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
        ori_title =TextMobject("队列", color=RED, fontsize=42)
        self.play(Write(ori_title), Write(logo))
        self.wait(1)
        title = TextMobject("队列", fontsize=32).set_color(WHITE)
        title.to_edge(UP)
        self.play(ReplacementTransform(ori_title,title))
        #
        self.queue_description()
        #self.queue_actions()

    # 队列的描述
    def queue_description(self):
        # 队列
        color_dict={"队列":RED, "先进先出":ORANGE, "队尾":GREEN,"队头": BLUE}
        queue_description = TextMobject("队列(queue)是一种先进先出(first in first out, FIFO)的线性表,它只允许在表的一端进行插入",
        "而在另一端删除元素,最早进入队列的元素最早离开。在队列中，允许插入的一端叫做队尾(rear)，允许删除的一端则成为队头(front)", 
        alignment="\\raggedright", font="heiti", tex_to_color_map=color_dict).scale(0.5)
        queue_description.move_to(2 * UP)
        self.play(Write(queue_description))
        self.queue_illustrator()
        # 双端队列
        deque_color_dict = {"限定插入和删除操作在表的两端进行的线性表": GOLD}
        deque_description = TextMobject("双端队列(deque)是限定插入和删除操作在表的两端进行的线性表。这两端分别称作端点1和端点2",
        "在实际应用中,有输出受限的双端队列(即一个端点允许插入和删除，一个端点只允许插入的双端队列)和",
        "输入受限的双端队列(即一个端点允许插入和删除，一个端点只允许删除的双端队列)。", tex_to_color_map=deque_color_dict,
        alignment="\\raggedright", font="heiti").scale(0.5).shift(2 * UP)
        self.play(ReplacementTransform(queue_description, deque_description))
        self.queue_illustrator(is_dequeued=True)
        #循环队列
   

    def queue_illustrator(self, is_dequeued=False):
        line_left = -2
        line_bottom = -1
        line_1 = Line(start = [line_left, line_bottom, 0], end = [line_left * (-1), line_bottom, 0], color = GREEN)
        line_2 = Line(start = [line_left, line_bottom + 1, 0], end = [line_left * (-1), line_bottom + 1, 0], color = GREEN)
        lines_group= VGroup(line_1, line_2)
        #
        string_txt = "ABCDE"
        radius = 0.3
        str_objects = create_element(string_txt, radius)
        position = [line_left+radius, line_bottom + 0.5, 0]
        object_group = VGroup()
        for i in range(5):
            item = str_objects[i]
            item.move_to(position)
            position[0] += 3* radius
            object_group.add(item)
        #
        if not is_dequeued:
            queue_text = MyText("队列的示意图").next_to(line_2, UP)
            bottom_arrow = arrow_build(start=DOWN, end=UP, color=RED, string_txt="对头", direction=DOWN)
            bottom_arrow.next_to(object_group[0], DOWN)
            top_arrow = arrow_build(start=DOWN, end=UP, color=RED, string_txt="队尾", direction=DOWN)
            top_arrow.next_to(object_group[4], DOWN)
            #
            front_arrow = arrow_build(start=RIGHT, end=LEFT, color=BLUE, string_txt="出队列", direction=UP)
            rear_arrow = arrow_build(start=RIGHT, end=LEFT, color=GREEN, string_txt="入队列", direction=UP)
            front_arrow.move_to([line_left -1, line_bottom + 0.5, 0])
            rear_arrow.move_to([line_left*(-1) +1, line_bottom + 0.5, 0])
            arrow_group = VGroup(queue_text, bottom_arrow, top_arrow, front_arrow, rear_arrow)
        else:
            de_queue_text = MyText("双端队列的示意图").next_to(line_2, UP)
            bottom_arrow = arrow_build(start=DOWN, end=UP, color=RED, string_txt="端1", direction=DOWN)
            bottom_arrow.next_to(object_group[0], DOWN)
            top_arrow = arrow_build(start=DOWN, end=UP, color=RED, string_txt="端2", direction=DOWN)
            top_arrow.next_to(object_group[4], DOWN)
            front_arrow_del = arrow_build(start=RIGHT, end=LEFT, color=BLUE, string_txt="删除", direction=LEFT)
            front_arrow_inp = arrow_build(start=LEFT, end=RIGHT, color=GREEN, string_txt="插入", direction=LEFT)
            rear_arrow_del = arrow_build(start=LEFT, end=RIGHT, color=BLUE, string_txt="删除", direction=RIGHT)
            rear_arrow_inp = arrow_build(start=RIGHT, end=LEFT, color=GREEN, string_txt="插入", direction=RIGHT)
            front_arrow_del.move_to([line_left -1, line_bottom + radius, 0])
            front_arrow_inp.move_to([line_left -1, line_bottom + 2 * radius, 0])
            rear_arrow_del.move_to([line_left*(-1) +1, line_bottom + radius, 0])
            rear_arrow_inp.move_to([line_left*(-1) +1, line_bottom + 2 * radius, 0])
            arrow_group = VGroup(de_queue_text, bottom_arrow, top_arrow, front_arrow_inp, front_arrow_del, rear_arrow_del, rear_arrow_inp)
        self.play(Write(VGroup(lines_group, object_group, arrow_group)), run_time=3)
        self.wait(3)
        self.play(Uncreate(VGroup(lines_group, object_group, arrow_group)))

    # 队列动作实例
    def queue_actions(self):
         # 队列的线条
        line_top = 1
        line_bottom = -3
        line_left = 2
        line_1 = Line(start = [line_left, line_bottom, 0], end = [line_left, line_top, 0], color = GREEN)
        line_2 = Line(start = [line_left + 1, line_bottom, 0], end = [line_left + 1, line_top, 0], color = GREEN)
        line_3 = Line(start = [line_left, line_bottom, 0], end = [line_left + 1, line_bottom, 0], color = GREEN)
        stack_txt = MyText("栈").next_to(line_3, DOWN)
        self.play(ShowCreation(VGroup(line_1, line_2, line_3)), ShowCreation(stack_txt))


class StackToQueue(Scene):
    def construct(self):
        self.camera.background_color = BLACK


class QueueToStack(Scene):
    def construct(self):
        self.camera.background_color = BLACK



