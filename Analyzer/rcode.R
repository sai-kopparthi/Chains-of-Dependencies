library(car)
dd = read.csv("mycsvfile.csv",header=T,sep=",")
#Model1
#check how the data is distributed by plotting a boxplot if the data for any of our explonatory  variable is not normally distributed I "log" the values if log(explonator variables) are giving me NAN because of log(0) is not defined I am removing those rows using my python create_csv.py script
boxplot(dd$complexity)
boxplot(dd$timelag)
boxplot(dd$nloc)
linearMod1 <- lm(depth~(complexity)+(nloc)+(timelag), data=dd)
summary(linearMod1)
plot(linearMod1)
#MODEL 2
#As we can se above the box plots of the above data are very skewwed and I am logging the variables and also removed in my data with rows of value zero from my python script (create_csv.py)
boxplot(log(dd$nloc))
boxplot(log(dd$complexity))
boxplot(log(dd$timelag))
linearMod <- lm(depth~log(complexity)+log(nloc)+log(timelag), data=dd)
#coefficients of our fitted model
linearMod$coefficients
#checking for any outliers with any high leverage values and high residuals and you can see there are no such points in my case 
outlierTest(linearMod)
#You can see my Adjusted R-square value is increased from previous model before normalizing the data
summary(linearMod)
anova(linearMod)
#Gives us all the Dignositic plots for our model .
plot(linearMod)
#checking for multi-collinearity between vvariables if value of any of our variable is >5 remove those variable and fit a new model. But in my case all the values are <5
vif(linearMod)

#Model 3 - Checking for any interaction between independent variables gives me any better results
linearMod3<-lm(depth~log(nloc)+log(timelag)+log(complexity)+timelag*nloc,data=dd)
summary(linearMod3)
plot(linearMod3)
vif(linearMod3)
#You can clearly see from the Model3 My plot with residuals vs leverage I can see the cook curves which makes it a bad model and hence I am discarding this model and I can Model2 is better than Model1 and Model3

#this is the main influence plot for my Model2
cutoff <- 4/((nrow(dd)-length(linearMod$coefficients)-2)) 
influencePlot(linearMod, id.method="identify", main="Influence Plot", sub="Circle size is proportial to Cook's Distance" )
#Since I am not sure about my high leverage points from the points I am not removing those points

