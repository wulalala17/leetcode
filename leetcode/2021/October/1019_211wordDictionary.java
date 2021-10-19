/*
211. 添加与搜索单词 - 数据结构设计

请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

    WordDictionary() 初始化词典对象
    void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
    bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。



示例：

输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True



提示：

    1 <= word.length <= 500
    addWord 中的 word 由小写英文字母组成
    search 中的 word 由 '.' 或小写英文字母组成
    最多调用 50000 次 addWord 和 search
*/
class WordDictionary {
    Map<Integer,Set<String>> map = new HashMap<>();//根据字符串长度分开存放
    public WordDictionary() {

    }
    public void addWord(String word) {
        int length = word.length();
        if(map.get(length)!=null){
            map.get(length).add(word);
        }else{
            Set<String> set = new HashSet<>();
            set.add(word);
            map.put(length, set);
        }
    }
    public boolean search(String word) {
        Set<String> set = map.get(word.length());
        if(set==null){  //不存在该长度的字符串，直接返回false；
            return false;
        }
        if(set.contains(word)) return true;
        char[] chars = word.toCharArray();
        P:for(String s : set){
            if(word.length()!=s.length()){
                continue;
            }
            char[] cs = s.toCharArray();
            for(int i = 0; i< cs.length; i++){//逐个字符对比
                if(chars[i] != '.' && chars[i] != cs[i]){
                    continue P;
                }
            }
            set.add(word);
            return true;
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */