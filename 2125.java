// leetcode problem no. 2125(Medium )

class Solution {
    public int numberOfBeams(String[] bank) {
        int prev = 0, ans = 0; 


        for(String row: bank){
            int count = 0;

            for(char i = 0; i < row.length(); i++ ){
                if(row.charAt(i) == '1'){
                    count++;
                }
            }
            if(count > 0){
                ans = ans + (prev * count );
                prev = count;
            }            
        }
        return ans;
    }
}