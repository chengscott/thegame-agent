from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '123'

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        self.accelerate(2)
        if polygons:
            self.shoot_at(*polygons[0].position)
        if heroes:
            self.shoot_at(*heroes[0].position)
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.BodyDamage)
        self.level_up(Ability.Reload)
        self.level_up(Ability.BulletPenetration)
        self.level_up(Ability.BulletDamage)
        self.level_up(Ability.BulletSpeed)


Client.main()
