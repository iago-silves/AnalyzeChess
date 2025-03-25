import sqlite3
import json
import datetime

# Criacao do banco de dados:
def conn( ):
	return sqlite3.connect('historico_puzzles.db')

# Tabela de armazenamanto de dados json:
def tabela_desempenho( ):
	with conn( ) as conexao:
		cursor = conexao.cursor( )
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS desempenho(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			historico_json TEXT)
			""")
			
		# Salvando dados:
		conexao.commit( )

# Inserindo dados json no data base:
def inserir_dados(dado):	
	with conn( ) as conexao:
		cursor = conexao.cursor( )
		cursor.execute("""
        INSERT INTO desempenho (historico_json) VALUES (?) """, [json.dumps(dado)])
		
		# Salvando dados:
		conexao.commit( )

# Acessando dados especificos:
def especificos_dados(categoria):
    with conn() as conexao:
        cursor = conexao.cursor()
        # Consulta dinâmica para acessar uma categoria
        cursor.execute(f"""
        SELECT json_extract(value, '$.data') AS data,
               json_extract(value, '$.resultado') AS resultado,
               json_extract(value, '$.mais_alto') As mais_alto
        FROM desempenho,
             json_each(json_extract(historico_json, '$.desempenho.{categoria}'))
        """)
        return cursor.fetchall()

# Adicionar novos dados ao json:
def adicionar_dado_categoria(categoria, novo_dado):
    with conn() as conexao:
        cursor = conexao.cursor()
        # Obter o array atual da categoria
        cursor.execute(f"""
        SELECT json_extract(historico_json, '$.desempenho.{categoria}')
        FROM desempenho
        WHERE id = ?
        """, (1,))
        resultado = cursor.fetchone()

        if resultado and resultado[0]:
            # Converter o array JSON para uma lista Python
            array_atual = json.loads(resultado[0])
        else:
            array_atual = []

        # Adicionar o novo dado ao array
        array_atual.append(novo_dado)

        # Atualizar o JSON no banco com o array modificado
        cursor.execute(f"""
        UPDATE desempenho
        SET historico_json = json_set(
            historico_json,
            '$.desempenho.{categoria}',
            ?
        )
        WHERE id = ?
        """, (json.dumps(array_atual), 1))
        
        # Confirmar a atualização
        conexao.commit()

# formato de arquivo json:
def formato_salvar(resultado, ranting, serie='', tempo=''):
	# inseri a data automaticamente:
	data = datetime.datetime.now().strftime('%d/%m/%Y')	
	# inserir categoria automaticamente:
	if resultado <= 19 and resultado >= 10:
		categoria = 'ruim'
	elif resultado <= 25 and resultado >= 20:
		categoria = 'bom'
	elif resultado <= 30 and resultado >= 26:
		categoria = 'excelente'
	elif resultado >= 31:
		categoria = 'lendario'	
	# O que sera armazenado:
	dados = {
		        "data": data,
                "resultado": resultado,
                "serie": serie,
                "mais_alto": ranting,
                "tempo_medio": tempo
	}
	# Salva no json:
	adicionar_dado_categoria(categoria, dados)
	print('\033[0;32mConteúdo Salvo.\033[0m')