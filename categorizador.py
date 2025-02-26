from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4o-mini"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    prompt_system = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.
        
        #Lista de Categorias Válidas
        {lista_categorias_possiveis.split(", ")}
        
        #Formato de Saída
        Produto: Nome do Produto
        Categoria: apresente aqui a categoria do produto
        
        #Exemplo de Saída
        Produto: Camiseta de Algodão Orgânico
        Categoria: Moda Sustentável
    """
    response = client.chat.completions.create(
        model = model,
        messages=[
            {
                "role": "system",
                "content": prompt_system
            },
            {
                "role": "user",
                "content": nome_produto
            },
        ],
        temperature = 0,
        max_tokens=200
    )
    
    return response.choices[0].message.content

categorias_validas = input("Digite as categorias válidas, separadas por vírgula: ")

while True:
    nome_produto = input("Digite o nome do produto: ")
    text_response = categoriza_produto(nome_produto, categorias_validas)
    print(text_response)
    
   
   