/**
 * https://leetcode.com/problems/reorder-list/
 * Time O(N) | Space O(1)
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    const mid = getMid(head);           /* Time O(N) */
    const reversedFromMid = reverse(mid);/* Time O(N) */

    reorder(head, reversedFromMid);      /* Time O(N) */
};

const getMid = (head) => {
    let [ slow, fast ] = [ head, head ];

    while (fast && fast.next) {         /* Time O(N) */
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
}

const reverse = (head) => {
    let [ prev, curr, next ] = [ null, head, null ];

    while (curr) {                      /* Time O(N) */
        next = curr.next;
        curr.next = prev;

        prev = curr;
        curr = next;
    }

    return prev;
}

const reorder = (l1, l2) => {
    let [ first, next, second ] = [ l1, null, l2 ];

    while (second.next) {              /* Time O(N) */
        next = first.next;
        first.next = second;
        first = next;

        next = second.next;
        second.next = first;
        second = next;
    }
}

// claudia
// time o(n/2) - space o(1)
const reorderList = (head) => {
    // PART 1 - find head2
    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let head2 = slow.next;
    slow.next = null;

    // PART 2 - reverse head2
    const reversedHead2 = reverseHead2(head2);

    // PART 3 - zip lists
    zipLists(head, reversedHead2)
};

const reverseHead2 = (head2) => {
    let current = head2;
    let prev = null;

    while (current !== null) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }

    return prev;
};

const zipLists = (h1, h2) => {
    while (h2 !== null) {
        const temp1 = h1.next;
        const temp2 = h2.next;

        h1.next = h2;
        h2.next = temp1;

        h1 = temp1;
        h2 = temp2;
    }
}
