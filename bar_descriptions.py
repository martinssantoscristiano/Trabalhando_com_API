import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart._title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'lable': 'Description of django.'},
    {'value': 14798, 'lable': 'Description of flask.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')