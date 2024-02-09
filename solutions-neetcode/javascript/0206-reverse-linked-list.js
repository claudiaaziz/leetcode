/**
 * https://leetcode.com/problems/reverse-linked-list/
 * Time O(N) | Space O(N)
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    const isBaseCase = !head?.next;
    if (isBaseCase) return head;

    return dfs(head);                   /* Time O(N) | Space O(N) */
}

const dfs = (curr) => {
    const prev = reverseList(curr.next);/* Time O(N) | Space O(N) */

    curr.next.next = curr;
    curr.next = null;

    return prev;
}

/**
 * https://leetcode.com/problems/reverse-linked-list/
 * Time O(N) | Space O(1)
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function (head) {
    let [ prev, curr, next ] = [ null, head, null ];

    while (curr) {/* Time O(N) */
        next = curr.next;
        curr.next = prev;

        prev = curr;
        curr = next;
    }

    return prev;
};

// claudia
// time o(n) - space o(1)
const reverseList = (head) => {
    let prev = null
    let current = head

    while (current !== null) {
        const next = current.next 
        current.next = prev 
        prev = current
        current = next
    }

    return prev
};

// time o(n) - space o(n)
const reverseList = (head, prev = null) => {
    if (head === null) return prev
    const next = head.next
    head.next = prev
    return reverseList(next, head)
};