from cgitb import text
from collections import deque
from ctypes.wintypes import DWORD
import queue
from tkinter import font
from turtle import left
from cv2 import circle, line
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
        "入栈：栈的插入操作", "出栈：栈的删除操作", dot_color=BLUE).scale(0.5)
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

class CircualGroup:
    def __init__(self, string_text, position):
        self.string_text = string_text
        self.position = position
        self.Annular_Sectors = self.get_Annular_Sector()
        self.Characters = self.get_Character()

    def get_Annular_Sector(self):
        element = VGroup()
        for i in range(len(self.string_text)):
            start_angle = i * TAU / 6
            annu_sector = AnnularSector(start_angle=start_angle, angle=TAU / 6., inner_radius=0.5,outer_radius=1,color=random_color())
            annu_sector.shift(self.position)
            element.add(annu_sector)
        return element
    
    def get_Character(self):
        element = VGroup()
        for i in range(len(self.string_text)):
            character = TextMobject(self.string_text[i], color=WHITE).move_to(self.Annular_Sectors[i].get_center()).scale(0.8)
            element.add(character)
        return element


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

    # 队列的描述
    def queue_description(self):
        # 队列
        color_dict={"队列":RED, "先进先出":ORANGE, "队尾":GREEN,"队头": BLUE}
        queue_description = TextMobject("队列(queue)是一种先进先出(first in first out, FIFO)的线性表,它只允许在表的一端进行插入",
        "而在另一端删除元素,最早进入队列的元素最早离开。在队列中，允许插入的一端叫做队尾(rear)，允许删除的一端则成为队头(front)", 
        alignment="\\raggedright", font="heiti", tex_to_color_map=color_dict).scale(0.5)
        queue_description.move_to(2 * UP)
        self.play(Write(queue_description), run_time=2)
        self.queue_illustrator()
        self.wait(2)
        queue_text = TextMobject("C++ STL中队列声明的基本格式是:queue<结构类型> 队列名", alignment="\\raggedright").scale(0.5)
        queue_text.next_to(queue_description, DOWN)
        self.play(Write(queue_text))
        queue_fun_bull_list = BulletedList("size: 返回队列中的元素个数", 
        "empty:判断队列是否为空","push:在队尾插入一个元素",
        "pop: 删除队列的第一个元素","front:返回队列的第一个元素",
        "back:返回队列的最后一个元素", dot_color=BLUE).scale(0.5)
        queue_fun_bull_list.next_to(queue_text, DOWN)
        self.play(Write(queue_fun_bull_list), run_time=2)
        self.wait(2)
        self.play(Uncreate(VGroup(queue_text, queue_fun_bull_list)))
        # 双端队列
        deque_color_dict = {"双端队列":RED, "限定插入和删除操作在表的两端进行的线性表": GOLD}
        deque_description = TextMobject("双端队列(deque)是限定插入和删除操作在表的两端进行的线性表。这两端分别称作端点1和端点2",
        "在实际应用中,有输出受限的双端队列(即一个端点允许插入和删除，一个端点只允许插入的双端队列)和",
        "输入受限的双端队列(即一个端点允许插入和删除，一个端点只允许删除的双端队列)。", tex_to_color_map=deque_color_dict,
        alignment="\\raggedright", font="heiti").scale(0.5).shift(2 * UP)
        self.play(ReplacementTransform(queue_description, deque_description))
        self.queue_illustrator(is_dequeued=True)
        self.wait(2)
        deque_text = TextMobject("C++ STL中队列声明的基本格式是:deque<结构类型> 队列名", alignment="\\raggedright").scale(0.5)
        deque_text.next_to(deque_description, DOWN)
        self.play(Write(deque_text))
        deque_fun_bull_list = BulletedList("size: 返回双向队列中的元素个数", 
        "empty:判断双向队列是否为空","push\_front:在队头插入一个元素","push\_back:在尾部加入一个元素",
        "pop\_front: 删除头部的元素","pop\_back:删除尾部的元素",
        "insert:插入一个元素", "erase:删除一个元素",dot_color=BLUE).scale(0.5)
        deque_fun_bull_list.next_to(deque_text, DOWN)
        self.play(Write(deque_fun_bull_list), run_time=2)
        self.wait(2)
        self.play(Uncreate(VGroup(deque_text, deque_fun_bull_list)))
        # 循环队列
        circular_color_dict = {"循环队列": RED, "逻辑上的环状空间": GREEN, "队列大小是固定的":GOLD}
        circular_queue=TextMobject("循环队列(circular queue)将队列存储空间的最后一个位置与第一个位置首尾相连，形成逻辑上的环状空间，供队列循环使用。",
        "在循环队列结构中，当存储空间的最后一个位置已被使用，而有新的元素要入队列时，",
        "只需要将存储空间的第一个位置空闲，将新元素加入到第一元素的位置即可。","循环队列的队列大小是固定的，可以防止伪溢出的发生。" ,
        tex_to_color_map=circular_color_dict, alignment="\\raggedright", font="heiti").scale(0.5).shift(2 * UP)
        self.play(ReplacementTransform(deque_description, circular_queue))
        self.wait(2)
        self.circularQueue()
        # 优先队列
        priority_color_dict = {"优先队列":RED, "优先级": PURPLE, "最高级先出": ORANGE, "堆排序": GOLD}
        priority_queue = TextMobject("优先队列(priority queue)中,元素被赋予优先级, 优先级最高的先出队列。", 
        "优先队列具有最高级先出(first in, larger in)的行为特性。","通常采用堆排序实现。",
        tex_to_color_map=priority_color_dict, alignment="\\raggedright", font="heiti").scale(0.5).shift(2 * UP)
        self.wait(2)
        self.play(ReplacementTransform(circular_queue, priority_queue))
        #
        priority_text = TextMobject("C++ STL中优先队列声明的基本格式是:priority\_queue<结构类型> 队列名", alignment="\\raggedright").scale(0.5)
        priority_text.next_to(priority_queue, DOWN)
        self.play(Write(priority_text))
        priority_bull_list = BulletedList("从大到小排序:priority\_queue<int,vector<int>,less<int> >q;",
        "从大到小排序:priority\_queue<int,vector<int>,greater<int> >q;",dot_color=BLUE).scale(0.5)
        priority_bull_list.next_to(priority_text, DOWN, aligned_edge=LEFT)
        self.play(Write(priority_bull_list), run_time=2)
        self.wait(2)
        priotiry_fun_bull_list = BulletedList("size: 返回优先队列中的元素个数", 
        "empty:判断优先队列是否为空","push:向优先队列插入元素",
        "pop: 删除优先队列的第一个元素","top:返回优先队列的第一个元素",dot_color=BLUE).scale(0.5)
        priotiry_fun_bull_list.next_to(priority_bull_list, DOWN)
        self.play(Write(priotiry_fun_bull_list), run_time=2)
        self.wait(2)
        self.play(Uncreate(VGroup(priority_text, priority_bull_list, priotiry_fun_bull_list)))
        # 单调队列
        monotone_color_dict = {"单调队列":RED, "某个范围内的最小值或者最大值": ORANGE, "N=8": ORANGE, "k=3": BLUE}
        monotone_queue = TextMobject("单调队列(monotone queue)是有某种单调性的队列,它分为两种,一种是单调递增,另一种是单调递减的。",
        "单调队列通常用来得到某个范围内的最小值或者最大值", tex_to_color_map=monotone_color_dict,
        alignment="\\raggedright", font="heiti").scale(0.5).shift(2 * UP)
        self.play(ReplacementTransform(priority_queue, monotone_queue))
        self.wait(2)
        monotone_queue_text = TextMobject("有一整数数组nums=[1,3,-1,-3,5,3,6,7],有N=8个元素,",
        "有一个大小为k=3的滑动窗口从数组的最左侧移动到数组的最右侧",
        "每次只能看到滑动窗口中的k个数字,滑动窗口每次只向右移动一位。",tex_to_color_map=monotone_color_dict,
        alignment="\\raggedright", font="heiti").scale(0.5)
        monotone_queue_text.shift(2 * UP)
        self.play(ReplacementTransform(monotone_queue, monotone_queue_text))
        self.wait(2)
        self.mon_queue_action()         
  

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

    # 循环队列
    def circularQueue(self):
        texts = ["假设循环队列的空间大小为MaxSize,当队列为空时,front=rear;",
        "而当队列空间全占满时,有front=rear。","为了区分这两种情况,规定循环队列最多只有MaxSize-1个队列元素",
        "队列判空的条件是front=rear","队列判满的条件是front=(rear+1)\% MaxSize","队列的长队为(rear-front + MaxSize) \% Maxsize"]
        string_text = "ABCDEF"
        position = DOWN + 4 * LEFT
        circual =  CircualGroup(string_text, position)
        # arrow
        front_arrow = arrow_build(start=RIGHT, end=LEFT, color=BLUE, string_txt="front", direction=RIGHT)
        rear_arrow = arrow_build(start=RIGHT, end=LEFT, color=GREEN, string_txt="rear", direction=RIGHT)
        self.play(Write(circual.Annular_Sectors))
        rear_arrow.next_to(circual.Annular_Sectors[0], RIGHT)
        front_arrow.next_to(rear_arrow, 0.3 * UP)
        circual_text = TextMobject("循环队列").scale(0.5)
        circual_text.next_to(circual.Annular_Sectors, DOWN)
        self.play(Write(VGroup(front_arrow, rear_arrow, circual_text)))
        self.wait(1)
        # 队列的一般情况
        for i in range(len(string_text)):
            self.play(Write(circual.Characters[i]), Rotating(rear_arrow, radians=TAU/6 , run_time=1, about_point=position))
            self.wait(1)
        text = TextMobject(texts[0], texts[1], texts[2], alignment="\\raggedright", font="heiti").scale(0.5)
        text.move_to([2.5, 0, 0])
        self.play(Write(text))
        self.wait(2)
        bul_list = BulletedList(texts[3], texts[4], texts[5]).scale(0.5)
        bul_list.move_to([2.5, -1, 0])
        self.play(ReplacementTransform(text, bul_list))
        self.wait(2)
        self.play(Uncreate(VGroup(circual.Annular_Sectors, circual.Characters, front_arrow, rear_arrow, circual_text, text, bul_list)))

    def mon_queue_action(self):
        nums = [1,3,-1,-3,5,3,6,7]
        length = len(nums)
        # array
        elements = VGroup()
        for i, x in enumerate(nums):
            cell = Integer(x).set_color(BLUE)
            if i != 0:
                cell.next_to(elements[i-1], RIGHT, buff=1)
            else:
                cell.move_to([-5, 0, 0])
            elements.add(cell)
        # copy
        elements_tmp = elements.copy()
        # index
        Indexs = VGroup()
        for i in range(length):
            index = Integer(i).scale(0.4)
            index.next_to(elements[i], 0.5*UP)
            Indexs.add(index)
        #
        self.play(Write(VGroup(elements, Indexs)), run_time=2)
        rect = Rectangle(color=RED, width=4.0, height=1.0)
        rect.move_to(elements[1].get_center())
        self.play(Write(rect), run_time=1)
        # 单调队列
        left_p, right_p = -5, 1
        bottom_p , top_p = -2, -1
        line_1 = Line(start = [left_p, top_p, 0], end = [right_p, top_p, 0], color = YELLOW)
        line_2 = Line(start = [left_p, bottom_p, 0], end = [right_p, bottom_p, 0], color = YELLOW)
        stack_txt = MyText("这是基于双端队列实现的单调队列").next_to(line_2, DOWN)
        #
        top_queue_positions = [left_p - 0.5, (bottom_p + top_p) / 2.0, 0]
        bottom_queue_positions = [right_p + 0.5, (bottom_p + top_p) / 2.0, 0]
        current_positions = [left_p, (bottom_p + top_p) / 2.0, 0]
        final_positions = [left_p, bottom_p - 1, 0]
        res_text = TextMobject("滑动窗口\\\\最大值", color=RED, front="heiti").scale(0.6)
        res_text.move_to([left_p - 1, bottom_p - 1, 0])
        #
        self.play(ShowCreation(VGroup(line_1, line_2, stack_txt, res_text)))
        #
        actions_text = MyText("单调队列求滑窗大小过程展示")
        self.wait(1)
        actions_text.move_to([right_p + 2, top_p , 0])
        self.play(Write(actions_text))
        res = []
        Q = []
        for i in range(3):
            text = MyText("第1个滑动窗口")
            text.move_to([right_p + 2, top_p , 0])
            self.play(ReplacementTransform(actions_text, text))
            actions_text = text
            while len(Q) > 0 and nums[Q[len(Q)-1]] <= nums[i]:
                text = MyText(str(nums[Q[len(Q)-1]]) + "<=" + str(nums[i]) + ",弹出" + str(nums[Q[len(Q)-1]]))
                text.move_to([right_p + 2, top_p , 0])
                self.play(ReplacementTransform(actions_text, text))
                actions_text = text
                front = Q[-1] #从队尾删除
                Q = Q[:-1]
                #出队列
                out_tmp = elements_tmp[front]
                out_lines = Line(start = out_tmp.get_center(), end = bottom_queue_positions)
                self.play(MoveAlongPath(out_tmp, out_lines),run_time=1,rate_func=linear)
                self.play(Uncreate(out_tmp))
                current_positions[0] -= 0.7
            Q.append(i)
            # 进队列
            in_tmp = elements_tmp[i]
            in_arc = ArcBetweenPoints(start=in_tmp.get_center(), end=np.array(bottom_queue_positions), angle=-TAU / 4)
            self.play(MoveAlongPath(in_tmp, in_arc),run_time=2,rate_func=linear)
            in_lines = Line(start = bottom_queue_positions, end = current_positions)
            self.play(MoveAlongPath(in_tmp, in_lines),run_time=2,rate_func=linear)
            current_positions[0] += 0.7
        res.append(nums[Q[0]])
        #
        text = MyText("取对首元素为:第1个滑动窗口的最大值")
        text.move_to([right_p + 2, top_p , 0])
        self.play(ReplacementTransform(actions_text, text))
        actions_text = text
        #
        res_tmp = elements_tmp[Q[0]].copy()
        out_arc = ArcBetweenPoints(start=np.array(res_tmp.get_center()), end=np.array(final_positions), angle= - TAU / 4)
        self.play(MoveAlongPath(res_tmp, out_arc),run_time=2,rate_func=linear)
        final_positions[0] += 0.5
        for i in range(3, length):
            rect.move_to(elements[i-1].get_center())
            self.play(Write(rect), run_time=1)
            text = MyText("第"+str(i-1) + "个滑动窗口")
            text.move_to([right_p + 2, top_p , 0])
            self.play(ReplacementTransform(actions_text, text))
            actions_text = text
            #
            while len(Q) > 0  and nums[Q[len(Q)-1]] <= nums[i]:
                text = MyText(str(nums[Q[len(Q)-1]]) + "<=" + str(nums[i]) + ",弹出" + str(nums[Q[len(Q)-1]]))
                text.move_to([right_p + 1, top_p , 0])
                self.play(ReplacementTransform(actions_text, text))
                actions_text = text
                #
                front = Q[-1] #从队尾删除
                Q = Q[:-1]
                out_tmp = elements_tmp[front]
                out_lines = Line(start = out_tmp.get_center(), end = bottom_queue_positions)
                self.play(MoveAlongPath(out_tmp, out_lines),run_time=1,rate_func=linear)
                self.play(Uncreate(out_tmp))
                current_positions[0] -= 0.7
            # 进队列
            Q.append(i)
            in_tmp = elements_tmp[i]
            in_arc = ArcBetweenPoints(start=in_tmp.get_center(), end=np.array(bottom_queue_positions), angle=-TAU / 4)
            self.play(MoveAlongPath(in_tmp, in_arc),run_time=2,rate_func=linear)
            in_lines = Line(start = bottom_queue_positions, end = current_positions)
            self.play(MoveAlongPath(in_tmp, in_lines),run_time=2,rate_func=linear)
            current_positions[0] += 0.7
            while Q[0] <= (i-3):
                front = Q.pop(0)
                #
                text = MyText("队列中仅保持当前滑窗的元素，弹出前滑窗的元素"+str(nums[front]))
                text.move_to([right_p + 2, top_p , 0])
                self.play(ReplacementTransform(actions_text, text))
                actions_text = text
                #
                out_tmp = elements_tmp[front]
                out_lines = Line(start = out_tmp.get_center(), end = top_queue_positions)
                self.play(MoveAlongPath(out_tmp, out_lines),run_time=2,rate_func=linear)
                self.play(Uncreate(out_tmp))
            #
            text = MyText("取对首元素为:第"+ str(i-1) +"个滑动窗口的最大值")
            text.move_to([right_p + 2, top_p , 0])
            self.play(ReplacementTransform(actions_text, text))
            actions_text = text
            #
            res.append(nums[Q[0]])
            res_tmp = elements_tmp[Q[0]].copy()
            out_arc = ArcBetweenPoints(start=res_tmp.get_center(), end=np.array(final_positions), angle= - TAU / 4)
            self.play(MoveAlongPath(res_tmp, out_arc),run_time=2,rate_func=linear)
            final_positions[0] += 0.5
            #
        text = TextMobject("单调队列中的元素一直保持降序排序，\\\\保证了对首元素为当前滑窗的最大值,\\\\时间复杂度为O(n)", color=RED, alignment="\\raggedright").scale(0.5)
        text.move_to([right_p + 3, top_p , 0])
        self.play(ReplacementTransform(actions_text, text))
        self.wait(2)