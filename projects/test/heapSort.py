from ctypes import alignment
from operator import index
from os import path
from tkinter import font
from tokenize import String
from tracemalloc import start
from turtle import circle, dot, position, width
from cv2 import line
from matplotlib.pyplot import arrow, axes
from nbformat import write
from sklearn import tree
from manim import *
from manimlib.imports import *
import random
import numpy as np

class Graph:
    def __init__(self, data, graph_datas, positions, radius):
        self.elements = self.create_element(data, positions, radius)
        self.line_groups = self.build_graph(graph_datas)

    def create_element(self, data, position, radius):
        elements = VGroup()
        for i, value in enumerate(data):
            element = VGroup()
            circle = Circle(radius=radius, stroke_color=BLUE)
            circle.move_to(position[i])
            number = Integer(value).move_to(circle.get_center())
            index = Integer(i).scale(0.3).next_to(circle, 0.1*DOWN)
            element.add(circle, number, index)
            elements.add(element)
        return elements

    def build_graph(self, graph_datas):
        #
        lines_groups = VGroup()
        length = len(graph_datas)
        for i in range(length):
            element_1 = self.elements[graph_datas[i][0] - 1]
            element_2 = self.elements[graph_datas[i][1] - 1]
            line = Line(start=element_1.get_center(), end=element_2.get_center(),color=GREEN, buff=.42)
            lines_groups.add(line)
        return lines_groups

class Arrays:
    def __init__(self, data, positions):
        self.data = data
        self.positions = positions
        #self.array_groups = self.get_arrays()
    
    def get_arrays(self):
        length = len(self.data)
        array_groups = VGroup()
        for i in range(length):
            items = VGroup()
            rect = Rectangle(height=0.7, width=0.7, color=PURPLE)
            if i == 0:
                rect.move_to(self.positions)
            else:
                rect.next_to(array_groups[i-1][0], RIGHT, buff=0.05)
            integer = Integer(self.data[i], color=RED).move_to(rect.get_center())
            index = Integer(i).scale(0.3).next_to(rect, 0.1*UP)
            items.add(rect, integer, index)
            array_groups.add(items)
        return array_groups

class  Heap_Sort_cover(Scene):
    def construct(self):
       # logo
        logo_text = TextMobject("陶将",  font="lishu", color=RED, weight="bold")
        height = logo_text.get_height() + 2 * 0.2
        width = logo_text.get_width() + 2 * 0.3
        logo_ellipse = Ellipse(
            width=width,           
            height=height, stroke_width=0.5
        )
        logo_ellipse.set_fill(color=PURPLE,opacity=0.3)
        logo_ellipse.set_stroke(color=GRAY)
        logo_text.move_to(logo_ellipse.get_center())
        logo = VGroup(logo_ellipse, logo_text)
        logo.shift(np.array((5.5, 2.5, 0.)))  # left/right  up/dowm
        self.play(Write(logo))
        #
        text_1 = TextMobject("堆",color=YELLOW).scale(3).move_to([0,1.5,0])
        text_2 = TextMobject("排", color=YELLOW).scale(3).move_to([2,-1,0])
        text_3 = TextMobject("What", color=RED).scale(2).move_to([-4.5,1.5,0])
        text_5 = TextMobject("is", color=WHITE).scale(1).move_to([-2,1.5,0])
        text_4 = TextMobject("How", color=BLUE).scale(2).move_to([-2,-1,0])
        text_6 = TextMobject("to", color=WHITE).scale(1).move_to([0,-1,0])
        text_group = VGroup(text_1, text_2, text_3, text_4, text_5, text_6)
        self.play(Write(text_group))


