import math
from tour import Tour
from projectileFeu import ProjectileFeu

class TourFeu(Tour):
    def __init__(self, parent, clic_x, clic_y):
        super().__init__(clic_x, clic_y, 35, 35)
        self.parent = parent # Partie
        self.type = "FEU"
        self.portee_attaque = self.largeur + self.longueur * 2
        self.aire_attaque = self.determine_circonference_attaque()
        self.cible = None
        self.projectiles = []
        self.image = "images\Towers\Tour_feu.png"

    def determine_circonference_attaque(self):
        return 2 * math.pi * self.portee_attaque

    def attaque(self, creep_cible):
        if not self.attaque_en_cours:
            self.attaque_en_cours = True
            self.cible = creep_cible
            self.projectiles.append(ProjectileFeu(self, self.x, self.y, self.cible, self.parent))