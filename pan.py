from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):

    def init(self):
        self.name = 'pan' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        if hero.reload_level != 8:
            self.level_up(6)
        elif hero.bullet_damage_level != 8:
            self.level_up(5)
        elif hero.health_regen_level <4 or hero.movement_speed_level != 8:
            if hero.health_regen_level < hero.movement_speed_level/2:
                self.level_up(0)
            else:
                self.level_up(7)
        elif hero.max_health_level != 8:
            self.level_up(1)
        elif hero.body_damage_level != 8:
            self.level_up(2)
        else:
            self.level_up(4)
            self.level_up(3)

        if polygons:
            mindist = 9999
            for i in range(0,len(polygons)):
                poly_dist = ((polygons[i].position[0]-hero.position[0])**2 + (polygons[i].position[1]-hero.position[1])**2)**0.5
                if poly_dist < mindist:
                    mindist = poly_dist
                    poly = polygons[i]
            self.shoot_at(*poly.position)
            if(mindist > 200):
                self.accelerate_towards(*poly.position)
            else:
                posx = 1.5*hero.position[0]-0.5*poly.position[0]
                posy = 1.5*hero.position[1]-0.5*poly.position[1]
                self.accelerate_towards(posx,posy)
        if heroes:
            mindist = 9999
            for i in range(0,len(heroes)):
                hero_dist = ((heroes[i].position[0]-hero.position[0])**2 + (heroes[i].position[1]-hero.position[1])**2)**0.5
                if hero_dist < mindist:
                    mindist = hero_dist
                    target_hero = heroes[i]
            if hero.health >= target_hero.health and hero.level >= target_hero.level and hero.health/hero.max_health >= 0.2:
                self.accelerate_towards(*target_hero.position)
                self.shoot_at(*target_hero.position)
            else:
                self.accelerate_towards(2*hero.position[0]-target_hero.position[0],2*hero.position[1]-target_hero.position[1])
                self.shoot_at(*target_hero.position)
        if polygons:
            if poly.edges == 5 and ((poly.position[0]-hero.position[0])**2 + (poly.position[1]-hero.position[1])**2)**0.5 <=200:
                posx = 1.5*hero.position[0]-0.5*poly.position[0]
                posy = 1.5*hero.position[1]-0.5*poly.position[1]
                self.accelerate_towards(posx,posy)
        ##if (hero.position[0]==0 and hero.position[1]==0) or 

Client.main()