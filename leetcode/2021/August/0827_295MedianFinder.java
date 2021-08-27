/*
295. 数据流的中位数

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

进阶:

    如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
    如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
*/

class MedianFinder {//超慢的二分
    List<Integer> list;
    /** initialize your data structure here. */
    public MedianFinder() {
        list = new ArrayList<>();
    }

    public void addNum(int num) {
        int n = list.size();
        if(n == 0){
            list.add(num);
            return;
        }
        if(num > list.get(n - 1)){
            list.add(num);
            return;
        }
        if(num < list.get(0)){
            list.add(0, num);
            return;
        }
        int i = 0, j = n;
        while(i < j){
            int m = (i + j) / 2;
            if(list.get(m) < num){
                i = m + 1;
            }
            else if(list.get(m) > num){
                j = m;
            }
            else{
                list.add(m, num);
                return;
            }
        }
        list.add(i, num);
        return;
    }

    public double findMedian() {
        int n = list.size();
        double res = (double)list.get(n / 2);
        if(n % 2 == 0){
            res = (res + (double)list.get(n / 2 - 1))/2;
        }
        return res;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */