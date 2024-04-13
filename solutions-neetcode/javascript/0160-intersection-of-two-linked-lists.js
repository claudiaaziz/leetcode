/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
    let a = headA;
    let b = headB;
    while (a !== b) {
        a = a === null ? headB : a.next;
        b = b === null ? headA : b.next;
    }

    return a;
};

var getIntersectionNode = function(headA, headB) {
    const set = new Set()

    let curr1 = headA

    while (curr1) {
        set.add(curr1)
        curr1 = curr1.next
    }

    let curr2 = headB

    while (curr2) {
        if (set.has(curr2)) return curr2
        curr2 = curr2.next
    }

    return null
};