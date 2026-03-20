# Big O

## Simplification Rules

- Drop any constant factor: *O(4n) => O(n)*
- Drop smaller terms in a sum: *O(n**2 + n) => O(n**2)* 


## Rankings

    ### Worse

    **Factorial**   O(n!) => 8!: 8*7*6...*1: 40320
    **Exponential** O(c**n) => O(2**n), O(3**n) => 2**10 : 1024
    **Polynomial**  O(n**c) => O(n**2), O(n**3) => 10**2 : 100
    **Linear**      O(n)
    **Logarithmic** O(log(n))
    **Constant**    O(1) *performance does not scale with input size*

    ### Better