## CLOSURES
Let's start with the why. Here are two examples of times when code may not work the way one would hope:

### Example 1: The loop that stores state
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

### Example 2: The private variable
Imagine you'd like to write a function to allow someone to guess a secret password

```javascript
var password = 'abc123'

function guessPassword(guess) {
  if guess == password: 
    return true
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

But what if you really needed the password to be secret? It's in the global scope and is accessible to the guesser that also has access to the function 'guessPassword' that is in the global scope. 

```javascript
> password
abc123
```

That wasn't very secret. How might you write a guessPassword function so the user of the function wouldn't have access to the secret value? 


