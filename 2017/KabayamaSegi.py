from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):

    def init(self):
        self.name = 'Kabayama' # 設定名稱

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
        if heroes:
            a=int(heroes[0].position[0])
            b=int(heroes[0].position[1])
            e=int(heroes[0].health)
            f=int(heroes[0].level)
            g=int(hero.health)
            h=int(hero.level)
            if g>=e and h>=f:
                self.shoot_at(*heroes[0].position)
                self.accelerate_towards(a+150,b+150)
            else:
                c=int(polygons[0].position[0])
                d=int(polygons[0].position[1])
                self.shoot_at(*polygons[0].position)
                self.accelerate_towards(c+150,d+150)
        else:
            c=int(polygons[0].position[0])
            d=int(polygons[0].position[1])
            self.shoot_at(*polygons[0].position)
            self.accelerate_towards(c+250,d+250)
        for a in range(0,8):
            self.level_up(Ability.Reload)
        for b in range(0,8):
            self.level_up(Ability.HealthRegen)
        for c in range(0,8):
            self.level_up(Ability.MaxHealth)
        for d in range(0,8):
            self.level_up(Ability.BulletDamage)
        for e in range(0,8):
            self.level_up(Ability.MovementSpeed)
            self.level_up(Ability.BulletSpeed)
            self.level_up(Ability.BodyDamage)
            self.level_up(Ability.BulletPenetration)

Client.main()