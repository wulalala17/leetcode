# 925.长按键入
# 你的朋友正在使用键盘输入他的名字name。偶尔，在键入字符c时，按键可能会被长按，而字符可能被输入1次或多次。
# 你将会检查键盘输入的字符typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回True。

# 示例
# 1：
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex'中的'a'和'e'被长按。
# 示例
# 2：
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e'一定需要被键入两次，但在typed的输出中不是这样。
# 示例
# 3：
# 输入：name = "leelee", typed = "lleeelee"
# 输出：true
# 示例
# 4：
# 输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。
# 提示：
# name.length <= 1000
# typed.length <= 1000 name和typed的字符都是小写字母。
def isLongPressedName(name, typed):
    if name == typed:
        return True
    if len(typed) < len(name):
        return False

    i = 0
    j = 0
    while i < len(name):
        count = 0  # 记录name相同字符个数
        c = name[i]
        while i < len(name) and name[i] == c:
            count += 1
            i += 1
        while count > 0 and j < len(typed):
            if typed[j] == c:
                count -= 1
                j += 1
            else:
                return False
        while j < len(typed) and typed[j] == c:
            j += 1
        if count > 0:
            return False
    if j < len(typed) and typed[j] != name[-1]:  # name完了 typed还有
        return False
    return True

a = "shit"
b = "sshhiitt"
print(isLongPressedName(a, b))


# def isLongPressedName(self, name: str, typed: str) -> bool: 别人写的，用栈，强！
#     name = list(name)
#     typed = list(typed)
#     while name:
#         c = name.pop()
#         if not typed or typed.pop() != c:
#             return False
#         if not name or name[-1] != c:
#             while typed and typed[-1] == c:
#                 typed.pop()
#     return not typed
