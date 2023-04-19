#!/usr/bin/env python3
from io import FileIO
import openai
import logging
import ast

def compile_file(file: FileIO, tries=5) -> str:
    logging.info("Compiling file: %s", file)
    with file:
        source = file.read()

    for i in range(tries):
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful compiler."},
                {"role": "user", "content":
                 "Can you compile this source code to a Python. Only return the python source code. Do not do anything else only translate the given code.\n" +
                 "If you need you can import anything. If you can't make out what the source language is just assume what the syntax might do."},
                {"role": "user", "content": f"Source:\n{source}"},
                {"role": "assistant",
                    "content": "Sure, here's the Python code for the given source code:"}
            ],
            temperature=0.9,
        )

        code = result["choices"][0]["message"]['content']
        try:
            ast.parse(code)
        except Exception as e:
            logging.warning("Got invalid code: %s", code)
            continue

        logging.info("Got code: %s", code)
        return f"#!/usr/bin/env python3\n{code}"

    raise Exception("Could not compile file: %s", file)


if __name__ == "__main__":
    import glob
    all_sources = glob.glob("**/*.any")
    for file in all_sources:
        script = compile_file(file)
        print(f"{file}\n\n{script}")
        # eval(script)
