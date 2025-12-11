/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> ls, int id) {
        Map<Integer,Integer>map=new HashMap<>();
        int sum=0;
        map.put(id,1);
        while (!map.isEmpty()) {
            for (int i = 0; i < ls.size(); i++) {
                Employee emp = ls.get(i);
                if (map.containsKey(emp.id)) 
                {
                    sum += emp.importance;
                    if (emp.subordinates != null)
                        for (Integer subId : emp.subordinates)
                                map.put(subId, 1);
                    map.remove(emp.id);
                }
            }
        }
        return sum;
    }
}
