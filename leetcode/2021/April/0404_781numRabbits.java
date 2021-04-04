/*781. 森林中的兔子

森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
返回森林中兔子的最少数量。

示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0

说明:
    answers 的长度最大为1000。
    answers[i] 是在 [0, 999] 范围内的整数。
*/

class Solution {//错了好几次，写了快半小时
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        int t;
        for (int i = 0; i < answers.length; i++){
            if(answers[i] == 0){ //说明只有一只，直接加到结果
                res++;
                continue;
            }
            else{//统计出现次数
                if(map.get(answers[i]) == null)//不包含在map里
                    map.put(answers[i], 1);
                else{
                    t = map.get(answers[i]);
                    map.put(answers[i], ++t);
                }
            }
        }
        for(Integer key:map.keySet()){
            int value = map.get(key);
            if (value <= key + 1)
                res += (key + 1);
            else{
                if (value % (key + 1) == 0)
                    res += (key + 1) * (value / (key + 1));
                else
                    res += (key + 1) * (value / (key + 1) + 1);
            }
        }
        return res;
    }
}

class Solution {//虽然思路差不多，但这个快很多。评论区的优秀写法
    public int numRabbits(int[] answers) {
        Map<Integer,Integer> map = new HashMap<>();
        int num = 0;
        for (int answer : answers) {
            if(map.containsKey(answer)&&map.get(answer)>0){
                map.put(answer,map.get(answer)-1);
            }else {
                num+=answer+1;
                map.put(answer,answer);
            }
        }
        return num;
    }
}