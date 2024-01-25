import pygame
import pygame.font
import sys
import random

# Initialisation de Pygame
pygame.init()
clock = pygame.time.Clock()

# Paramètres du jeu
largeur, hauteur = 800, 600
taille_case = 20
vitesse = 15

# Couleurs
couleur_fond = (0, 0, 0)
couleur_serpent = (0, 255, 0)
couleur_pomme = (255, 0, 0)

# Définition des directions
HAUT = (0, -1)
BAS = (0, 1)
GAUCHE = (-1, 0)
DROITE = (1, 0)

# Classe représentant le serpent
class Serpent:
    def __init__(self):
        self.longueur = 1
        self.corps = [(largeur // 2, hauteur // 2)]
        self.direction = DROITE

    def deplacer(self):
        tete = (self.corps[0][0] + self.direction[0] * taille_case,
                self.corps[0][1] + self.direction[1] * taille_case)

        # Correction pour réapparaître de l'autre côté
        tete = (tete[0] % largeur, tete[1] % hauteur)

        self.corps.insert(0, tete)
        if len(self.corps) > self.longueur:
            self.corps.pop()

    def manger_pomme(self):
        self.longueur += 1

    def verifier_collision(self):
        if self.corps[0] in self.corps[1:]:
            raise CollisionException("Le serpent s'est mangé lui-même!")

# Classe représentant la pomme
class Pomme:
    def __init__(self):
        self.position = self.generer_position()

    def generer_position(self):
        x = random.randint(0, (largeur - taille_case) // taille_case) * taille_case
        y = random.randint(0, (hauteur - taille_case) // taille_case) * taille_case
        return x, y

    def deplacer(self):
        self.position = self.generer_position()

# Exception pour gérer les collisions
class CollisionException(Exception):
    pass

# Initialisation du jeu
score = 0
font = pygame.font.Font(None, 36)
couleur_texte = (255, 255, 255)  # Couleur du texte

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake Game")

# Initialisation du serpent et de la pomme
serpent = Serpent()
pomme = Pomme()

# Fonction pour afficher le menu
def afficher_menu():
    fenetre.fill(couleur_fond)
    titre_font = pygame.font.Font(None, 60)
    titre_texte = titre_font.render("Snake Game", True, (255, 255, 255))
    fenetre.blit(titre_texte, ((largeur - titre_texte.get_width()) // 2, 50))

    options_font = pygame.font.Font(None, 36)
    jouer_texte = options_font.render("1. Jouer", True, couleur_texte)
    scores_texte = options_font.render("2. Scores précédents", True, couleur_texte)
    quitter_texte = options_font.render("3. Quitter", True, couleur_texte)

    fenetre.blit(jouer_texte, (50, 200))
    fenetre.blit(scores_texte, (50, 250))
    fenetre.blit(quitter_texte, (50, 300))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "jouer"
                elif event.key == pygame.K_2:
                    return "scores"
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

#Fonction afficher game over
def afficher_game_over():
    fenetre.fill(couleur_fond)

    game_over_font = pygame.font.Font(None, 60)
    game_over_texte = game_over_font.render("Game Over", True, (255, 255, 255))
    fenetre.blit(game_over_texte, ((largeur - game_over_texte.get_width()) // 2, 50))

    score_texte = font.render(f"Score: {score}", True, couleur_texte)
    fenetre.blit(score_texte, ((largeur - score_texte.get_width()) // 2, 150))

    quitter_texte = font.render("Quitter (Q)", True, couleur_texte)
    rejouer_texte = font.render("Rejouer (R)", True, couleur_texte)

    fenetre.blit(quitter_texte, ((largeur - quitter_texte.get_width()) // 2, 250))
    fenetre.blit(rejouer_texte, ((largeur - rejouer_texte.get_width()) // 2, 300))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return "rejouer"

# Fonction pour sauvegarder les scores dans un fichier
def sauvegarder_scores(scores):
    with open("scores.txt", "w") as fichier:
        for score in scores:
            fichier.write(f"{score}\n")

# Fonction pour charger les scores depuis un fichier
def charger_scores():
    scores = []
    try:
        with open("scores.txt", "r") as fichier:
            for ligne in fichier:
                scores.append(int(ligne.strip()))
    except FileNotFoundError:
        # Le fichier n'existe pas encore, retourner une liste vide
        pass
    return scores

# Fonction pour afficher les scores
def afficher_scores():
    scores = charger_scores()
    print("Scores précédents:")
    for i, s in enumerate(scores, start=1):
        print(f"{i}. {s}")

# Fonction pour afficher les scores à l'écran
def afficher_scores_ecran(scores):
    fenetre.fill(couleur_fond)

    scores_font = pygame.font.Font(None, 36)
    titre_texte = scores_font.render("Scores précédents", True, couleur_texte)
    fenetre.blit(titre_texte, ((largeur - titre_texte.get_width()) // 2, 50))

    y_position = 150
    for i, s in enumerate(scores, start=1):
        score_texte = scores_font.render(f"{i}. {s}", True, couleur_texte)
        fenetre.blit(score_texte, ((largeur - score_texte.get_width()) // 2, y_position))
        y_position += 40

    retour_texte = scores_font.render("Appuyez sur Echap pour retourner au menu", True, couleur_texte)
    fenetre.blit(retour_texte, ((largeur - retour_texte.get_width()) // 2, hauteur - 50))

    pygame.display.flip()

    attendre_retour_menu()

# Fonction pour attendre que l'utilisateur appuie sur la touche Echap
def attendre_retour_menu():
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    attente = False

# Boucle principale du jeu
jeu_en_cours = False  # Initialisation en dehors de la boucle du menu
while True:
    choix = afficher_menu()

    if choix == "jouer":
        # Réinitialiser le jeu
        serpent = Serpent()
        pomme = Pomme()
        score = 0

        # Activer la boucle du jeu
        jeu_en_cours = True


        # Boucle principale du jeu (désactivée tant que jeu_en_cours est False)
    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jeu_en_cours = False  # Désactiver la boucle du jeu si Echap est appuyé
                # Ajoutez d'autres conditions pour gérer les autres touches du jeu

        # Obtenez l'état des touches
        touches = pygame.key.get_pressed()

        # Déplacement du serpent en fonction des touches enfoncées
        if touches[pygame.K_UP] and serpent.direction != BAS:
            serpent.direction = HAUT
        elif touches[pygame.K_DOWN] and serpent.direction != HAUT:
            serpent.direction = BAS
        elif touches[pygame.K_LEFT] and serpent.direction != DROITE:
            serpent.direction = GAUCHE
        elif touches[pygame.K_RIGHT] and serpent.direction != GAUCHE:
            serpent.direction = DROITE

        # Déplacement du serpent
        serpent.deplacer()

        # Vérification des collisions
        try:
            serpent.verifier_collision()
        except CollisionException as e:
            print(e)
                # Afficher l'écran de Game Over
            choix_game_over = afficher_game_over()
            if choix_game_over == "rejouer":
                # Réinitialiser le jeu
                serpent = Serpent()
                pomme = Pomme()
                score = 0
            else:
                    # Sauvegarder le score avant de quitter
                scores = charger_scores()
                scores.append(score)
                scores.sort(reverse=True)
                sauvegarder_scores(scores)
                pygame.quit()
                sys.exit()

        # Vérification de la capture de la pomme
        if serpent.corps[0] == pomme.position:
            serpent.manger_pomme()
            pomme.deplacer()
            score += 1  # Augmenter le score du joueur

        # Affichage
        fenetre.fill(couleur_fond)

        # Dessiner le serpent avec des cercles
        for i, pos in enumerate(serpent.corps):
            rayon = taille_case // 2
            couleur = couleur_serpent if i == 0 else (0, 150, 0)  # Tête du serpent de couleur différente
            pygame.draw.circle(fenetre, couleur, (pos[0] + rayon, pos[1] + rayon), rayon)

        # Dessiner la pomme avec un cercle
        rayon_pomme = taille_case // 2
        pygame.draw.circle(fenetre, couleur_pomme, (pomme.position[0] + rayon_pomme, pomme.position[1] + rayon_pomme), rayon_pomme)

        # Affichage du score
        texte_score = font.render(f"Score: {score}", True, couleur_texte)
        fenetre.blit(texte_score, (10, 10))

        pygame.display.flip()

        # Limiter la vitesse du jeu
        clock.tick(vitesse)
        if choix == "scores":
    # Afficher les scores
            scores = charger_scores()
            afficher_scores_ecran(scores)