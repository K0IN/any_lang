# Any Lang

A simple language for any purpose.

## What is Any Lang?

It's a simple language that uses no syntax and is easy to learn.

## How to get started?

set your openai api key in your environment variables as `OPENAI_API_KEY` and
download this repo and run `main.py source1.any source2.any ... sourceN.any -o output`

## Examples

here is a example of a simple program:

```any
# this script is just an example
for (int i =(int) 0; i < 10; i++) {
    print(i);
}

// now we can use the variable i
print(i);

while (FALSE) {
    print("this will never be printed")
} else {
    print("why else?")
}

{
    text = readFile("file.txt"); // this file does not exist so this throws an error

}.try (error) {
    print("error: " + error);
}
```

compiles (best case)

```python
#!/usr/bin/env python3
# this script is just an example
for i in range(0, 10):
    print(i)

# now we can use the variable i
print(i)

if False:
    print("this will never be printed")
else:
    print("why else?")

try:
    with open("file.txt", "r") as f:
        text = f.read() # this file does not exist so this throws an error
except Exception as error:
    print("error: " + str(error))
```

or

```any
function resultOf(a, b) {
    return { 
        a: a, 
        b: b - 1 - a, 
        c: log(a) + log(b)
    };
}

def calculate(x) {
    int a = 1;
    int b = 1337;
    return resultOf(a * x, b + 1);
}

fn main(int x) {
   res = calculate(x)
   print(res)
}

main(1);
```

compiles (best case)

```python
#!/usr/bin/env python3
from math import log

def resultOf(a, b):
    return { 
        'a': a, 
        'b': b - 1 - a, 
        'c': log(a) + log(b)
    }

def calculate(x):
    a = 1
    b = 1337
    return resultOf(a * x, b + 1)

def main(x):
   res = calculate(x)
   print(res)

main(1)
```

## How does it work?

your code -> chatgpt -> magic -> python code (and if your lucky it works)
