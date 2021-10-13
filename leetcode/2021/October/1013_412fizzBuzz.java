/*
412. Fizz Buzz

写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
*/
class Solution {//模拟，就考基本语法
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<>();
        for(int i = 1; i <= n; i++){
            if(i % 3 == 0 && i % 5 != 0){
                res.add("Fizz");
            }
            else if(i % 3 != 0 && i % 5 == 0){
                res.add("Buzz");
            }
            else if(i % 3 == 0 && i % 5 == 0){
                res.add("FizzBuzz");
            }
            else{
                res.add(String.valueOf(i));
            }
        }
        return res;
    }
}