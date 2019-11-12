import requests
import json
import counter

additional_users = [{'name': 'ibmcorp'},
                    {'name': 'oracle'},
                    {'name': 'elastic'}]


def get_list_of_users():
    list_of_users = {}
    page_number = 1
    total_num = 0
    list_of_users['library'] = []
    link = 'https://hub.docker.com/v2/repositories/library/?page_size=10&page='

    def get_info_from_user(possible_user):
        number = 0
        possible_page_number = 1
        possible_link = 'https://hub.docker.com/v2/repositories/' + possible_user['name'] + '/?page_size=10&page='
        while True:
            if '.' not in possible_user['name']:
                if not possible_user['name'] == 'sl':
                    possible_response = json.loads(requests.get(possible_link + str(possible_page_number)).text)
                    if 'results' in possible_response:
                        for repo in possible_response['results']:
                            if possible_user['name'] not in list_of_users:
                                list_of_users[possible_user['name']] = []
                            list_of_users[possible_user['name']].append(repo['name'])
                            number += 1
                        if possible_response['next'] is None:
                            break
                        possible_page_number += 1
                else:
                    break
            else:
                break
        return number

    for possible_user in additional_users:
        total_num += get_info_from_user(possible_user)

    while True:
        response = json.loads(requests.get(link + str(page_number)).text)
        for possible_user in response['results']:
            total_num += get_info_from_user(possible_user)
            total_num += 1
            list_of_users['library'].append(possible_user['name'])
        if response['next'] is None:
            break
        page_number += 1
    print(total_num)
    print(list_of_users)
    return list_of_users


def get_json(dict_of_users):
    end_dict = {}
    for user in dict_of_users:
        for repo in dict_of_users[user]:
            link = 'https://hub.docker.com/v2/repositories/%s/%s/'
            latest_response = json.loads(requests.get(link % (user, repo) + 'tags').text)
            print(latest_response)
            end_dict['{}/{}'.format(user, repo)] = latest_response
    return end_dict


#print(get_json(get_list_of_users()))
sample = get_list_of_users()
with open('result.json', 'w') as fp:
    json.dump(sample, fp)
with open('result.json') as input:
    data = json.load(input)
with open('final.json', 'w') as output:
    end = get_json(data)
    json.dump(end, output)

counter.count('final.json')
