# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    evens = []
    odds = []
    for i in range(num+1):
        if i % 2 != 0:
            odds.append(i)
        else:
            evens.append(i)
    evens_count = len(evens)
    odds_count = len(odds)
    return print(f"The number of odds are {odds_count}. The number of evens are {evens_count}.")


evens_and_odds(100)

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    total = 1
    for i in range(1,num+1):
        total = total * i
    return total

print(factorial(10))


    