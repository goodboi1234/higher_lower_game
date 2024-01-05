import pygame
import sys
from dict_data import most_searched_google as data
import random




class logic(pygame.sprite.Sprite):
    def __init__(self  , group):
        super().__init__(group)
        self.j = True
        self.val()
        self.count = 0  
        self.feel  = True
        self.game1 = True
        # self.font = pygame.font.SysFont("/Users/zeeldarji/Desktop/python files/the_higher_lower_game.py/fonts/test" , 20)
        # self.text = "thanks for playing the game"

    def val(self):
        while self.j == True:    
            
            self.k1 , self.v1 = random.choice(list(data.items()))
            self.k2 , self.v2 = random.choice(list(data.items()))
            if self.k2 != self.k1 and self.v2 != self.v1:
                self.j = False

            else:   
                self.j = True
            


#self.j = False

    def play(self):
        inter = input(f"you think {self.k2} is more searched then {self.k1} or less searched? \n type high or low")
        if inter =="high" and  self.v1<=self.v2:
            print('you are wrong')
            return  False
        if inter == "high" and self.v2<=self.v1:
            print("you won")
            return  True
    
        if inter =="low" and  self.v2>=self.v1:
            print('you are right')
            return  True
        
        if inter == "low" and self.v2<=self.v1:
            print("you lost")
            return  False

    def game(self):
        while self.game1 == True:
   
            if  self.play() == True:
                    n_j = True
                    self.count +=1
                    self.k1 = self.k2
                    self.v1 = self.v2
                    while n_j == True:
                        self.k2 , self.v2 = random.choice(list(data.items()))
                        if self.k2 != self.k1 and self.v2 != self.v1:
                            n_j = False

                        else:   
                            n_j = True
                    
                    
                    continue

            
            if self.play()== False:
                    print(f"your total score is {self.count}")
                    print('you lost')
                    break
                    

                
    def update(self):
        self.play()
        self.game()
                


#THE OBJECT
group = pygame.sprite.Group()
lo = logic(group)
lo.update()