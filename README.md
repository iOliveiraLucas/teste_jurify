# teste_jurify

<!-- Description -->
Teste proposto pela empresa Jurify a fim de determinar capacidades e senioridade através de raspagem de dados de 250 páginas consecutivas do site https://stackoverflow.com/questions.
Realizei o teste de 3 maneiras diferentes encontrando diferentes obstaculos em cada uma.

No primeiro utilizei a biblioteca BeautifulSoup para criar um arquivo básico que realiza a função desejada apenas executando o mesmo pelo compilador da IDE.

Em sequencia implementei a lógica do primeiro projeto em uma API para que fosse possível obter e utilizar um response Json e implementar possíveis tratativas para validação.

Por fim, buscando uma maior agilidade no processo e utilizando uma tecnologia nova a fim de ampliar meus conhecimentos pessoais, utilizei o framework scrapy para realizar o teste. O mesmo se mostrou bem eficiente, porém o site em questão possui medidas para impedir multiplas requisições simultâneas e o projeto é bloqueado pelo site antes de finalizar o processo, não conseguindo assim coletar de todas as 250 páginas. Pretendo dar sequência e descobrir meios de resolver este obstáculo no futuro.

<!-- Atualização -->
Na primeira entrega o problema de excesso de requisições ultilizando o framework scrapy se manteve e recebi como feedback para correção a ultilização de proxy para contornar o bloqueio temporário.

Já em relação ao BeautifulSoup o mesmo apresentou um problema para reconhecer a resposta verificada que levava a quebra do código, recebi como feedback a sugestão de ultilizar uma forma mais acertiva para a coleta dos dados, que já implementada, se mostrou eficiente e corrigiu os problemas de leitura do programa e um novo problema foi encontrado. 
Para a realização do teste completo foram necessários 3 hora de funcionamento no código. Para esta recebi como feedback a sugestão de utilizar programação assíncrona com o python para aumentar a agilidade do processo, uma vez que o mesmo se mostrou acertivo.

<!-- Run -->
Read_only_bs: Just run to write a file json with response
scrap_bs: API with BeautifulSoup.
stackoverflow: Aplication using scrapy framework to write a file json with response (command: scrapy crawl stackoverflow250 -O teste.json)