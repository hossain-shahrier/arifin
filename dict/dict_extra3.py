given_dict = {"Normal Skills": [10, 10, 10], "Ultimate Skill": 30}
additive_damage_score = sum(given_dict["Normal Skills"]) + given_dict["Ultimate Skill"]

if additive_damage_score <= 70:
    agent_name = "Rage"
elif additive_damage_score <= 100:
    agent_name = "Jett"
else:
    agent_name = "Sage"

# print the results
print("Additive Damage Score is", additive_damage_score)
print("The agent's name is", agent_name)
