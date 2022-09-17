import java.util.ArrayList;
import java.util.List;

class Result {
    public static List<String> checkSimilarPasswords(List<String> newPasswords, List<String> oldPasswords)
    {
        // Initialize return object of the list of string 
        List<String> ans = new ArrayList<>();
        
        // Calculate total number of passwords to check
        int n = newPasswords.size();

        // iterate over all passwords to check it is similar or not
        for(int idx=0;idx<n;idx++)
        {
            // get a new Password from newPasswords List
            String newPass = newPasswords.get(idx);

            // get a old password from oldPasswords List
            String oldPass = oldPasswords.get(idx);

            // declare two variables to track the current index of the string in both passwords
            // point current index in newPassword
            int i = 0;
            // point current index in oldPassword
            int j = 0;

            // while loop till one of the passwords is a traverse
            while(i<newPass.length() && j<oldPass.length())
            {
                // get newPassword char at current index
                char newPassChar = newPass.charAt(i);

                // calculate newPassword Shifted old char ar current index
                char newPassShiftedOldChar;
                if(newPassChar == 'z')
                    newPassShiftedOldChar = 'a';
                else
                    newPassShiftedOldChar = (char)(newPassChar+1);

                // get oldPasswod char at current index
                char oldPassChar = oldPass.charAt(j);

                // if the newPassChar or newPassShiftedOldChar match with oldPassChar then we serach for next oldPass char 
                // So, increament oldPassword pointer
                if(newPassChar == oldPassChar || newPassShiftedOldChar == oldPassChar)
                {
                    j++;
                }

                // increment newPassword point to check next char match or not
                i++;
                
            } 
            // if we get all matches of oldPassword then add 'YES' in ans object
            if(j==oldPass.length())
                ans.add("YES");
            // if we do not find all matches in sequence then add 'NO' in add object
            else
                ans.add("NO");
        }
        // return List<String> object
        return ans;
    }
    
}


