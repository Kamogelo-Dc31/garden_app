# Hardcoded values for the season and plant type
season = input("Enter the season (e.g., summer, winter): ").lower()
plant_type = input("Enter the plant type (e.g., flower, vegetable): ").lower()


# Variable to hold gardening advice
advice = "this is advice"


def get_season_advice(season):
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
    }
    return season_advice.get(season, "No advice for this season.")


def get_plant_advice(plant_type):
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
    }
    return plant_advice.get(plant_type, "No advice for this type of plant.")


# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
