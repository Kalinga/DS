#apply family of function
#sapply dataobject and a function to apply
vapply
bank <- read.csv("bank.csv", stringsAsFactors = F)
str(bank)
levels(bank$marital)

for (i in 1:ncol(bank)) {
  q = names(bank[i])
  print(q)
  bank[,i] <- factor(bank[,i] )
}
str(bank)

levels(bank$month)

# for (i in 1:32) {
#   Sys.sleep(0.1)
#   print(i) 
# }

head(bank)

bank2 <- data.frame(sapply(bank, factor))
str(bank2)

mark <- c(12,23,34,23,23)
mark_per <- sapply(mark, function(x) x/40 *100)
mark_per


M <- matrix(seq(1,16), 4, 4)
M

rep(1:4)
rep(4:1)
mapply(rep, 1:4 ,4:1)
mapply(sum, 1:4 ,4:1)
rep(1,1)
rep(2,2)
rep(3,4)

