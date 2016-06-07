# super_simple_stock

# Super Simple Stocks
Super simple stocks is an application to manage trades on a set of stocks and it's a technical test as part of
the hiring process for a very important company.

### 1. Assignment Description

##### Requirements

1.	Provide working source code that will:

    a.	For a given stock:

        i.    Calculate the dividend yield.
        ii.   Calculate the P/E Ratio.
        iii.  Record a trade, with timestamp, quantity of shares, buy or sell indicator and price.
        iv.   Calculate Stock Price based on trades recorded in past 15 minutes.

    b.	Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

##### Constraints & Notes

1.	Written in one of these languages:

    * Java, C#, C++, Python.

2.	No database or GUI is required, all data need only be held in memory.

3.	Formulas and data provided are simplified representations for the purpose of this exercise.

##### Global Beverage Corporation Exchange

Stock Symbol  | Type | Last Dividend | Fixed Dividend | Par Value
------------- | ---- | ------------: | :------------: | --------:
TEA           | Common    | 0  |    | 100
POP           | Common    | 8  |    | 100
ALE           | Common    | 23 |    | 60
GIN           | Preferred | 8  | 2% | 100
JOE           | Common    | 13 |    | 250



### 2. Solution

##### Assumptions
A  solution for the assignment is designed to provide a service
 which has operations to calculate the dividend yield, P/E Ratio,
Stock Price and record trades for a given stock. Besides, the service provides an operation
to calculate the GBCE All Share Index for all stocks supported by the Super Simple Stocks application.
Providing this service, all the requirements of the assignment are met.

Responding to one of the constraints, the implementation of the solution is written in Python
language.
##### Unit Test

To test the code of the technical test, it has been used Test Driven Approach.

##### Try Yourself

The code for the technical test was built as an Pycharm project. To compile the code, download the folder super-simple-stock and import the project in Pycharm.










