/**
 * https://leetcode.com/problems/add-two-numbers/
 * Time O(MAX(N, M)) | Space O(MAX(N, M))
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let sentinel = tail = new ListNode();

    return add(l1, l2, tail, sentinel);       /* Time O(MAX(N, M)) | Space O(MAX(N, M)) */
}

const add = (l1, l2, tail, sentinel, carry = 0) => {
    const isBaseCase = !(l1 || l2 || carry);
    if (isBaseCase) return sentinel.next;

    return dfs(l1, l2, tail, sentinel, carry);/* Time O(MAX(N, M)) | Space O(MAX(N, M)) */
}

const dfs = (l1, l2, tail, sentinel, carry) => {
    const sum = (l1?.val || 0) + (l2?.val || 0) + carry;
    const val = sum % 10;
    carry = Math.floor(sum / 10);

    tail.next = new ListNode(val);
    tail = tail.next;

    l1 = l1?.next || null;
    l2 = l2?.next || null;

    add(l1, l2, tail, sentinel, carry);     /* Time O(MAX(N, M)) | Space O(MAX(N, M)) */

    return sentinel.next;
}

/**
 * https://leetcode.com/problems/add-two-numbers/
 * Time O(MAX(N, M)) | Space O(MAX(N, M))
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2, carry = 0) {
    let sentinel = tail = new ListNode();

    while (l1 || l2 || carry) {/* Time O(MAX(N, M)) */
        const sum = (l1?.val || 0) + (l2?.val || 0) + carry;
        const val = sum % 10;
        carry = Math.floor(sum / 10);

        tail.next = new ListNode(val);
        tail = tail.next;

        l1 = l1?.next || null;
        l2 = l2?.next || null;
    }

    return sentinel.next;
};

// claudia
// time o(n) - space o(n)
var addTwoNumbers = function(l1, l2) {
    const newL1 = concatNumsReversed(l1);
    const newL2 = concatNumsReversed(l2);

    const sum = BigInt(newL1) + BigInt(newL2);
    const reversedSum = String(sum).split("").reverse().join("");
    
    let dummyHead = new ListNode(0);
    let current = dummyHead;

    for (let i = 0; i < reversedSum.length; i++) {
        current.next = new ListNode(Number(reversedSum[i]));
        current = current.next;
    }

    return dummyHead.next;
};

const concatNumsReversed = (head) => {
    let reverse = "";
    let curr = head;

    while (curr) {
        reverse += curr.val;
        curr = curr.next;
    }

    return reverse.split("").reverse().join("");
};

// claudia
// time o(max(m, n)) - space o(max(m, n))
const addTwoNumbers = (l1, l2) => {
    const dummy = new ListNode(0)
    let pointer = dummy
    let carry = 0

    while (l1 || l2 || carry) {
        let sum = 0

        if (l1) {
            sum += l1.val
            l1 = l1.next    
        }
        
        if (l2) {
            sum += l2.val
            l2 = l2.next    
        }

        sum += carry
        carry = Math.floor(sum / 10)
        const addNode = new ListNode(sum % 10)
        pointer.next = addNode
        pointer = pointer.next
    }

    return dummy.next
};
