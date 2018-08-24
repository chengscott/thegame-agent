from thegame import *
from thegame.gui import *
from math import*
import random


class Client(GuiClient):

    def init(self):
        self.name = 'Destroy Mode' # 設定名稱
    def action(self, hero, heroes, polygons, bullets):
        def dis(my_pos,ene_pos):
            x1,y1=my_pos
            x2,y2=ene_pos
            return (x1-x2)**2+(y1-y2)**2
        def move():
            z=0
            for h in heroes:
                w=heroes.index(h)
                if dis(hero.position,h.position)<dis(hero.position,heroes[z].position):
                    z=w
            x1,y1=hero.position
            x2,y2=heroes[z].position
            if hero.level>=9:
                self.shoot_at(*heroes[z].position)
            if hero.level<17:
                if abs(x1-x2)<=100 and abs(y1-y2)<=350:
                    self.accelerate(pi)
                elif abs(y1-y2)<=100 and abs(x1-x2)<=350:
                    self.accelerate(1.5*pi)
                elif abs(y1-y2)<=100 and not abs(x1-x2)<=350:
                    self.accelerate_towards(x2-x1,float(random.choice(['800','-800'])))
                elif abs(x1-x2) and not abs(y1-y2)<=350:
                    self.accelerate_towards(float(random.choice(['800','-800'])),y2-y1)
                elif abs(x1-x2)<=300 and abs(x1-x2)<=300:
                    self.accelerate_towards(-x2+random.randint(-100,100),-y2+random.randint(-100,100))
                else:
                    self.accelerate_towards(x1,y1)
            else:
                self.name = 'Suicide Mode'
                if hero.health>=heroes[z].health and hero.health/hero.abilities.max_health.value>=0.15:
                    self.accelerate_towards(x2,y2)
                elif hero.health/hero.abilities.max_health.value<0.5:

                    self.accelerate_towards(-x2,-y2)
                else:
                    self.accelerate_towards(x1,y1)
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        if polygons:
            if hero.level<9:
                cont=0
                exp=polygons[0].rewarding_experience
                for p in polygons:
                    p1=polygons.index(p)
                    ex=p.rewarding_experience
                    if exp<ex and sqrt(dis(hero.position,p.position))>=hero.bullet_speed*2:
                        cont=p1
                x2,y2=polygons[cont].position
                self.shoot_at(*polygons[cont].position)
                self.accelerate_towards(-x2,-y2)
            elif 9<=hero.level<17:
                if not heroes:
                    cont=0
                    exp=polygons[0].rewarding_experience
                    for p in polygons:
                        p1=polygons.index(p)
                        ex=p.rewarding_experience
                        if exp<ex and sqrt(dis(hero.position,p.position))>=hero.bullet_speed*2:
                            cont=p1
                    x2,y2=polygons[cont].position
                    self.shoot_at(*polygons[cont].position)
                    self.accelerate_towards(-x2,-y2)
                else:
                    move()
            else:
                if not heroes:
                    cont=0
                    exp=polygons[0].rewarding_experience
                    for p in polygons:
                        p1=polygons.index(p)
                        ex=p.rewarding_experience
                        if exp>ex and (p.health<polygons[cont].health or sqrt(dis(hero.position,p.position))>=hero.bullet_speed*3):
                            cont=p1
                    x1,y1=hero.position
                    x2,y2=polygons[cont].position
                    self.shoot_at(*polygons[cont].position)
                    if hero.health>=polygons[cont].health and hero.health/hero.abilities.max_health.value>=0.75:
                        self.accelerate_towards(x2,y2)
                    else:
                        self.accelerate_towards(x1,y1)
                else:
                    move()

        else:
            self.accelerate_towards(random.randint(-800,800),random.randint(-800,800))
        if hero.skill_points!=0:
            if hero.level<=9:
                self.level_up(2)
            elif 10<=hero.level<=17:
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(1)
            else:
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(2)
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(1)
                self.level_up(7)
                self.level_up(7)
                self.level_up(5)
                self.level_up(3)
                self.level_up(6)
                self.level_up(4)

Client.main()