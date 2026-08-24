/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode currentNode = head;
        ListNode prevNode = null;
        while (currentNode.next != null) {
            ListNode temp = prevNode;
            prevNode = currentNode;
            currentNode = currentNode.next;
            prevNode.next = temp;
        }
        currentNode.next = prevNode;
        return currentNode;
    }
}