class HeapSort(Scene):
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
        ori_title =TextMobject("堆排序", color=RED, fontsize=42)
        self.play(Write(ori_title), Write(logo))
        self.wait(1)
        title = TextMobject("堆排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(ReplacementTransform(ori_title,title))
        ################################################################
        self.heap_description()
        ################################################################
        # trees
        data = [83,96,38,7,11,9,27]
        graph_datas = [[1,2], [1,3], [2,4], [2,5], [3,6],[3,7]]
        left_right, top_bottom = -3, 2
        positions = [[left_right, top_bottom, 0], 
        [left_right - 2, top_bottom-1, 0], [left_right + 2, top_bottom - 1, 0], 
        [left_right - 3, top_bottom -2, 0], [left_right - 1, top_bottom-2, 0], 
        [left_right + 1, top_bottom-2, 0], [left_right + 3, top_bottom-2, 0]]
        trees = Graph(data=data, graph_datas=graph_datas, positions=positions, radius=0.4)
        array_groups = Arrays(data=data, positions=[2, 1, 0]).get_arrays()
        self.play(ShowCreation(VGroup(trees.elements, trees.line_groups)), ShowCreation(array_groups))
        #
        length = len(data)
        lines_length = len(trees.line_groups)
        #
        steps_description = ["构造初始堆, 将给定无序序列构建成一个大顶堆。从最后一个非叶子结点开始(第一个非叶子结点 length/2-1=7/2-1=2,),从左至右,从下至上进行调整。", 
        "初始序列已符合大顶堆的要求,下面需要开始"+str(length-1)+"次的循环得到每次的最大值和重新调整大顶堆。", 
        "将根节点和末尾结点交换，然后重新调整大顶堆,重建堆时每次都是从根节点往下循环查找,自上而下。", "大顶堆已调节完成, 开始下一次交换和调整。"]
        color_dict = {"最后一个非叶子结点": GOLD, "从下至上": ORANGE, "自上而下": PURPLE, "6次": PURPLE}
        step_one_description = TextMobject(steps_description[0], alignment="\\raggedright", tex_to_color_map=color_dict).scale(0.5)
        step_one_description.move_to([0,-1.5,0])
        self.play(Write(step_one_description))
        self.wait(4)
        ########
        descriptions = ["从下标为2的元素38开始调整堆,记录tmp=38,指针为index=2。从下标为5的左子点9开始,左子点9小于右子点27,右子节点为节点中的最大值。下标加1,此次调整完成。",
        "从下标为1的元素96开始调整堆,记录tmp=96,指针为index=1。从下标为3的左子点7开始,左子点7小于右子点11,右子节点为节点中的最大值。下标加1,此次调整完成。",
        "从下标为0的元素83开始调整堆,记录tmp=83,指针为index=0。从下标为1的左子点96开始,子节点96大于tmp=83,将子节点的值赋予于指针所指的元素:data[0]=96,并将子节点的下标赋值给指针index=1。从下标为3的左子点7开始,左子点7小于右子点11,右子节点为节点中的最大值,下标加1。将83赋给指针index=1所指的位置:data[1] =83。此次调整完成。",
        "从下标为0的元素27开始调整堆,记录tmp=27,指针为index=0。从下标为1的左子点83开始,子节点83大于tmp=27,将子节点的值赋予于指针所指的元素:data[0]=83,并将子节点的下标赋值给指针index=1。从下标为3的左子点7开始,左子点7小于右子点11,右子节点为节点中的最大值,下标加1。将27赋给指针index=1所指的位置:data[1] =27。此次调整完成。",
        "从下标为0的元素9开始调整堆,记录tmp=9,指针为index=0。从下标为1的左子点27开始,左子点27小于右子点38,右子节点为节点中的最大值。下标加1,子节点38大于tmp=9,将子节点的值赋予于指针所指的元素:data[0] =38,并将子节点的下标赋值给指针index=2。将9赋给指 针index=2所指的位置:data[2] =9。此次调整完成。",
        "从下标为0的元素11开始调整堆,记录tmp=11,指针为index=0。从下标为1的左子点27开始,子节点27大于tmp=11,将子节点的值赋予于指针所指的元素:data[0]=27,并将子节点的下标赋值给指针index=1。从下标为3的左子点7开始,将11赋给指针index=1所指的位置:data[1]=11。此次调整完成。",
        "从下标为0的元素7开始调整堆,记录tmp=7,指针为index=0。从下标为1的左子点11开始,子节点11大于tmp=7,将子节点的值赋予于指针所指的元素:data[0]=11,并将子节点的下标赋值给指针index=1。将7赋给指针index=1所指的位置:data[1]=7。此次调整完成。",
        "从下标为0的元素9开始调整堆,记录tmp=9,指针为index=0。从下标为1的左子点7开始,此次调整完成。",
        "从下标为0的元素7开始调整堆,记录tmp=7,指针为index=0。此次调整完成。",
        "从下标为0的元素7开始调整堆,记录tmp=7,指针为index=0。此次调整完成。"]
        descriptions_index = 0
        descriptions_color_dict = {
            "tmp=": MAROON, "index=1": ORANGE, "index=0": ORANGE, "index=2": ORANGE,
            "27": TEAL,"38": GREEN,"96": YELLOW,
            "11": GOLD,"83": RED, "0": PURPLE, "指针": GRAY}
        ###构造大顶堆，从非叶子结点开始倒序遍历
        for i in range(length//2-1, -1, -1):
            text = TextMobject(descriptions[descriptions_index], alignment="\\raggedright", tex_to_color_map=descriptions_color_dict).scale(0.5)
            text.next_to(step_one_description, DOWN, aligned_edge=LEFT)
            self.play(Write(text), run_time=1)
            self.wait(3)
            self.adjust_heap(data, trees, array_groups, i, length)
            descriptions_index += 1
            self.play(Uncreate(text))
        # 初始堆完成
        step_two_description = TextMobject(steps_description[1], alignment="\\raggedright", tex_to_color_map=color_dict).scale(0.5)
        step_two_description.move_to([0,-1.5,0])
        self.play(ReplacementTransform(step_one_description, step_two_description))
        self.wait(2)
        # print(data)
        # for t in range(length):
        #     print(array_groups.submobjects[t][1].get_value(), trees.elements[t][1].get_value())
        # 上面的循环完成了大顶堆的构造，那么就开始把根节点和末尾结点交换，然后重新调整大顶堆。
        for j in range(length-1, -1, -1):
            # 文字描述
            step_swap_description = TextMobject(steps_description[2], alignment="\\raggedright", tex_to_color_map=color_dict).scale(0.5)
            step_swap_description.move_to([0,-1.5,0])
            self.play(ReplacementTransform(step_two_description, step_swap_description))
            #将堆顶元素与末尾元素进行交换
            tmp = data[0]
            data[0] = data[j]
            data[j] = tmp
            # array
            self.play(Swap(array_groups.submobjects[j].submobjects[1], array_groups.submobjects[0].submobjects[1]))
            submobjects_tmp = array_groups.submobjects[j].submobjects[1]
            array_groups.submobjects[j].submobjects[1] = array_groups.submobjects[0].submobjects[1]
            array_groups.submobjects[0].submobjects[1] = submobjects_tmp
            #
            self.play(Swap(trees.elements[j].submobjects[1], trees.elements[0].submobjects[1]))
            submobjects_trees = trees.elements[j].submobjects[1]
            trees.elements[j].submobjects[1] = trees.elements[0].submobjects[1]
            trees.elements[0].submobjects[1] = submobjects_trees
            trees.elements[j].submobjects[0].set_color(RED)
            lines_length -= 1
            self.play(Uncreate(trees.line_groups[lines_length]), ShowCreation(trees.elements[j].submobjects[0]))
            #### text 每次调整详细描述
            text = TextMobject(descriptions[descriptions_index],alignment="\\raggedright", tex_to_color_map=descriptions_color_dict).scale(0.5)
            descriptions_index +=1
            text.next_to(step_swap_description, DOWN, aligned_edge=LEFT)
            self.play(Write(text), run_time=1)
            # for t in range(length):
            #     print(array_groups.submobjects[t][1].get_value(), trees.elements[t][1].get_value())
            # 重新对堆进行调整
            self.adjust_heap(data, trees, array_groups, 0, j)
            # print(data)
            # for t in range(length):
            #     print(array_groups.submobjects[t][1].get_value(), trees.elements[t][1].get_value())
            # 文字描述
            step_after_swap_description = TextMobject(steps_description[3]).scale(0.5)
            step_after_swap_description.move_to([0,-1.5,0])
            self.play(Uncreate(text),ReplacementTransform(step_swap_description, step_after_swap_description))
            step_two_description = step_after_swap_description
            self.wait(1)
        self.play(Uncreate(VGroup(trees.elements, trees.line_groups, array_groups, step_two_description)))
        ########################################################################
        self.code_complexity()
        self.wait(2)

        
    # 构建堆
    def adjust_heap(self, data, trees, array_groups, index, len):
        # 取出index位置的元素
        tmp = data[index]
        begin = index
        submobjects_tmp = array_groups.submobjects[index].submobjects[1]
        submobjects_trees = trees.elements[index].submobjects[1]
        # play
        self.play(ShowCreation(array_groups.submobjects[index].submobjects[1].shift(DOWN)))
        self.play(ShowCreation(trees.elements[index].submobjects[1].shift(RIGHT)))
        #
        #string_text =  "从下标为" + str(index) + "的元素"+str(data[index])+"开始调整堆,记录tmp="+str(data[index])+",指针为index="+str(index)+"。"
        # 从index节点的左子节点开始，也就是从2 * index+1开始
        k = 2 * index + 1
        while k < len:
            #string_text += "从下标为"+str(k) + "的左子点"+str(data[k]) + "开始，"
            #如果左子节点小于右子节点，k指向右子节点
            if (k+1) < len and data[k] < data[k+1]:
                #string_text += "左子点"+str(data[k])+"小于右子点" + str(data[k+1]) + ",右子节点为节点中的最大值。下标加1,"
                k += 1
            # 如果子节点大于父节点，将子节点的值赋给父节点
            if data[k] > tmp:
                #string_text += "子节点"+str(data[k])+"大于tmp="+str(tmp)+",将子节点的值赋予于指针所指的元素:"+"data["+str(index)+"] ="+str(data[k])+",并将子节点的下标赋值给指针index="+str(k)+"。"
                data[index] = data[k]
                # array
                array_groups.submobjects[index].submobjects[1] = array_groups.submobjects[k].submobjects[1]
                array_groups.submobjects[index].submobjects[1].move_to(array_groups.submobjects[index].submobjects[0].get_center())
                self.play(ShowCreation(array_groups.submobjects[index].submobjects[1]))
                # trees
                trees.elements[index].submobjects[1] = trees.elements[k].submobjects[1]
                trees.elements[index].submobjects[1].move_to(trees.elements[index].submobjects[0].get_center())
                self.play(ShowCreation(trees.elements[index].submobjects[1]))
                #
                index = k
            else:
                break
            k = 2 * k + 1
        # if begin == index:
        #     string_text +=  "此次调整完成。"
        #     #print(string_text)
        # else:
        #     string_text += "将"+str(tmp)+"赋给指针index="+str(index)+"所指的位置:" + "data["+str(index)+"] =" + str(tmp) + "。此次调整完成。"
        #     #print(string_text)
        #
        data[index] = tmp #将tmp值放到最终的位置
        array_groups.submobjects[index].submobjects[1] = submobjects_tmp
        #print("final, index=", index, array_groups.submobjects[index].submobjects[1].get_value())
        array_groups.submobjects[index].submobjects[1].move_to(array_groups.submobjects[index].submobjects[0].get_center())
        self.play(ShowCreation(array_groups.submobjects[index].submobjects[1]))
        # trees
        trees.elements[index].submobjects[1] = submobjects_trees
        trees.elements[index].submobjects[1].move_to(trees.elements[index].submobjects[0].get_center())
        self.play(ShowCreation(trees.elements[index].submobjects[1]))
        #
        self.play(ShowCreation(VGroup(array_groups.submobjects[begin].submobjects[1],trees.elements[begin].submobjects[1])))

    def heap_description(self):
        ############
        heap_color_dict = {"堆的定义如下:":RED,
        "堆":RED, 
        "堆的最大值(最小值)总是位于根节点":ORANGE, 
        "完全二叉树": GREEN}
        heap_desc = TextMobject("堆的定义如下: n个元素的序列$\{k_{1}, k_{2}, \cdots , k_{n}\}$",
        "当且满足如下关系时,称之为堆。",alignment="\\raggedright", tex_to_color_map=heap_color_dict).scale(0.5)
        self.play(Write(heap_desc.shift(2*UP)), run_time=2)
        heap_desc_func_1 = TexMobject("k_{i} \leq k_{2i+1}  \\\\" "k_{i} \leq k_{2i+2}").scale(0.7)
        heap_desc_func_2 = TexMobject("k_{i} \geq k_{2i+1}  \\\\" "k_{i} \geq k_{2i+2}").scale(0.7)
        heap_desc_func_2_text = TextMobject("或").scale(0.5)
        heap_desc_func_3 = TexMobject("i = 0, 1, 2, \cdots, \left \lfloor \\frac{n}{2} \\right \\rfloor - 1").scale(0.5)
        heap_desc_func = VGroup(heap_desc_func_1, heap_desc_func_2_text, heap_desc_func_2, heap_desc_func_3)
        self.play(Write(heap_desc_func.arrange_submobjects(RIGHT).next_to(heap_desc, DOWN)), run_time=2)
        heap_bull_list = BulletedList("大顶堆：每个节点的值都大于其子节点的值;",
        "小顶堆：每个节点的值都小于其子节点的值。", dot_color=BLUE).scale(0.5)
        heap_bull_list.next_to(heap_desc_func, 2 * DOWN, aligned_edge=LEFT)
        self.play(Write(heap_bull_list), run_time=2)
        self.wait(3)
        self.play(Write(heap_bull_list.scale(0.5).next_to(heap_desc_func, DOWN, aligned_edge=RIGHT)))
        #
        data = [96,83,27,38,11,9,7]
        graph_datas = [[1,2], [1,3], [2,4], [2,5], [3,6],[3,7]]
        left_right, top_bottom = -3, -0.5
        positions = [[left_right, top_bottom, 0], 
        [left_right - 2, top_bottom-1, 0], [left_right + 2, top_bottom - 1, 0], 
        [left_right - 3, top_bottom -2, 0], [left_right - 1, top_bottom-2, 0], 
        [left_right + 1, top_bottom-2, 0], [left_right + 3, top_bottom-2, 0]]
        trees = Graph(data=data, graph_datas=graph_datas, positions=positions, radius= 0.4)
        heap_illustrator_text = TextMobject("堆的逻辑表示").scale(0.5)
        heap_illustrator_text.move_to([-3,-3.5,0])
        #
        array_groups = Arrays(data=data, positions=[2, -1, 0]).get_arrays()
        array_illustrator_text = TextMobject("数组储存结构").scale(0.5)
        array_illustrator_text.next_to(array_groups, DOWN)
        # 数组储存结构
        self.play(ShowCreation(VGroup(array_groups, array_illustrator_text)))
        self.wait(2)
        # 逻辑表示
        self.play(ShowCreation(VGroup(trees.elements, trees.line_groups, heap_illustrator_text)))
        self.wait(2)
        ##
        self.play(Uncreate(VGroup(trees.elements, trees.line_groups, heap_illustrator_text)))
        self.play(Uncreate(VGroup(array_groups, array_illustrator_text)))
        ######
        heap_sort_desc = TextMobject("堆是一个近似完全二叉树的结构，且每个节点的值都大于(或小于)其子节点的值。",
        "堆的这个性质使得堆的最大值(最小值)总是位于根节点。","堆排序(Heap Sort)是基于堆这种数据结构的一种排序算法。",
        alignment="\\raggedright", tex_to_color_map=heap_color_dict).scale(0.5).shift(2 * UP)
        self.play(ReplacementTransform(VGroup(heap_desc, heap_desc_func, heap_bull_list), heap_sort_desc), run_time=2)
        self.wait(2)
        heap_sort_dict = {"堆的排序过程":RED, "最大堆":ORANGE, "最大值":ORANGE, "最小堆":GREEN, "最小值":GREEN, "次大":ORANGE, "次小": GREEN}
        heap_sort_processors = TextMobject("堆的排序过程: 对于有n个元素的最大堆(最小堆),输出堆顶的最大值(最小值),",
        "剩下n-1个元素重新组成一个新的堆,那么堆顶元素则是n个元素中的次大(次小)值","如此反复，便能得到一个有序的序列。",
        alignment="\\raggedright", tex_to_color_map=heap_sort_dict).scale(0.5)
        heap_sort_processors.next_to(heap_sort_desc, DOWN, aligned_edge=LEFT)
        self.play(Write(heap_sort_processors), run_time=2)
        self.wait(2)
        heap_sort_list = BulletedList("如何由一个无序序列建成一个堆?","如何在输出堆顶元素之后，调整剩余元素称为一个新的堆？").scale(0.5)
        heap_sort_list.next_to(heap_sort_processors, DOWN, aligned_edge=LEFT)
        self.play(Write(heap_sort_list), run_time=2)
        self.wait(2)
        self.play(Uncreate(VGroup(heap_sort_desc, heap_sort_processors, heap_sort_list)))
    
    def code_complexity(self):
        #
        heap_sort_code = Code(file_name="F:\manim\\projects\\test\\codes\\heapSort.py", insert_line_no=False, 
        style=code_styles_list[11], language="python").scale(0.7)
        heap_sort_code.move_to([-4,-0.5,0])
        self.play(Write(heap_sort_code), run_time=5)
        self.wait(5)
        color_dict = {"建堆的时间复杂度为O(n)": RED,"自上而下调整堆结构的时间复杂度为O(nlogn)": ORANGE, 
        "O(nlogn)": GOLD, "空间复杂度为O(1)":GREEN, "n-1次": BLUE}
        complexity_description_1 =TextMobject("建堆的时间复杂度为O(n)。","对于一棵完全二叉树,树高为h=logn,对于第i层, 最多有$2^{i-1}$个元素", 
        "由于建堆时从第一个非叶子节点开始不断地从下往上调整,位于树倒数第二层的非叶子结点至多有$2^{h-2}$个元素，只需要一次线性比较就可调整成功",
        "位于树倒数第三层的非叶子结点至多有$2^{h-3}$个元素,其需要往下调整的层数最多为2;",
        "以此类推,位于树倒数第x层的非叶子结点至多有$2^{h-x}$个元素,其需要往下调整的层数最多为x-1。", 
        "设总的时间复杂度为$S = \sum_{x=2}^{h}2^{h-x}*(x-1)=2^{h}-h-1=n-logn-1$。", tex_to_color_map=color_dict,
        alignment="\\raggedright").scale(0.4)
        complexity_description_1.move_to([3,1,0])
        self.play(Write(complexity_description_1), run_time=2)
        complexity_description_2 = TextMobject("更改堆元素后重建堆,需要循环n-1次,每次都是从根节点往下循环查找,时间复杂度为logn。",
        "自上而下调整堆结构的时间复杂度为O(nlogn)。", tex_to_color_map=color_dict, alignment="\\raggedright").scale(0.4)
        complexity_description_2.next_to(complexity_description_1, DOWN, aligned_edge=LEFT)
        self.play(Write(complexity_description_2), run_time=2)
        complexity_description = TextMobject("综上所述:建堆的时间复杂度为O(n),建堆只需要一次;调整堆的时间复杂度为logn,需要n-1次,时间复杂度为O(nlogn)。",
        "所以堆排序的总时间复杂度为O(nlogn)。", tex_to_color_map=color_dict, alignment="\\raggedright").scale(0.4)
        complexity_description.next_to(complexity_description_2, DOWN, aligned_edge=LEFT)
        self.play(Write(complexity_description), run_time=2)
        space_description = TextMobject("堆排是就地排序,空间复杂度为O(1)。",alignment="\\raggedright", tex_to_color_map=color_dict).scale(0.4)
        space_description.next_to(complexity_description, DOWN, aligned_edge=LEFT)
        self.play(Write(space_description))
        self.wait(2)
        #self.play(Uncreate(VGroup(heap_sort_code, complexity_description_1, complexity_description_2, complexity_description, space_description)))
