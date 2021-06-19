/*
1239. 串联字符串的最大长度

给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。

请返回所有可行解 s 中最长长度。



示例 1：

输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。

示例 2：

输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。

示例 3：

输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26



提示：

    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] 中只含有小写英文字母
*/
class Solution {//浅拷贝害死我了
    int res = 0;
    public List<String> a;
    void dfs(int index, int[] nums, int length){//当前位置 nums代表26个字母出现了几个,length代表当前串联组合长度
        res = Math.max(res, length);
        if(index == a.size())
            return;
        int[] oldNums = new int[26];
        for(int i = 0; i < 26; i++)//这里只能用循环深拷贝，浅拷贝的话改变nums, oldNums也会跟着改变
            oldNums[i] = nums[i];
        int oldLength = length;
        int f = -1;
        String s = a.get(index);
        for(int i = 0; i < s.length(); i++){
            if (nums[s.charAt(i) - 'a'] == 1){
                f = i;
                break;
            }
            else{
                length++;
                nums[s.charAt(i) - 'a'] = 1;
            }
        }
        if(f == -1){//选当前的
            dfs(index+1, nums, length);
        }
        dfs(index+1, oldNums, oldLength);//不选
    }
    public int maxLength(List<String> arr) {
        a = arr;
        int[] nums = new int[26];
        dfs(0, nums, 0);
        return res;
    }
}