// Basically we need to add the two bits and take carry into consideration
// Use b as carry and a as the addition
// loop until the carry is 0


class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int temp = (a & b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}