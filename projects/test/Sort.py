from cgitb import text
from operator import le, rshift
from tracemalloc import start
from turtle import circle, right
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
    def __init__(self, array, color=BLUE, ori_position=ORIGIN, run_time=0.5):
        super().__init__()
        self.run_time = run_time
        self.color = color
        self.ori_position = ori_position
        self.build_array(array)

    def build_array(self, array):
        for i, x in enumerate(array):
            cell = Integer(x).set_color(self.color)
            if i != 0:
                cell.next_to(self, RIGHT, buff=1)
            self.add(cell)
        self.move_to(self.ori_position)

    def value_at_index(self, index):
        return self[index].get_value()
    
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
        

# python -m manim F:\manim\\projects\\test\\Sort.py QuickSort  -p --media_dir F:\\manim_vedio_dirs
class QuickSort(Scene):
    def construct(self):
        self.description()
        self.camera.background_color =  WHITE
        self.low_arrow = self.get_arrows(start_position=DOWN, end_position=UP, text="low", color=GREEN)
        self.high_arrow = self.get_arrows(start_position=DOWN, end_position=UP, text="high", color=BLUE)
        self.sort_array()
        
    def description(self):
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
        self.play(Write(logo))
        #############
        title = TextMobject("快排", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        # 快排
        quicksort_desc = TextMobject("快速排序(Quick Sort)的 基本思想：通过一趟排序将一无序序列分割成独立的两个子序列,",
        "其中左序列的数值均比右序列的数值小，然后再分别对这两个子序列进行上述操作, 依次递归, 直到整个序列有序。",
        alignment="\\raggedright").scale(0.5).shift(2 * UP)
        self.play(Write(quicksort_desc, run_time = 2))
        # 一趟快排的具体做法
        one_round_quicksort_des = TextMobject("假设有一无序序列Array,第i个位置的数值为Array[i]。",
        "一趟快排的具体做法:设两个指针,它们所对应的下标分别为low和high,","取下标low的数值Array[low]作为轴点(pivot);",
        "首先从high处向前搜索找到第一个数值小于支点的元素, 并与轴点进行交换;",
        "然后从low处向后搜索,找到第一个数值大于支点的元素, 并与轴点进行交换. 重复前两步直到low=high为止.",
        "一趟快排结束后, 以轴点为分界线, 轴点前边的元素都小于轴点数值; 轴点右边的元素都大于轴点元素。", alignment="\\raggedright").scale(0.5)
        one_round_quicksort_des.next_to(quicksort_desc, DOWN)
        self.play(Write(one_round_quicksort_des, run_time = 4))
        self.wait(10)
        self.play(Uncreate(VGroup(quicksort_desc, one_round_quicksort_des)))

    def  get_arrows(self, start_position, end_position, text, color=RED):
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
        txt = TexMobject(text,color=color).scale(0.5).next_to(arrow, DOWN)
        return VGroup(arrow, txt)
    

    def sort_array(self):
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr, color=RED)
        arr_mob.set_width(10)

        S_Groups = VGroup()
        for  i in range(len(arr)):
            square = Square(side_length=0.5, color=BLUE_A, stroke_width=2)
            square.move_to(arr_mob[i].get_center())
            S_Groups.add(square)
        # 显示创建过程
        self.play(ShowCreation(VGroup(arr_mob, S_Groups)))
        self.wait(2)
        
        # quick sort 
        # 1st
        arr_mob[0].set_color(BLUE) # 更改pivot颜色
        low = self.partition(arr_mob, 0, len(arr)-1)
        self.wait(2)
        self.why_go_first_from_right()
        # 2st
        arr_mob[0].set_color(YELLOW)
        self.partition(arr_mob, 0, low-1)
        self.wait(2)
        arr_mob[low + 1].set_color(GREEN)
        low_1 = self.partition(arr_mob, low + 1, len(arr)-1)
        self.wait(2)
        # # 3nd
        arr_mob[low + 1].set_color(GOLD)
        self.partition(arr_mob, low + 1, low_1 - 1)
        self.wait(2)
        # # 4st
        arr_mob[low + 2].set_color(PURPLE)
        self.partition(arr_mob, low + 2, low_1 - 1)
        self.wait(2)
        finish_text = TextMobject("至此，排序完成！", color=RED).scale(0.8).shift(DOWN)
        self.play(Write(finish_text))

    def partition(self, arrays_mob, start, end):
        if start < end:
            # 轴点
            pivot = arrays_mob.value_at_index(start)
            #
            low = start
            high = end
            self.low_arrow.next_to(arrays_mob[low], DOWN)
            self.high_arrow.next_to(arrays_mob[high], DOWN)
            self.play(ShowCreation(VGroup(self.low_arrow, self.high_arrow)))
            while(low < high):
                high_text = TextMobject("从high处向前搜索:").scale(0.5).next_to(arrays_mob[1], 1.5* UP)
                self.play(Write(high_text))
                while(low < high and arrays_mob.value_at_index(high) >= pivot):
                    high_succ_text = TextMobject(str(arrays_mob.value_at_index(high)) + "大于等于轴点"+str(pivot) + ", high指针向前走一步").scale(0.5)
                    high_succ_text.shift(2 * DOWN)
                    self.play(Write(high_succ_text), runtime=1)
                    ######
                    high -= 1
                    self.high_arrow.next_to(arrays_mob[high], DOWN)  
                    self.play(ShowCreation(self.high_arrow), Uncreate(high_succ_text))  
                if low < high:
                    high_fail_text = TextMobject(str(arrays_mob.value_at_index(high)) + "小于轴点"+str(pivot) + ",与轴点进行交换").scale(0.5).shift(2 * DOWN)
                    self.play(Write(high_fail_text), runtime=1)
                    arrays_mob.swap(self, low, high) # 交换
                    self.play(Uncreate(high_fail_text))
                self.play(Uncreate(high_text))
                #
                low_text = TextMobject("从low处向后搜索:").scale(0.5).next_to(arrays_mob[1], 1.5* UP)
                self.play(Write(low_text))
                while(low < high and arrays_mob.value_at_index(low) <= pivot):
                    low_succ_text = TextMobject(str(arrays_mob.value_at_index(low)) + "小于等于轴点"+str(pivot) + ", low指针向后走一步").scale(0.5)
                    low_succ_text.shift(2 * DOWN)
                    self.play(Write(low_succ_text), runtime=1)
                    ####
                    low += 1
                    self.low_arrow.next_to(arrays_mob[low], DOWN)
                    self.play(ShowCreation(self.low_arrow), Uncreate(low_succ_text)) 
                # 交换
                if low < high:
                    low_fail_text = TextMobject(str(arrays_mob.value_at_index(low)) + "大于轴点"+str(pivot) + ",与轴点进行交换").scale(0.5).shift(2 * DOWN)
                    self.play(Write(low_fail_text), runtime=1)
                    arrays_mob.swap(self, low, high) # 交换
                    self.play(Uncreate(low_fail_text))
                self.play(Uncreate(low_text))
            ####
            end_text = TextMobject("指针low和指针high重合,一趟快排结束.").scale(0.5).shift(2 * DOWN)
            self.play(Write(end_text))
            left_begin = arrays_mob[start].get_center()
            left_begin[1] -= 0.5
            left_end = arrays_mob[low-1].get_center()
            left_end[1] -= 0.5
            right_begin = arrays_mob[low+1].get_center()
            right_begin[1] -= 0.5
            right_end = arrays_mob[end].get_center()
            right_end[1] -= 0.5
            left_line = Line(start = left_begin, end =left_end)
            brace_left = BraceText(left_line, text="此区间元素数值都小于轴点"+str(pivot), brace_direction=DOWN, color=RED)
            brace_left.brace.stroke_width =2
            brace_left.label.scale(0.45)
            right_line = Line(start = right_begin, end = right_end)
            right_brace = BraceText(right_line, text="此区间元素数值都大于轴点"+str(pivot), brace_direction=DOWN, color=BLUE)
            right_brace.brace.stroke_width = 2
            right_brace.label.scale(0.5)
            if start < (low - 1) and (low +  1) < end:
                self.play(ShowCreation(brace_left, runtime=2), ShowCreation(right_brace, runtime=2))
                self.wait(2)
                self.play(Uncreate(VGroup(brace_left, right_brace)))
            elif start < (low - 1) and (low +  1) == end:
                self.play(ShowCreation(brace_left, runtime=2))
                self.wait(2)
                self.play(Uncreate(brace_left))
            elif start == (low - 1) and (low +  1) < end:
                self.play(ShowCreation(right_brace, runtime=2))
                self.wait(2)
                self.play(Uncreate(right_brace))
            self.wait(2)
            # 恢复
            #arrays_mob[low].set_color(RED)
            self.play(Uncreate(end_text))
            self.play(FadeOut(VGroup(self.low_arrow, self.high_arrow)))
        return low

    def why_go_first_from_right(self):
        text_qestions = TextMobject("为什么总是先从high处向前搜索呢?", color=YELLOW).scale(0.8).shift(UP)
        self.play(Write(text_qestions))
        text_answers = TextMobject("因为我们默认选取选取的privot是首个元素,",
        "先从high处往前搜索是为了保证每次交换时的元素一定是小于privot的.", alignment="\\raggedright", 
        tex_to_color_map={"交换时的元素一定是小于privot的": RED}).scale(0.5).shift(DOWN)
        self.play(Write(text_answers))
        self.wait(2)
        self.play(Uncreate(VGroup(text_qestions, text_answers)))

        
