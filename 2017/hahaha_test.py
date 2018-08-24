from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'hahaha test'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        if heroes:
            sum1 = []
            sum2 = []
            for p in range(len(heroes)):
                x = (heroes[p].position[0] - hero.position[0])**2
                y = (heroes[p].position[1] - hero.position[1])**2
                sum1.append(x + y)
            sum2 = sorted(sum1)
            for i in range(len(sum1)):
                if sum1[i] == sum2[0]:
                    close1 = i
            if hero.position != heroes[close1].position:
                self.accelerate_towards(*heroes[close1].position)
                self.shoot_at(*heroes[close1].position)
        if polygons:
            ## not collide
            sum3 = []
            sum4 = []
            close = 0
            sclose = 0
            for p in range(len(polygons)):
                x = (polygons[p].position[0] - hero.position[0])**2
                y = (polygons[p].position[1] - hero.position[1])**2
                sum3.append(x + y)
                sum4 = sorted(sum3)
            for i in range(len(sum3)):
                if sum3[i] == sum4[0]:
                    close = i
                elif sum3[i] == sum4[int(len(sum3) / 2)]:
                    sclose = i
            if hero.position != polygons[close].position:
                self.accelerate_towards(*polygons[sclose].position)
                if polygons[close].health < 300:
                    self.shoot_at(*polygons[close].position)
                elif polygons[close].max_health == 100:
                    self.shoot_at(*polygons[close].position)
                elif polygons[close].max_health == 300:
                    self.shoot_at(*polygons[close].position)
                elif polygons[close].max_health == 1000:
                    self.shoot_at(*polygons[close].position)
            ##


## upgrade
        if hero.reload_level < 6:
            self.level_up(Ability.Reload)
        elif hero.health_regen_level < 3:
            self.level_up(Ability.HealthRegen)
        elif hero.bullet_penetration_level < 5:
            self.level_up(Ability.BulletPenetration)
        elif hero.reload_level < 8 or hero.bullet_penetration_level < 8 or hero.bullet_damage_level < 8:
            self.level_up(Ability.Reload)
            self.level_up(Ability.BulletPenetration)
            self.level_up(Ability.BulletDamage)
        elif hero.health_regen_level < 8 or hero.max_health_level < 8:
            self.level_up(Ability.MaxHealth)
            self.level_up(Ability.HealthRegen)
        elif hero.movement_speed_level < 8 or hero.bullet_speed_level < 8 or hero.body_damage_level < 8:
            self.level_up(Ability.BodyDamage)
            self.level_up(Ability.BulletSpeed)
            self.level_up(Ability.MovementSpeed)

Client.main()
