from openai import OpenAI
import os
import tiktoken
import tokenize
enc = tiktoken.encoding_for_model("gpt-4o-mini")

tokens = enc.encode("Olá, Gláudia! Como está você?")
print(len(tokens))