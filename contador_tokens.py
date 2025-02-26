import tiktoken_ext
import tiktoken
from tiktoken.core import Encoding

modelo1 = "gpt-4o-mini"
codificador1 = tiktoken.encoding_for_model(modelo1)
lista_tokens1 = codificador1.encode("Você é um categorizador de produtos.")
print("Lista de tokens:", lista_tokens1)
print("Quantidade de tokens:", len(lista_tokens1))
print(f"Custo para o modelo {modelo1} é de ${(len(lista_tokens1)/1000) * 0.03} ")

modelo2 = "gpt-4o"
codificador2 = tiktoken.encoding_for_model(modelo2)
lista_tokens2 = codificador2.encode("Você é um categorizador de produtos.")
print("Lista de tokens:", lista_tokens2)
print("Quantidade de tokens:", len(lista_tokens2))
print(f"Custo para o modelo {modelo2} é de ${(len(lista_tokens2)/1000) * 0.03} ")

modelo3 = "gpt-3.5-turbo"
codificador3 = tiktoken.encoding_for_model(modelo3)
lista_tokens3 = codificador3.encode("Você é um categorizador de produtos.")
print("Lista de tokens:", lista_tokens3)
print("Quantidade de tokens:", len(lista_tokens3))
print(f"Custo para o modelo {modelo3} é de ${(len(lista_tokens3)/1000) * 0.001} ")

modelo4 = "gpt-3.5-turbo-1106"
codificador4 = tiktoken.encoding_for_model(modelo4)
lista_tokens4 = codificador4.encode("Você é um categorizador de produtos.")
print("Lista de tokens:", lista_tokens4)
print("Quantidade de tokens:", len(lista_tokens4))
print(f"Custo para o modelo {modelo4} é de ${(len(lista_tokens4)/1000) * 0.03} ")