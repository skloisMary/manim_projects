from manim import *
from manimlib.imports import *
import random

# Title: 排序
# Tags:
# Desc:
# Author: Mary
# Date:2022-02-19 15:43:55

class MyText(Text):
    CONFIG = {
        'font': 'songti',
        'size': 0.5
    }

class Array(VGroup):
    def __init__(self, array, run_time=0.5):
        super().__init__()
        self.run_time = run_time
        self.build_array(array)

    def build_array(self, array):
        for i, x in enumerate(array):
            cell = Integer(x).set_color(BLUE)
            if i != 0:
                cell.next_to(self, RIGHT, buff=1)
            self.add(cell)
        self.move_to(ORIGIN)

    def value_at_index(self, index):
        return self[index].get_value()
    
    def set_val_at_index(self, index, value):
        return self[index].set_value(value)
    
    def swap(self, scn, i, j):
        # swap
        tmp = self.submobjects[i];
        self.submobjects[i] = self.submobjects[j]
        self.submobjects[j] = tmp;

        scn.play(Swap(self.submobjects[i], self.submobjects[j]))


class bubbleSort_cover(Scene):
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
        logo.shift(np.array((6.5, 3.5, 0.)))
        self.play(Write(logo))
        #
        text_1 = TextMobject("冒泡排序", color=YELLOW).scale(2)
        text_1.shift(2 * UP)
        self.play(Write(text_1))
        #
        start_position = [-5.5, -0.5, 0]
        for i in range(8):
            radius = 0.3 +  0.05 * (i+1)
            circle = Circle(radius=radius, color=random_color(), stroke_width=4)
            # circle.set_fill(color=random_color(), opacity=0.3)
            circle.move_to(start_position)
            index = Integer((i+1)).move_to(circle.get_center())
            start_position[0] += 3 * radius
            self.play(ShowCreation(VGroup(circle, index)))


