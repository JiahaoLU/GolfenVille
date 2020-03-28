# encoding: utf-8
"""
@author: Jiahao LU
@contact: lujiahao8146@gmail.com
@file: GolfDistributionMap.py
@time: 2020/3/28
@desc:
"""
import pygal
from pygal.style import LightColorizedStyle
import pygal_maps_fr.maps
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# Selon les données sur:
    # 1. https://www.touslesgolfs.com/
    # 2. Federation francaise de golf
def draw_distribution_map():
    filename='./plottings/dmap'

    fr_chart = pygal_maps_fr.maps.Departments(human_readable=True, legend_at_bottom=True)
    fr_chart.title = 'Nombre de golfs par département'
    fr_chart.add('Départements avec plus de 20 golfs en 2019',
                 {'06': 21, '13': 20, '33': 20, '78': 30, '83': 21})
    fr_chart.add('Métropole/DOM/COM en 2019', {
        '01': 16, '02': 6, '03': 6, '04': 4, '05': 2, '07': 2, '08': 3, '09': 3, '10': 3, '11': 3, '12': 3,
        '14': 14, '15': 5, '16': 5, '17': 11, '18': 5, '19': 5, '21': 8, '22': 11,
        '23': 2, '24': 10, '25': 4, '26': 8, '27': 8, '28': 8, '29': 12, '30': 5, '31': 12, '32': 7,
        '34': 10, '35': 11, '36': 3, '37': 7, '38': 11, '39': 6, '40': 9, '41': 6, '42': 6, '43': 4, '44': 14, '45': 8,
        '46': 4, '47': 7, '48': 4, '49': 11, '50': 8, '51': 5, '52': 1, '53': 1, '54': 4, '55': 2, '56': 10, '57': 9,
        '58': 1, '59': 16, '60': 12, '61': 6, '62': 9, '63': 6, '64': 14, '65': 5, '66': 6, '67': 5, '68': 7, '69': 10,
        '70': 1, '71': 7, '72': 4, '73': 8, '74': 17, '75': 1, '76': 16, '77': 18, '79': 5, '80': 5, '81': 6,
        '82': 4, '84': 6, '85': 7, '86': 6, '87': 4, '88': 5, '89': 7, '90': 1, '91': 19, '92': 5, '93': 2,
        '94': 5, '95': 15, '971': 1, '2A': 4, '2B': 4
    })

    fr_chart.render_to_file(filename=filename + '.svg')


def draw_player_sorting():
    filename = './plottings/playersort'
    depart_num_tend = [
        ('Ain', 10175, 0.8), ('Alpes Maritimes', 11887, 4.0), ('Ardennes', 430, 13.8), ('Bouches-du-Rhône', 14007, 0.3),
        ('Cantal', 759, 10.3), ('Haute-Garonne', 11121, 2.5), ('Gironde', 14926, 2.9), ('Nord', 14285, 3.1),
        ('Pyrénées Atlantiques', 10735, 3.5), ('Rhône', 10583, 1.8), ('Sarthe', 2668, 39.3), ('Paris', 12380, -3.9),
        ('Seine-et-Marne', 10050, 0), ('Yvelines', 26899, -1.2), ('Var', 11395, 2.6), ('Haute-Vienne', 2141, 12.7),
        ('Hauts-de-Seine', 15544, -2.0), ('Val-d\'Oise', 10633, -1.1)
    ]
    depart_num_tend.sort(key=(lambda x: x[1]), reverse=True)
    df = pd.DataFrame({
        'departements': [depart_num_tend[i][0] for i in range(len(depart_num_tend))],
        'Nom': [depart_num_tend[i][1] / 1000 for i in range(len(depart_num_tend))],
        'Taux': [depart_num_tend[i][2] for i in range(len(depart_num_tend))]
    })

    sns.set_style('dark')
    fig, ax1 = plt.subplots(figsize=(11.7, 8.27))
    g = '#76d0b4'
    r = '#cfa19b'

    ax1 = sns.barplot(x='departements', y='Nom', data=df, color=g)

    ax2 = ax1.twinx()
    ax2 = sns.pointplot(x='departements', y='Taux', data=df, color=r)

    ax2.set(ylabel='Taux de croissance (%)', )
    ax1.set(xlabel='départements', ylabel='Nombre de licenciés (mille)')
    ax1.yaxis.label.set_color(g)
    ax2.yaxis.label.set_color(r)
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right", fontsize=8)
    ax1.figure.savefig(filename + '.png')
    plt.show()


if __name__ == '__main__':
    draw_distribution_map()