# python -m manim F:\manim\\projects\\test\\Sort.py Insertion -p --media_dir F:\\manim_vedio_dirs     
class Insertion(Scene):
    def construct(self):
        #self.description()
        self.camera.background_color =  WHITE
        self.description()
        self.in_arrow = self.get_arrows(start_position=DOWN, end_position=UP, text="内循环\\\\指针", color=YELLOW)
        self.out_arrow = self.get_arrows(start_position=DOWN, end_position=UP, text="外循环\\\\指针", color=BLUE)
        self.sort_array()
    
    def description(self):
        """description"""
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
        #############
        title = TextMobject("插入排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        insert_description_txt = TextMobject("插入排序(insertion sort)的思路简要描述为: 始终将整个序列视作并切分为两部分: 有序的前缀和无序的后缀."
        "通过迭代, 反复地将后缀的首元素转移到前缀中, 如此, 该前缀的范围不断扩展直至覆盖整个序列, 那么整个序列将变成有序序列.", alignment="\\raggedright").scale(0.5).shift(2*UP)
        self.play(Write(insert_description_txt), runtime=2)
        self.wait(3)
        sorted_rec = Rectangle(height=1, width=3, color=GREEN).shift(2*LEFT)
        sorted_txt = TextMobject("2 5 7 ").move_to(sorted_rec.get_center())
        sorted_brace = BraceText(sorted_rec, text="有序序列Q[0, r)", brace_direction=DOWN, color=GREEN)
        sorted_brace.label.scale(0.5)
        unsorted_rec_e = Rectangle(height=1, width=0.5, color=BLUE).next_to(sorted_rec, RIGHT)
        unsorted_txt_e = TextMobject("4").move_to(unsorted_rec_e.get_center())
        unsorted_rec = Rectangle(height=1, width=3, color=BLUE).next_to(unsorted_rec_e , RIGHT)
        unsorted_txt = TextMobject("6 3 1").move_to(unsorted_rec.get_center())
        unsorted_brace = BraceText(VGroup(unsorted_rec_e, unsorted_rec), text="无序序列Q[r,n)", brace_direction=DOWN, color=BLUE)
        unsorted_brace.label.scale(0.5)
        self.play(ShowCreation(VGroup(sorted_rec, sorted_txt, sorted_brace, unsorted_rec_e, unsorted_txt_e, unsorted_rec, unsorted_txt, unsorted_brace)))
        self.wait(2)
        # 
        step_description = TextMobject("上图所示前缀Q[0,r)已然有序, 借助有序序列的查找算法,在前缀中定位到不大(小)于e的最大(小)元素",
        "将e从无序后缀中取出, 并紧邻查找返回位置之后(前)插入即可, 就使得前缀的范围扩大到Q[0,r]",alignment="\\raggedright").scale(0.5).shift(3*DOWN)
        self.play(ShowCreation(step_description), runtime=2)
        self.wait(3)
        self.play(Uncreate(VGroup(sorted_txt, unsorted_rec_e, unsorted_txt_e, unsorted_brace)))
        sorted_txt_update = TextMobject("2 4 5 7 ", tex_to_color_map={"4": RED}).move_to(sorted_rec.get_center())
        sorted_brace.change_label("有序序列Q[0, r]").label.scale(0.5)
        unsorted_rec.next_to(sorted_rec, RIGHT)
        unsorted_txt.move_to(unsorted_rec.get_center())
        unsorted_brace_update = BraceText(unsorted_rec, text="无序序列Q(r,n)", brace_direction=DOWN, color=BLUE)
        unsorted_brace_update.label.scale(0.5)
        self.play(ShowCreation(VGroup(sorted_txt_update, unsorted_brace_update)))
        self.wait(2)
        self.play(Uncreate(VGroup(step_description, unsorted_brace_update, unsorted_txt, unsorted_rec, sorted_brace, sorted_txt_update, sorted_rec, insert_description_txt)))


    def sort_array(self):
        # 数组
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr, color=RED)
        arr_mob.set_width(10)
        # squares
        S_Groups = VGroup()
        for  i in range(len(arr)):
            square = Square(side_length=0.5, color=BLUE_A, stroke_width=2)
            square.move_to(arr_mob[i].get_center())
            S_Groups.add(square)
        # index
        index_group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            index_group.add(index)
        # 显示创建过程
        self.play(ShowCreation(VGroup(arr_mob, S_Groups, index_group)))
        self.wait(2)
        # 排序
        for i in range(1, len(arr)):
            current = arr_mob.value_at_index(i)
            self.out_arrow.next_to(arr_mob[i], DOWN)
            self.play(ShowCreation(self.out_arrow))
            for preindex in range(i - 1, -1, -1):
                self.in_arrow.next_to(arr_mob[preindex], DOWN)
                self.play(ShowCreation(self.in_arrow))
                if(arr_mob.value_at_index(preindex) > current):
                    arr_mob.swap(self, preindex, preindex + 1)
                    preindex -= 1
                else:
                    break
            self.play(FadeOut(self.in_arrow))
        self.play(Uncreate(VGroup(self.out_arrow, self.in_arrow)))
        end_description = TextMobject("排序完成!",color=RED).scale(0.5).shift(1.5*DOWN)
        self.play(Write(end_description))
        self.wait(1)
    
    def  get_arrows(self, start_position, end_position, text, color=RED):
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
        txt = TextMobject(text,color=color).scale(0.45).next_to(arrow, DOWN)
        return VGroup(arrow, txt)
    

