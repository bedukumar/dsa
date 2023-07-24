import java.io.*;
import java.util.*;

public class Solution {
    
    public static void printDate(long seconds) {
    // Number of seconds in a day, hour, minute
    final int DAY = 86400;
    final int HOUR = 3600;
    final int MINUTE = 60;
    
    // Days of the week and months
    final String[] WEEKDAYS = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    final String[] MONTHS = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
    
    // Epoch time
    final long EPOCH_SECONDS = 0;
    final int EPOCH_YEAR = 1970;
    final int EPOCH_MONTH = 0; // January
    final int EPOCH_DAY = 1;
    final int EPOCH_WEEKDAY = 4; // Thursday
    
    // Compute the elapsed time since epoch
    long elapsedSeconds = seconds - EPOCH_SECONDS;
    
    // Compute the year
    int year = EPOCH_YEAR;
    while (true) {
        int daysInYear = 365;
        if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
            daysInYear = 366;
        }
        if (elapsedSeconds < daysInYear * DAY) {
            break;
        }
        elapsedSeconds -= daysInYear * DAY;
        year++;
    }
    
    // Compute the month and day
    int month = EPOCH_MONTH;
    while (true) {
        int daysInMonth = 31;
        if (month == 1) {
            if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
                daysInMonth = 29;
            } else {
                daysInMonth = 28;
            }
        } else if (month == 3 || month == 5 || month == 8 || month == 10) {
            daysInMonth = 30;
        }
        if (elapsedSeconds < daysInMonth * DAY) {
            break;
        }
        elapsedSeconds -= daysInMonth * DAY;
        month++;
    }
    int day = EPOCH_DAY + (int) (elapsedSeconds / DAY);
    
    // Compute the hour, minute, and second
    int hour = (int) ((elapsedSeconds % DAY) / HOUR);
    int minute = (int) ((elapsedSeconds % HOUR) / MINUTE);
    int second = (int) (elapsedSeconds % MINUTE);
    
    // Print the date and day
    System.out.printf("%02d-%s-%04d %s\n", day, MONTHS[month], year, WEEKDAYS[(EPOCH_WEEKDAY + (int) (seconds / DAY)) % 7]);
}


    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) 
        {
            long seconds = sc.nextLong();
            printDate(seconds);
        }
    }
}
