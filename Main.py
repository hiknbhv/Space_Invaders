import pygame, random

#Intialize pygame
pygame.init()

#Set Display Surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        #Set game values
        self.round_number = 1
        self.score = 0
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group
        # TODO: set the player to self.player
        # TODO: repeat for alien_group, player_bullet_group, alien_bullet_group.  set all to a self. version.

        #Set sounds and music
        self.new_round_sound = pygame.mixer.Sound("./assets/audio/new_round.wav")
        self.breach_sound = pygame.mixer.Sound("./assets/audio/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("./assets/audio/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("./assets/audio/player_hit.wav")
        #TODO: repeat for breach_sound (using self) breach.wav
        #TODO: (cont.)  alien_hit_sound to alien_hit.wav
        #TODO: (cont.) player_hit_sound to player_hit.wav

        #Set font
        self.font = pygame.font.Font("./assets/fonts/Facon.ttf", 32)

    def update(self):
        """Update the game"""
        ... #TODO: we will do this one later.

    def draw(self):
        """Draw the HUD and other information to display"""
        ... #TODO: we will do this one later.

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""
        ... #TODO: we will do this one later.

    def check_collision(self):
        """Check for collisions"""
        ... #TODO: we will do this one later.

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        ... #TODO: we will do this one later.

    def start_new_round(self):
        """Start a new round"""
        ... #TODO: we will do this one later.

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        ... #TODO: we will do this one later.

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        ... #TODO: we will do this one later.

    def reset_game(self):
        """Reset the game"""
        ... #TODO: we will do this one later.


class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("./assets/images/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_HEIGHT // 2
        self.rect.bottom = WINDOW_HEIGHT
        # TODO: (3/11/2025) assign to self.image the image loaded from "player_ship.png"
        # TODO: (3/11/2025) assign to self.rect the rect from the image
        # TODO: (3/11/2025) assign to self.rect.centerx the value of half of the WINDOW_WIDTH use //
        # TODO: (3/11/2025) assign to self.rect.bottom the WINDOW_HEIGHT

        self.lives = 5
        self.velocity = 8
        # TODO: (3/11/2025) assign to self.lives the value of 5
        # TODO: (3/11/2025) assign to self.velocity the value 8

        self.bullet_group = my_player_bullet_group

        self.shoot_sound = pygame.mixer.Sound(".Assets/audio/player_fire.wav")


    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()

        #Move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x =- self.velocity
        if keys[pygame.K_RIGHT] and self.rect.left > 0:
                self.rect.x =+ self.velocity

            # TODO: (3/11/2025) subtract self.velocity from self.rect.x
        # TODO: (3/11/2025) handle pressing K_RIGHT similarly to K_LEFT

    def fire(self):
        """Fire a bullet"""
        #Restrict the number of bullets on screen at a time
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
            # TODO: (3/11/2025) call self.shoot_sound's play method.
            # Call means to tell the funtion to start doing it's job

    def reset(self):
        """Reset the players position"""
        self.rect.cemnterx = WINDOW_WIDTH // 2


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("./Assets/images/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft =(x, y)
        # TODO: (3/11/2025) assign to self.image an image loaded from alien.png
        # TODO: (3/11/2025) assign to self.rect the rect from the self.image
        # TODO: (3/11/2025) assign to self.rect.topleft the tuple (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = my_alien_bullet_group

        self.shoot_sound = pygame.mixer.Sound("./assest/audio/alien_fire.wav")


    def update(self):
        """Update the alien"""
        self.rect.x =+ self.direction * self.velocity
        # TODO: (3/11/2025) add to self.rect.x the value of direction * velocity.  (Don't forget self

        #Randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        """Fire a bullet"""
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

    def reset(self):
        """Reset the alien position"""
        self.rect.lopleft = (self.starting_x , self.starting_y)
        self.direction = 1


class PlayerBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("./assets/images/green_laser.png")
        self.rect = self.image.get_rect()
        self.rect,centerx = x
        self.centery = y

        self.velcity = 10
        bullet_group.add(self)
        # TODO: (3/11/2025) assign 10 to self.velocity
        # TODO: (3/11/2025) call bullet_group's add method and pass in self.

    def update(self):
        """Update the bullet"""
        self.rect.y =- self.velcity
        if self.rect.bottom == 0:

        # TODO: (3/11/2025) subtract self.velocity from self.rect.y:
        # TODO: (3/11/2025) check if self.rect.bottom is less than 0.
            # TODO: (3/11/2025) the if block will then kill the sprite.


class AlienBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("./assets/images/red_laser.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y



        #TODO: (3/11/2025) assign x to self.rect.centerx
        #TODO: (3/11/2025) do the same for centery

        #TODO: (3/11/2025) assign 10 to self.velocity
        #TODO: (3/11/2025) call bullet_group's add method and pass in self.

    def update(self):
        """Update the bullet"""
         #TODO: (3/11/2025) add to self.velocity to self.rect.y:  Hint Hint:  +=

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()




#Create bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()
#TODO: repeat for my_alien_bullet_group

#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

my_alien_group = pygame.sprite.Group()
#Create an alien group.  Will add Alien objects via the game's start new round method
#TODO: create my_alien_group

#Create the Game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
my_game.start_new_round()

#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #The player wants to fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()

    # Fill the display
    display_surface.fill((0, 0, 0))

    #Update and display all sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    #Update and draw Game object
    my_game.update()
    my_game.draw()

    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()