# python -m manim F:\manim\\projects\\test\\Sort.py ShellSort -p --media_dir F:\\manim_vedio_dirs
class ShellSort(Scene):
    def construct(self):
        self.description()
        self.sort_array()
    
    def description(self):
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
        self.play(Write(logo))
        #############
        title = TextMobject("希尔排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        #
        shell_description = TextMobject("希尔排序(Shell Sort)是插入排序的一种, 又被称为缩小增量排序(Diminishing Increment Sort)", 
        "是直接插入排序算法的一种更高效的改进版本。\\\\", "希尔排序是基于插入排序的以下两点性质提出改进方法的:", alignment="\\raggedright", 
        tex_to_color_map={"缩小增量排序": YELLOW}).scale(0.5).shift(2*UP)
        self.play(Write(shell_description), runtime=6)
        shell_bullist_description = BulletedList("因为插入排序每次只能将数据移动一位，通常情况下，插入排序是低效的",
        "插入排序在近乎有序的数组中, 排序效率高", buff=1, dot_color=BLUE).scale(0.5).next_to(shell_description, 1.2 * DOWN)
        self.play(Write(shell_bullist_description), runtime=5)
        shell_steps_description = TextMobject("希尔排序是将把无序序列按照下标的一定增量进行分组,对每组元素使用插入排序算法进行排序;",
        "随着增量逐渐减少,每组包含的元素数量原来越多,当增量减少至1时,整个序列则被分为一组, ",
        "然后对整个序列进行插入排序,至此排序完成.",alignment="\\raggedright", 
        tex_to_color_map={"增量": ORANGE, "插入排序": PURPLE}).scale(0.5).next_to(shell_bullist_description, 1.5 * DOWN)
        self.play(Write(shell_steps_description), runtime=8)
        shell_reason_description = TextMobject("最后一次插入排序时, 序列近乎有序, 排序效率会高很多.", alignment="\\raggedright").scale(0.5).next_to(shell_steps_description, DOWN)
        self.play(Write(shell_reason_description), runtime=2)
        self.wait(8)
        self.play(Uncreate(VGroup(shell_reason_description, shell_steps_description, shell_bullist_description, shell_description)), runtime=2)


    def sort_array(self):
        # 数组
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr, color=WHITE, ori_position=UP)
        arr_mob.set_width(10)
        # circle
        S_Groups = VGroup()
        for  i in range(len(arr)):
            circle = Circle(radius=0.4, color=BLUE, stroke_width=2)
            circle.move_to(arr_mob[i].get_center())
            S_Groups.add(circle)
        # index
        index_group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i],  1.2 * UP)
            index_group.add(index)
        # 显示创建过程
        self.play(ShowCreation(VGroup(arr_mob, S_Groups, index_group)))
        self.wait(4)
        tips_text = TextMobject("拥有相同颜色圆圈的元素属于同一组数组, 同一组元素之间进行插入排序", color=YELLOW).scale(0.6).shift(3 * DOWN)
        self.play(Write(tips_text), runtime=2)
        color_arrays = [GOLD, TEAL, RED, GREEN, PINK, PURPLE, ORANGE]
        # sort
        length = len(arr)
        d = length
        def Increment(index, increament):
            text = TextMobject("第"+str(index)+ "趟, 增量为: " + str(increament), color=RED).scale(0.5).next_to(arr_mob[1], 2 * UP)
            return text
        for k in range(math.ceil(math.log(length, 2))): # 
            d = math.ceil(d/2)
            increament_txt = always_redraw(lambda : Increment(k,d))
            self.play(ShowCreation(increament_txt), runtime=2)
            self.wait(2)
            # 给每组涂上不同的颜色  
            for i in range(0, d, 1): 
                for j in range(i, length, d):
                    S_Groups[j].set_fill(color=color_arrays[i], opacity=0.6)    
            self.wait(2)
            # 分组插入排序
            for i in range(d, length, 1):
                for j in range(i-d, -1, -d):
                    if (arr_mob.value_at_index(j) > arr_mob.value_at_index(j+d)):
                        arr_mob.swap(self, j, j+d)
            self.wait(2)
            result_txt = "第"+str(k)+ "趟, 结果为: "
            for i in range(length):
                if i < length-1:
                    result_txt += str(arr_mob.value_at_index(i)) + "  "
                else:
                    result_txt += str(arr_mob.value_at_index(i))
            if k == 0:
                results_text = TextMobject(result_txt, alignment="\\raggedright").scale(0.6).shift(-0.2*DOWN)
            else:
                results_text = TextMobject(result_txt, alignment="\\raggedright").scale(0.6).shift((k-0.4)*DOWN)
            self.play(Write(results_text), runtime=2)
            self.wait(2)
            self.play(Uncreate(increament_txt))
        self.wait(3)
        #self.play(Uncreate(VGroup(tips_text, arr_mob, S_Groups, index_group)))

