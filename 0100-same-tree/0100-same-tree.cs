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

        while (stack.Count > 0) {
            var (pNode, qNode) = stack.Pop();
            if (pNode == null && qNode== null) continue;
            if (pNode?.val != qNode?.val) return false;
            stack.Push((pNode.right, qNode.right));
            stack.Push((pNode.left, qNode.left));
        }

        return true;
    }
}
