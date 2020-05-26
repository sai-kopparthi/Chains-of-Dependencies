# Chains-of-Dependencies
Longer and more complex code has more bugs, and so does code that is not updated as often. But there are other risk factors for bugs. As we know, to not reinvent the wheel, npm packages commonly include other packages, or dependencies, in their code. Often, those dependencies have their own dependencies, thus creating dependency chains, sometimes multiple levels deep. While dependency chaining can speed up development, it also opens up the risk of bug propagation through the levels of dependency chains. In the paper “Structure and Evolution of Package Dependency Networks,” (Links to an external site.) Kikas et al. study dependency chaining, and specifically transitive dependencies.

Inspired by that paper, in this homework, you will look at dependency chains and transitive dependencies. You will also be looking at factors which you’ve already studied that might be predictive of those, in particular source lines of code (LOC), cyclomatic complexity (CYC), and lagginess (LAG).

A transitive dependency is an indirect dependency between packages. E.g., if package A depends on B, and B depends on C, but A does not directly depend on C, then A’s dependence on C is a transitive one.

1) Using the r2c platform write a script to determine if each of the 1,000 packages has a transitive dependency or not, and calculate TRC (package)=the maximal dependency chain depth per package. E.g., for packages A, B, C, D, let A depend on B and D, B on C and D, and D on C. Then, A has C as a transitive dependency. Also, TRC(A)=3 (A->B->D->C), TRC(B)=2 (B->D->C), TRC(C)=0, and TRC(D)=1. 

2) Using the r2c platform, and the statistical package R, build a regression model for TRC, the max chain depth per package (dependent variable) as a function of the package's LOC, CYC, and LAG (dependent variables). You can use your code and results from the previous homeworks to get LOC, CYC, and LAG. Give the regression coefficients and the goodness of fit for the model. Make sure to do the appropriate regression diagnostics. 