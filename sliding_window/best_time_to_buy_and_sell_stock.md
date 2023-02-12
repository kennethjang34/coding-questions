# LC problem link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# question
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


# solution

Python3:

def maxProfit(self, prices: List[int]) -> int:
	i = 0
	n=len(prices)
	after_first_buy=-prices[0]
	after_first_sell=0
	after_second_buy=-prices[0]
	after_second_sell=0
	for i in range(n):
		price=prices[i]
		after_first_buy=max(after_first_buy, -price)
		after_first_sell=max(after_first_sell, price+after_first_buy)
		after_second_buy=max(after_second_buy, after_first_sell-price)
		after_second_sell=max(after_second_sell, after_second_buy+price)
	return total_profit


Proof:
There are two cases to consider for this question. 1) you only need to buy and sell a stock once over the whole period. 2) you need to buy and sell stocks twice.

for case (1), it is not so hard to see that the algorithm works

for case (2),
	1. Let p1,p2,p3,p4 be first buy, sell, second buy, sell points. That is, maximum total_profit is prices[p4]-prices[p3]+prices[p2]-prices[p1]
	2. It is easy to verify that prices[p2]-prices[p1] is the biggest difference you can find before point p3 and prices[p4]-prices[p3] is the biggest after p2
	3. Once you reach p4, it is guaranteed that -prices[p3]+prices[p2]-prices[p1] >= -prices[k]+prices[j]-prices[i] for any i<=j<=k<=p4. This is because otherwise, prices[p4]+(-prices[p3]+prices[p2]-prices[p1]) will be less than prices[p4]+(-prices[k]+prices[j]-prices[i]) for some (i,j,k)!=(p1,p2,p3), which contradicts the assumption: p1,p2,p3,p4 are those that make the maximum profit.
	4. Similarly, In order to have maximum value of -prices[p3]+prices[p2]-prices[p1], prices[p2]-prices[p1] >= prices[j]-prices[i] for any i<=j<=p3. Therefore prices[p2]-prices[p1] is the largest before p3.
	5. Therefore, we have the following implications: -1)if prices[p4]-prices[p3]+prices[p2]-prices[p1]>=prices[r]-prices[k]+prices[j]-prices[i], then -prices[p3]+prices[p2]-prices[p1] is maximum. 
													  -2) if -prices[p3]+prices[p2]-prices[p1] is the maximum, then prices[p2]-prices[p1] is the biggest difference that can be found before p3
	6. when p1<=i<=p2, prices[p1] < prices[i]. So after_first_buy is -prices[p1]
	6. When i = p2, after_first_buy=-prices[p1], and after_first_sell will be prices[p2]-after_first_sell=prices[p2]-prices[p1] for p2<=i<=p3, as this is the biggest value that has been encountered and will be the biggest at least up to p3.
	7. When i = p3, after_first_sell=prices[p2]-prices[p1], and after_second_buy will be -prices[p3]+after_first_sell=-prices[p3]+prices[p2]-prices[p1], as this is the biggest value for p3<=i<=p4 that has been encountered and will be the biggest at least up to p4 (from 3).
	8. When i = p4, after_second_buy=-prices[p3]+prices[p2]-prices[p1], and after_second_sell will be prices[p4]-prices[p3]+prices[p2]-prices[p1].
	9. We have proven that if there exist p1,p2,p3,p4 that make the profit the biggest, after_second_sell will be set to that maximum value.
	10. Now suppose when i = r, for r > p4, after_second_sell > desired=prices[p4]-prices[p3]+prices[p2]-prices[p1]. 
	11. Then after_second_buy+prices[r] >  desired. If prices[r]>prices[p4], it is easy to see that this contradicts our assumption that you need to sell on day p4 to make the biggest profit. So prices[p4] >= prices[r]. This leads to after_second_buy>-prices[p3]+prices[p2]-prices[p1]
	12. Suppose there exists k for p3 < k< r such that -prices[i]+after_first_buy > -prices[p3]+prices[p2]-prices[p1]. If -prices[k]>-prices[p3], then this contradicts the assumption that prices[p4]-prices[p3]+prices[p2]-prices[p1] is the max profit as we can make a bigger profit using prices[r]-prices[k]+prices[p2]-prices[p1]. Therefore, -prices[k] <= prices[p2] and after_first_buy must be bigger than prices[p2]-prices[p1]
	13. This means after_first_sell > prices[p2]-prices[p1]. Suppose we have j for j <= k such that prices[j] + after_first_buy > prices[p2]-prices[p1]. Because after_first_buy is prices[i] for some i <= j, this indicates prices[p2]-prices[p1] <= prices[j]-prices[i]. This means we have some (i,j,k,r), where i<=j<=k<=r such that prices[r]-prices[k]+prices[j]-prices[i] > prices[p4]-prices[p3]+prices[p2]-prices[p1], which contradicts our assumption.

	With 9 and 13, we have proven the algorithm must give the right answer
