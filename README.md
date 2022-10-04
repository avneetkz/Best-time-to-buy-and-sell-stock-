# Best-time-to-buy-and-sell-stock-
This repository focuses on telling when is the best time to buy and sell stocks. It will give you the maximum profit. If the profit is high then it's time to sell your stocks and it will show not to sell when there's no profit. Keeping in mind that we may not engage in multiple transactions at the same time. So we have to sell the stock before buying the new one. 

# Code approach
An array is to be inputed by the user for the prices of stock on the consecutive days. Inside the function, it will check if the price of the (ith) day is greater than the price of (ith-1) day then it will calculate the profit else it will increase the values of both the days by 1, again going in loop till the length of array is not met. Once we get the maximum profit, the second function will be called in which we will find the local maxima and local minima to get to know the days for buying and selling stocks.  

## Example:
Suppose the array is like A = [ 7, 1, 5, 3, 6, 4 ], then the result will be 7. As we can see, if we buy on day 2 (index 1), then it will take 1 as a buying price. Then if we sell on day 3, the profit will be 5 – 1 = 4. Then buy on day 4, and sell on day 5, so profit will be 6 – 3 = 3. 
So, the maximum profit will be 7 here.
