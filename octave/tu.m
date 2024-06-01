
## initializing the matrix
a = [1 2 ; 3 4 ; 5 6 ]; ## 3*2
b = [ 11 12 ; 13 14 ; 15 16]; #3*2
c = [1 1 ; 2 2 ]; # 2*2

## matrix multiplication
a*c

# multiplying each element to the cooresponding one
a
b
a .* b

## power operation
a .^ 2

# transpose
a'

# props of matrix
val = max(a)
sz = size(a)
size(a, 1) # rows
size(a, 2 ) # column
[val , ind ] = max(a)

# accessing the matrix elements
# matrix name ( r , c ) < : means every thing >
a(3,2)
a(2 , : )
a( : , 2)
a([1 3 ] , : )
a = [a, [7 ; 8 ; 9 ]];


# magic matrix
m = magic(3)
max(m , [] , 1 ) # one means column
max(m , [] , 2 ) # two means row
pinv(m)
m(:) # turning the matrix into a vector
m2 = magic(9)
sum(m2 , 1 )
sum(m2 , 2 )
m2 .* eye(9)
sum(sum(m2 .* eye(9) ))
flipud(eye(9))


# vectors
v = [1 ; -2 ; 3]
1 ./ v
log(v)
exp(v)
abs(v)
v + ones(length(v) , 1 ) ## making a ones vector
v + 1  # same results
v < 3
find(v < 3)

v2 = [ 0.24   ;  3.0000 ; 4.00000 ]
prod(v2)
sum(v2)
floor(v2)
ceil(v2)

# loops , conditions

v = zeros(10 , 1 )
for i = 1 : 10
  v(i) = 2^i
end;

while i = 1:5 ,
 v(i) = 100
 i = i + 1
end;
