class bubbleSort(Scene):
    def construct(self):
        self.camera.background_color =  BLACK
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
        self.play(Write(logo))
        # descriptions
        title = TextMobject("冒泡排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        text_1  = MyText("冒泡排序, 是最简单的排序方法。它重复地走访过要排序的元素列,依次比较两个相邻的元素,")
        text_1.set_color_by_t2c(t2c={"冒泡排序": RED})
        text_2 = MyText("如果顺序错误就把他们交换过来。重复地进行直到没有相邻元素需要交换。")
        text_2.next_to(text_1, DOWN)
        text_groups = VGroup(text_1, text_2)
        text_groups.shift(2*UP)
        self.play(Write(text_groups))
        self.wait(1)
        text_3 = MyText("现在有一数组nums=[4, 1, 9, 3, 2, 7, 10, 6, 8, 5], 包含10个元素,使用冒泡排序对此数组进行升序排列。")
        text_3.set_color_by_t2c(t2c={"nums=[4, 1, 9, 3, 2, 7, 10, 6, 8, 5]": GREEN, "升序": RED_E})
        text_3.shift(UP*2)
        self.play(ReplacementTransform(text_groups, text_3))
        text_steps = BulletedList(
            "第一轮:从nums[0]开始,依次比较两个相邻的元素直到nums[9], 如果左边的元素大于右边的元素, 交换它们。那么nums[9]就是最大的元素", 
            "第二轮:从nums[0]开始,依次比较两个相邻的元素直到nums[8], 如果左边的元素大于右边的元素,交换它们。那么nums[8]就是第二大的元素",
            "...",
            "第九轮:比较nums[0]和nums[1],如果nums[0]大于nums[1],交换它们。至此排列完成", dot_color=BLUE
        )
        text_steps.scale(0.5)
        text_steps.next_to(text_3, DOWN * 2)
        self.play(Write(text_steps))
        self.wait(3)
        text_steps.scale(0.5)
        text_steps.shift(2 * (DOWN + RIGHT))
        self.play(Write(text_steps))
        # sort  arrays
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr)
        arr_mob.set_width(10)
        # 显示创建过程
        self.play(ShowCreation(arr_mob))
        self.wait(2)

        # index
        group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            group.add(index)
        self.play(ShowCreation(group))
        #
        # bubble sort
        tmp = MyText("开始排序:")
        tmp.next_to(arr_mob[0], 2 * UP)
        for i in range(len(arr) - 1):
            text = MyText("第" + str(i + 1) + "轮:", color=RED)
            text.next_to(arr_mob[0], UP)
            self.play(ReplacementTransform(tmp, text))
            for j in range(len(arr) - 1 - i):
                self.play(Indicate(arr_mob[j]), Indicate(arr_mob[j + 1]))
                if arr_mob.value_at_index(j) > arr_mob.value_at_index(j + 1):
                    if i == 0:
                        gt_text= MyText(str(arr_mob.value_at_index(j)) + ">" + str(arr_mob.value_at_index(j+1)), color=GREEN)
                        gt_text.next_to(arr_mob[j], DOWN)
                        self.play(Write(gt_text))
                        exchange_text = MyText("交换"+ str(arr_mob.value_at_index(j)) + "和" + str(arr_mob.value_at_index(j+1)), color=GREEN)
                        exchange_text.next_to(arr_mob[j], DOWN)
                        self.play(ReplacementTransform(gt_text, exchange_text))
                        arr_mob.swap(self, j, j + 1)
                        self.play(Uncreate(exchange_text)) 
                    else:
                        arr_mob.swap(self, j, j + 1)
                else:
                    if i == 0:
                        lt_text= MyText(str(arr_mob.value_at_index(j)) + "<" + str(arr_mob.value_at_index(j+1)), color=RED)
                        lt_text.next_to(arr_mob[j], DOWN)
                        self.play(Write(lt_text))
                        exchange_text = MyText("不交换"+ str(arr_mob.value_at_index(j)) + "和" + str(arr_mob.value_at_index(j+1)), color=RED)
                        exchange_text.next_to(arr_mob[j], DOWN)
                        self.play(ReplacementTransform(lt_text, exchange_text))
                        self.play(Uncreate(exchange_text)) 
            tmp = text
            arr_mob[len(arr) - 1 - i].set_color(RED)
        # 
        self.play(Uncreate(tmp), Uncreate(text_3), Uncreate(text_steps))
        self.play(Uncreate(VGroup(arr_mob,group)))
        # 新的一帧
        # 冒泡代码
        rendered_code = Code(file_name="F:\manim\\projects\\test\\codes\\bubbleSort.py", style=code_styles_list[14], language="Python").scale(0.7)
        rendered_code.to_edge(LEFT)
        # 性能分析
        text_4 = TextMobject("以升序为例,假设待排序数组长度为n,冒泡排序需要两层for循环,\\\\",
            "冒泡排序算法在每一轮排序中会使一个元素排到一端,\\\\",
            "外层循环循环n-1次,每轮排序都需要相邻的两个元素进行比较。\\\\",
            "在最坏的情况（降序排列）下,内层循环最多时循环n-1次,时间复杂度为$O\left( n^{2}\\right)$;\\\\",
            "在最好的情况（升序排列）下,最少循环0次,时间复杂度为$O\left( n \\right)$。\\\\", 
            "冒泡排序的平均时间复杂度为$O\left( n^{2} \\right)$。\\\\",
            "冒泡排序用到的空间只有交换时的临时变量,空间复杂度为$O\left( 1 \\right)$。", alignment="\\raggedright").scale(0.4)
        text_4.next_to(rendered_code, RIGHT)
        self.play(ShowCreation(rendered_code))
        self.play(ShowCreation(text_4), runtime=2)
        self.wait(5)

        
class QuickSort(Scene):
    def construct(self):
        self.description()
        self.camera.background_color =  WHITE
        self.sort_array()
        
    def description(self):
        title = TextMobject("快排", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))

    def sort_array(self):
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr)
        arr_mob.set_width(10)
        # 显示创建过程
        self.play(ShowCreation(arr_mob))
        self.wait(1)
        
        # quick sort 
        # 1st
        low = self.partition(arr_mob, 0, len(arr)-1)
        # 2st
        self.partition(arr_mob, 0, low-1)
        low_1 = self.partition(arr_mob, low + 1, len(arr)-1)
        # 3nd
        self.partition(arr_mob, low + 1, low_1 - 1)
        # 4st
        self.partition(arr_mob, low+2, low_1 - 1)
        #
        self.wait()

    def partition(self, arrays_mob, start, end):
        if start < end:
            low = start
            high = end
            pivot = arrays_mob.value_at_index(low)
            while(low < high):
                while(arrays_mob.value_at_index(high) >= pivot and low < high):
                    high -= 1
                arrays_mob.swap(self, low, high)
                while(arrays_mob.value_at_index(low) <= pivot and low < high):
                    low += 1
                arrays_mob.swap(self, low, high)
            arrays_mob[low].set_value(pivot)
        return low
        
        
