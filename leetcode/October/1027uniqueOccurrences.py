# 1207.独一无二的出现次数
# 给你一个整数数组arr，请你帮忙统计数组中每个数的出现次数。
# 如果每个数的出现次数都是独一无二的，就返回true；否则返回false。
# 示例
# 1：
# 输入：arr = [1, 2, 2, 1, 1, 3]
# 输出：true
# 解释：在该数组中，1出现了3次，2出现了2次，3只出现了1次。没有两个数的出现次数相同。
# 示例
# 2：
# 输入：arr = [1, 2]
# 输出：false
# 示例
# 3：
# 输入：arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# 输出：true
# 提示：
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
# class Solution:  别人写的一行版本
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         return len((Counter(arr).values())) ==  len(set(Counter(arr).values()))