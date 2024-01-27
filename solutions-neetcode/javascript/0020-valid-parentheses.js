/**
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/valid-parentheses/
 * @param {string} s
 * @return {boolean}
 */
 var isValid = (s, stack = []) => {
    for (const bracket of s.split('')) {/* Time O(N) */
        const isParenthesis = bracket === '(';
        if (isParenthesis) stack.push(')');  /* Space O(N) */

        const isCurlyBrace = bracket === '{';
        if (isCurlyBrace) stack.push('}');   /* Space O(N) */

        const isSquareBracket = bracket === '[';
        if (isSquareBracket) stack.push(']');/* Space O(N) */

        const isOpenPair = isParenthesis || isCurlyBrace || isSquareBracket;
        if (isOpenPair) continue;

        const isEmpty = !stack.length;
        const isWrongPair = stack.pop() !== bracket;
        const isInvalid = isEmpty || isWrongPair;
        if (isInvalid) return false;
    }

    return (stack.length === 0);
};

/**
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/valid-parentheses/
 * @param {string} s
 * @return {boolean}
 */
var isValid = (s, stack = []) => {
    const map = {
        '}': '{',
        ']': '[',
        ')': '(',
    };
    
    for (const char of s) {/* Time O(N) */
        const isBracket = (char in map)
        if (!isBracket) { stack.push(char); continue; }/* Space O(N) */

        const isEqual = (stack[stack.length - 1] === map[char])
        if (isEqual) { stack.pop(); continue; }

        return false;
    }

    return (stack.length === 0);
};

// time - o(n) where n is the lenght of input string s
// space - o(n) bc in worse case can store all parens in s if theyre all opening parens
const isValid = (s) => {
    if (s.length <= 1) return false
    const openingParens = [] 

    for (const paren of s) {
        if (paren === "(" || paren === "[" || paren === "{") {
            openingParens.push(paren)
        } else {
            const lastParen = openingParens.pop()
            if (!(lastParen === "(" && paren === ")" ||
                  lastParen === "{" && paren === "}" ||
                  lastParen === "[" && paren === "]")) {
                return false
            }
        }
    }

    return openingParens.length === 0
};
