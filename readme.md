# Kaprekar's Constat 

This is a program which exercises an interesting algorithm I found while traversing the internet.

## The Algorythm
---

We start with an integer. This integer must abide by some rules. It must be four digits, and at least one of the digits must be different from the rest. So integers like 1211, 1298, and 8564 work. Integers like 1111, 2222, and 9999 do not. The reason for this will become evident later.

Let us pick an arbitrary qualifying number then. We will select 2734. Now we can start the algorithm:

**Step 1)** Arrange the digits of the integer from highest to lowest (*HL*), and separately from lowest to highest (*LH*). We should now have the following:
$$HL = 7432$$
$$LH = 2347$$

**Step 2)** Subtract *LH* from *HL*. Note that at this point, having started with an integer such as 1111 would result in zero:
$$7432 - 2347 = 5085$$

**Step 3)** If 6174 is the result we are done. This is *Kaprekar's Constant*! Otherwise, the result becomes our new integer. We will take it and return to **Step 1**.

What is interesting, is that no mater what integer we start with (so long as it follows our rules), this process will always converge to *Kaprekar's Constant*.

## Running the Code
---

Run the program using the command, replacing '####' with your integer of choice:
```
python kaprekar.py ####
```
Note that your machine may have both Python 2 and 3 installed, in which case you might get an error. Instead use this command:
```
python3 kaprekar.py ####
```
For this program I allow for the use of integers with fewer that four digits, but the missing digits will be replaced with leading zeros.