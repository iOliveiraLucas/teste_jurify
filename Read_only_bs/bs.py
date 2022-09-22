from bs4 import BeautifulSoup as bs
import requests
import json

def escrever_json(lista):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(lista, f, indent=4)

def answers(url):
    result = requests.get(url)
    soup = bs(result.content, 'html.parser')
    answers = [answer.attrs['id'] for answer in soup.select(".answer")]
    return {"answers": answers}

def scrap_stackoverflow():
    list_response = []         
    for idx in range(2):
        url = f"https://stackoverflow.com/questions?tab=active&pagesize=15&page={str(idx)}"
        response = requests.get(url)
        soup = bs(response.content, 'html.parser')

        for question in soup.select(".js-post-summary"):
            temp_dict = {}
            temp_dict['url']= f"https://stackoverflow.com{question.select_one('.s-post-summary--content h3 a').attrs['href']}"
            temp_dict['tags']= [i.text for i in question.select('.list-ls-none li a')]
            temp_dict['verify_answer']= ""
            temp_dict['answers']= []
            temp_dict['votes']= question.select_one('div> div> span').text
            temp_dict['views']= question.select_one('div> div:nth-of-type(2)> span').text
            
            count_answers = int(question.select_one('div> div:nth-of-type(1)> span').text)
            if count_answers > 0:
                dict_answers = answers(temp_dict['url'])
                temp_dict['answers']= dict_answers["answers"]
                temp_dict['verify_answer']= dict_answers['answers'][0]
            
            list_response.append(temp_dict)

    return list_response

escrever_json(scrap_stackoverflow())