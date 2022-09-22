# teste_jurify

<!-- Description -->
Teste proposto pela empresa Jurify a fim de determinar capacidades e senioridade através de raspagem de dados de 250 páginas consecutivas do site https://stackoverflow.com/questions.
Realizei o teste de 3 maneiras diferentes encontrando diferentes obstaculos em cada um.

No primeiro utilizei a biblioteca BeautifulSoup para criar um arquivo básico que executava a função desejada apesar executando o mesmo pelo compilador da IDE.

Em sequencia implementei a lógica do primeiro projeto em uma API para que fosse possível obter e utilizar um response Json e implementar possíveis tratativas.

Por fim, buscando uma maior agilidade no processo e utilizando uma tecnologia nova a fim de ampliar meus conhecimento pessoais, utilizei o framework scrapy para realizar o teste. O mesmo se mostrou bem eficiente, porém o site em questão possui medidas para impedir multiplas requisições simultâneas e o mesmo é bloqueado pelo site antes de finalizar o processo. Pretendo dar sequência e descobrir meios de resolver este obstáculo no futuro.

<!-- Run -->
Read_only_bs: Just run to write a file json with response
scrap_bs: API with BeautifulSoup.
stackoverflow: Aplication using scrapy framework to write a file json with response