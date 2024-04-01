import json
import re
import time

import bs4
import requests


def remove_empty_lines_with_whitespace(text):
    return "\n".join(line for line in text.splitlines() if not re.match(r"^\s*$", line))


def format_content_with_headers(data):
    formatted_data = []
    for item in data:
        item['content'] = remove_empty_lines_with_whitespace(item['content'])
        formatted_content = "\n".join(f"# {line}" for line in item["content"].split("\n"))
        formatted_item = {"name": item["name"], "url": item['url'], "title": item["title"],
                          "content": formatted_content}
        formatted_data.append(formatted_item)
    return formatted_data


def get_single_problem(parsed_html: bs4.BeautifulSoup):
    """
    Get the problem from the html with paresed by bs4
    """
    question = {
        'name': parsed_html.find('meta', {'property': 'og:url'}).get('content').split('/')[-2].replace('-', '_'),
        'url': parsed_html.find('meta', {'property': 'og:url'}).get('content'),
        'title': parsed_html.find('title').text,
        'content': parsed_html.find('meta', {'name': 'description'}).get('content')
    }
    return question


def get_problems_from_leetcode(url: str, rg: list) -> list:
    """
    :param url: 
    :param count: limit get 
    :return: 
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'Cookie': 'Cookie: csrftoken=BTODZnyGkjKzEzg5ErFD7NuEFE2Z4J37rBSIEnIMGRFsFWenRk5uNeYwbr0g9gVk; Hm_lvt_f0faad39bcf8471e3ab3ef70125152c3=1711948610; gr_user_id=46545e3d-23f9-4abd-9add-c8a3f9c4af30; _gid=GA1.2.927931147.1711948612; _bl_uid=CClh0u8egO8iUXhhOoXFhdyagCva; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiLz91dG1fc291cmNlPUxDVVMmdXRtX21lZGl1bT1pcF9yZWRpcmVjdCZ1dG1fY2FtcGFpZ249dHJhbnNmZXIyY2hpbmEiLCJfYXV0aF91c2VyX2lkIjoiNzEzMDM2OCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjNkYmVhMmU5YjY0NmQ0MWQ4ZDE4MjVkNGVjZGExYTNkYzE0NDFmZDQ4Y2U2Zjc2Njk1ODMwZjc5ZTVjMzhiMiIsImlkIjo3MTMwMzY4LCJlbWFpbCI6IiIsInVzZXJuYW1lIjoic3RvaWMtaGVybWFubmhvYSIsInVzZXJfc2x1ZyI6InN0b2ljLWhlcm1hbm5ob2EiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jbi9hbGl5dW4tbGMtdXBsb2FkL3VzZXJzL3N0b2ljLWhlcm1hbm5ob2EvYXZhdGFyXzE3MTE5NDUxNDgucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE3MTE5NDk0NTYuNjE1NTU1MywiZXhwaXJlZF90aW1lXyI6MTcxNDUwMzYwMCwidmVyc2lvbl9rZXlfIjowfQ.T-XDNnZEZWg2VHmU8amGkH_8t3bQ75HJsslou2M40jI; a2873925c34ecbd2_gr_last_sent_cs1=stoic-hermannhoa; tfstk=fCXBr0xbYaBZBKOKggENcxTssGp7uww4R0tRmgHE2ppLVY_VD98Urkf6PNTgx9zHLYC5mgYpUpWUF_T9pQfeze8WFgbbbry43MjHEdU4u-rGPWXHnbHpe4-tB33IbR483MjnXd8KFOeqNWXbtYTRyBptWH8tw3QJ2CE623uKwvQRXE1_HkkKAiUsLvDuPH7yno15ZOtB6SSpW8S1BH1HlMBIeYE9ABTAvFa4WpXWNwOCQJgDA1IfoH_unvvpNsjyVwwIpd5V-sdcszGXksSDpnS3dA9Av1WWbTrrNeINCGBB1mk2U9sOLhb7h2YFwiX5Mar-GUjNGQC262szUx8fqHcSfIDWfEr_fbcoOYfc8hYSyZdpjhm4flGqZBKMfEr_fbck9hxi0lZsgbf..; a2873925c34ecbd2_gr_session_id=48b05374-3bcb-4e94-8921-4e5a4122a017; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=48b05374-3bcb-4e94-8921-4e5a4122a017; a2873925c34ecbd2_gr_session_id_sent_vst=48b05374-3bcb-4e94-8921-4e5a4122a017; Hm_lpvt_f0faad39bcf8471e3ab3ef70125152c3=1711978316; _ga=GA1.1.960707821.1711948612; a2873925c34ecbd2_gr_cs1=stoic-hermannhoa; _ga_PDVPZYN3CW=GS1.1.1711977586.2.1.1711978488.58.0.0'
    }
    env = url.split('/')[-1]
    html = requests.request(method='get', url=url, headers=headers)
    # with open('tools/test_for_using.html', 'w') as f:
    #     f.write(html.text)
    parsed_html = bs4.BeautifulSoup(html.text, 'html.parser')
    parsed_html.find('script', id='__NEXT_DATA__')
    json_data = parsed_html.find('script', id='__NEXT_DATA__').text
    json_data = json.loads(json_data)
    questions = (json_data['props']['pageProps']['dehydratedState']
    ['queries'][0]['state']['data']['studyPlanV2Detail']['planSubGroups']
    [0]['questions'])
    qs, c = [], 0
    for index in range(rg[0], len(questions)):
        u = questions[index]['titleSlug']
        url = f'https://leetcode.cn/problems/{u}/?envType=study-plan-v2&envId={env}'
        parsed_html = bs4.BeautifulSoup(requests.request('get', url).text, 'html.parser')
        qs.append(get_single_problem(parsed_html))
        c += 1
        if c >= rg[1]:
            break
    qs = format_content_with_headers(qs)
    return qs


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} milliseconds to execute.")
        return result

    return wrapper
