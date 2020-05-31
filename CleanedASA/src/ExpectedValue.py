# Name: Expected.py
# This program calculates the expected MSE value for a theoretically random keyword
# We found MSE = 416.5

sum = 0
for i in range(1, 51):
    for j in range(1,51):
        sum  = sum + (i - j)**2
sum = sum/2500
print(sum)

map = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
              projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('st99_d00', name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca()  # get current axes instance

holder_list = []

for nshape, seg in enumerate(map.states):
    # skip DC and Puerto Rico.
    if state_names[nshape] not in ['Puerto Rico', 'District of Columbia']:
        if state_names[nshape] in convert(globals()[kw + '_states']):
            if state_names[nshape] not in holder_list:
                holder_list.append(state_names[nshape])
            if state_names[nshape] in convert(globals()[kw + '_increase_states']):
                if 1.3 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 1.5:
                    color = '#00EFFF'
                if 1.5 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 1.7:
                    color = '#00E8F9'
                if 1.7 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 1.9:
                    color = '#00DFEF'
                if 1.9 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.1:
                    color = '#00BEE4'
                if 2.1 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.3:
                    color = '#00AEE4'
                if 2.3 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.5:
                    color = '#00A5D7'
                if 2.5 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.7:
                    color = '#0089D8'
                if 2.7 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.9:
                    color = '#0073D8'
                if 2.9 < globals()[kw + '_significance_level'][len(holder_list) - 1]:
                    color = '#0056D8'
            else:
                if 1.3 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 1.6:
                    color = 'xkcd:pale rose'
                if 1.6 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 1.9:
                    color = 'xkcd:salmon pink'
                if 1.9 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.2:
                    color = 'xkcd:light red'
                if 2.2 < globals()[kw + '_significance_level'][len(holder_list) - 1] <= 2.5:
                    color = 'xkcd:strawberry'
                if 2.5 < globals()[kw + '_significance_level'][len(holder_list) - 1]:
                    color = 'xkcd:bright red'

            poly = Polygon(seg, facecolor=color, edgecolor=color)
            ax.add_patch(poly)

fname = datetime.datetime.now().strftime("%m-%d-%Y _ %H:%M:%S")
name = "{}.png".format(fname)
plt.savefig(name)