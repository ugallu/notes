# Advanced cargo

Packages: cargo feature to build test share creates
Crates: Tree of modules that produces a lib or executable
Modules and use: Control the organization, scope and privacy of paths
Paths: A way of naming an item, such as a struct, function, module

## Package and crates
Crate: binary or lib
Crate root: file, the rust compiler starts from here, module
Package: one or more crates that provides set of functionality, it has cargo.toml, 0-1 lib craete, many binary crates, and 1+ create

* cargo new myproject -> creates package
* src/main.rs crate root of of binary crate
* src/lib.rs lib create with the same name of package, crate root

## Modules

* private and public function grouping
* cargo new --lib restaurant;

```
mod front_of_house {
    mod hosting {
        fn add_to_waitlist(){}
    }
}
```

Absolute paths to refer from root of the crate
Relative path using self or super
Separator is ::
Child modules hides privacy from outer/parent/higher modules

```
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    front_of_house::hosting::add_to_waitlist();
}
```

Pub struct, pub field
Only need pub before enum keyword

## Use