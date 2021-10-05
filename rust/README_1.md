# rustbook

To teach myself rust by coding and documenting small projects based on the rustbook

- Install for linux: `curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh`
- Update: `rustup update`
- Uninstall: `rustup self uninstall`
- Check version: `rustc --version`
- Local documentation: `rustup doc`

> First project: hello_world

- Compile & Run: `rustc main.rs; ./main`
- To format code, use tool/extension: rustfmt
- Indenting with 4 spaces
- Marco (somewhat different from functions): func! format
- Line ended with `;`: expression is over, next one is ready to begin

- Cargo version: `cargo --version`

> Create new project: `cargo new hello_cargo`
> creates main.rs and Cargo.toml dependency file too, gitrepo

- In rust, packages of code are referred as crates.
- To build with cargo: `cargo build` or `cargo build --release`
- To run with cargo: `cargo run`
- To check: `cargo check`

- `use package` syntax, like `use std::io;` for Strings
- `let` to create a variable
- immutable variables by default
- `let mut` for mutable variable creation
- `=` for binding variable
- in String::new the `:` is an associated function - implemented on a type (aka static method)
- passing argument for a function like this: `&mut guess` is a mutable reference - to modify its value
-
