class StatePopulation:
    def __init__(self):
        self.population_map = {}

    def add_data(self, state, population):
        self.population_map[state] = population

    def get_data(self, state):
        if not self.isEmpty():
            if state in self.population_map:
                print(f'Value of {state} is {self.population_map[state]}')
            else:
                print(f'{state} not found')
        else:
            print('Map is empty')

    def remove_data(self, state):
        if not self.isEmpty():
            if state in self.population_map:
                del self.population_map[state]
                print(f'{state} is removed.')
            else:
                print(f'{state} not found.')
        else:
            print('Map is empty')
            
    def update_data(self, state, population):
        self.population_map[state] = population

    def display_all(self):
        if not self.isEmpty():
            for state, population in self.population_map.items():
                print(f'{state} : {population}')
        else:
            print('Map is empty')

    def isEmpty(self):
        return not self.population_map

if __name__ == '__main__':
    state_population = StatePopulation()
    state_population.add_data('Texas', 10000)    
    state_population.add_data('New York', 20000)    
    state_population.add_data('California', 30400)
    state_population.get_data('Texas')
    state_population.remove_data('New York')
    state_population.update_data('New Jersey', 5000)
    state_population.display_all()
