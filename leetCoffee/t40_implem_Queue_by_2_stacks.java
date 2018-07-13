public class MyQueue {
    private Stack<Integer> s1;
    private Stack<Integer> s2;
    
    public MyQueue() {
        // do intialization if necessary
        s1 = new Stack();
        s2 = new Stack();
    }

    /*
     * @param element: An integer
     * @return: nothing
     */
    public void push(int element) {
        // write your code here
        s1.push(element);
    }

    /*
     * @return: An integer
     */
    public int pop() {
        int ret = 0;
        if (!s2.empty()) {
            ret = s2.pop();
            if (s2.empty()){
                while (!s1.empty()) {
                    s2.push(s1.pop());
                }
            }
        } else {
            if (!s1.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.pop());
                }
                ret = s2.pop();
            }
        }
        return ret;   
    }

    /*
     * @return: An integer
     */
    public int top() {
        int ret = 0;
        if (!s2.empty()) {
            ret = s2.peek();
        } else {
            if (!s1.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.pop());
                }
                ret = s2.peek();
            }
        }
        return ret;
    } 
}
