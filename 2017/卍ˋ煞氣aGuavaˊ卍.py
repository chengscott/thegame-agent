from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '卍ˋ煞氣aGuavaˊ卍'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.BodyDamage)
        self.level_up(Ability.Reload)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.BulletDamage)
        self.level_up(Ability.BulletPenetration)
        self.level_up(Ability.BulletSpeed)
        self.level_up(Ability.MovementSpeed)
        if heroes:
            self.shoot_at(*heroes[0].position)
            if heroes[0].health < hero.health:
                self.accelerate_towards(*heroes[0].position)
            else:
                self.accelerate_towards(0, 0)
        elif polygons:
            self.shoot_at(*polygons[0].position)
            if hero.health > hero.max_health * 0.7:
                self.accelerate_towards(*polygons[0].position)
            else:
                self.accelerate_towards(0, 0)
        else:
            self.accelerate_towards(4000, 5000)


Client.main()
