## CLOSURES
### Why? What's the point? 
Let's start with the why. Here are two examples of times when code may not work the way one would hope:

#### Example 1: The loop that stores state
```javascript
var arr = []

for (var i = 0; i < 5; i++) {
  arr[i] = function() {
    console.log(i);
  }
}
```

What would you expect the outcome of the following code to be?
```javascript
> arr[0]()
> arr[1]()
> arr[2]()
> arr[3]()
> arr[4]()
```

Try it! Can you explain what's going on? Can you think of a way to get the expected result?

#### Example 2: The private variable
Imagine you'd like to write a function to allow someone to guess a secret password

```javascript
var password = 'abc123'

function guessPassword(guess) {
  if (guess == password){ 
    return true
  }
  return false
}
```

The function will work appropriately: 

```javascript
> guessPassword('xyz987')
false
> guessPassword('abc123')
true
```

But what if you really needed the password to be secret? It's in the global scope and is accessible to the guesser that also has access to the function `guessPassword` that is in the global scope. 

```javascript
> password
abc123
```

That wasn't very secret. How might you write a `guessPassword` function so the user of the function wouldn't have access to the secret value? 

### Closures

A **closure** is an inner function that has access to its outer (enclosing) function's scope and variable assignments. 

#### Example 1: A closure with scoped variable parameters
```javascript
function addOuter(x) {
  function addInner(y) {
    return x + y;
  }
  return addInner;  // A _reference_ to the inner function is returned; `addInner` is not invoked here. 
}
```

**We would say that `addInner` is a closure, because it is enclosed by 'addOuter'**.

What would you expect the outcome of the following code to be?

```javascript
> var addToTwo = addOuter(2)
> var addToFive = addOuter(5)
> addToTwo(3)
> addToFive(4)
```

What's going on? The function `addOuter` returns a reference to `addInner` and assigns it to a variable that can later be invoked with any argument for `y`. The function `addInner` is a **closure**, so it has access to the variable `x` in the `addOuter` function's scope. When `addOuter` is invoked and assigned to a new variable we are left with code equivelent to: 

```javascript
function addToTwo(y) {
  return 2 + y;  // The '2' is the value that was passed in as 'x' to 'addOuter' when 'addToTwo' was defined. It can't be changed. 
}

function addToFive(y) {
  return 5 + y;
}
```

So the result is 

```javascript
> addToTwo(3)
5
> addToFive(4)
9
```

#### Example 2: A closure with hoisted variable declarations
```javascript
function greet() {
  var speak() {
    console.log(phrase);
    var phrase = 'Hello, World!'
  }
  return speak;
}
```

In this example, `speak` is a closure because it is wrapped by the outer function `greet`. What would you expect the following to output?

```javascript
> var sayHello = greet()
> sayHello()
```

You may be wondering why this works, as the variable `phrase` isn't assigned a value until after the logging statement. This is because the variable `phrase` is _declared_ through hoisting at the time of creation, so the log statement will have access to `phrase`. The _assigned_ value of `'Hello, World!'` isn't needed until later, after it has been assigned, when `sayHello` is invoked and executed. This example demonstrates that 

**closures contain any and all local variables that were declared inside the outer enclosing function**.

#### Example 3: Dynamically scoped variables
In the following example, what will the output be?

```javascript
function numberGenerator() {
  var num = 0
  function logNumber() {
    console.log(num);
  }
  num ++;
  return logNumber;
}

> var generate = numberGenerator()
> generate()
```

What's going on? When `numberGenerator` is invoked and assigned to the variable `generate`, all of its code is executed and the function returns before the assignment to `generate` is complete. When `generate` is then later invoked, the value of `num` will be whatever it is at the time of invocation, which, in this case, will be `1`, since `num` was incremented before `generate` was called. This example demonstrates that 

**closures will execute with the current state of any variables declared outside of its own scope**.

Here's another example of dynamic scoping and how it affect closures:

```javascript
var x = 5

function foo() {
  var y = x + 5;
  return y;
}

function bar() {
  var x = 0;
  return foo();
}

> foo()
> bar()
```

Deciphering the output of `bar()` can be difficult - what scope will the inner `foo()` use for the assignment of the variable `x`? Globally, `x = 5`, but within the scope of `bar`, the variable `x` is reset to `x = 0`. Because `foo()` is invoked after the reassignment of `x`, `bar()`, the code becomes: 

```javascript
var x = 5; 

function bar() {
  var x = 0;
  return function() {
    var y = x + 5;
    return y;
  }()
}
```

It is easier to see by rewriting `foo` in its entirety within the scope of `bar` that the state of the variable `x` will be its assigned value from within `bar` when `foo` is executed as a result of invoking `bar`. 

### Revisiting the Why of Closures
In our initial example, a for loop was expected to return a function that incremented a variable on each call of a for loop: 

```javascript
var arr = []

for (var i = 0; i < 5; i++) {
  arr[i] = function() {
    console.log(i);
  }
}

> arr[0]()  // 0, expected 0
> arr[1]()  // 0, expected 1
> arr[2]()  // 0, expected 2
> arr[3]()  // 0, expected 3
> arr[4]()  // 0, expected 4
```

We can fix this with a closure!

```javascript
var arr = []

for (var i = 0; i < 5; i++) {
  arr[i] = (function inner(x) {  // The variable `x` is now a private variable local to the closure or inner function
    return function(x) {
      console.log(x);
    }
  })(i)  // The wrapping function will execute on each iteration of the for loop with a new value of `i`
}

> arr[0]()  // 0, expected 0
> arr[1]()  // 1, expected 1
> arr[2]()  // 2, expected 2
> arr[3]()  // 3, expected 3
> arr[4]()  // 4, expected 4
```

Why does this work? Instead of assigning a function to each index in the array that logs the value of the outer-scoped variable `i`, we freeze the state of the outer variable `i` on each iteration of the loop and assign it to a new variable `x` which is local to the inner function. This way, a different function will be inserted on each iteration of the loop with a frozen state of `i` stored in `x`. 

_NOTE_: In ES6 there is an even more cleaver and straightforward way to solve this problem using 'let'. Can you figure it out? 

This can take a while to grasp. Let's fix our other example of the secret password: 

```javascript
function secretPassword() {
  var password = 'abc123'
  return function guessPassword(guess) {
    if (guess == password){ 
      return true
    }
    return false
  }
}

> var guessingGame = secretPassword()
> guessingGame('xyz987')
false
> guessingGame('abc123')
true
```

Why does this work? Well, the variable `password` is now only available within the scope of `secretPassword` and can't be accessed or changed. By assigning the inner function, `guessPassword` (the return value of `secretPassword`) to a new variable, `guessingGame`, the function we're now using, `guessingGame` has access to the secret variable `password` to assess the accuracy of the guess, but nothing outside of `secretPassword` has access to it. 

### Summary
* A **closure** is an inner function that has access to any and all variables _declared_ within and outside its own scope. 
* A **closure** will execute with the _current state_ of any external variable _assignments_ at the time of its execution. 
