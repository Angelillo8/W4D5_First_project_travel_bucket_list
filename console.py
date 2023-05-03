from models.user import User
from models.continent import Continent
from models.country import Country
from models.city import City
from models.visited_city import Visited_city

import repositories.user_repository as user_repo
import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo
import repositories.visited_city_repository as visited_city_repo

visited_city_repo.delete_all()
city_repo.delete_all()
country_repo.delete_all()
continent_repo.delete_all()
user_repo.delete_all()

user1 = User("Angel", "Gonzalez")
user_repo.save(user1)
user2 = User("Arik", "The Terrible")
user_repo.save(user2)
user3 = User("Calum", "Lord of the...")
user_repo.save(user3)
user4 = User("Reka", "The Woman")
user_repo.save(user4)



# city1 = City("Caracas", country1)
# city_repo.save(city1)
# city2 = City("Maracaibo", country2)
# city_repo.save(city2)

# visited1 = Visited_city(user2, city1, True, "Beautiful place")
# visited_city_repo.save(visited1)

# visited2 = Visited_city(user2, city2, True, "Very warm place")
# visited_city_repo.save(visited2)

# visited3 = Visited_city(user1, city1, True, "Busy place")
# visited_city_repo.save(visited3)

# visited4 = Visited_city(user1, city2, False, "I would love to go there. People says it is very warm.")
# visited_city_repo.save(visited4)

# user1 = user_repo.select(34)
# city2 = city_repo.select(28)

# # print(city2)
# visited_city_test = Visited_city(user1, city2, True, "I would asdfasdfasdfasd to go there. People says it is very warm.", 37)

# visited_city_repo.update(visited_city_test)

# print(visited_city_test.id)


# visited_test = visited_city_repo.select(1)
# print(visited_test.city.country.continent.name)


