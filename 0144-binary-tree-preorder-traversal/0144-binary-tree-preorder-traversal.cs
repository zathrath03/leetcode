/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<int> PreorderTraversal(TreeNode root) {
        var stack = new Stack<TreeNode>();
        var output = new List<int>();
        stack.Push(root);
        
        while (stack.Count > 0) {
            var node = stack.Pop();
            if (node == null) continue;
            output.Add(node.val);
            stack.Push(node.right);
            stack.Push(node.left);
        }
        
        return output;
    }
}