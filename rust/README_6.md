# Enums

```
enum IpAddrKind {
    V4,
    V6,
}

let four = IpAddrKind::V4;

fn test(ip: IpAddrKind) {
    ip
}

struct Ip {
    type: IpAddrKind,
    address: String,
}

let ip = Ip {
    type: IpaddrKind,
    address: String::from("127.0.0.1"),
}

fn test2(ip: Ip){
    ip
}

enum IpAddr {
    V4(u8,u8,u8,u8),
    V6(String),
}

let ip = IpAddr::V4(String::from(127,0,0,1));
```
// can put different type of data within enums
// can use impl to implement functions
// grouping data together like a class

## Option enum
to handle Nullpointer cases
> The problem with null values is that if you try to use a null value as a not-null value, you’ll get an error 
So how to solve? Null value will be moved to type level.
On unwrapping, you should handle the empty scenario.
```
enum Option<T> {
    Some(T),
    None,
}
```

```
let s = Some(5);
let s2 = 7;
let s3: Option<i8> = None;
let a = s + s2; // ERR
```
## Match

patterns can be ltierals, variable names, wildcards, etcs.

```
match coin {
    Coin::Penny => { println!("Penny!"); 1}
    Coin::Nickel => 5,
    Coin::Quarter(state) => {
    println!("State quarter from {:?}!", state);
    25
}
}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five);
let none = plus_one(None);
```

matches are exhaustive

The _ pattern

## If let
when you would write match to handle only one case:

if let Some(3) = some_u8_value {
        println!("three");
}
