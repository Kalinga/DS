dice  <-  c(1, 2, 4, 5, 5, 3, 2, 6, 3, 5, 6, 2, 1, 4, 3, 6, 5, 3, 2, 2, 5) 
dice_factor <-  factor(dice)
dice_factor
dice_factor[2]<-12
dice_factor[3]<-122
summary(dice_factor)
dice_levels <- levels(dice_factor)
dice_levels
rm(list=ls())