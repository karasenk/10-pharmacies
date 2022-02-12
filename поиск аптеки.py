import sys
from geocoder import get_ll_span, get_nearest_organization
from mapapi import show_map


def main(toponim):
    ll = get_ll_span(toponim)[0]
    points = get_nearest_organization(ll.split(','), 'аптека')
    pt = []
    for i, p in enumerate(points):
        if not p[1]:
            color = 'gr'
        elif p[1].split(' ')[1] == 'круглосуточно':
            color = 'gn'
        else:
            color = 'bl'
        pt.append(f'{(p[0][0])},{p[0][1]},pm{color}m{i + 1}')
    show_map(f'll={ll}&pt={"~".join(pt)}')


if __name__ == '__main__':
    t = " ".join(sys.argv[1:])
    if t:
        main(t)
