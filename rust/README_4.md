# Ownership

Memory management choices:

- garbage collection
- manual memory allocation and freeing
- ownership - set of rules which are checked at compiler time -> Rust

## Stack and Heap

- stack is LiFo, data in there have a fixed size
- data with unknown size at compl. time will be stored in heap
- heap: less organized. mem allocator finds space to that, allocates, returns pointer.
- so pointer stored in stack, alloc memory used in heap
- using stack is faster - no need for allocation

* data access for stack is faster
* on func call, func params and pointers pushed to stack, at returns, popped
* ownership addresses proper memory freeing on heap

## Rules

- each value in Rust has a variable called owner
- there can be one owner at a time
- when owner goes out of scope, the value will be dropped

## Variable Scope

- in the scope of {} the variable is valid

## String type

- for an example
- immutable fixed size string: string literal - stored in stack
- any other strings: String type on heap
  let literal = "hello";
  let s = String::from("hello");
  s.push_str(", world!"); // push_str() appends a literal to a String
  println!("{}", s); // This will print `hello, world!`
- String is mutable growable
- memory must be requested at runtime, and we need to return this memory when we are done
- mem request was done by String::from
- if we mess up freeing: forgetting will waste memory, too early freeing will invalidate it, doing it twice will be error
- we need exactly one allocation and free
  Similar to C++ RAII:
- Rust ownership: the memory is automatically returned once the variable that owns it goes out of scope
- when a variable goes out of scope, it will call its drop function
- rust calls drop automatically at '}'

## Primitive vs Object variable behaviour at assignment

```
let s1 = 5;
let s2 = s1; // this is copy
```

```
let s1 = String::from("hello");
let s2 = s1; // now is this a copy?
```

btw there is a pointer, capacity and lenght - stored in stack. on heap, the content
so s2 = s1

- cant be deep copy because its very slow
- cant be a shallow (pointer, capactiy, length) copy, because at the end of scope, s1 and s2 will be both freeing the heap -> double free problem
- so its a MOVE
  this means, the following will be invalid:

```
let s1 = String::from("hello");
let s2 = s1; // MOVE
println!("{}", s1); // compile error. s1 is invalid now, motherfcker
```

## How to create deep copy? Clone

```
let s1 = String::from("hi");
let s2 = s1.clone();
println!("s1 = {}, s2 = {}", s1, s2);
```

## Copy train vs Drop

Copy trait can be placed on types which are stored in stack - so older variable is still usable after assignment.
Rust will forbid usnig Copy on type which components implemented Drop. (because its frees the heap)
Note: Tuples containing Copy-able variables are primitive.

## Ownership with function parameters

So if calling a function with parameters is a value assignment - we'll lose ownership.
How to use the variables further?

```
fn main() {
    let s1 = gives_ownership();         // gives_ownership moves its return
                                        // value into s1
    let s2 = String::from("hello");     // s2 comes into scope

    let s3 = takes_and_gives_back(s2);

}

fn gives_ownership() -> String {             // gives_ownership will move its
                                             // return value into the function
                                             // that calls it

    let some_string = String::from("hello"); // some_string comes into scope

    some_string                              // some_string is returned and
                                             // moves out to the calling
                                             // function
}


// takes_and_gives_back will take a String and return one
fn takes_and_gives_back(a_string: String) -> String { // a_string comes into
                                                      // scope

    a_string  // a_string is returned and moves out to the calling function
}


```

When we want to calculate length:

```
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{}' is {}.", s2, len);
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() returns the length of a String

    (s, length)
}
```

But overall, it would be nice to borrow just s1.

## References

We can use references in Rust like this:

```
fn main(){
  let s1 = String::from("hello");
  let len = calculate_length(&s1);
}

fn calculate_length(s: &String) -> usize {
  str.len()
}
```

So how does it work?
s -- points to ----> s1 ---- points to ---> heap
So & creates a non-owning reference (out of scope heap will not be dropped)
References are immutable by default.
We can create mutable references:

```
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

But not multiple ones in the same scope (this will ERR):

```
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{}, {}", r1, r2);
```

This can be fixed with adding a scope:

```
    let mut s = String::from("hello");

    {
        let r1 = &mut s;
    } // r1 goes out of scope here, so we can make a new reference with no problems.

    let r2 = &mut s;
```

- We also cannot have a mutable reference while we have an immutable one.
- Multiple immutable references are OK
- ALLOWED if scopes are not overlapping, like using immutable ones, printing THEN creating mutable ones
- Rust errors if it rust to dangling references - like refs from inside a function, copy by value

## Slices

- to reference to contiguous seq of elements in a collection rather than the whole collection
  Note: for iterating, can use this: `for (i, &item) in bytes.iter().enumerate()`
- giving back search result indexes is a bad idea - string can be dead long ago
- String slice:

```
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11]; // can be used as ..11 and 2..
```

so returning the slice can be as &str
now if you try to use it after clearing the string, it will ERR

- string literals are immutable slices
  improved parametering: `fn first_word(s: &str) -> &str {` to more flexible usage

```
let my_string = String::from("hello world");
// first_word works on slices of `String`s
let word = first_word(&my_string[..]);
let my_string_literal = "hello world";
// first_word works on slices of string literals
let word = first_word(&my_string_literal[..]);
// Because string literals *are* string slices already,
// this works too, without the slice syntax!
let word = first_word(my_string_literal);
```
