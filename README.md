DocMyCodeGPT - Gerador de Documentação Técnica em PDF
======================================================

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-CC0-blue)
![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-green)


Descrição
---------
O DocMyCodeGPT é uma ferramenta open-source que utiliza a __Inteligência Artificial__ da OpenAi para gerar documentação técnica em PDF a partir de arquivos de código fonte de inúmeras linguagens de programação. Ideal para um primeiro contato com o código, compreensão e organização de ideias, uma vez que o relatório além de explicar um pouco do código, avalia pontos fortes e possíveis vulnerabilidades, além de sugerir correções e melhorias. Utilizando a API do OpenAI, o script analisa seu código e produz um relatório técnico detalhado em Markdown – que é, em seguida, convertido em um PDF profissional com formatação personalizada.

Funcionalidades
----------------
- Análise Técnica Automatizada: Gera um relatório técnico abrangente com:
  - Visão geral do projeto
  - Funcionamento técnico
  - Ambiente e dependências
  - Análise crítica e recomendações
  - Conclusão

- Geração de PDF Profissional: Cria um documento PDF estilizado com cabeçalho, seções e listas customizadas utilizando a biblioteca ReportLab.

- Integração com OpenAI: Realiza a análise do código por meio de um modelo avançado da OpenAI, garantindo uma avaliação precisa e detalhada.

- Feedback Visual: Exibe status e progresso durante a análise e geração do PDF com a biblioteca Rich.

Pré-requisitos
--------------
- Python 3.6+ (recomendado Python 3.8 ou superior)
- Chave de API do OpenAI: Necessária para acesso à API. Saiba como obter uma chave em https://beta.openai.com/.
- Bibliotecas Python:
  - openai
  - python-dotenv
  - rich
  - reportlab

Instalação
----------
1. Clone o repositório:
   git clone https://github.com/seu_usuario/DocMyCodeGPT.git
   cd DocMyCodeGPT

2. Crie um ambiente virtual (opcional, mas recomendado):
   python -m venv venv
   source venv/bin/activate  (No Windows use: venv\Scripts\activate)

3. Instale as dependências:
   Se houver um arquivo requirements.txt:
      pip install -r requirements.txt
   Caso contrário, instale manualmente:
      pip install openai python-dotenv rich reportlab

Configuração
------------
Crie um arquivo .env na raiz do projeto e adicione sua chave de API do OpenAI:
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Certifique-se de que a chave esteja correta e comece com "sk-".

Uma excelente alternativa é criar uma variável de ambiente OPENAI_API_KEY e informar sua chave de API.

**Uso Direto via Curl:**

Instale todas as dependências e rode direto via linha de comando (CMD):

```
curl -s https://raw.githubusercontent.com/tsachetto/CodeDocGPT/refs/heads/main/src/docmycodegpt.py | python - script.py
```

Essa é uma maneira bem mais simplificada e prática!

Uso
---
Para gerar a documentação técnica de um arquivo de código, execute o comando:
   python docmycodegpt.py caminho/para/seu_codigo.py -o caminho/para/diretorio_saida

- Parâmetro obrigatório: caminho/para/seu_codigo.py – O arquivo de código que será analisado.
- Parâmetro opcional: -o ou --output – Diretório onde o PDF gerado será salvo. Se não especificado, o PDF será salvo no mesmo diretório do arquivo analisado.

Exemplo:
   python docmycodegpt.py exemplo.py -o ./documentacao

Estrutura do Relatório Técnico
------------------------------
1. Visão Geral
   - Objetivo principal
   - Contexto de uso
   - Arquitetura geral

2. Funcionamento Técnico
   - Fluxo de execução (resumido em até 250 palavras)
   - Componentes principais
   - Estruturas de dados

3. Ambiente e Dependências
   - Linguagem e versão
   - Bibliotecas essenciais
   - Requisitos do sistema

4. Análise Crítica
   - Pontos Fortes: Aspectos positivos do código
   - Vulnerabilidades: Possíveis riscos e pontos de melhoria
   - Recomendações: Sugestões para aprimoramento

5. Conclusão
   - Avaliação geral
   - Considerações finais

Contribuições
--------------
Contribuições são muito bem-vindas! Para contribuir com melhorias, correções ou novas funcionalidades:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção:
      git checkout -b minha-nova-feature
3. Faça suas alterações e commit:
      git commit -am 'Adiciona nova feature'
4. Envie para sua branch:
      git push origin minha-nova-feature
5. Abra um Pull Request.

Licença
-------
Este projeto está licenciado sob a Creative Commons Zero (CC0).

Isso significa que você pode usar, modificar e distribuir o código sem restrições. Para mais detalhes, veja o arquivo LICENSE.


## 👏 Créditos

Desenvolvido por Thomaz Sachetto Silva.

Powered by OpenAI 🧠.

## 📬 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

**Email:** thomazsachetto@gmail.com

**GitHub:** @tsachetto

Feito com muito ☕ e um pouco de magia da IA! ✨

![BR](https://img.shields.io/badge/contribua%20você%20também!-8A2BE2)
