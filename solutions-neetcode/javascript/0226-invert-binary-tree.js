/**
 * https://leetcode.com/problems/invert-binary-tree/
 * TIme O(N) | Space O(N)
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = (root) => {
    const isBaseCase = root === null;
    if (isBaseCase) return root;

    return dfs(root);
}

const dfs = (root) => {
    const left = invertTree(root.left);
    const right = invertTree(root.right);

    root.left = right;
    root.right = left;

    return root;
}

/**
 * https://leetcode.com/problems/invert-binary-tree/
 * TIme O(N) | Space O(W)
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = (root,) => {
    const isBaseCase = root === null;
    if (isBaseCase) return root;

    bfs([ root ]);

    return root;
}

const bfs = (queue) => {
    while (queue.length) {
        for (let i = (queue.length - 1); 0 <= i; i--) {
            const node = queue.shift();
            const left = node.right;
            const right = node.left;

            node.left = left;
            node.right = right;

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }
}

// claudia
// time o(n) - space o(h)
const invertTree = (root) => {
    if (root) [root.left, root.right] = [invertTree(root.right), invertTree(root.left)]
    return root
};

// time o(n) - space o(n)
const invertTree = (root) => {
    const queue = [root]

    while (queue.length) {
        const node = queue.shift()
        if (node) {
            [node.left, node.right] = [node.right, node.left]   
            queue.push(node.left)
            queue.push(node.right)
        }
    }

    return root
};