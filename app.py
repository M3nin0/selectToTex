from selecttotex.totex import Totex

# Criando instância do SelectToTex
tt = Totex()

# Comandos que serão utilizados
commands = ['SELECT * FROM aluno;', 'SELECT * FROM materia;', 'SELECT * FROM matricula;']

# Chama a função para a conversão
tt.to_tex(commands, 'tabelas.txt')
