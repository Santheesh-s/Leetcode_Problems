class Solution {
    public int deleteAndEarn(int[] nums) {
        Map<Integer, Integer> freq = new TreeMap<>();

        for (int x : nums)
            freq.put(x, freq.getOrDefault(x, 0) + 1);

        List<Integer> values = new ArrayList<>(freq.keySet());
        int n = values.size();

        if (n == 0) return 0;

        int[] points = new int[n];
        for (int i = 0; i < n; i++) {
            int v = values.get(i);
            points[i] = v * freq.get(v);
        }
        
        int prev2 = 0;
        int prev1 = points[0];

        for (int i = 1; i < n; i++) {
            int cur;
            int v = values.get(i);
            int prevV = values.get(i - 1);
            if (v == prevV + 1)
                cur = Math.max(prev1, prev2 + points[i]);
            else
                cur = prev1 + points[i];
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}

