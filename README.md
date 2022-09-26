# Little Glue Web
Aquele programinha maroto pra fazer aquela colinha marota pras eleições! Versão Web!

**Este programa é uma versão Web do [Little Glue](https://www.github.com/Wolfterro/Little-Glue) criado por mim.**

## Descrição
Bom, devido as últimas decisões do Tribunal Superior Eleitoral (TSE) que desfavorecem o uso de celulares nas seções de votação, decidi criar este programa para as pessoas que possuem dificuldades de memorizar os vários números de diversos candidatos nas eleições presidenciais e municipais que ocorrerem.

É bem provável também que muita gente já tenha recebido o famoso "santinho" de seus candidatos ou já tenha preenchido os números com a famosa dupla Papel e Caneta, mas pensando em utilizar a mais alta tecnologia de ponta dos frameworks Web aliado a linguagem Python de programação, decidi criar este pequeno programinha para gerar as famosas "colinhas" que podem ser usadas como guia na hora da votação. Você pode criar colinhas para você, seus amigos, parentes, ou qualquer outra pessoa que tenha interesse em ter uma colinha impressa com os candidatos que a pessoa quiser.

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

## Exemplos de Uso
Diferente da outra versão, que utiliza o Terminal do GNU/Linux, esta versão utiliza a framework web FastAPI, que similar ao Flask e ao Django, fornece endpoints em API Rest. Portanto há apenas uma forma de utilização que é fazendo uma requisição POST para o endpoint de geração de colinhas.

No exemplo abaixo, utilizamos o comando cURL para enviar uma requisição de geração de uma colinha para eleições presidenciais. O link que será gerado irá apontar para o arquivo PDF com a nossa colinha.

```shell
curl --location --request POST 'http://localhost:8000/generate/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "candidates_data": {
    "federal_deputy": [
      {
        "number": "9999",
        "name": "João da Feira"
      }
    ],
    "state_deputy": [
      {
        "number": "99999",
        "name": "Marcos do Gás"
      }
    ],
    "senator": [
      {
        "number": "999",
        "name": "Toninho da Padaria"
      }
    ],
    "governor": {
      "number": "99",
      "name": "Delegado José"
    },
    "president": {
      "number": "99",
      "name": "Professor Pereira"
    }
  },
  "color_scheme": ["#ffffff", "#000000"],
  "export_format": "pdf",
  "font_configs": [12, 32, 15, "bold"],
  "election_type": "presidential"
}'
```

Repare que o JSON enviado **é o mesmo utilizado pelo programa em sua versão de terminal**, com os mesmos campos e os mesmos valores utilizados no exemplo do outro repositório. Recomendo que dê uma olhada no repositório **[Little Glue](https://www.github.com/Wolfterro/Little-Glue)** caso tenha alguma dúvida em relação ao JSON utilizado.
