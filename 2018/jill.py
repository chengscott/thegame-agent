from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'jill'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        m, e = hero.position

        if polygons:
            x, y = polygons[0].position
            self.shoot_at(*polygons[0].position)
            for j in polygons:
                if j.health >= hero.health / 2:
                    self.accelerate_towards(-y, x)
                else:
                    if j.health >= 0 and j.health <= hero.health / 2:
                        self.accelerate_towards(x, y)
                        self.shoot_at(x, y)

        if bullets:
            m, e = hero.position
            z, w = bullets[0].position

            self.accelerate_towards((e - w) * 120, (z - m) * 120)
        if heroes:
            self.shoot_at(*heroes[0].position)
            a, b = heroes[0].position

            for i in heroes:
                if i.health >= hero.health / 2 or i.level > hero.level:
                    self.accelerate_towards((-b - e + 10) * 120, (a - m) * 120)
                else:
                    if i.health >= 0:
                        self.accelerate_towards(a, b)
                        self.shoot_at(a, b)

        i = hero.level

        if i <= 6:
            self.level_up(Ability.HealthRegen)
        elif i <= 12:
            self.level_up(Ability.MaxHealth)
        elif i <= 18:
            self.level_up(Ability.Reload)
        elif i <= 24:
            self.level_up(Ability.MovementSpeed)
        elif i <= 28:
            self.level_up(Ability.BulletDamage)
        elif i <= 32:
            self.level_up(Ability.BodyDamage)
        else:
            self.level_up(Ability.BulletPenetration)


Client.main()
