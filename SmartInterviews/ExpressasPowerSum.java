// express as power sum
import java.io.*;
import java.util.*;

public class Solution {
    
    
    public static int countSumPower(int x,int n,int c)
    {
        if(((int)Math.pow(c,n))<x)
        {
          return  countSumPower(x,n,c+1)+countSumPower((x-(int)Math.pow(c,n)),n,c+1);
            
        }
        else if(((int)Math.pow(c,n))==x)
        {
            return 1;
        }
        else
        {
           return 0;
        }
    }
    
     
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {     
        int num = sc.nextInt();
        int power = sc.nextInt();
            int c=1;
        System.out.println(countSumPower(num,power,c));
        }
        
    }
    
   
}
