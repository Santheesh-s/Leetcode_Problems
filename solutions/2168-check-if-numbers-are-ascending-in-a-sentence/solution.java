class Solution {
    public boolean areNumbersAscending(String s) {
        List<Integer>ls=new ArrayList<>();
        String[] words = s.split("\\s+");
       for (String word : words) {
            try {
                int number = Integer.parseInt(word);
                ls.add(number);
            } catch (NumberFormatException e) {
                // Skip non-integer words
            }
        }
        for(int i=0;i<ls.size()-1;i++)
        {
            if(!(ls.get(i)<ls.get(i+1)))
                return false;
        }
        return true;
    }
}
