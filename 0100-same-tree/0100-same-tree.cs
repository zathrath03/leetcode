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
    public bool IsSameTree(TreeNode p, TreeNode q) {
        var stack = new Stack<(TreeNode, TreeNode)>();
        stack.Push((p, q));

        while (stack.Count > 0){
            var (node_p, node_q) = stack.Pop();
            if (node_p == null && node_q == null) continue;
            if (node_p == null || node_q == null || node_p.val != node_q.val)
                return false;
            stack.Push((node_p.right, node_q.right));
            stack.Push((node_p.left, node_q.left));
        }

        return true;
    }
}
