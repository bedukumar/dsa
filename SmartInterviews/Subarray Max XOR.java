import java.util.Scanner;

class TrieNode {
    TrieNode[] children;
    
    TrieNode() {
        children = new TrieNode[2];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        while (t-- > 0) {
            int n = scanner.nextInt();
            int[] arr = new int[n];
            
            for (int i = 0; i < n; i++) {
                arr[i] = scanner.nextInt();
            }
            
            System.out.println(maxSubarrayXOR(arr));
        }
    }
    
    private static int maxSubarrayXOR(int[] arr) {
        TrieNode root = new TrieNode();
        int maxSubarrayXOR = 0;
        int currXOR = 0;
        
        // Insert 0 into the trie to handle the case when the XOR is 0.
        insert(root, 0);
        
        for (int num : arr) {
            currXOR ^= num;
            insert(root, currXOR);
            maxSubarrayXOR = Math.max(maxSubarrayXOR, findMaxXOR(root, currXOR));
        }
        
        return maxSubarrayXOR;
    }
    
    private static void insert(TrieNode root, int num) {
        TrieNode curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
        }
    }
    
    private static int findMaxXOR(TrieNode root, int num) {
        TrieNode curr = root;
        int maxXOR = 0;
        
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int oppositeBit = bit ^ 1;
            
            if (curr.children[oppositeBit] != null) {
                maxXOR += (1 << i);
                curr = curr.children[oppositeBit];
            } else {
                curr = curr.children[bit];
            }
        }
        
        return maxXOR;
    }
}
