import data_base
		
# Obter resultado e ranting:
def pegar_dados( ):
	while True:
		try:
			acertos = int(input('Quantos acertos? '))
			ranting = int(input('Qual o ranting? '))
			
			# Retono de dados:
			return acertos, ranting
		except ValueError:
			print('\033[0;31mErro: Dado inválido.\033[0m')

# Historico de acertos:
def exibir_historico_puzzles():
    # Obter dados de todas as categorias:
    categorias = {
        "Ruim": data_base.especificos_dados('ruim'),
        "Bom": data_base.especificos_dados('bom'),
        "Excelente": data_base.especificos_dados('excelente'),
        "Lendário": data_base.especificos_dados('lendario'),
    }   
    # Exibir os dados de cada categoria:
    for nome, dados in categorias.items():
        print(f'\n{nome}:')
        for i, registro in enumerate(dados, start=1):
        	data, resultado, mais_alto = registro
        	print(f'{i}ⁿ data: {data}, acertos: {resultado}, rating: {mais_alto}.')

def quantidade_puzzles():
    # Somatoria:
    puzzles = 0
    ranting = 0
    # Inicializar listas para cada categoria
    acertos = [ [ ], [ ], [ ], [ ] ]  
    # Obter dados de todas as categorias
    categorias = {
        "Ruim": data_base.especificos_dados('ruim'),
        "Bom": data_base.especificos_dados('bom'),
        "Excelente": data_base.especificos_dados('excelente'),
        "Lendario": data_base.especificos_dados('lendario'),
    }

    # Iterar pelas categorias e extrair resultados
    for categoria, dados in categorias.items():
        for registro in dados:
            data, resultado, mais_alto = registro
            puzzles += resultado
            ranting += mais_alto
            if categoria == 'Ruim':
                acertos[0].append(resultado)
            elif categoria == 'Bom':
                acertos[1].append(resultado)
            elif categoria == 'Excelente':
                acertos[2].append(resultado)
            elif categoria == 'Lendario':
                acertos[3].append(resultado)
    return acertos, puzzles, ranting

def porcentagem_puzzles( ):
    acerto, puzzle, rating= quantidade_puzzles()             
   # Quantidade total de acertos:
    total = sum([len(itens) for itens in acerto])
    # Separana porcentagem de cada:
    ruim = (len(acerto[0]) * 100) / total
    bom =  (len(acerto[1]) * 100) / total
    excelente =  (len(acerto[2]) * 100) / total
    lendario =  (len(acerto[3]) * 100) / total
    # medias:
    m_acerto = puzzle // total
    m_rating = rating // total
    
    return ruim, bom, excelente, lendario, m_acerto,m_rating