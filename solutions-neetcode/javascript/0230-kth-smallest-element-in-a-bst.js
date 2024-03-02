/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * Time O(N + K) | Space O(H)
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
 var kthSmallest = function(root, k, inOrder = []) {
    if (!root) return inOrder

    return dfs(root, k, inOrder);
};

const dfs = (root, k, inOrder) => {
    if (root.left) kthSmallest(root.left, k, inOrder);

    inOrder.push(root.val);

    if (root.right) kthSmallest(root.right, k, inOrder);

    return inOrder[(k - 1)];
}

/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * Time O(N + K) | Space O(H)
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
 var kthSmallest = function(root, k, stack = []) {
    while (k--) {
        root = moveLeft(root, stack);

        const isSmallest = k === 0;
        if (isSmallest) return root.val;

        root = root.right;
    }
}

const moveLeft = (root, stack) => {
    while (root !== null) {
        stack.push(root);
        root = root.left;
    }

    return stack.pop();
}

// claudia 
// t o(n) - s o(h)
var kthSmallest = function(root, k) {
    let target = 0

    const inOrderTraversal = (node) => {
        if (!node) return
        inOrderTraversal(node.left)
        k--
        if (k === 0) target = node.val
        inOrderTraversal(node.right)
    }

    inOrderTraversal(root)

    return target
};

// recursive t o(h + k) - s o(h)
var kthSmallest = function(root, k) {
    let count = 0
    let target = null

    const dfs = (node) => {
        if (node.left) dfs(node.left)
        count++
        if (k === count) {
            target = node.val
        }
        if (node.right) dfs(node.right)
    }

    dfs(root)
    return target
};


// iterative t o(h + k) - s o(h)
var kthSmallest = function(root, k) {
    const stack = []
    let curr = root

    while (curr || stack.length) {
        while (curr) {
            stack.push(curr)
            curr = curr.left
        }

        if (stack.length) {
            curr = stack.pop()
            k--
            if (k === 0) return curr.val
            curr = curr.right
        }
    }
};