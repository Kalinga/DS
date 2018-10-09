which(c(T,T,F,F, T, T, F, T)) # 1, 2, 5, 6, 8 
length(which(c(T,T,F,F, T, T, F, T)))  #which takes expression retuning logical vector

numbers <- c(2:100)
(numbers%%2 == 0) #TRUE FALSE  TRUE FALSE  TRUE FALSE  TRUE FALS...
which(numbers%%2 == 0) # 1  3  5  7  9 11 13 15 1...
even <- numbers[which(numbers%%2 == 0)]
even

gender <-  c("m", "f", "m", "m", "f", "m")
str(gender)
gender <- as.factor(gender)
str(gender)
summary(gender)

which.max(airquality$Temp)
which(is.na(airquality$Solar.R)== TRUE)
sum(airquality$Temp > mean(airquality$Solar.R, na.rm = TRUE))
length(which(airquality$Temp>mean(airquality$Temp)))
lapply(airquality, class)
sapply(airquality, class)
lapply(airquality, mean, na.rm=TRUE)

