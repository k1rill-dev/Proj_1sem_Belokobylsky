import re
from pprint import pprint

with open('9_File_judical.txt', 'r', encoding='utf-8') as file:
    data = file.read()

data = data.split('''window.Ya.adfoxCode.create({
        ownerId: 317061,
        containerId: 'adfox_16073307352856796',
        params: {
            pp: 'g',
            ps: 'dzwe',
            p2: 'harn'
        }
    });''')


# resolution = re.findall('Решение № [0-9-/ ~М;()]*', data)

# resolution = [re.findall('Решение № [0-9-/ ~М;()]*', i) for i in data]

# pprint((resolution))

# date = re.findall('[0-9]+[0-9] [а-я]* [0-9]+[0-9]+[0-9]+[0-9]', data)
# num = re.findall(
#     "(?:﻿№[\s\S][0-9-/ ]*)|(?:﻿[дД]ело № (?<!\S)[0-9]*\s.[0-9/]*)|(?:﻿[дД]ело № [0-9]+[а-я -/~]+[0-9/-]*)|(?:﻿[дД]ело №[УИД()A-Z0-9- ]*)|(?:﻿№[\s\S][0-9]*[\s\S][0-9()]*[\s\S].[\s\S][0-9/ ]*)|(?:﻿[дД]ело[\s\S]№[\s\S][0-9]*[\s\S][0-9()]*[\s\S].[\s\S][0-9/ ]*)",
#     data)

# num = [i.strip().replace('\ufeff', '') for i in num]
#
# s = [i for i in data.split('\n')]

# city = [re.findall('г\.[\s\S][А-Яа-я]*', _) for _ in s]

# pprint(city)

# pprint(len(num))