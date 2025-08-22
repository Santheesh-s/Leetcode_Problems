class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int sum1=0;
        for(int i=0;i<seats.length;i++)
            sum1+=Math.abs(students[i]-seats[i]);
        return sum1;
    }
}
