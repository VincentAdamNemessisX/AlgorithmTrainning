import datetime

from tools.tool import get_problems_from_leetcode


def generate_files_with_problems(qs: list[dict]):
    now_time = datetime.datetime.now()
    url = f'{now_time.year}-{now_time.month}-{now_time.day}/'
    for question in qs:
        with open(url + f'{question["name"]}.py', 'w') as f:
            f.write(f'# {question["url"]}\n')
            f.write(f'{question["content"]}\n')


if __name__ == '__main__':
    questions = get_problems_from_leetcode(
        'https://leetcode.cn/studyplan/top-interview-150/', [0, 151])
    generate_files_with_problems(questions[95:100]) # next [101:106]
    # print(len(questions))
