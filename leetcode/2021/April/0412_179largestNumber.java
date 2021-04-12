/*
179. 最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。


示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"



提示：

    1 <= nums.length <= 100
    0 <= nums[i] <= 109
*/
class Solution { //排序规则比较字符串重写了半天，还不如直接return (s1+s2).compareTo((s2+s2));
    public String largestNumber(int[] nums) {
        if (nums.length == 0)
            return "";
        if (nums.length == 1)
            return String.valueOf(nums[0]);
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            list.add(nums[i]);
        }
        Collections.sort(list, new Comparator<Integer>() {
            @Override
            public int compare(Integer i1, Integer i2) {
                String s1 = String.valueOf(i1);
                String s2 = String.valueOf(i2);
                return (s1+s2).compareTo((s2+s2));
            }
        });
        String res = "";
        for(int i = list.size() - 1; i >=0; i--){
            res = res + list.get(i);
        }
        if(res.charAt(0) == '0')
            return "0";
        return res;

    }
}