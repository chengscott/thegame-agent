from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'hsueh'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        if int(hero.health) <= 0.3 * int(hero.max_health):
            g = int(polygons[0].position[0])
            h = int(polygons[0].position[1])
            self.shoot_at(*polygons[0].position)
            self.accelerate_towards(g + 100, h + 100)
        else:
            if heroes:
                a = int(heroes[0].position[0])
                b = int(heroes[0].position[1])
                c = int(heroes[0].health)
                d = int(heroes[0].level)
                i = int(heroes[0].abilities.movement_speed.value)
                e = int(hero.health)
                f = int(hero.level)
                j = int(hero.abilities.movement_speed.value)
                if e >= c and f >= d and j >= i:
                    self.shoot_at(*heroes[0].position)
                    self.accelerate_towards(a - 160, b + 160)
                else:
                    g = int(polygons[0].position[0])
                    h = int(polygons[0].position[1])
                    self.shoot_at(*polygons[0].position)
                    self.accelerate_towards(g, h + 70)
            else:
                g = int(polygons[0].position[0])
                h = int(polygons[0].position[1])
                self.shoot_at(*polygons[0].position)
                self.accelerate_towards(g, h + 70)
            for x in range(0, 6):
                self.level_up(Ability.Reload)
                self.level_up(Ability.HealthRegen)
                self.level_up(Ability.MaxHealth)
                self.level_up(Ability.BulletPenetration)
                self.level_up(Ability.MovementSpeed)
                self.level_up(Ability.BulletSpeed)
                self.level_up(Ability.BodyDamage)
                self.level_up(Ability.BulletDamage)


Client.main()
