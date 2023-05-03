class Country:
    def __init__(self, name, continent, id = None):
        self.name = name
        self.continent = continent
        self.id = id

    # def get_countries_by_continent(countries, continent_id):
    #     countries_to_return = []
    #     for country in countries:
    #         if country.continent == continent_id:
    #             countries_to_return.append(country)
    #     return countries_to_return