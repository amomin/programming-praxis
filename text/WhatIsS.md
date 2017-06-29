Let X = min(x,y,z)
    Y = min(y,z)
    Z = z

Then it's equivalent to 
```
int s = 0;

for (int i=0; i<X; i++)
    for (int j=i+1; j<Y; j++)
        for (int k=j+1; k<Z; k++)
            s++;
```

So WOLOG `x<=y<=z`.


Second let me assume the sum is `1..X` inclusive (this is easy to achieve by a small change of variables (`x=x+1,...`).

Then

```
=sum(i=1_X)sum(j=i+1_Y)sum(j+1_Z) 1
=sum(i=1_X)sum(j=i+1_Y)Z-j
=sum(i=1_X)Z*(Y-i)-sum(j=i+1_Y)j
=sum(i=1_X)ZY-Zi-sum(j=1_Y)j+sum(j=1_i)j
=sum(i=1_X)ZY-Zi-Y(Y+1)/2+i(i+1)/2
=sum(i=1_X)ZY-Y(Y+1)/2+-Zi+i/2+ii/2
=sum(i=1_X)ZY-Y(Y+1)/2 + .5(-2Z+1)i + .5ii
=XZY-XY(Y+1)/2 + .5(-2Z+1)sum(i=1_X)i + .5sum(i=1_X)ii
=XZY-XY(Y+1)/2 + .5(-2Z+1)X(X+1)/2 + .5*sum(i=1_X)ii
=XYZ-XY(Y+1)/2 + (1/4)(-2Z+1)X(X+1) + .5*sum(i=1_X)ii
=XYZ-XY(Y+1)/2 + (1/4)(-2Z+1)X(X+1) + .5*X(X+1)(2X+1)/6

=XYZ-XY(Y+1)/2 + (1/4)(-2Z+1)X(X+1) + .5*((XX+X)(2X+1))/6
=XYZ-XY(Y+1)/2 + (1/4)(-2Z+1)X(X+1) + .5*((2XXX+3XX+X)/6
=XYZ-XY(Y+1)/2 + (1/4)(-2Z+1)X(X+1) + XXX/6 + XX/4 + X/12
=  XYZ-XYY/2 -XY/2 
 - ZXX/2 -ZX/2 + XX/4 + X/4 
 + XXX/6       + XX/4 + X/12
=  XYZ  -XYY/2  -XY/2 
 - ZXX/2 -ZX/2 + XX/2 + X/3 
 + 6/XXX
```

Where we use the formula for the sum of squares:
```
n(n+1)(2n+1)/6
```
which is easy to guess if you know it's a cubic with denominator 6and leading co-efficient 1 (by using the first 3 sums `1,1+4=5,1+4+9=14` to find the co-efficients.
