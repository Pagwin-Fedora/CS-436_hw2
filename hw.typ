#set heading(numbering: "1.a.i)")
#show strike: it =>[
    #set text(red)
    #it
]

// TOTAL: 1500

#let E(str) = $E_(str)$

// Q1 (200)
// DONE
= A data set has 600 examples. To properly test the performance of the final hypothesis, you set aside a randomly selected subset of 200 examples which are never used in the training phase; these form a test se. You use a learning model with 1,000 hypotheses and select the final hypothesis $g$ based on 400 training examples. We wish to estimate $E("out")(g)$. We have acces to two estimates: $E("in")(g)$, the in sample error on the 400 training examples; and, $E("test")(g)$, the test error on the 200 test examples that were set aside.

== Using a 5% error tolerance ($delta = 0.05$), which estimate has the higher 'error bar'

$ E("out")(g) lt.eq E("in")(g) + sqrt(1/(2N)ln(2(m_H (N))/delta)) $

not sure how to plug into Hoeffding’s Bound to get actual numbers but I'd expect the estimate with #E("in") to have larger error bars due to over fitting

== Is there any reason why you shouldn't reserve even more examples for testing?

It makes it harder to lower $E("in")$ which is a pre-requisite for lowering $E("out")$

//Q2 (100)
// NOPE
= #strike[For an $H$ with $d_("VC") = 10$, what sample size do you need (as prescribed by the generalization bound) to have a $95%$ confidence that your generalization error is at most 0.05?]


//Q3 (400)
= Consider a simplified learning scenario. Assume that the input dimension is one. Assume that the input variable $x$ is uniformaly distributed in the interval $\[-1,1\]$. The data set consists of 2 points ${x_1,x_2}$ and assume that the target function is $f(x) = x^2$. Thus, the full data set is $D = {(x_1, x^2_1), (x_2,x^2_2)}$. The learning algorithm returns the line fitting these two points as $g$ ($H$ consists of functions of the form $h(x)=a x + b$). We are interested in the test performance ($E("out")$) of our learning system with respect to the squared error measure, the bias and the var.

#let ag = $overline(g)$

// DONE
== Give the analytic expression for the average function $ag(x)$

//https://www.wolframalpha.com/input?i2d=true&i=Divide%5B1%2C4%5DIntegrate%5BIntegrate%5BDivide%5BPower%5Ba%2C2%5D-Power%5Bb%2C2%5D%2Ca-b%5D%5C%2840%29x-b%5C%2841%29%2BPower%5Bb%2C2%5D%2C%7Bb%2C-1%2C1%7D%5D%2C%7Ba%2C-1%2C1%7D%5D
// (1)^2x/4-(-1)^2x/4 = x/4 - x/4= 0
$ ag(x)=1/4 integral_(-1)^(1)(integral_(-1)^(1)((a^2-b^2)/(a-b)(x-b)+b^(2))"db") "da" = 0$

// DONE
== Describe an experiment that you could run to determine (numerically) $ag(x)$, $E("out")$, bias, and variance

Pick $n$ pairs of points, for each pair calculate the line of best fit, calculate #E("out") then using the results of that calculate average function, bias and variance

// NOPE
== #strike[Run your experiment and report the result. Compare $E("out")$ with bias+var. Provide a plot of your $ag(x)$ and $f(x)$ (on the same plot).]

// nope
== #strike[Compute analytically what $E("out")$, bias and var should be.]

//Q4 (200)
#strike[
= Compute gradient descent on $f$ 

$f(x,y)=2x^2+y^2+3sin(2 pi x)cos(2 pi y)$

// NO
== starting from the point $(0.1, 0.1)$. Learning rate of 0.01, and 50 iterations. Give a plot that displays how the function value drops through successive iterations of gradient descent. Repeat this with a learning rate of 0.1 and provide a function plot with each iteration

// NO
== Obtain the “minimum” value and location of the minimum value of the function you get using gradient descent with the same learning rate 0f 0.01 and 50 iterations from the following start points. Write the minimum value for each

=== (0.1,0.1)

=== (1,1)

=== (0.5, 0.5)

=== (0.0, 0.5)

=== (-0.5, -0.5)

=== (-1, -1)
]
//Q5 (100)
// TODO
= Using the MNIST dataset only considering the digits 1 and 5 (other digits must be removed) do the following.

see filter.py for details on how this filtering was done

== Familiarize yourself with the dataset by giving a plot of the first two digits in ZipDigits.train.


Hint: If you are using the Python programming language, you may use matplotlib.pyplot.imshow which takes a 2-D array as input. You may refer to the documentation on how to display a grayscale image.

== Develop two features to measure properties of the image that would be useful in distinguishing between the digits 1 and 5. You may use average intensity and symmetry (defined in LFD Example 3.1) as your two features, or define and compute any other features you think are better suited to help distinguish between 1 and 5. Provide a mathematical definition of the two features you compute using the notation discussed in class.

== Provide a 2-D scatter plot of the examples in ZipDigits.train w.r.t. the two features you defined in Part (b), similarly to the scatter plot in LFD Example 3.1 and elsewhere in LFD Chapter 3. For each example, plot the values of the two features with a red ‘×’ marker if it is a 5 and and a blue ‘◦’ marker if it is a 1. You must clearly label each axis with the feature it represents, and it should be possible to determine for each data point, the values of the two features you computed. You must also include a legend on the upper right corner of your scatter plot which clearly identifies that data points marked with ‘×’ represent examples of the digit 5 those marked ‘◦’ marker represent examples of the digit 1.

Additional tips for plotting:

- You may find it useful in the long run to use matplotlib.pyplot.subplots to generate both a matplotlib.figure.Figure object and one or more matplotlib.axes.Axes objects. At a high level, you may think of the Figure object as a sort of canvas that gets displayed or saved as a file and the Axes object as a collection of plot elements that need to be printed onto the canvas. Each Axes object may therefore refer to a different collection of plot elements that together make up a plot and you get to pick where it gets printed on the canvas or let the library decide it for you. Therefore, it will often be useful to maintain a pointer to the Axes objects of interest so you can manipulate them and add different plot elements like axis labels, legends, and so forth.
For more details, you may find this article and this article to be of interest.
- To add a legend to your plot, you may find this guide and this guide.
- To manually control how the values along each axis are marked, you may use
matplotlib.axes.Axes.set xticks and matplotlib.axes.Axes.set yticks, and find
this guide helpful.
- If you are having trouble printing your image, you may use matplotlib.pyplot.tight layout. Its use
is documented in this guide.

//Q6 (500)
// TODO
= Train a classifier using linear regression via pocket algorithm or logistic regression using gradient descent +1 for 1 -1 for 5. Using the clasifier

== Give separate plots of the training data (ZipDigits.train) and test data (ZipDigits.test) which display the data points using the two features you computed in HW2, together with the separator.

== Compute $E("in")$ on your training data (ZipDigits.train) and $E("test")$, the error of your separator on the test data (ZipDigits.test).

== Obtain a bound on the true out-of-sample error (Eout). You should get two bounds, one based on $E("in")$ and another based on $E("test")$. Use a tolerance of $delta = 0.05$. Which is the better bound?
