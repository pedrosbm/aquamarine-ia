# Aquamarine
### By NovaTech Solutions
---
| integrante        | rm     |
| ----------------- | ------ |
| Arthur Koga       | 99503  |
| Gabriel Benjamim  | 552254 |
| Henry Ribeiro     | 550684 |
| Murilo José       | 99538  |
| Pedro Sena Borges | 98021  |
---

### Esse repositório é dedicado ao versionamento do servidor flask da IA da Aquamrine, um modelo de classificação por imagem.

Aquamarine se trata de um aplicativo mobile desenvolvido pela NovaTech Solutions em pról de um mar mais limpo, em parceria a iniciativa oceans 20 do g20. Com o objetivo de fazer detecção de água suja para o sistema de postagens da nossa aplicação, nós desenvolvemos essa ia que é capaz de detectar a presença de resíduos plásticos na água.

[vídeo da nossa IA](https://youtu.be/kvu7dFbNXw0)

Esse projeto de IA foi desenvolvido utilizando um conjunto de imagens de água limpa e água com resíduos plasticos vindo do Kaggle. O dataset utilizado para o treinamento está disponível [aqui](https://www.kaggle.com/datasets/surajit651/souvikdataset).

Para o treinamento da nossa ia, utilizamos um serviço de treinamento de IA chamado [teachable machine](https://teachablemachine.withgoogle.com/), nele somos capazes de fazer modelos classificatórios de forma rápida em alguns cliques.

## Resultados do nosso modelo

Não temos uma métrica exata para avaliar o nosso modelo, mas ao fazer testes com nosso modelo do tensorflow foi possível perceber que: 

- Imagens de água limpa com muitos detalhes, reflexos e objetos podem ser classificadas como água suja por acidente.
- Imagens de água suja que não ilustrem bem o contexto/ falta de detalhes, podem ser classificadas como água limpa por acidente.
- A foto ideal para reconhecimento de água limpa é uma foto sem muitos detalhes.
- A foto ideal para reconhecimento de água suja é uma foto que apresente diversos artigos plásticos, e não apenas um de forma isolada.
- A versão do python recomendada para a criação do ambiente virtual é python 3.9 devido ao suporte do tensorflow para o windows.

## Como fazer requisição http (postman)

Para fazer uma requisição para o nosso modelo, basta executar a api flask e mandar uma requisição `post` para o seguinte endpoint:

```
http://127.0.0.1:5000/predict
```

O corpo da requisição deve ser um formulário com o campo `image` contendo o arquivo de imagem que você desejar.

Resposta:

``` js
{
    prediction: String
}
```
