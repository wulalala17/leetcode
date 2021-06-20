//https://leetcode-cn.com/problems/throne-inheritance/

/*class ThroneInheritance { // 没想到回溯，直接暴力搜索超时了
    Set<String> isDead = new HashSet<>();//死亡
    Map<String, Integer> generation = new HashMap<>();//第几代
    List<String> order = new ArrayList<>();//继承顺序

    public ThroneInheritance(String kingName) {
        generation.put(kingName, 1);
        //alive.put(kingName, 1);
        order.add(kingName);
    }

    public void birth(String parentName, String childName) {
        int g = generation.get(parentName) + 1;//childName是第g代人
        generation.put(childName, g);
        int cur = 0;//查找兄弟
        //alive.put(childName, 1);
        int index = order.indexOf(parentName);
        for(int i = index + 1; i <= order.size(); i++){
            if(i == order.size()){
                order.add(childName);
                break;
            }
            else{
                cur = generation.get(order.get(i));
                if(cur == g)
                    continue;
                else if(cur > g){
                    continue;
                }
                else{
                    order.add(i, childName);
                    break;
                }
            }
        }
    }

    public void death(String name) {
        isDead.add(name);
    }

    public List<String> getInheritanceOrder() {
        List<String> res = new ArrayList<>();
        for(String s : order){
            if(isDead.contains(s))
                continue;
            else{
                res.add(s);
            }
        }
        return res;
    }
}*/
class ThroneInheritance {//官方题解 DFS
    Map<String, List<String>> edges;
    Set<String> dead;
    String king;

    public ThroneInheritance(String kingName) {
        edges = new HashMap<String, List<String>>();
        dead = new HashSet<String>();
        king = kingName;
    }

    public void birth(String parentName, String childName) {
        List<String> children = edges.getOrDefault(parentName, new ArrayList<String>());
        children.add(childName);
        edges.put(parentName, children);
    }

    public void death(String name) {
        dead.add(name);
    }

    public List<String> getInheritanceOrder() {
        List<String> ans = new ArrayList<String>();
        preorder(ans, king);
        return ans;
    }

    private void preorder(List<String> ans, String name) {
        if (!dead.contains(name)) {
            ans.add(name);
        }
        List<String> children = edges.getOrDefault(name, new ArrayList<String>());
        for (String childName : children) {
            preorder(ans, childName);
        }
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param_3 = obj.getInheritanceOrder();
 */