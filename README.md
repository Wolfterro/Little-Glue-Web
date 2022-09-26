# Little Glue Web
Aquele programinha maroto pra fazer aquela colinha marota pras eleições! Versão Web!

**Este programa é uma versão Web do [Little Glue](https://www.github.com/Wolfterro/Little-Glue) criado por mim.**

## Descrição
Bom, devido as últimas decisões do Tribunal Superior Eleitoral (TSE) que desfavorecem o uso de celulares nas seções de votação, decidi criar este programa para as pessoas que possuem dificuldades de memorizar os vários números de diversos candidatos nas eleições presidenciais e municipais que ocorrerem.

É bem provável também que muita gente já tenha recebido o famoso "santinho" de seus candidatos ou já tenha preenchido os números com a famosa dupla Papel e Caneta, mas pensando em utilizar a mais alta tecnologia de ponta do Terminal do GNU/Linux aliado a linguagem Python de programação, decidi criar este pequeno programinha para gerar as famosas "colinhas" que podem ser usadas como guia na hora da votação. Você pode criar colinhas para você, seus amigos, parentes, ou qualquer outra pessoa que tenha interesse em ter uma colinha impressa com os candidatos que a pessoa quiser.

**Este programa consegue preencher, salvar e gerar uma colinha em formato HTML, PDF ou imagem JPG para que você possa imprimir e levar no dia da votação.**


## Instalação
É bem simples instalar esse programa, porém ele foi desenvolvido pensando na plataforma GNU/Linux e requer algumas dependências que, talvez, possam estar apenas disponível pra ela. Portanto, o tutorial abaixo seguirá presumindo que você esteja utilizando alguma distribuição baseada no Debian (como o Ubuntu ou Linux Mint, por exemplo).

- **Passo Um:** Baixe o programa clonando o projeto em sua máquina
```shell
git clone https://github.com/Wolfterro/Little-Glue-Web.git
cd Little-Glue-Web
```

- **Passo Dois:** Execute o comando abaixo
```shell
make install
```

- **Passo Trẽs:** Siga as instruções que aparecem no terminal
```shell
================================================================================
===!!! Você vai precisar criar agora uma virtualenv para rodar o projeto! !!!===
================================================================================
===!!! Para isso, execute: mkvirtualenv little-glue --python=python3 && workon little-glue

===!!! OU !!!===

===!!! Execute este: virtualenv little-glue --python=python3 && source little-glue/bin/activate
===!!! Após esse processo, execute o comando: pip install -r requirements.txt
===!!! E pronto, basta rodar o projeto usando o comando: make run
```

E pronto! Você poderá rodar o projeto rodando apenas o último comando do passo três!
```shell
make run
```
