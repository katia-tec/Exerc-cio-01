lista_compras = []

while True:
    item = input("Digite o nome do item:")
    quantidade = int(input("Digite a quantidade desejada: "))
        
    continuar = input("Deseja adicionar mais itens? (s/n): ")
    if continuar.lower() != "s":
        break
    
    
    lista_compras.append({'Nome do item': item, 'Quantidade': quantidade})
   
   # Exibir lista
    
print("Lista de compras: ")
for item, quantidade in lista_compras:
    print(f"Item: {item}, Qualidade: {quantidade}")
    
    # Media de notas
    
    num_notas = int(input("Digite o número de notas: "))
    notas = []
    
    for i in range(num_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
        
        
    media = sum(notas) / num_notas
    print(f"A média das notas é: {media}")
    
    
    # Pandas dicionários
    
    import pandas as pd
    
    compras_data = [
        {'Código': 1, 'Produto': 'Arroz', 'Categoria': 'Alimentos', 'Quantidade': 50, 'Valor unitário': 6 },
         {'Código': 2, 'Produto': 'leite', 'Categoria': 'Alimentos', 'Quantidade': 25, 'Valor unitário': 4}, 
         {'Código': 3, 'Produto': 'Sabonete', 'Categoria': 'Higiene', 'Quantidade': 15, 'Valor unitário': 3}    
    ]
    
    # DataFrame
    
    compras_df = pd.DataFrame(compras_data)
    
    # Exibir o DataFrame
    
    print("\nDataFrame - Lista de compras:")
    print(compras_df)
        
       # Resultados
    
    quantidade_vendida_por_produto = compras_df.groupby('Produto')['Quantidade'].sum()
    ticket_medio = compras_df.groupby['Valor total comprado'].mean()
    quantidade_media_por_compra = compras_df['Quantidade'].mean()
    total_vendido_por_produto = compras_df.groupby('Produto')['Total'].sum()
    
    # Exibir resultado
    
    print("\nResultados:")
    print(f"Quantidade vendida por produto:\n{quantidade_vendida_por_produto}")
    print(f"\nTicket médio: {ticket_medio:.2f}")
    print(f"\nQuantidade médio comprada por compra: {quantidade_media_por_compra:.2f}")
    print(f"\nTotal vendido por produto:\n{total_vendido_por_produto}")
    