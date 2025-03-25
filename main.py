import data_base
import data_analysis 

# Organizacao:
def println(estilo='-', quant=60):
	print(estilo * quant)

# Opcoes de menu:
def menu( ):
	print('\nMenu: \n1 - Adicionar\n2 - Estatisticas\n3 - Historico\n4 - Sair')
	while True:
		try:
			opcao = int(input('Escolha uma opção: '))
			if opcao in [1, 2, 3, 4]:
				return opcao
			print('\033[0;31mErro: Opção inválida.\033[0m')
		except ValueError:
			print('\033[0;31mErro: Opção inválida.\033[0m')
	
def mostar_estatisticas( ):
	acertos, puzzles, ranting = data_analysis.quantidade_puzzles( )
	ofenciva = sum([len(itens) for itens in acertos])
	maxi = max(acertos[3])
	mini = min(acertos[0])
	return ofenciva, maxi, mini, puzzles
	
# Codigo principal
def main( ):
	while True:
		escolhas = menu( )
		println()
		if escolhas == 1:
			acerto, rating = data_analysis.pegar_dados()
			adicionar = data_base.formato_salvar(acerto,rating)
		elif escolhas == 2:
			ofenciva, maxi, mini,puzzles = mostar_estatisticas( )
			r, b, e, l, mediaC,mediaR = data_analysis.porcentagem_puzzles()
			print(
    f'Ofensiva:         \033[0;35m{ofenciva}\033[0m dias\n'
    f'Quantidade:       {puzzles} puzzles\n'
    f'Maior acerto:     \033[0;32m{maxi}\033[0m\n'
    f'Menor acerto:     \033[0;31m{mini}\033[0m\n'
    f'Média de acertos: {mediaC}\n'
    f'Média de rating:  {mediaR}\n'
    f'Ruim:             \033[0;31m{r:.2f}%\033[0m\n'
    f'Bom:              \033[0;32m{b:.2f}%\033[0m\n'
    f'Excelente:        \033[0;35m{e:.2f}%\033[0m\n'
    f'Lendário:         \033[0;33m{l:.2f}%\033[0m\n'
)			
		elif escolhas == 3:
			historico = data_analysis.exibir_historico_puzzles()
		else:
			break
		println()	
	
if __name__=='__main__':
	main( )