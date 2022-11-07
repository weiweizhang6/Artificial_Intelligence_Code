# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


from typing import List  # 引进线性元素？？
def twosums(array:list[int],target:int)-> list[int]: #定义函数的输入和输出，功能
    n = len(array) # #遍历前先知道数组多长。即，要知道边界
    for i in range(n):#i遍历一遍，range是遍历函数
        for j in range(i+1,n): # i固定时，j遍历剩下的元素
            if array[i]+array[j]==target:#直到两者相加得到目标值
                return [i,j]
                #self.twosums(array,target) 怎么样把相当等于12的所有项都输出
    return [] #当第一个指针i都遍历完还没有找到，就返回空。缩进对齐很重要

if __name__ == '__main__':
    array = [0,3,6,9,6,6]
    target = 1
    print(twosums(array,target))



# #def twoSum(nums: List[int], target: int) -> List[int]:
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []#
# #

# #if __name__ == '__main__':
#     nums = [1, 3, 5, 7, 9]
#     target = 11
#     print(twoSum(nums, target))#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
