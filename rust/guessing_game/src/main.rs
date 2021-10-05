use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number");

    let secret_number = rand::thread_rng().gen_range(1,101);


    // new variable, which is mutable
    // :: means its a "static" function
    let mut guess = String::new();
    // &mut guess - so its mutable AND a reference
    // the read_line returns an io::Result enum
    // which contains Ok or Err (in Ok, there is a real value)
    // Ok and Err has expect function, it crashes the program on Err
    // ok Ok, it just unwraps the value
    loop {
        println!("Please input your guess.");
        io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse(){
            Ok(num) => num,
            Err(_) => { println!("ERR? {}", guess); continue },
        };
        // cast it with match checking - just continue if Err

        match guess.cmp(&secret_number) {
            Ordering::Less => { println!("Smaller than needed!"); },
            Ordering::Greater => { println!("Too big!"); },
            Ordering::Equal => { println!("Correct number. You won."); break; },
        }

        println!("You guessed: {}", guess);
    }

    // cargo toml has the list of "compatile versions, like 0.5.5 public api compatible"
    // but what if 0.5.6 breaks something? cargo lockfile stores the actual versions to make it reproducable
    // you can ignore lockfile with cargo update
    // read document with cargo doc --open
    

}
