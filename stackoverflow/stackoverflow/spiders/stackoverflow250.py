import scrapy

class Stackoverflow250Spider(scrapy.Spider):
    name = 'stackoverflow250'
    start_urls = ['https://stackoverflow.com/questions?tab=active&pagesize=15']
    
    def parse_answers(self, response, url, tags, votes, views, verify_answer, answers):
        list_answers = []
        for answer in response.css('div.answer.js-answer'):
            list_answers.append(answer.attrib['id'])
        
        temp_dict = {
            'url': url,
            'tags': tags,
            'verify_answer': "",
            'answers': [],
            'votes': votes,
            'views': views
        }
        temp_dict['answers'] = list_answers
        if verify_answer:
            temp_dict['verify_answer'] = temp_dict['answers'][0]
        
        yield temp_dict
    
    def parse(self, response):
        for quote in response.css('div.s-post-summary.js-post-summary'):
            try:
                verify_answer = quote.xpath('div/div/svg').attrib['aria-hidden']
            except:
                verify_answer = None
            
            temp_dict = {
                'url': 'https://stackoverflow.com/'+quote.xpath('div/h3/a').attrib['href'],
                'tags': quote.xpath('div/div/div/ul/li/a/text()').getall(),
                'verify_answer': "",
                'answers': [],
                'votes': quote.xpath('div/div/span/text()').get(),
                'views': quote.xpath('div/div/span/text()').getall()[-2]
            }

            count_answers = int(quote.xpath('div/div/span/text()').getall()[2])
            if count_answers >0:
                request = scrapy.Request(temp_dict['url'], callback=self.parse_answers, cb_kwargs= temp_dict)
                request.cb_kwargs['verify_answer'] = verify_answer
                yield request
            else:
                yield temp_dict

        temp_page = response.xpath('//*[@id="mainbar"]/div[5]/div[1]/text()').get()
        current_page = int(temp_page) if temp_page.isnumeric() else int(response.xpath('//*[@id="mainbar"]/div[5]/div[2]/text()').get())

        print ("+"*20, current_page)
        if current_page < 2:
            yield response.follow(f'https://stackoverflow.com/questions?tab=active&pagesize=15&page={current_page+1}', callback=self.parse)