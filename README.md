# Processo Seletivo Elixir - Stone
Candidato: Igor Rosa

A linguagem utilizada para a realização deste desafio foi python e o arquivo foi nomeado como elixir.py.

O programa foi desenvolvido de maneira que para a inicialização são necessários mais 2 command line arguments, ambos arquivos '.csv'. O primeiro é o dicionário correspondente à lista de compras a ser dividida e o segundo corresponde às pessoas que irão dividir a conta.

Caso os command line arguments não sejam devidamente fornecidos, o programa informará a forma correta de inicialização e fechará.

É importante ressaltar que os valores utilizados neste desafio são todos inteiro ou strings, ou seja, é importante que os valores utilizados na lista de compras sejam considerados em centavos ao invés de reais (ex.: item: banana, price: 999 = R$9,99). Portanto, o dicionário resultado da divisão também fornecerá o valor em centavos, o que pode ser facilmente alterado, porém não sei se é algo desejável para o desafio.

Testes:
Para a realização de testes criei alguns arquivos '.csv' e executei o programa utilizando estes como command line arguments, estes arquivos estão nas pastas databases (listas de compras) e people (listas de pessoas). Disponibilizei abaixo alguns exemplos para a execução e realização de alguns testes:

python elixir.py databases/test1.csv people/1.csv
python elixir.py databases/test1.csv people/2.csv
python elixir.py databases/test1.csv people/3.csv
python elixir.py databases/test1.csv people/4.csv
python elixir.py databases/test1.csv people/5.csv
python elixir.py databases/test2.csv people/1.csv
python elixir.py databases/test2.csv people/2.csv
python elixir.py databases/test2.csv people/3.csv
python elixir.py databases/test2.csv people/4.csv
python elixir.py databases/test2.csv people/5.csv
python elixir.py databases/test3.csv people/1.csv
python elixir.py databases/test3.csv people/2.csv
python elixir.py databases/test3.csv people/3.csv
python elixir.py databases/test3.csv people/4.csv
python elixir.py databases/test3.csv people/5.csv
python elixir.py databases/test4.csv people/1.csv
python elixir.py databases/test4.csv people/2.csv
python elixir.py databases/test4.csv people/3.csv
python elixir.py databases/test4.csv people/4.csv
python elixir.py databases/test4.csv people/5.csv
python elixir.py databases/test5.csv people/1.csv
python elixir.py databases/test5.csv people/2.csv
python elixir.py databases/test5.csv people/3.csv
python elixir.py databases/test5.csv people/4.csv
python elixir.py databases/test5.csv people/5.csv
[...]

