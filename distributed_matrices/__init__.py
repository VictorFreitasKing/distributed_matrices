'''
UFRPE - Universidade Federal Rural de Pernambuco
UAST - Unidade Acadêmicas de Serra Talhada

Alunos: José Victor de Freitas Nunes
        Julio Costa

Bibliotecas utilizadas: numpy - biblioteca usada para trabalhar com arrays de forma  mais eficiente (https://numpy.org/)


-----------------------> OBJETIVO:
-> inicia programa (processo base: process)

-> Ler parâmetros de entrada no Arquivo
------> Parâmetros:
----------->tempo: tempo de execução - inicia em 00:00
----------->cpus -> Necessário para grafico
----------->-------leitura só daqui pra baixo --------------
----------->colunas + ' ' + linhas
----------->matriz

-> Carrega arquivo com a matriz a ser multiplicada
------> Carrega matriz a partir de arquivo

-> Inicia Contagem de TEMPO

-> Chama função de multiplicação (remota e ou local) - Utilizar Pool para dividir  os processos
------> Multiplica  matriz
----------> Pega Linhas
----------> Pega Colunas

-> Termina Multiplicação (retorna todos os resultados)

-> Agrupa os resultados

-> Termina Contagem de TEMPO

-> Escreve arquivo de saída.
'''