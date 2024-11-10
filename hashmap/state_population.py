class StatePopulationMap:
    def __init__(self):
        # Initialize an empty dictionary to act as the hashmap
        self.population_map = {}

    def add_state(self, state, population):
        """Adds or updates the population of a state."""
        self.population_map[state] = population
        print(f"{state} added with population {population}")

    def get_population(self, state):
        """Retrieves the population of a state."""
        return self.population_map.get(state, "State not found")

    def remove_state(self, state):
        """Removes a state from the hashmap."""
        if state in self.population_map:
            del self.population_map[state]
            print(f"{state} removed.")
        else:
            print("State not found in the map.")

    def display_all(self):
        """Displays all states and their populations."""
        if not self.population_map:
            print("No states in the map.")
        else:
            for state, population in self.population_map.items():
                print(f"State: {state}, Population: {population}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the class
    state_population = StatePopulationMap()
    
    # Add states with populations
    state_population.add_state("California", 39538223)
    state_population.add_state("Texas", 29145505)
    state_population.add_state("Florida", 21538187)

    # Retrieve population of a specific state
    print(f"Population of Texas: {state_population.get_population('Texas')}")
    
    # Display all states and populations
    print("\nAll states and populations:")
    state_population.display_all()
    
    # Remove a state
    state_population.remove_state("Florida")

    # Display all states and populations after removal
    print("\nAll states and populations after removal:")
    state_population.display_all()
