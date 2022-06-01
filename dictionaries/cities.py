cities = {
    'Mesa': {
        'country': 'USA',
        'population': 497720, 
        'fact': 'lots of mormons',
    },
    'Tokyo': {
        'country': 'tokyo',
        'population': 10000000,
        'fact': 'love hotels everywhere!',
    },
    'London': {
        'country': 'London',
        'population': 6598222,
        'fact': 'tea and crumpets everywhere!',
    }
}

for city, stats in cities.items():
    print(f"\nHere are some stats about {city}:")
    for key, value in stats.items():
        print(f"\t{key} is {value} ")