from tkinter import font

from click import group
from nbformat import write
from manimlib import *
from manimlib.imports import *
from  os  import system
import random


class MyText(Text):
    CONFIG = {
        'font': 'heiti',
        'size': 0.5
    }

class Array(VGroup):
    def __init__(self, array, run_time=0.5):
        super().__init__()
        self.run_time = run_time
        self.build_array(array)

    def build_array(self, array):
        for i, x in enumerate(array):
            cell = Integer(x).set_color(GREEN)
            if i != 0:
                cell.next_to(self, RIGHT, buff=1)
            self.add(cell)
        self.move_to(ORIGIN + DOWN)

    def value_at_index(self, index):
        return self[index].get_value()



class BinarySearch(Scene):
    def construct(self):
        #
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
        binary_search_title  = TextMobject("二分查找", color=RED, fontsize=42)
        self.play(Write(binary_search_title), Write(logo))
        self.wait(1)
        # title
        title = TextMobject("二分查找", fontsize=32).set_color(RED)
        title.to_edge(UP)
        self.play(ReplacementTransform(binary_search_title,title))
        # 什么是二分查找
        text_1 = MyText("二分查找(Binary Search),也叫作折半查找,是在分治算法基础上设计出来的查找算法,对应的时间复杂度为O(logn)")
        text_1.set_color_by_t2c(t2c={
            "二分查找(Binary Search)":GOLD_A,
            "分治算法": RED,
        })
        text_1.shift(2 * UP)
        text_2 = MyText("二分查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。")
        text_2.set_color_by_t2c(t2c={
            "顺序存储结构": RED_E,
            "有序": RED_E,
        })
        text_2.next_to(text_1, DOWN)
        text_groups = VGroup(text_1, text_2)
        self.play(Write(text_groups), runtime=3)
        self.wait(2)
        text_3 = MyText("假设某一有序队列nums=[1, 3, 5, 7, 9, 11, 13, 17, 19],如何用二分查找定位17在nums中的位置?")
        text_3.set_color_by_t2c(t2c={
            "nums=[1, 3, 5, 7, 9, 11, 13, 17, 19]": BLUE,
            "17": RED,
        })
        text_3.shift(2 * UP)
        self.play(ReplacementTransform(text_groups, text_3))
        # 二分查找步骤
        color_dict_1 = {"low=0,high=nums.length-1": RED, "中点位置": BLUE, "nums[mid]=target": PURPLE}
        text_steps1 = TextMobject(
            "1. 预设两个指针low=0,high=nums.length-1,我们需要在nums[low, high]区间查找目标数target。\\\\",
            "2. 确定区间[low, high]的中点位置mid=low+ (high-low)/2 \\\\", 
            "3. 然后比较target和nums[mid],如nums[mid]=target,则查找成功并返回位置mid;否则须确定新的查找区间，继续二分查找\\\\",
            alignment="\\raggedright", tex_to_color_map=color_dict_1,
        ).scale(0.5)
        text_steps1.next_to(text_3, DOWN)
        text_steps2 = BulletedList(
            "如果nums[mid]>target,按照数组的有序性,须向左区间nums[low, mid-1]查找,则需要设置high=mid-1。",
            "如果nums[mid]<target,按照数组的有序性,须向右区间nums[mid+1, high]查找,则需要low=mid+1。", dot_color=BLUE, 
        ).scale(0.45)
        text_steps2.next_to(text_steps1, DOWN)
        text_steps = VGroup(text_steps1, text_steps2)
        self.play(Write(text_steps), runtime=2)
        self.wait(3)
        self.play(FadeOut(text_steps))
        #text_steps.scale(0.5)
        #text_steps.shift(DOWN + LEFT)
        #self.play(Write(text_steps))
        #
        arr = list([1, 3, 5, 7, 9, 11, 13, 17, 19])
        arr_mob = Array(arr)
        arr_mob.shift(UP)
        self.play(ShowCreation(arr_mob))
        self.wait(1)

        group = VGroup()
        for i in range(0, len(arr)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob[i], 0.5*UP)
            group.add(index)
        self.play(ShowCreation(group))
        #
        target = 17
        #  arrow
        low_arrow = Arrow(
            start=DOWN, 
            end=UP, 
            color=RED, 
            buff=0.8, 
            tip_length=0.2, 
            stroke_width=4, 
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
        low_text = MyText('low', color=RED)  # size 文字的缩放比例，默认为1，表示原来的尺寸48
        low_text.next_to(low_arrow, DOWN)
        low_group = VGroup(low_arrow, low_text)
        #
        high_arrow = Arrow(
            start=DOWN, 
            end=UP, 
            color=TEAL, 
            buff=0.8,
            tip_length=0.2, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
        high_text = MyText('high',color=TEAL)
        high_text.next_to(high_arrow, DOWN)
        high_group = VGroup(high_arrow, high_text)
        #
        length = len(arr) - 1
        left = 0
        right = length
        low_group.next_to(arr_mob[left], DOWN)
        high_group.next_to(arr_mob[right], DOWN)
        self.play(ShowCreation(low_group), ShowCreation(high_group))
        # 
        tmp = MyText("")
        while left <= right:
            mid = int((left + right) / 2)
            #
            mid_index = MyText("mid="+str(mid), color=MAROON)
            mid_index.next_to(arr_mob[mid], UP * 2)
            self.play(ReplacementTransform(tmp, mid_index))
            tmp = mid_index
            #
            self.play(Indicate(arr_mob[mid]))
            self.play(Indicate(arr_mob[left], color=PINK), Indicate(arr_mob[right], color=PURPLE))
            #print(mid)
            if arr_mob.value_at_index(mid) == target:
                target_box = SurroundingRectangle(arr_mob[mid], color=RED, buff=.1)
                final_text = MyText("查找成功！", color=RED).scale(2)
                final_text.move_to(BOTTOM + UP)
                self.play(ShowCreation(final_text), ShowCreation(target_box))
                self.wait(2)
                self.play(Uncreate(target_box), Uncreate(final_text))
                break
            elif arr_mob.value_at_index(mid) < target:
                text_compare = Text(
                    str(arr_mob.value_at_index(mid)) + "<" + str(target), 
                    font='songti',color=YELLOW,
                )
                text_compare.next_to(arr_mob[mid], DOWN)
                self.play(Write(text_compare))
                self.play(Uncreate(text_compare))
                #
                left = mid + 1
                low_group.next_to(arr_mob[left], DOWN)
                self.play(ShowCreation(low_group))
            elif arr_mob.value_at_index(mid) > target:
                text_compare = Text(
                    str(arr_mob.value_at_index(mid)) + ">" + str(target), 
                    font='songti',color=YELLOW,
                )
                text_compare.next_to(arr_mob[mid], DOWN)
                self.play(Write(text_compare))
                self.play(Uncreate(text_compare))
                #
                right = mid - 1
                high_group.next_to(arr_mob[right], DOWN)
                self.play(ShowCreation(high_group))
        self.play(Uncreate(VGroup(tmp, text_3, low_group, high_group)))
        self.play(Uncreate(VGroup(group, arr_mob)))
        #
        rendered_code_1 = Code(file_name="F:\manim\\projects\\test\\codes\\binarySearch.cpp", style=code_styles_list[14])
        rendered_code_1.shift(0.5 * UP)
        self.play(ShowCreation(rendered_code_1), runtime=3)
        text_4 = MyText("Tips: 每次查找的区间是[low, high]（左闭右闭区间），那么需要注意以下细节")
        text_4.set_color_by_t2c(t2c={
            "[low, high]（左闭右闭区间）": MAROON
        })
        text_4_1 = BulletedList(
            "high的初始值为n-1",
            "循环条件要使用while(low <= high)",
            "target在左区间时, high赋值为mid-1", dot_color=BLUE
        ).scale(0.45)
        text_4_1.next_to(text_4, DOWN)
        text_4_group = VGroup(text_4, text_4_1)
        text_4_group.next_to(rendered_code_1, DOWN)
        self.play(Write(text_4_group), runtime=2)
        self.wait(3)
        text_5 = MyText("假如high的初始值预设为n,每次查找的区间为[low, high)（左闭右开区间），那么需要注意如下：")
        text_5.set_color_by_t2c(t2c={
            "n-1": YELLOW,
            "[low, high)（左闭右开区间）": MAROON
        })
        text_5_1 = BulletedList(
            "循环条件要使用while(low < high)",
            "target在左区间时, high赋值为mid", dot_color=BLUE
        ).scale(0.45)
        text_5_1.next_to(text_5, DOWN)
        text_5_group = VGroup(text_5, text_5_1)
        text_5_group.shift(2* UP)
        self.play(ReplacementTransform(VGroup(rendered_code_1, text_4_group), text_5_group))
        self.wait(1)
        rendered_code_2 = Code(file_name="F:\manim\\projects\\test\\codes\\binarySearch_1.cpp", style=code_styles_list[14])
        rendered_code_2.next_to(text_5_group, DOWN)
        self.play(FadeIn(rendered_code_2), runtime=3)
        self.wait(5)
        self.play(FadeOut(rendered_code_2))
        #
        text_6 = MyText("假如升序数组nums=[5,7,7,8,8,10],有一目标值target=8,那么如何找出8在数组nums中的开始位置和结束位置?")
        text_6.set_color_by_t2c(t2c={
            "8": YELLOW,
            "开始位置": MAROON,
            "结束位置": ORANGE
        })
        text_6.shift(2 * UP)
        self.play(ReplacementTransform(text_5_group, text_6))
        self.wait(1)
        color_dict = {"思路": RED, "第一个等于target的元素的下标": BLUE, "第一个大于target元素的下标减1": MAROON}
        text_7 = TextMobject("思路:找出target在nums中的开始位置,等价于在nums数组中找到第一个等于target的元素的下标,记为leftIdx;\\\\",
        "找到target在nums中的结束位置,等价于在nums中找到第一个大于target元素的下标减1,记为rightIdx。\\\\", 
        alignment="\\raggedright",tex_to_color_map=color_dict).scale(0.5)
        text_7.next_to(text_6, DOWN)
        self.play(Write(text_7), runtime=2)

        arr_1 = list([5,7,7,8,8,10])
        arr_mob_1 = Array(arr_1)
        arr_mob_1.shift(0.5 * DOWN)
        self.play(ShowCreation(arr_mob_1))
        self.wait(1)

        group_1 = VGroup()
        for i in range(0, len(arr_1)):
            index = Integer(i).set_color(WHITE).scale(0.3)
            index.next_to(arr_mob_1[i], 0.5*UP)
            group_1.add(index)
        self.play(ShowCreation(group_1))

        target = 8
        # 
        left_text = MyText("寻找leftIdx", color=PURPLE)
        left_text.next_to(arr_mob_1[0], LEFT)
        self.play(ShowCreation(left_text))
        #  arrow
        low_arrow = Arrow(
            start=DOWN, 
            end=UP, 
            color=RED, 
            buff=0.8, 
            tip_length=0.2, 
            stroke_width=4, 
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
        low_text = MyText('low', color=RED)  # size 文字的缩放比例，默认为1，表示原来的尺寸48
        low_text.next_to(low_arrow, DOWN)
        low_group = VGroup(low_arrow, low_text)
        #
        high_arrow = Arrow(
            start=DOWN, 
            end=UP, 
            color=ORANGE, 
            buff=0.8,
            tip_length=0.2, 
            stroke_width=4,
            max_tip_length_to_length_ratio=0.35,
            max_stroke_width_to_length_ratio=5
        )
        high_text = MyText('high',color=GREEN)
        high_text.next_to(high_arrow, DOWN)
        high_group = VGroup(high_arrow, high_text)
        #寻找leftIdx
        left = 0
        right = len(arr_1) - 1
        low_group.next_to(arr_mob_1[left], DOWN)
        high_group.next_to(arr_mob_1[right], DOWN)
        self.play(ShowCreation(VGroup(low_group, high_group)))
        mid = int((left + right) / 2)
        mid_box_tmp =  SurroundingRectangle(arr_mob_1[mid], color=BLACK, buff=.1)
        mid_index = MyText("mid", color=MAROON)
        while left <= right:
            mid = int((left + right) / 2)
            mid_index.next_to(arr_mob_1[mid],2 * UP)
            mid_box =  SurroundingRectangle(arr_mob_1[mid], color=TEAL, buff=.1)
            self.play(ShowCreation(mid_index), ReplacementTransform(mid_box_tmp, mid_box))
            mid_box_tmp = mid_box
            if arr_1[mid] >= target:
                right = mid - 1
                high_group.next_to(arr_mob_1[left], DOWN)
                self.play(ShowCreation(high_group))
                leftIdx = mid 
            else:
                left = mid + 1
                low_group.next_to(arr_mob_1[left], DOWN)
                self.play(ShowCreation(low_group))
        #
        self.wait(1)
        self.play(Uncreate(mid_index))
        left = 0
        right =  len(arr_1) - 1
        low_group.next_to(arr_mob_1[left], DOWN)
        high_group.next_to(arr_mob_1[right], DOWN)
        #
        leftIdx_box = mid_box_tmp.set_color(RED)
        text_8 = MyText("leftIdx=" + str(leftIdx)).scale(0.7)
        text_8.next_to(leftIdx_box, DOWN)
        self.play(ShowCreation(VGroup(leftIdx_box, text_8)), ShowCreation(VGroup(low_group, high_group)))
        # 寻找rightIdx
        right_text = MyText("寻找rightIdx", color=PURPLE)
        right_text.next_to(arr_mob_1[0], LEFT)
        self.play(ReplacementTransform(left_text, right_text))
        #
        mid = int((left + right) / 2)
        mid_box_tmp =  SurroundingRectangle(arr_mob_1[mid], color=BLACK, buff=.1)
        mid_index = MyText("mid", color=MAROON)
        while left <= right:
            mid = int((left + right) / 2)
            mid_index.next_to(arr_mob_1[mid],2 * UP)
            #print(left, mid, right)
            mid_box =  SurroundingRectangle(arr_mob_1[mid], color=TEAL, buff=.1)
            self.play(ShowCreation(mid_index), ReplacementTransform(mid_box_tmp, mid_box))
            mid_box_tmp = mid_box
            if arr_1[mid] > target:
                right = mid - 1
                high_group.next_to(arr_mob_1[left], DOWN)
                self.play(ShowCreation(high_group))
                rightIdx = mid 
            else:
                left = mid + 1
                low_group.next_to(arr_mob_1[left], DOWN)
                self.play(ShowCreation(low_group))
        #
        self.play(Uncreate(low_group), Uncreate(high_group), Uncreate(mid_index))
        #
        text = MyText("rightIdx还需要减一")
        text.move_to(BOTTOM + 1.5 * UP)
        self.play(ShowCreation(text))
        rightIdx_box = SurroundingRectangle(arr_mob_1[rightIdx - 1], color=YELLOW, buff=.1)
        text_9 = MyText("rightIdx=" +str(rightIdx - 1)).scale(0.7)
        text_9.next_to(rightIdx_box , DOWN)
        self.play(ReplacementTransform(mid_box_tmp, rightIdx_box),ShowCreation(text_9), Uncreate(text))
        self.wait(2)
        #
        rendered_code_3 = Code(file_name="F:\manim\\projects\\test\\codes\\binarySearch_2.cpp", style=code_styles_list[14]).scale(0.95)
        self.play(ReplacementTransform(VGroup(text_6, text_7, arr_mob_1, group_1, leftIdx_box, text_8, rightIdx_box, text_9), rendered_code_3))
        self.wait(5)