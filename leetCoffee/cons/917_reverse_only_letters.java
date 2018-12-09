/*
 917. Reverse Only Letters
 Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

 */
 class Solution {
     public String reverseOnlyLetters(String S) {
         char[] s1 = S.toCharArray();
         int len = S.length();
         Stack<Character> stack = new Stack();
         Set<Integer> set = new HashSet<>();
         for (int i = 0; i < len; i++) {
             if (isLetter(s1[i])) {
                 stack.push(s1[i]);
             } else {
                 set.add(i);
             }
         }
         for (int i = 0; i < len; i++) {
             if (!set.contains(new Integer(i))) {
                 s1[i] = stack.pop();
             }
         }
         return new String(s1);
     }

     private boolean isLetter(char c) {
         if ((65 <= c &&  c <= 90) || (c >= 97) && (c <= 122)) {
             return true;
         }
         return false;
     }
 }
