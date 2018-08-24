# coding:

# In[ ]:

from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


def A(self, polygons, T):
    if len(polygons) > 0:
        #對多邊形
        self.shoot_at(*polygons[T].position)
        self.accelerate_towards(*polygons[T].position)


def AR(self, polygons, T, hero):
    if len(polygons) > 0:
        x = hero.position[0] - polygons[T].position[0]
        y = hero.position[1] - polygons[T].position[1]
        self.shoot_at(*polygons[T].position)
        self.accelerate_towards(hero.position[0] + x, hero.position[1] + y)


def B(self, heroes, K):
    if len(heroes) > 0:  #對敵人
        self.shoot_at(*heroes[K].position)
        self.accelerate_towards(*heroes[K].position)


def BR(self, heroes, K, hero):
    if len(heroes) > 0:
        self.shoot_at(*heroes[K].position)
        x = hero.position[0] - heroes[K].position[0]
        y = hero.position[1] - heroes[K].position[1]
        self.accelerate_towards(hero.position[0] + x, hero.position[1] + y)


def C(hero, self):
    #升級
    if hero.movement_speed_level < 2:
        self.level_up(Ability.MovementSpeed)
    if hero.health_regen_level < 3:
        self.level_up(Ability.HealthRegen)
    if hero.reload_level < 2:
        self.level_up(Ability.Reload)
    self.level_up(Ability.BulletDamage)

    if hero.bullet_damage_level == 8:
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.BulletSpeed)
        self.level_up(Ability.Reload)
        self.level_up(Ability.MovementSpeed)
        self.level_up(Ability.BodyDamage)
        self.level_up(Ability.BulletPenetration)


class Client(HeadlessClient):
    def init(self):
        self.name = 'Ｃ８７６３'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        distance_heroes = []
        for i in range(len(heroes)):
            x = hero.position[0] - heroes[i].position[0]
            y = hero.position[1] - heroes[i].position[1]
            d = (x**2 + y**2)**0.5
            distance_heroes.append(d)
        if len(distance_heroes) > 0:
            K = distance_heroes.index(min(distance_heroes))
            DH = min(distance_heroes)

        distance_polygons = []
        for i in range(len(polygons)):
            x = hero.position[0] - polygons[i].position[0]
            y = hero.position[1] - polygons[i].position[1]
            d = (x**2 + y**2)**0.5
            distance_polygons.append(d)
        if len(distance_polygons) > 0:
            T = distance_polygons.index(min(distance_polygons))
            DP = min(distance_polygons)

        if len(polygons) > 0:
            if DP < 200:
                AR(self, polygons, T, hero)
            elif polygons[T].body_damage < 30 or polygons[T].health < 10 * hero.bullet_damage:
                A(self, polygons, T)
            else:
                if polygons[len(polygons) - 1].body_damage < 30 or polygons[len(
                        polygons) - 1].health < 10 * hero.bullet_damage:
                    A(self, polygons, len(polygons) - 1)
                else:
                    AR(self, polygons, len(polygons) - 1, hero)

        if len(heroes) > 0:
            if DH < 300:
                BR(self, heroes, K, hero)
            elif heroes[K].level < hero.level - 10 or heroes[K].health < 20 * hero.bullet_damage and heroes[K].movement_speed_level < hero.movement_speed_level and DH < 800:
                B(self, heroes, K)
            elif len(polygons) > 0:
                if polygons[len(polygons) - 1].body_damage < 30 or polygons[len(
                        polygons) - 1].health < 10 * hero.bullet_damage:
                    A(self, polygons, len(polygons) - 1)
                else:
                    AR(self, polygons, len(polygons) - 1)
        C(hero, self)


Client.main()
