vector1 <- c(10,15,9) 
vector2 <- c(4,7)

vector3 <- vector1 + vector2
print(vector3)

vector3 <- vector1 * vector2
print(vector3)

#Rules of coercion, the order is Logical < Numeric < Character


vector_bool_int <- c(1,2,3,3,4,5,5,5,T)
typeof(vector_bool_int) # double
class(vector_bool_int) # numeric

vector_bool_char <- c(1,2,3,3,4,5,5,5,"T")
typeof(vector_bool_char) # character
class(vector_bool_char) # character

combined_vector = c(vector_bool_char, vector_bool_int)
typeof(combined_vector) # character
class(combined_vector) # character

vector_bool_short <- c(T,F,T,T,T,F,T,F,T,T)
typeof(vector_bool_short) # logical
class(vector_bool_short) # logical
sum(vector_bool_short)
sum(vector_bool_short == F)
