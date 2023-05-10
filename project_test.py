#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hello!")


# In[ ]:


print("Firstly, what is the surface of the tournament?")


# In[ ]:


surface = input()


# In[ ]:


if surface == "clay":
    weights = {"surface": 0.31, "rank": 0.19, "tournament": 0.11, "country": 0.10, "age": 0.07, "h2h": 0.08, "height": 0.04, "odd": 0.10}
elif surface == "hard":
    weights = {"surface": 0.27, "rank": 0.16, "tournament": 0.12, "country": 0.11, "age": 0.06, "h2h": 0.08, "height": 0.10, "odd": 0.10}
elif surface == "grass":
    weights = {"surface": 0.37, "rank": 0.16, "tournament": 0.10, "country": 0.04, "age": 0.06, "h2h": 0.06, "height": 0.10, "odd": 0.11}
elif surface == "indoors":
    weights = {"surface": 0.35, "rank": 0.16, "tournament": 0.12, "country": 0.08, "age": 0.07, "h2h": 0.08, "height": 0.05, "odd": 0.09}
else:
    print("Invalid")


# In[ ]:


print("So the attributes for this surface are...")


# In[ ]:


for surface in weights:
    print(surface, "-" , weights[surface])


# In[ ]:


print("Now, tell me who is the first player of the match:")


# In[ ]:


p1 = input()


# In[ ]:


print("And who is the second player?")


# In[ ]:


p2 = input()


# In[ ]:


print("Match:", p1, "x", p2)


# ### This part is about the surface of each player

# In[ ]:


print("Now lets calculate the use of each player on", surface)


# In[ ]:


print("How many matches the first player won?")


# In[ ]:


p1_wins_surface = input()


# In[ ]:


print("How many matches the first player lost?")


# In[ ]:


p1_losts_surface = input()


# In[ ]:


p1_surface_percentage = int(p1_wins_surface) / (int(p1_losts_surface) + int(p1_wins_surface))


# In[ ]:


print("So player one has a leverage of", p1_surface_percentage , "at this surface.")


# In[ ]:


print("So, how many matches the second player won?")


# In[ ]:


p2_wins_surface = input()


# In[ ]:


print("So, how many matches the second player lost?")


# In[ ]:


p2_losts_surface = input()


# In[ ]:


p2_surface_percentage = int(p2_wins_surface) / (int(p2_losts_surface) + int(p2_wins_surface))


# In[ ]:


print("So player two has a leverage of", p2_surface_percentage)


# In[ ]:


p1_surface = p1_surface_percentage / (p1_surface_percentage + p2_surface_percentage)


# In[ ]:


p2_surface = p2_surface_percentage / (p2_surface_percentage + p1_surface_percentage)


# In[ ]:


print("This part is the rank of the each player, usinga a scale 1.0 to 4.0 (float). Where 1 to 11 = 4 / 12 to 35 = 3 / 36 to 68 = 2 / 69 to ...) = 1")


# In[ ]:


print("What is the rank power of the first player?")


# In[ ]:


p1_ranking = input()


# In[ ]:


print("And what is the rank power of the second player?")


# In[ ]:


p2_ranking = input()


# In[ ]:


p1_rank = float(p1_ranking) / (float(p1_ranking) + (float(p2_ranking)))


# In[ ]:


p2_rank = float(p2_ranking) / (float(p2_ranking) + (float(p1_ranking)))


# In[ ]:


print("This part is about the weight of the tournmament for each player (in scale of 1.0 to 4.0 - Using float numbers).")


# In[ ]:


print("What is the importance of the tournament for the p1?")


# In[ ]:


p1_tournament_percentage = input()


# In[ ]:


print("What is the importance of the tournament for the p2?")


# In[ ]:


p2_tournament_percentage = input()


# In[ ]:


p1_tournament = float(p1_tournament_percentage) / (float(p1_tournament_percentage) + float(p2_tournament_percentage))


# In[ ]:


p2_tournament = float(p2_tournament_percentage) / (float(p2_tournament_percentage) + float(p1_tournament_percentage))


# In[ ]:


