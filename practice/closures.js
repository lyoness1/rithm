/* CLOSURES PRACTICE */

/* SHORT ANSWER

1. What is 'scope'?
2. What is 'hoisting'?
3. What is the definition of a closure?
4. What are some common use cases for closures?
*/

/* PRACTICE */

// 1. What will the following code output?
var arr = [2, 3, 4];

for (i = 0; i < 3; i++) {
	arr[i] = function() {
		console.log(i);
	};
}

arr[0](); // ?
arr[1](); // ?
arr[2](); // ?

// 2. Rewrite the above code so its output will be 4, 6, 8 (each on a new line)

// 3. What will each of the following code snippets output?

function outer(x) {
	return function inner(y) {
		return x * y;
	};
}

var outer2 = outer(2);
var outer5 = outer(5);
outer2(3); // ?
outer2(6); // ?

function makeNameFunc() {
	var name = 'John';
	function displayName() {
		console.log(name);
	}
	return displayName;
}

var myFunc = makeNameFunc();
myFunc(); // ?
var name = 'Susam';
myFunc(); // ?

// 4. Write a function that will allow this:

var addSix = createBase(6);
addSix(10); // 16
addSix(21); // 27

// 5. Write a function that will allow this:

var counter1 = counter();
counter1(); // 1
counter1(); // 2
var counter2 = counter();
counter2(); // 1
counter1(); // 3

/* ADVANCED PRACTICE */

// 1. Rewrite #4 and #5, above, using a language other than Javascript

// 2. Can you think of any other ways - besides global variables or closures -
//    to create a private counter object, as in #5, above?
