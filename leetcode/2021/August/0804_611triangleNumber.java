/*611. 有效三角形的个数

给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

注意:

    数组长度不超过1000。
    数组里整数的范围为 [0, 1000]。
*/c
class Solution {//暴力基础上优化一丢丢，改成二分
    int count(int[] n, int index, int target){//数组n[]从下标index+1开始，满足小于target的数的个数
        if(n[index + 1] >= target)
            return 0;
        if(n[n.length - 1] < target)
            return n.length - 1 - index;
        int i = index + 1, j = n.length;
        while(i < j){
            int m = (i + j) / 2;
            if(n[m] >= target){
                j = m;
            }
            else{
                i = m + 1;
            }
        }
        return i - 1 - index;
    }
    public int triangleNumber(int[] nums) {
        if(nums.length < 3)
            return 0;
        Arrays.sort(nums);
        List<Integer> sum = new ArrayList<>();
        List<Integer> index = new ArrayList<>();
        for(int i = 0; i < nums.length - 2; i++){
            for(int j = i + 1; j < nums.length - 1; j++){
                sum.add(nums[i] + nums[j]);
                index.add(j);
            }
        }
        int res = 0;
        int[] array = new int[index.size()];
        for(int i = 0; i < index.size(); i++){
            array[i] = index.get(i);
        }
        for(int i = 0; i < sum.size(); i++){
            res += count(nums, array[i], sum.get(i));
            /*for(int j = index.get(i) + 1; j < nums.length; j++){
                if(nums[j] < sum.get(i))
                    res++;
                else
                    break;
            }*/
        }
        return res;
    }
}

/*Arrays.sort(nums);//n^2的做法
int result = 0;
for (int i = nums.length - 1; i >= 2; i--) {
    int k = 0;
    int j = i - 1;
    while (k < j) {
        //满足该条件，说明从num[k]到num[j]的数都满足要求，结果直接加上j - k
        if (nums[k] + nums[j] > nums[i]) {
            result += j - k;
            j--;
        } else {
            //否则k自增，重新判断
            k++;
        }
    }
}
return result;*/