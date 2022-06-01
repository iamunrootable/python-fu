river_pairs = {
    'Nile':'Egypt',
    'Mississipi': 'USA',
    'NiagraFalls': 'Canada'
}

for river, country in river_pairs.items():
    print(f"\nThe {river} river runs through {country}.")

for river in river_pairs.keys():
    print(f"\n{river}")

for country in river_pairs.values():
    print(f"\n{country}")


