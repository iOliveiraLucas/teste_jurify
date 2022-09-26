from bs4 import BeautifulSoup as bs
import requests
import json
from datetime import datetime as dt

def escrever_json(lista):
    with open('teste.json', 'w') as f:
        json.dump(lista, f, indent=4)

def answers(url):
    result = requests.get(url)
    soup = bs(result.content, 'html.parser')
    list_answers = [answer.attrs['id'] for answer in soup.select(".answer")]
    
    verify_answer = soup.find(class_="js-accepted-answer") or ""
    if verify_answer != "":
        verify_answer = verify_answer.get("id")
    
    return {"answers": list_answers, "verify_answer": verify_answer}

def scrap_stackoverflow():
    start = dt.now()
    list_response = []         
    for idx in range(1,250):
        url = f"https://stackoverflow.com/questions?tab=active&pagesize=15&page={str(idx)}"
        response = requests.get(url)
        soup = bs(response.content, 'html.parser')

        for question in soup.select(".js-post-summary"):
            question_stats = question.find_all(class_="s-post-summary--stats-item-number")
            question_url = question.find(class_="s-post-summary--content-title").a.get("href")

            temp_dict = {}
            temp_dict['url']= f"https://stackoverflow.com{question_url}"
            temp_dict['tags']= [i.text for i in question.select('.js-post-tag-list-wrapper li a')]
            temp_dict['verify_answer']= ""
            temp_dict['answers']= []
            temp_dict['votes']= question_stats[0].text
            temp_dict['views']= question_stats[2].text
            
            count_answers = int(question_stats[1].text)
            if count_answers > 0:
                dict_answers = answers(temp_dict['url'])
                temp_dict['answers']= dict_answers["answers"]
                temp_dict['verify_answer']= dict_answers['verify_answer']
            
            list_response.append(temp_dict)

    finished = dt.now()
    time = finished - start
    print ("current time: ",time)
    return list_response

escrever_json(scrap_stackoverflow())