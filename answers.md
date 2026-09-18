# CMPS 2200 Assignment 02
## Answers

**Name:** Will Cunningham


Place all written answers from `assignment-02.md` here for easier grading.

1. **Asymptotic notation**

    a) $T(n)=2T(n/3)+1$

    Base case is reached once $\frac{n}{3^{h}} = 1$ or when $h = log{_3}{n}$

    Level 1: has 2 calls contributes 2 units of 1 = 2

    Level $i$: has $2^{i}$ calls contributes $2^{i}$ units of 1 = $2^{i}$

    $\[
\sum_{i=0}^{\log_3 n - 1} 2^i = \Theta\left(2^{\log_3 n}\right) = \Theta\left(n^{\log_3 2}\right).\]$

    b) $T(n)=5T(n/4)+n$
.  
.  
.  
.  
    c) $T(n)=7T(n/7)+n$
.  
.  
.  
.  
    d) $T(n)=9T(n/3)+n^2$
.  
.  
.  
.  
    e) $T(n)=8T(n/2)+n^3$
.  
.  
.  
.  
    f) $T(n)=49T(n/25)+n^{3/2}\log n$
.  
.  
.  
.  
    g) $T(n)=T(n-1)+2$
.  
.  
.  
.  
    h) $T(n)= T(n-1)+n^c$, with $c\geq 1$
.  
.  
.  
.  
    i) $T(n)=T(\sqrt{n})+1$
.  
.  
.  
.  
   
1. **Algorithms Comparison**
