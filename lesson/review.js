### Review
A **scope** in code refers to where variables are accessible within that code. If a variable has a '_global_' scope, it will be useable by any code within that module or file. If a variable is defined within a function (or object, in javascript), it will have a '_local_' scope and can only be accessed within that function. 

**Example:**
```javascript
// Define a variable in the global scope (this will be the "window" in a browser running javascript code)
var globalVariable = 10;

// Define a function that adds two variables
function add () {
  var localVariable = 5;
  return globalVariable + localVariable;
}

// Any variable defined in the global scope is accessible everywhere
> globalVariable
10

// Any variable defined inside a function is only accessible inside the scope of that function
> localVariable
ReferenceError: localVariable is not defined

// Use the function, noting that it has access to both the global variable outside of its local scope and the local variable defined within its scope
> add()
15
```

As a rule of thumb, every local scope has access to any variable defined outside its own scope. However, local variables are not availble to any scopes outside of themselves.

**Example**
```javascript
// The variable 'x' is within the global scope
var x = 3;

// Nest some functional scopes and define variables within each
function outer() {
  var y = 7;  // The variable 'y' is available within the 'outer' function's scope
  function inner() {
    var z = 10; // The variable 'z' is availible within the 'inner' function's scope
    console.log('z: ' + z);
    console.log('y: ' + y);
    console.log('x: ' + x);
   }
   inner();  // Make a call to the inner function to see its output
   console.log('z: ' + z);
   console.log('y: ' + y);
   console.log('x: ' + x);
 }
 
 // See what happens...
 > outer()
 ReferenceError: z is not defined
 ```
 
 Where in the code was the error?
 
 ```javascript 
 // Rewrite 'outer' without the reference to 'z' outside of the 'inner' scope
 function outer() {
  var y = 7;
  function inner() {
    var z = 10;
    console.log('z: ' + z);
    console.log('y: ' + y);
    console.log('x: ' + x);
   }
   inner();
   console.log('y: ' + y);
   console.log('x: ' + x);
 }
 
 > outer()
 z: 10
 y: 7
 x: 3
 y: 3
 x: 7
 ```