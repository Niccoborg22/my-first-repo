#%%

empty_dict = {}

championships = {
    "it" : "Serie A",
    "es" : "La Liga",
    "uk" : "Premier League",
    "fr" : "Ligue 1"
}

championships["ne"] = "Eredivise"

championships.pop("ne")

print(championships["uk"] + " " + championships["it"])

for league in championships:
    print(championships[league])


# %%