class Insertion(Scene):
    def construct(self):
        #self.description()
        self.camera.background_color =  WHITE
        self.sort_array()
    
    def sort_array(self):
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr)
        arr_mob.set_width(10)
        # 显示创建过程
        self.play(ShowCreation(arr_mob))
        self.wait(2)

        # index
        group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            group.add(index)
        self.play(ShowCreation(group))
        #
        current_arrow = Arrow(
            start=DOWN, 
            end=UP, 
            color=RED, 
            buff=0.8, 
            tip_length=0.2, 
            stroke_width=4, 
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
        #
        length = len(arr)
        for i in range(1, length):
            current_arrow.next_to(arr_mob[i], DOWN)
            self.play(ShowCreation(current_arrow))
            current = arr_mob.value_at_index(i)
            for preindex in range(i - 1, -1, -1):
                if(arr_mob.value_at_index(preindex) > current):
                    arr_mob.swap(self, preindex, preindex + 1)
                    current_arrow.next_to(arr_mob[preindex], DOWN)
                    self.play(ShowCreation(current_arrow))
                    preindex -= 1


class ShellSort(Scene):
    def construct(self):
        self.description()
        self.camera.background_color =  WHITE
        self.sort_array()
    
    def description(self):
        title = TextMobject("冒泡排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        shell_text_1 = MyText("希尔排序是将待排序的数组元素 按下标的一定增量分组 ,分成多个子序列,然后对各个子序列进行直接插入排序算法排序;")
        shell_text_2 = MyText("然后依次缩减增量再进行排序,直到增量为1时,进行最后一次直接插入排序,排序结束。")
        shell_text_2.next_to(shell_text_1, DOWN)
        shell_text = VGroup(shell_text_1, shell_text_2)
        shell_text.shift(2*UP)
        self.play(Write(shell_text))

    def sort_array(self):
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr)
        arr_mob.set_width(10)
        # 显示创建过程
        self.play(ShowCreation(arr_mob))
        self.wait(2)

        # index
        group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            group.add(index)
        self.play(ShowCreation(group))
        # sort
        length = len(arr)
        d = length
        for k in  range(4):
            d = math.ceil(d/2)
            for i in range(d, length, 1):
                for j in range(i-d, -1, -d):
                    if (arr_mob.value_at_index(j) > arr_mob.value_at_index(j+d)):
                        arr_mob.swap(self, j, j+d)

class Selection(Scene):
    def construct(self):
        self.description()
        self.camera.background_color =  WHITE
        self.sort_array()
    
    def description(self):
        title = TextMobject("选择排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        # shell_text_1 = MyText("希尔排序是将待排序的数组元素 按下标的一定增量分组 ,分成多个子序列,然后对各个子序列进行直接插入排序算法排序;")
        # shell_text_2 = MyText("然后依次缩减增量再进行排序,直到增量为1时,进行最后一次直接插入排序,排序结束。")
        # shell_text_2.next_to(shell_text_1, DOWN)
        # shell_text = VGroup(shell_text_1, shell_text_2)
        # shell_text.shift(2*UP)
        # self.play(Write(shell_text))

    def sort_array(self):
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr)
        arr_mob.set_width(10)
        # sr_group = VGroup()
        # for i in range(len(arr)):
        #     arr_mob_box = SurroundingRectangle(arr_mob[i], color=GOLD_A, buff=.1)
        #     sr_group.add(arr_mob_box)
        # 显示创建过程
        self.play(ShowCreation(arr_mob))
        self.wait(2)

        # index
        group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            group.add(index)
        self.play(ShowCreation(group))
        # sort
        length = len(arr)
        for i in range(length - 1):
            minIndex = i
            for  j in range(i+1, length):
                if (arr_mob.value_at_index(j) < arr_mob.value_at_index(minIndex)):
                    minIndex = j
            if i != minIndex:
                arr_mob.swap(self, minIndex, i)

class Merge(Scene):
    def construct(self):
        self.description()
        self.camera.background_color =  WHITE
        self.sort_array()
    
    def description(self):
        title = TextMobject("归并排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        # shell_text_1 = MyText("希尔排序是将待排序的数组元素 按下标的一定增量分组 ,分成多个子序列,然后对各个子序列进行直接插入排序算法排序;")
        # shell_text_2 = MyText("然后依次缩减增量再进行排序,直到增量为1时,进行最后一次直接插入排序,排序结束。")
        # shell_text_2.next_to(shell_text_1, DOWN)
        # shell_text = VGroup(shell_text_1, shell_text_2)
        # shell_text.shift(2*UP)
        # self.play(Write(shell_text))

    def sort_array(self):
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr)
        arr_mob.set_width(10)
        # 显示创建过程
        self.play(ShowCreation(arr_mob))
        self.wait(2)

        # index
        group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            group.add(index)
        self.play(ShowCreation(group))
