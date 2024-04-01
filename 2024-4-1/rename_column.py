# 2885. 重命名列
# DataFrame students
# +-------------+--------+
# | Column Name | Type |
# +-------------+--------+
# | id | int |
# | first | object |
# | last | object |
# | age | int |
# +-------------+--------+
# 编写一个解决方案，按以下方式重命名列：
# id重命名为student_id
# first重命名为first_name
# last重命名为last_name
# age重命名为age_in_years
# 返回结果格式如下示例所示。
# 示例1:
# 输入：
# +----+---------+----------+-----+
# | id | first | last | age |
# +----+---------+----------+-----+
# | 1 | Mason | King | 6 |
# | 2 | Ava | Wright | 7 |
# | 3 | Taylor | Hall | 16 |
# | 4 | Georgia | Thompson | 18 |
# | 5 | Thomas | Moore | 10 |
# +----+---------+----------+-----+
# 输出：
# +------------+------------+-----------+--------------+
# | student_id | first_name | last_name | age_in_years |
# +------------+------------+-----------+--------------+
# | 1 | Mason | King | 6 |
# | 2 | Ava | Wright | 7 |
# | 3 | Taylor | Hall | 16 |
# | 4 | Georgia | Thompson | 18 |
# | 5 | Thomas | Moore | 10 |
# +------------+------------+-----------+--------------+

import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(
        columns={"id": "student_id",
                 "first": "first_name",
                 "last": "last_name",
                 "age": "age_in_years"}, inplace=True)
    return students


if __name__ == "__main__":
    students = pd.DataFrame(
        [
            [1, "Mason", "King", 6],
            [2, "Ava", "Wright", 7],
            [3, "Taylor", "Hall", 16]
        ])
    students.columns = ["id", "first", "last", "age"]
    students = renameColumns(students)
    print(students)