print("In this part we will approach the country of the tournament and the nationality of the player. Where if the player is native of the country we will attributed to him 1, else we will attributed to him 0")


# In[ ]:


print("The player 1 is the country of the tournament?")


# In[ ]:


p1_country = input()


# In[ ]:


print("The player 2 is the country of the tournament?")


# In[ ]:


p2_country = input()


# In[ ]:


print("This part is about the age of the player. Where the range gonna be - 1 to 3 (Use only 'float' numbers)")


# In[ ]:


print("Whats is the rate of age of the player 1?")


# In[ ]:


p1_age_percentage = input()


# In[ ]:


print("Whats is the rate of age of the player 2?")


# In[ ]:


p2_age_percentage = input()


# In[ ]:


p1_age = float(p1_age_percentage) / (float(p1_age_percentage) + float(p2_age_percentage))


# In[ ]:


p2_age = float(p2_age_percentage) / (float(p2_age_percentage) + float(p1_age_percentage))


# In[ ]:


print("This part is about H2H topic. We have to pay attention on H2H numbers, not even every match has a H2H history.")


# In[ ]:


print("How many matches the player 1 won?")


# In[ ]:


p1_h2h_percentage = input()


# In[ ]:


print("How many matches the player 2 won?")


# In[ ]:


p2_h2h_percentage = input()


# In[ ]:


p1_h2h = int(p1_h2h_percentage) / (int(p1_h2h_percentage) + int(p2_h2h_percentage))


# In[ ]:


p2_h2h = int(p2_h2h_percentage) / (int(p2_h2h_percentage) + int(p1_h2h_percentage))


# In[ ]:


print("This part is about the height of the player, most valorized on fast courts.")


# In[ ]:


print("Whats the height of the player 1?")


# In[ ]:


p1_height_percentage = input()


# In[ ]:


print("Whats the height of the player 2?")


# In[ ]:


p2_height_percentage = input()


# In[ ]:


p1_height = int(p1_height_percentage) / (int(p1_height_percentage) + int(p2_height_percentage))


# In[ ]:


p2_height = int(p2_height_percentage) / (int(p2_height_percentage) + int(p1_height_percentage))


# In[ ]:


print("This part is about the odds.")


# In[ ]:


print("What's the odd for the player 1?")


# In[ ]:


p1_odd_percentage = input()


# In[ ]:


p1_odd = 1 / float(p1_odd_percentage)


# In[ ]:


print("What's the odd for the player 2?")


# In[ ]:


p2_odd_percentage = input()


# In[ ]:


p2_odd = 1 / float(p2_odd_percentage)


# In[ ]:


print("Lets calculate the probability of the match...")


# In[ ]:


p1_use = weights["surface"] * float(p1_surface) + weights["rank"] * float(p1_rank) + weights["tournament"] * float(p1_tournament) + weights["country"] * float(p1_country) + weights["age"] * float(p1_age) + weights["h2h"] * float(p1_h2h) + weights["height"] * float(p1_height) + weights["odd"] * float(p1_odd)


# In[ ]:


p2_use = weights["surface"] * float(p2_surface) + weights["rank"] * float(p2_rank) + weights["tournament"] * float(p2_tournament) + weights["country"] * float(p2_country) + weights["age"] * float(p2_age) + weights["h2h"] * float(p2_h2h) + weights["height"] * float(p2_height) + weights["odd"] * float(p2_odd)


# In[ ]:


p1_probability = p1_use / (p1_use + p2_use) * 100


# In[ ]:


p2_probability = p2_use / (p2_use + p1_use) * 100


# In[ ]:


p1_odd = 1 / (p1_probability / 100)


# In[ ]:


p2_odd = 1 / (p2_probability / 100)


# In[ ]:


print("The probability of the match is..")


# In[ ]:


print(p1, "-" , p1_probability)


# In[ ]:


print(p2, "-" , p2_probability)


# In[ ]:


print("The fair odds for this match are:")


# In[ ]:


print(p1, "-" , p1_odd)


# In[ ]:


print(p2, "-" , p2_odd)

