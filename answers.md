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

    Level 1: 9 sub-problems of size $(\frac{n}{3})^{2}$ which gives $n^{2}$

    Level $i$: $9^{i}$ sub-problems of size $(\frac{n}{3^{i}})^{2}$ which gives $n(\frac{9^{i}}{3^{2i}}) = n^{2}$

    This gives $log{_3}{n}$ levels of $n^{2}$ so $T(n) = \Theta(n^{2}log{_3}{n}) = \Theta(n^{2}logn)$

    e) $T(n)=8T(n/2)+n^3$

    Base case is reached once $\frac{n}{2^{h}} = 1$ or when $h = log{_2}{n}$

    Level 1: 8 sub-problems of size $(\frac{n}{2})^{3}$ which gives $n^{3}$

    Level $i$: $8^{i}$ sub-problems of size $(\frac{n}{2^{i}})^{3}$ which gives $n(\frac{8^{i}}{8^{i}}) = n^{3}$

    This gives $log{_2}{n}$ levels of $n^{3}$ so $T(n) = \Theta(n^{3}log{_2}{n}) = \Theta(n^{3}logn)$

    f) $T(n)=49T(n/25)+n^{3/2}\log n$

    Using the master theorem: $a = 49, b = 25, f(n) = n^{\frac{3}{2}}log{n}$

    $log{_25}{49} \approx 1.21$ this is less than $\frac{3}{2}$

    This means $49f(\frac{n}{25}) < cf(n)$ for some $c < 1$ for sufficiently large $n$ 

    So, $T(n) = \Theta(n^{\frac{3}{2}}logn)$

    g) $T(n)=T(n-1)+2$

    Substituting for $T(n-1)$ gives us $T(n) = (T(n-2)+2)+2$

    After expanding to the $i$ times: $T(n) = T(n-i)+2i$

    The base case would be $T(1) = \Theta(1)$ which is reached when $i = n-1$

    Substituting that back in: $T(n) = \Theta(1) + 2n - 2$ which gives the final run time of $T(n) = \Theta(n)$
  
    h) $T(n)= T(n-1)+n^c$, with $c\geq 1$

    Substituting for $T(n-1)$ gives us $T(n) = T(n-2)+(n-1)^{c})+n^{c}$

    The base case would be $T(1) = \Theta(1)$ which is reached when $i = n-1$

    At which point $T(n) = T(1)+ \sum_{k=2}^{n} k^c = 1^{c} + 2^{c} ... + n^{c} = \Theta(n^{c+1})$

    i) $T(n)=T(\sqrt{n})+1$

    Level 1: $T(n) = T(\sqrt{n}) + 1$

    Level 2: $T(n) = T(n^{\frac{1}{4}}) + 2$

    Level $i$: $T(n) = T(n^{\frac{1}{2^{i}}}) + i$

    Base case reached when $n^{\frac{1}{2^{i}}} = 2$ -> $2^{i} = log{_2}{n}$ -> $i = log{_2}{log{_2}{n}}$

    So $T(n) = T(2) + log{_2}{log{_2}{n}} = \Theta(log{_2}{log{_2}{n}})$
   
1. **Algorithms Comparison**
