from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import random

class Client(GuiClient):

    def init(self):
        self.name = '111' # 設定名稱

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

        self.accelerate_towards(3721,10)

        self.level_up(0)
        self.level_up(1)
        if hero.abilities.health_regen.value>7:
            self.level_up(5)
            self.accelerate_towards(5000,2000)
        if hero.abilities.bullet_damage.level>hero.abilities.bullet_penetration.level:
            self.level_up(4)

        if polygons:
            self.shoot_at(*polygons[0].position)
        if bullets:
            if abs(((bullets[0].position[0]-hero.position[0])**2+(bullets[0].position[1]-hero.position[1])**2)**0.5)<100:
                if abs(bullets[0].position[1]-hero.position[1])<100 or abs(bullets[0].position[0]-hero.position[0])<40:
                    self.accelerate(6.28)
                elif abs(bullets[0].position[1]-hero.position[1])<40 or abs(bullets[0].position[0]-hero.position[0])<100:
                    self.accelerate(1.57)
        if heroes:
            self.shoot_at(*heroes[0].position)


Client.main()
