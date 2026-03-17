/**
 * https://leetcode.com/problems/longest-common-prefix/
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
     if (strs.length === 0) return "";

       let s = strs[0];

       for (let i = 0; i < s.length; i++) {
        let ch = s[i];

        for (let j = 1; j < strs.length; j++) {
            if (i === strs[j].length || strs[j][i] !== ch) {
                return s.substring(0, i)
            }
        }
       }

       return s;
};