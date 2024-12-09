-------------------------------------------------------------------------------------------------------

Question 1: In bitcoin.py file, implement a program that:

-------------------------------------------------------------------------------------------------------

-> Expects the user to specify two  command-line arguments:
   the number of Bitcoins (a float), and the currency they have.
   If the first command-line argument cannot be converted to a float,
   the program should exit via sys.exit with an error message. 
   The same error message should be used if the second command-line argument 
   is not a valid currency (The only currenices supported are "GBP","USD" and "EUR"). 
-> Queries the API for the CoinDesk Bitcoin Price Index at
   https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
   among whose nested keys is the current price of Bitcoin as a float.
 -> Outputs the current cost of the number of  Bitcoins specified by the first command-line 
    argument in the currency specified by the second command-line argument.
    The result should be displayed with four decimal places, using , as a thousands separator.

-------------------------------------------------------------------------------------------------------

Question 2: In teach_math.py file, implement a program that:

-------------------------------------------------------------------------------------------------------

Prompts the user for a level, If the user does not input 1, 2, or 3, the program should prompt
 again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is 
a non-negative integer with n digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. 
If an answer is not correct (or not even a number), the program should output EEE and prompt
 the user again, allowing the user up to three tries in total for that problem. 
 If the user has still not answered correctly after three tries, the program should output
   the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.

'''