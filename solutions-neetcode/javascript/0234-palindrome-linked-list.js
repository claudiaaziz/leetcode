/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  // find mid point
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // reverse 2nd half
  let curr = slow;
  let prev = null;
  while (curr) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }
  let head2 = prev;

  // compare both halfs
  while (head && head2) {
    if (head.val !== head2.val) {
      return false;
    }

    head = head.next;
    head2 = head2.next;
  }

  return true;
};

// claudia
// t o(n) - s o(1)
const isPalindrome = head => {
  // Step 1 - obtain access the mid of the list 
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  fast = head;

  // Step 2 - reverse second half linked list
  slow = reverseSecondHalf(slow);

  // Step 3 - check if they equal, early false if not
  while (slow) {
    if (fast.val !== slow.val) return false;
    fast = fast.next;
    slow = slow.next;
  }

  return true;
};

const reverseSecondHalf = head => {
  let prev = null;

  while (head) {
    const next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }

  return prev;
};
