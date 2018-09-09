/*
 con 101
 Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6]

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

 */

 class StockSpanner {

     private int max;
     // the beginning of each span
     // linked[i]: the idx in prices of the last price that is > prices[i]
     private int linked[];
     private int prices[];
     private int cur;

     public StockSpanner() {
         linked = new int[10000];
         prices = new int[10000];
         max = 0;
         cur = -1;
     }

     public int next(int price) {
         max = Math.max(price, max);
         cur++;
         prices[cur] = price;
         if (price >= max) {
             linked[cur] = -1;
         } else {
             int ptr = cur-1;
             while (ptr > 0 && price >= prices[ptr]) {
                 if (ptr == linked[ptr]) ptr--;
                 ptr = linked[ptr];
             }
             // 0 is not a edge case here
             linked[cur] = ptr;
         }
         return cur - linked[cur];
     }
 }

 /**
  * Your StockSpanner object will be instantiated and called as such:
  * StockSpanner obj = new StockSpanner();
  * int param_1 = obj.next(price);
  */
