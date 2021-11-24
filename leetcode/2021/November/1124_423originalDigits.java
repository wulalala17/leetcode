/*
423. 从英文中重建数字

给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。



示例 1：

输入：s = "owoztneoer"
输出："012"

示例 2：

输入：s = "fviefuro"
输出："45"



提示：

    1 <= s.length <= 105
    s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
    s 保证是一个符合题目要求的字符串
*/
class Solution {//笨比式写法
    public String originalDigits(String s) {
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            count[c - 'a']++;
        }
        int[] nums = new int[10];
        if(count[25] > 0){//0
            nums[0] = count[25];
            count['e' - 'a'] -= count[25];//e
            count['r' - 'a'] -= count[25];//r
            count['o' - 'a'] -= count[25];//o
            count[25] = 0;
        }
        if(count['x' - 'a'] > 0){//6
            nums[6] = count['x' - 'a'];
            count['s' - 'a'] -= count['x' - 'a'];//s
            count['i' - 'a'] -= count['x' - 'a'];//i
            count['x' - 'a'] = 0;
        }
        if(count['g' - 'a'] > 0){//8
            nums[8] = count['g' - 'a'];
            count['e' - 'a'] -= count['g' - 'a'];//s
            count['i' - 'a'] -= count['g' - 'a'];//i
            count['h' - 'a'] -= count['g' - 'a'];//s
            count['t' - 'a'] -= count['g' - 'a'];//s
            count['g' - 'a'] = 0;
        }
        if(count['u' - 'a'] > 0){//4
            nums[4] = count['u' - 'a'];
            count['f' - 'a'] -= nums[4];//f
            count['o' - 'a'] -= nums[4];//o
            count['r' - 'a'] -= nums[4];//r
            count['u' - 'a'] = 0;
        }
        if(count['f' - 'a'] > 0){//5
            nums[5] = count['f' - 'a'];
            count['i' - 'a'] -= count['f' - 'a'];//i
            count['v' - 'a'] -= count['f' - 'a'];//v
            count['e' - 'a'] -= count['f' - 'a'];//e
            count['f' - 'a'] = 0;
        }
        if(count['s' - 'a'] > 0){//7
            nums[7] = count['s' - 'a'];
            count['e' - 'a'] -= nums[7] * 2;//e
            count['v' - 'a'] -= nums[7];//v
            count['n' - 'a'] -= nums[7];//n
            count['s' - 'a'] = 0;
        }
        if(count['h' - 'a'] > 0){//3
            nums[3] = count['h' - 'a'];
            count['t' - 'a'] -= nums[3];//t
            count['r' - 'a'] -= nums[3];//r
            count['e' - 'a'] -= nums[3] * 2;//e
            count['h' - 'a'] = 0;
        }
        if(count['w' - 'a'] > 0){//2
            nums[2] = count['w' - 'a'];
            count['t' - 'a'] -= nums[2];//t
            count['o' - 'a'] -= nums[2];//r
            count['w' - 'a'] = 0;
        }
        if(count['o' - 'a'] > 0){//1
            nums[1] = count['o' - 'a'];
            count['n' - 'a'] -= nums[1];//n
            count['e' - 'a'] -= nums[1];//e
            count['o' - 'a'] = 0;
        }
        if(count['i' - 'a'] > 0){//9
            nums[9] = count['i' - 'a'];
            count['n' - 'a'] -= nums[9] * 2;//n
            count['e' - 'a'] -= nums[9];//e
            count['i' - 'a'] = 0;
        }
        String[] s1 = new String[]{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        String res = "";
        for(int i = 0; i < 10; i++){
            if(nums[i] > 0){
                for(int j = 0; j < nums[i]; j++){
                    res += s1[i];
                }
            }
        }
        return res;
    }
}