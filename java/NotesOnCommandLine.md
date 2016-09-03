# Notes on using java from the command line

## Compiling

```
javac -classpath bin -d bin src/packageName/ClassName.java
```
This will create the file `bin/packageName/ClassName.class`.  This can be refernced
by other packages using the qualified name `packageName.ClassName` if `bin` is set
as the `-classpath` option.


## Running the compiled class

```
javac -classpath bin -d bin src/packageName/ClassName.java
```

will run the class and should resolve packages if they have been compiled as
above.
