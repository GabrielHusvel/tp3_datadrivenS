Scientific Research Assistant - Documentação

Descrição do Problema e da Solução

Problema

A pesquisa científica frequentemente envolve a busca de informações em múltiplas fontes, como artigos acadêmicos, enciclopédias digitais e ferramentas de busca online. Esse processo é manual, demorado e sujeito a falhas humanas, como dificuldades em acessar a fonte correta ou falta de contexto nas respostas.

Solução

O Scientific Research Assistant utiliza inteligência artificial e ferramentas avançadas para automatizar a busca, organização e contextualização de informações científicas. Com suporte a múltiplas fontes, como Arxiv, Wikipedia e DuckDuckGo, e estratégias de raciocínio adaptativas (como "plan_and_solve"), o agente facilita o trabalho dos pesquisadores, economizando tempo e aumentando a precisão das respostas.






Casos de Uso Testados e Resultados Observados


Pergunta: "I want learn about mission Voyager 1.".

Resultado: "Voyager 1 is a NASA space probe launched on September 5, 1977, to study the outer Solar System and beyond. It made flybys of Jupiter, Saturn, and Titan, Saturn's largest moon. On August 25, 2012, it became the first spacecraft to enter interstellar space. Currently, its extended mission is ongoing, with data expected until at least 2025. Significant discoveries include the similarity of magnetic fields on both sides of the heliopause, confirming its crossing into interstellar space, and the distortion of the heliosphere, indicating the obliquity of the local interstellar magnetic field."



Pergunta: "now, i want learn about black holes."

Resultado: "I hope the information provided about black holes was helpful. Do you need more details or have any other questions about black holes or any other topic?"








Instruções para Execução do Código

Pré-requisitos

Python 3.9 ou superior.

Ambiente virtual configurado.

Bibliotecas listadas no requirements.txt.

Passos

Clone o repositório:

git clone https://github.com/seu-usuario/scientific-research-assistant.git
cd scientific-research-assistant

Ative o ambiente virtual e instale as dependências:

python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt

Execute a aplicação:

streamlit run src/app.py

Acesse a aplicação no navegador em http://localhost:8501.







Reflexão:

Com o Agente

O agente automatiza a integração de múltiplas fontes de informação, permitindo que o pesquisador obtenha respostas contextualizadas em segundos. Além disso, a memória de conversação armazena o histórico, proporcionando continuidade no diálogo e evitando repetições.

Sem o Agente

Sem o agente, seria necessário:

Acessar manualmente cada fonte (Arxiv, Wikipedia, motores de busca).

Filtrar e interpretar os resultados.

Consolidar informações de diferentes fontes.

Este processo seria repetitivo, demorado e mais propenso a erros, dificultando a pesquisa científica em cenários com prazos apertados ou alto volume de dados.

