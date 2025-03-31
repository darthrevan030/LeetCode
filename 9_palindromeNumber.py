'''
Python3 int type has no lower or upper bounds. But if there are constraints given then we have to 
make sure that while reversing the integer we don't cross those constraints.

So, instead of reversing the whole integer, let's convert half of the integer and then check if it's palindrome.
But we don't know when is that half going to come.

Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

x = 1595, revX = 1
x = 159, revX = 15
x = 15, revX = 159

We see that revX > x after 3 loops and we crossed the half way in the integer because it's an odd length integer.
If it's an even length integer, our loop stops exactly in the middle.

Now we can compare x and revX, if even length, or x and revX//10 if odd length and return True if they match.
'''

def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    
    result = 0

    while x > result:
        result = result * 10 + x % 10
        x = x // 10

    return True if (x == result or x == result // 10) else False
