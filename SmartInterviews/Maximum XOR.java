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
            
            System.out.println(maxXORPair(arr));
        }
    }
    
    private static int maxXORPair(int[] arr) {
        TrieNode root = new TrieNode();
        
        // Insert elements into the trie
        for (int num : arr) {
            TrieNode curr = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (curr.children[bit] == null) {
                    curr.children[bit] = new TrieNode();
                }
                curr = curr.children[bit];
            }
        }
        
        int maxXOR = Integer.MIN_VALUE;
        
        // Find maximum XOR for each element
        for (int num : arr) {
            TrieNode curr = root;
            int currXOR = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (curr.children[bit ^ 1] != null) {
                    currXOR += (1 << i);
                    curr = curr.children[bit ^ 1];
                } else {
                    curr = curr.children[bit];
                }
            }
            maxXOR = Math.max(maxXOR, currXOR);
        }
        
        return maxXOR;
    }
}
