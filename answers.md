# CMPS 2200 Assignment 02
## Answers

**Name:** Will Cunningham


Place all written answers from `assignment-02.md` here for easier grading.

1. **Asymptotic notation**

    a) $T(n)=2T(n/3)+1$

    Base case is reached once $\frac{n}{3^{h}} = 1$ or when $h = log{_3}{n}$

    Level 1: 2 calls, which contributes 2 calls of 1 = 2

    Level $i$: $2^{i}$ calls contributes $2^{i}$ units of 1 = $2^{i}$

    $\sum_{i=0}^{\log_3 n - 1} 2^i = \Theta(2^{\log_3 n}) = \Theta(n^{\log_3 2})$

    b) $T(n)=5T(n/4)+n$

    Base case is reached once $\frac{n}{4^{h}} = 1$ or when $h = log{_4}{n}$

    Level 1: 5 sub-problems of size $\frac{n}{4}$ which gives $n\frac{5}{4}$

    Level $i$: $5^{i}$ sub-problems of size $\frac{n}{4^{i}}$ which gives $n\frac{5^{i}}{4^{i}}$

    This gives $\sum_{i=0}^{\log_4 n - 1}n(\frac{5}{4})^i=n(\frac{(\frac{5}{4})^{\log_4 n}-1}{\frac{5}{4}-1})=\Theta(n(\frac{5}{4})^{\log_4n})$

    $n(\frac{5}{4})^{\log_4n} = n(n^{log_4\frac{5}{4}}) = n^{log_45}$ -> $T(n) = \Theta(n^{log_45})$
   
    c) $T(n)=7T(n/7)+n$ 

    Base case is reached once $\frac{n}{7^{h}} = 1$ or when $h = log{_7}{n}$

    Level 1: 7 sub-problems of size $\frac{n}{7}$ which gives $n$

    Level $i$: $7^{i}$ sub-problems of size $\frac{n}{7^{i}}$ which gives $n(\frac{7^{i}}{7^{i}}) = n$

    This gives $log{_7}{n}$ levels of $n$ so $T(n) = \Theta(nlog{_7}{n}) = \Theta(nlogn)$

    d) $T(n)=9T(n/3)+n^2$

    Base case is reached once $\frac{n}{3^{h}} = 1$ or when $h = log{_3}{n}$

    Level 1: 9 sub-problems of size $\frac{n^{2}}{3}$ which gives $3n^{2}$

    Level $i$: $9^{i}$ sub-problems of size $\frac{n^{2}}{3^{i}}$ which gives $n(\frac{9^{i}}{3^{i}}) = 3^{i}n^{2}$

    e) $T(n)=8T(n/2)+n^3$

    Base case is reached once $\frac{n}{2^{h}} = 1$ or when $h = log{_2}{n}$

    Level 1: 8 sub-problems of size $\frac{n^{3}}{2}$ which gives $3n^{2}$

    Level $i$: $8^{i}$ sub-problems of size $\frac{n^{3}}{2^{i}}$ which gives $n(\frac{8^{i}}{2^{i}}) = 4^{i}n^{3}$

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
