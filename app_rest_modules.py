# List of rest modules to be initialized
from rest.approvisionnement_ressource import *
from rest.facture_ressource import *
from rest.fournisseur_ressource import *
from rest.produit_commande_ressource import *
from rest.produit_ressource import *
from rest.stock_ressource import *
from rest.client_ressource import *
from rest.commande_ressource import *
from rest.compte_ressource import *


def init():
    print("REST modules initialization")