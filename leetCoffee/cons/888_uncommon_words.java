/*
888. Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
*/

class Solution {
    public String[] uncommonFromSentences(String A, String B) {

        Map<String, Integer> wordmap = new HashMap<>();
        String[] sa;
        String c = A + " " + B;
        sa = c.split(" ");

        for (String str : sa) {
            if (wordmap.containsKey(str)) {
                Integer num = wordmap.get(str);
                wordmap.put(str, num+1);
            } else {
                wordmap.put(str, 1);
            }
        }
        List<String> strlist = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : wordmap.entrySet()) {
            if (entry.getValue().equals(1)) {
                strlist.add(entry.getKey());
            }
        }
        String[] strarr = strlist.toArray(new String[strlist.size()]);
        return strarr;
    }
}
