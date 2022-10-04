# defining function to find maximum profit
def maxP (price: list) -> int:

    left, right= 0, 1
    f_profit= 0

    # inializing while loop if position of right is less than length of price
    while(right < len(price)):

        # checking condition for profit 
        if(price[left] < price[right]):

            # calculating profit
            profit= price[right] - price[left]
            f_profit= max(f_profit, profit)

        else:
            left= right
        right += 1
    
    if (f_profit == 0):
        print("No profit, better not to sell stocks.")
    else:
        print(f'Maximum profit is {f_profit}')


# This function finds the buy sell
def stockBuySell(price, n):
	
	# Traverse through given price array
	i = 0
	while (i < (n - 1)):
		
        # The limit is (n-2) as
		# we are comparing present element
		# to the next element
		while ((i < (n - 1)) and
				(price[i + 1] <= price[i])):
			i += 1
		
		# If we reached the end, break
		# as no further solution possible
		if (i == n - 1):
			break
		
		# Storing the index 
		buy = i
		i += 1
		
		# Note that the limit is (n-1) as we are
		# comparing to previous element
		while ((i < n) and
			(price[i] >= price[i - 1])):
			i += 1
			
		# Storing the index
		sell = i - 1
		
		print("Buy on day: ",buy," ",
				"Sell on day: ",sell)
		

# Driver code 
if __name__ == "__main__":
    price = [ ]

    # taking length of price array as input
    length= int(input("Enter length of list: "))
    print("Enter the prices of stocks: ")

    # taking elements of array as input
    for item in range(length):
        element= int(input())
        price.append(element)
    print(f'List of prices is {price}')

    # calling the function
    maxP(price)

    # storing the length of array in a variable
    n = len(price)

    # calling another function 
    stockBuySell(price, n)
    
