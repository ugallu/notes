# Clean Code Notes

## Episode 1 - Clean Code

Good code matters. But does it really matter?

#### Story: Company killed by code.
They rushed with the development of the C debugger, causing mess which eventually killed the company.

General development process: 

* New project
* Fast development at the early stages
* Messy code
* Slower development time for features. 
* Business plan based on the early development speed - currently there is a gap.

Manager's solutions: 

* More pressure on developers -> More rushing and worse code quality
* More people - making their own bad code (partly because they are not familiar with the codebase) -> now more costs and lower productivity

Developer's solutions: Making redesign

* Get the "tiger team" (aka best 10 developers) to design the new project
* But what is the requirement? Non-existing docs or outdated. Only valid requirement is the currently working old system.
* Started to chase the old system's requirements by reading code. But during the time, the old system changed.
(Uncle Bob saw this during 10 years)

#### What makes the development hard? Code Rot.
Charasteristics of Code Rot:

* Rigid system. What it means? One modification requires several ones - often in hundreds of other modules just to work again. Unpredictable. Cannot estimate.

* Fragility. Simple change can cause malfunctions all trough the system. Difficult to estimate.

* Inseparability. We want separable and reusable modules. System designers fail to enforce module bounderies. Devs are taking shortcuts. Unpredictable.

* Opacity.
Wft/mins on review. Code is hard to read/understand/change.

At the end: we make the mess. We rush, saying we'll fix it later - but it never happens. Can't go fast without taking mess. 
Stay clean.

Rushing doesn't make development faster.
Watch the sushi master: he is cleaning his place during the very fast process. Its not an extra effort: its the only way that he can be so fast.
> Only way to go fast is go well.

What is clean code? Different answers: 

* Elegant and efficent?
* Simple and direct? Should read like well written prose?
* What is written by someone who cares?
* Each routine does what you expected?

The boy scout rule: Leave the world better then you found.

(and don't read the Implemetation patterns by Kent Beck - its a  terrifying book for good coding habits)

## Episode 2 - Names. 

> Not just stuff. The tools we use to communicate.

#### Tim Ottinger - naming rules.

> Reveal your intent. If the name needs comment, the name is bad.

Bad: `int d; // days`

Good: `int days;`

Bad: `int mm;`

Good: `int resultMonth;`

Bad: `+1 (some misterious incrementation)`

Good: `+ January`

Names are "compilable" comments which explains the authors intent.
True cost of software is in its maintenance. Lets try find names, so others don't have to dig too deep into the code.

#### Describle the problem

* The name is not about how the thing is implementated. Name the problem.

Bad: 
// Useful range constant
public static final int INCLUDE_NONE = 0;
Useful? Constant? Range? WTF.

Good:
// Upper bound of the date range
public enum DateInterval {
OPEN, CLOSED, LEFT_OPEN, RIGHT_OPEN
}

> If you have to go to the code to understand the name, then its a bad name.

#### Avoid disinformation
If the variable means something other than the name -> worst sins.

Bad example
abstract function: SerialDate

But "Serial" is pretty concrete. Don't name your abstract functions with concrete names.

#### Prononcable Names
PC_GWDA - naming. What? Leads to communication errors.
 
#### Avoid encodings.
Hungarian notation. Dont use prefixes for types.
Dont use interfaces or abstract class notations in classes. The IDE knows it, otherwise its just distraction.

#### Parts of Speech

* Classes and variables = nouns or nounphrase
* **Avoid Manager, Processor, Data, Info **
* Methods = verbs
* bool = isSomething
* methods with bool returns = isSomething()
* enums = states of object descriptors -> adjective
 
Bad: bool set(String name);

Good: 
void setName(String name) throws Exception
boolean isSetName(String name);
 
#### Scope length rule
If you use your name close to the declaration, keep it short. 
Its okay to use d, tr, if the code is only 3 line and its a local variable.

* Short scopes -> short variable names.
* Long scopes -> long variable names.
* public methods (long scope): short names are preferred.
* Public class: short names, private classes: longer names.
* Derived class: plus adjectives

