import math
# Turbine de référence NREL 5 MW
DIAMETRE = 126.0      # m
HAUTEUR_MOYEU = 90.0  # m
# Site synthétique : un carré en plaine
LARGEUR_SITE = 3000.0 # m
LONGUEUR_SITE = 3000.0 # m
N_TURBINES = 16
def aire_turbine (d):
    return math.pi * d**2/4
