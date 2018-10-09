age <- c(30:32)
income <- c(seq(3000,3200,250))
balance <- c(seq(1300,2000, 400))
m <- matrix(c(age, income, balance), nrow=5, ncol=3) #byrow FALSE by default
m

## To access elements in multiple rows and columns the syntax is 
## m_part<- m[c(row1,row2,..), c(column1,column2,..)]