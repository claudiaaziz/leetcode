/**
 * https://leetcode.com/problems/linked-list-cycle/
 * Time O(N) | Space O(N)
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head, seen = new Set()) {
    while (head) {/* Time O(N) */
        if (seen.has(head)) return true;

        seen.add(head);/* Space O(N) */
        head = head.next;
    }

    return false;
}

/**
 * https://leetcode.com/problems/linked-list-cycle/
 * Time O(N) | Space O(1)
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let [ slow, fast ] = [ head, head];

    while (fast && fast.next) {/* Time O(N) */
        slow = slow.next;
        fast = fast.next.next;

        const hasCycle = slow === fast;
        if (hasCycle) return true;
    }

    return false;
};

// claudia
// t o(n) - space o(1)
const hasCycle = head => {
    let slow = head
    let fast = head

    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
        if (fast === slow) return true
    }

    return false
};