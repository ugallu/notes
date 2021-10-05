# Structs

```
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}
```

Dot notation:

```
let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
```

- field init shorthand - use the same field as the var name
-

```
let user2 = User {
   email: String::from("another@example.com"),
   username: String::from("anotherusername567"),
   ..user1
};
```

- tuple structs:

```
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);
```

- string references in structs?
- unit-like struct witout fields?

rectangle calculator: variables -> coupling to tuples -> naming to structs
printing: #[derive(Debug)]
println!("rect1 is {:?}", rect1);
