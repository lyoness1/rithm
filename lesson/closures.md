/* CLOSURES */

// Let's start with the why. Here are two examples of times when code may not work the way one would hope

// Example 1: the loop
var arr = []
for (var i = 0; i < 5; i++) {
	arr[i] = function() {
		console.log(i);
	}
}

/* What would you expect the outcome of the following code to be?

> arr[0]()
> arr[1]()
> arr[2]()
> arr[3]()
> arr[4]()

Try it! Can you explain what's going on? */


