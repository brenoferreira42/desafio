import random
from property.property import Property


class PropertiesGenerator:
    def __init__(self):
        self.properties = []
        self.__properties_sell_values = []
        self.__properties_rent_values = []

    def __generate_properties_sell_values(self):
        min_property_value = 150
        max_property_value = 800
        total_property_values = 0

        for _ in range(20):
            property_value = random.randint(min_property_value, max_property_value)
            self.__properties_sell_values.append(property_value)
            total_property_values += property_value

        average_property_value = total_property_values / len(
            self.__properties_sell_values
        )

        self.__properties_sell_values = [
            int(value * (average_property_value / property_value))
            for value in self.__properties_sell_values
        ]

    def __generate_rent_values(self):
        for property_value in self.__properties_sell_values:
            rent_value = int(property_value * random.uniform(0.05, 0.1))
            self.__properties_rent_values.append(rent_value)

    def construct_properties(self) -> list:
        self.__generate_properties_sell_values()
        self.__generate_rent_values()
        for i in range(20):
            current_property = Property(
                self.__properties_sell_values[i], self.__properties_rent_values[i]
            )
            self.properties.append(current_property)

        return self.properties