# python -m manim F:\manim\\projects\\test\\Sort.py Selection -p --media_dir F:\\manim_vedio_dirs
class Selection(Scene):
    def construct(self):
        self.min_arrow = self.get_arrows(start_position=DOWN, end_position=UP, text="后缀中的\\\\最小值", color=YELLOW)
        self.description()
        self.sort_array()
    
    def description(self):
        """description"""
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
        #############
        title = TextMobject("选择排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        selection_description_txt = TextMobject("选择排序(selection sort)与插入排序类似，该算法也将序列划分为有序前缀和无序后缀两部分。",
        "升序排序时，要求有序前缀中的最大值不大于后缀中的最小值, 如此, 每次从后缀中选出最小者, 并作为最大元素转移到前缀最后端, 就可使有序部分的范围不断扩展.",
        "对于降序排列, 则反之.", alignment="\\raggedright").scale(0.5).shift(2*UP)
        self.play(Write(selection_description_txt), runtime=2)
        self.wait(3)
        sorted_rec = Rectangle(height=1, width=3, color=GREEN).shift(2*LEFT)
        sorted_txt = TextMobject("1 2 3").move_to(sorted_rec.get_center())
        sorted_brace = BraceText(sorted_rec, text="有序序列Q[0, r)", brace_direction=DOWN, color=GREEN)
        sorted_brace.label.scale(0.5)
        unsorted_rec = Rectangle(height=1, width=3, color=BLUE).next_to(sorted_rec, RIGHT)
        unsorted_txt = TextMobject("5 7 4 9", tex_to_color_map={"4": RED}).move_to(unsorted_rec.get_center())
        unsorted_brace = BraceText(unsorted_rec, text="无序序列Q[r,n)", brace_direction=DOWN, color=BLUE)
        unsorted_brace.label.scale(0.5)
        self.play(ShowCreation(VGroup(sorted_rec, sorted_txt, sorted_brace, unsorted_rec, unsorted_txt, unsorted_brace)))
        self.wait(2)
        #
        step_description = TextMobject("上图所示前缀Q[0,r)已然有序, 调用无序序列的查找算法, 从后缀中找到最小值4, ",
        "将4从从后缀中取出, 放入前缀的最后端, 就使得前缀的范围扩大到Q[0,r], 继续保持有序",alignment="\\raggedright").scale(0.5).shift(2.5*DOWN)
        self.play(ShowCreation(step_description), runtime=2)
        self.wait(3)   
        #
        self.play(Uncreate(VGroup(sorted_brace, unsorted_rec, unsorted_txt, unsorted_brace)))
        sorted_rec_e = Rectangle(height=1, width=0.5, color=BLUE).next_to(sorted_rec, RIGHT)
        sorted_txt_e = TextMobject("4", color=RED).move_to(sorted_rec_e.get_center())
        sorted_brace_update = BraceText(VGroup(sorted_rec, sorted_rec_e), text="有序序列Q[0, r]", brace_direction=DOWN, color=GREEN)
        sorted_brace_update.label.scale(0.5)
        unsorted_rec_update = Rectangle(height=1, width=3, color=BLUE).next_to(sorted_rec_e, RIGHT)
        unsorted_txt_update = TextMobject("5 7 9").move_to(unsorted_rec_update.get_center())
        unsorted_brace_update = BraceText(unsorted_rec_update, text="无序序列Q(r,n)", brace_direction=DOWN, color=BLUE)
        unsorted_brace_update.label.scale(0.5)
        self.play(ShowCreation(VGroup(sorted_rec_e, sorted_txt_e, sorted_brace_update, unsorted_rec_update, unsorted_txt_update, unsorted_brace_update)))
        self.wait(2)
        self.play(Uncreate(step_description))
        self.play(Uncreate(VGroup(sorted_rec, sorted_txt, sorted_rec_e, sorted_txt_e, sorted_brace_update, unsorted_rec_update, unsorted_txt_update, unsorted_brace_update)))
        self.play(Uncreate(selection_description_txt))

    def sort_array(self):
        # 数组
        arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
        arr_mob = Array(arr, color=RED)
        arr_mob.set_width(10)
        # squares
        S_Groups = VGroup()
        for  i in range(len(arr)):
            square = Square(side_length=0.5, color=BLUE_A, stroke_width=2)
            square.move_to(arr_mob[i].get_center())
            #print(arr_mob[i].get_center())
            S_Groups.add(square)
        # index
        index_group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5 * UP)
            index_group.add(index)
        # 显示创建过程
        self.play(ShowCreation(VGroup(arr_mob, S_Groups, index_group)))
        self.wait(2)
        #
        length = len(arr)
        # 默认无序
        def unsorted_brace(width):
            line = Line(start=[5.5, 0.5, 0], end=[5.5, -0.5, 0])
            unsorted_rec = Rectangle(height=1.1, width=width).next_to(line, LEFT)
            brace = Brace(unsorted_rec, brace_direction=DOWN, color=YELLOW)
            brace.stroke_width = 1
            text = TextMobject("无序后缀", color=RED).scale(0.5).next_to(brace, DOWN)
            return VGroup(brace, text)

        def sorted_brace(width):
            line = Line(start=[-5.5, 0.5, 0], end=[-5.5, -0.5, 0])
            unsorted_rec = Rectangle(height=1.1, width=width).next_to(line, RIGHT)
            brace = Brace(unsorted_rec, brace_direction=DOWN, color=ORANGE)
            brace.stroke_width = 1
            text = TextMobject("有序前缀", color=PURPLE).scale(0.5).next_to(brace, DOWN)
            return VGroup(brace, text)
        # sort
        for i in range(length):
            # 选择最小值
            minIndex = i
            for  j in range(i+1, length):
                if (arr_mob.value_at_index(j) < arr_mob.value_at_index(minIndex)): # 
                     minIndex = j
            #  最小值
            self.min_arrow.next_to(arr_mob[minIndex], DOWN)
            self.play(Indicate(arr_mob[minIndex]), ShowCreation(self.min_arrow))
            arr_mob.swap(self, minIndex, i)
            self.play(FadeOut(self.min_arrow))
            #
            if i > 0:
                self.play(Uncreate(sorted), Uncreate(unsorted))
            border_x = arr_mob[i].get_center()[0] + 0.15
            #print(border_x)
            sorted = always_redraw(lambda: sorted_brace(border_x - (-5.5)))
            unsorted = always_redraw(lambda: unsorted_brace(5 - border_x))
            #
            self.play(ShowCreation(sorted), ShowCreation(unsorted))
            if i == length - 1:
                self.wait(2)
                self.play(Uncreate(sorted), Uncreate(unsorted))
        self.play(Uncreate(VGroup(arr_mob, S_Groups, index_group)))
                 

    def  get_arrows(self, start_position, end_position, text, color=RED):
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
        txt = TextMobject(text,color=color).scale(0.45).next_to(arrow, DOWN)
        return VGroup(arrow, txt)

# python -m manim F:\manim\\projects\\test\\Sort.py Selection -p --media_dir F:\\manim_vedio_dirs
class Merge(Scene):
    def construct(self):
        self.description()
        self.camera.background_color =  WHITE
        self.sort_array()
    
    def description(self):
        title = TextMobject("归并排序", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))

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
