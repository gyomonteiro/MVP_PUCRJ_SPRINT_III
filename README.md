# AI Sleep Health Prediction
Neste projeto, foi desenvolvida uma aplicação para análise de variáveis relacionadas ao sono e aos hábitos diários dos usuários, com o objetivo de prever a ocorrência de distúrbios do sono. A aplicação utiliza técnicas de machine learning para identificar padrões nos dados e fornecer insights sobre possíveis problemas relacionados ao sono, permitindo um acompanhamento mais eficaz da saúde do usuário.

Desenvolvido como parte do MVP para o módulo "Qualidade de Software, Segurança e Sistemas Inteligentes" na pós-graduação em Engenharia de Software da PUC-Rio.

## Como executar local

1. Clone este repositório para sua máquina, se ainda não o fez:
```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Atualizar todas as libs python listadas conforme o arquivo `requirements.txt`. Ou seja, execute, no ambiente escolhido, a instalação através do comando: 
```
pip install -r requirements.txt
```
3. Para executar a API: 
```
flask run --host 0.0.0.0 --port 5000
```

Recomendá-se utilizar o comando abaixo, quando em modo de desenvolvimento:
```
flask run --host 0.0.0.0 --port 5000 --reload
```
Desta forma o servidor é reinicia automaticamente após mudanças no código fonte.


4. Acesse o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador de preferência para verificar a API em execução.

Posteriormente, basta testar quaisquer rotas da API que desejar para testar o sistema. Cada rota tem sua devida descrição na documentação acessada.
