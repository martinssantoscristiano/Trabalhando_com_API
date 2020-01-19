import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena a resposta
url='https://api.github.com/search/repositories?q=language:node&sort=stars'
r = requests.get(url)
print("status code:",r.status_code)

# Armazena a resposta de API em uma variável
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explora informações sobre os repositórios
#response_dicts = response_dict['items']
#print("Repositories returned:", len(response_dicts))
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))


# Analisa o primeiro repositório
#response_dict = response_dicts[0]
# print("\nKeys:", len(response_dict))
# for key in sorted(response_dict.keys()):
#     print(key)

print("\nSelected information about each repository:")
#names, stars = [], []
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'labe' : repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
 

#for response_dict in response_dicts:
    #names.append(response_dict['name'])
    #stars.append(response_dict['stargazers_count'])
    # print('Name:', response_dict['name'])
    # print("Owner:", response_dict['owner']['login'])
    # print('Stars:', response_dict['stargazers_count'])
    # print('Repository:', response_dict['html_url'])
    # print('Created:', response_dict['created_at'])
    # print('Updated:', response_dict['updated_at'])
    # print('Description:', response_dict['description'])
    
# Cria a visualização
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Nodejs Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
#chart.add('', stars)
chart.render_to_file('nodejs_repos.svg')    