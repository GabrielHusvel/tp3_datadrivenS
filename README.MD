Scientific Research Assistant - Documentação

Descrição do Problema e da Solução

Problema

A pesquisa científica frequentemente envolve a busca de informações em múltiplas fontes, como artigos acadêmicos, enciclopédias digitais e ferramentas de busca online. Esse processo é manual, demorado e sujeito a falhas humanas, como dificuldades em acessar a fonte correta ou falta de contexto nas respostas.

Solução

O Scientific Research Assistant utiliza inteligência artificial e ferramentas avançadas para automatizar a busca, organização e contextualização de informações científicas. Com suporte a múltiplas fontes, como Arxiv, Wikipedia e DuckDuckGo, e estratégias de raciocínio adaptativas (como "plan_and_solve"), o agente facilita o trabalho dos pesquisadores, economizando tempo e aumentando a precisão das respostas.



Casos de Uso Testados e Resultados Observados


Pergunta: "I want learn about mission Voyager 1.". 

Resultado: "Voyager 1 is a NASA space probe launched on September 5, 1977, to study the outer Solar System and beyond. It made flybys of Jupiter, Saturn, and Titan, Saturn's largest moon. On August 25, 2012, it became the first spacecraft to enter interstellar space. Currently, its extended mission is ongoing, with data expected until at least 2025. Significant discoveries include the similarity of magnetic fields on both sides of the heliopause, confirming its crossing into interstellar space, and the distortion of the heliosphere, indicating the obliquity of the local interstellar magnetic field." 

Precisão:  

A resposta é clara e acessível, com explicações concisas e está correta, com detalhes importantes sobre a missão Voyager 1, incluindo sua data de lançamento, marcos, descobertas relevantes e a situação atual da missão. 

 

Pergunta: "now, i want learn about black holes." 

Resultado: " Black holes are regions in space where gravity is so strong that nothing, not even light, can escape. They are formed when massive stars collapse at the end of their life cycle. Black holes can grow by absorbing mass from their surroundings. Supermassive black holes, millions of times the mass of the sun, exist in the centers of most galaxies. The presence of a black hole can be inferred through its interaction with other matter and with electromagnetic radiation such as visible light. Matter falling toward a black hole can form an accretion disk heated by friction, forming some of the brightest objects in the universe. Stars passing too close to a supermassive black hole can be shredded into streamers that shine very brightly before being 'swallowed.' " 

Precisão:  

A resposta explica corretamente buracos negros, sua formação, crescimento, características, a relação com a matéria circundante e os fenômenos associados, como o disco de acreção, a interação com estrelas próximas e até o supermassive black holes no centro das galáxias. 

 

Pergunta: "i want learn about fermions and bosons" 

Resultado: "Fermions and bosons are fundamental particles in quantum mechanics with distinct properties. Fermions have half-odd-integer spin and follow Fermi–Dirac statistics, obeying the Pauli exclusion principle which means only one fermion can occupy a particular quantum state at a time. Examples of fermions include all quarks and leptons, as well as composite particles made of an odd number of these, such as all baryons and many atoms and nuclei. On the other hand, bosons have integer spin and follow Bose–Einstein statistics, allowing multiple bosons to occupy the same quantum state. Examples of bosons include elementary particles such as photons, gluons, and the Higgs boson, which are force carriers in the Standard Model of particle physics. Additionally, composite particles like mesons, made up of an even number of fermion particles, are also classified as bosons. In summary, the key difference between fermions and bosons lies in their spin and the statistical behavior that results from this difference." 

Precisão:  

A resposta é correta e explica bem as diferenças entre férmions e bósons, a explicação é informativa. 



Instruções para Execução do Código

Python 3.9 ou superior.

Ambiente virtual.

Bibliotecas do requirements.txt.

Execute a aplicação:

streamlit run src/app.py

Acesse a aplicação no navegador em http://localhost:8501.



Reflexão:


O agente automatiza a integração de fontes de informação, permitindo que o pesquisador obtenha respostas contextualizadas em segundos. Além disso, a memória de conversação armazena o histórico, proporcionando continuidade no diálogo e evitando repetições.


Sem o agente, seria necessário:

Acessar manualmente cada fonte (Arxiv, Wikipedia, DuckDuckGo).

Filtrar e interpretar os resultados.

Consolidar informações de diferentes fontes.

Este processo seria repetitivo, demorado e mais propenso a erros, dificultando a pesquisa científica em cenários com prazos apertados ou alto volume de dados.

