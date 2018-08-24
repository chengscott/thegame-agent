from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import random
import math
from functools import cmp_to_key


class Client(HeadlessClient):
    def init(self):
        self.name = 'HunTer'  # 設定名稱
        self.clk = 1
        self.should_run = 0
        self.atkID = int(-1e9)
        self.stpl = 0

    def action(self, hero, heroes, polygons, bullets):
        self.clk += 1
        self.clk %= 877777777777

        def get_dis(x, y):
            return (hero.position[0] - x)**2 + (hero.position[1] - y)**2

        def rad(x, y):
            if x:
                return math.atan(y / x)
            else:
                return 0

        def cm_dis(a, b):
            return get_dis(*a.position) - get_dis(*b.position)

        def cm_mhp(a, b):
            return a.max_health - b.max_health

        def ATK():
            if heroes:
                for hr in heroes:
                    if (hr.id == self.atkID):
                        return True
            return False

        if (hero.abilities.bullet_damage.level == 0):
            self.level_up(Ability.BulletDamage)
        skills = [
            Ability.HealthRegen,
            Ability.MaxHealth,
            Ability.MovementSpeed,
            Ability.BodyDamage,
            Ability.Reload,
            Ability.BulletDamage,
            Ability.BulletSpeed,
            Ability.BulletPenetration,
        ]
        self.accelerate(random.uniform(0, 2 * math.pi))
        cntsk = hero.skill_points
        for skill in skills:
            while (hero.abilities[skill].level < 8 and cntsk > 0):
                self.level_up(skill)
                cntsk -= 1
        if heroes:
            heroes.sort(key=cmp_to_key(cm_dis))
        if polygons:
            polygons.sort(key=cmp_to_key(cm_dis))
        if self.should_run:
            self.should_run += 1
            if heroes:
                if self.should_run > 400:
                    self.should_run = 0
                    self.accelerate_towards(*heroes[0].position)
                    self.shoot(self.stpl + math.pi)
                elif self.should_run > 300:
                    self.accelerate_towards(*heroes[0].position)
                    self.shoot_at(*heroes[0].position)
                else:
                    self.accelerate(
                        rad(heroes[0].position[0] - hero.position[0], heroes[0]
                            .position[1] - hero.position[1]) + math.pi)
                    self.shoot_at(*heroes[0].position)
            else:
                run = 0
                self.shoot(self.stpl)
        elif ATK():
            for hr in heroes:
                if (hr.id == self.atkID):
                    self.accelerate_towards(*hr.position)
                    self.shoot(
                        rad(hr.position[0] - hero.position[0], hr.position[1] -
                            hero.position[1]) + math.pi)
        else:
            self.atkID = int(-1e9)
            for hr in heroes:
                if get_dis(*hr.position) < 8000 and hr.level - hero.level > 3:
                    self.should_run = 1
                    self.stpl = rad(heroes[0].position[0] - hero.position[0],
                                    heroes[0].position[1] - hero.position[1])
                    break
            if (hero.abilities.health_regen.level == 8
                    and hero.abilities.max_health.level == 8):
                if heroes and get_dis(*heroes[0].position) < 5000:
                    idx = 0
                    print("Win")
                    self.accelerate_towards(heroes[idx].position[0],
                                            heroes[idx].position[1])
                    self.shoot(
                        rad(heroes[idx].position[0] - hero.position[0],
                            heroes[idx].position[1] - hero.position[1]) +
                        math.pi)
                    if heroes[0].health < (heroes[0].max_health / 3):
                        self.atkID = heroes[0].id
                elif polygons:
                    idx = 0
                    if (self.clk % 100 < 50):
                        if (get_dis(*polygons[idx].position) > 3000
                                and polygons[idx].max_health < 200):
                            self.accelerate_towards(*polygons[idx].position)
                    if polygons[idx].max_health >= 200:
                        polygons.sort(key=cmp_to_key(cm_mhp))
                    self.shoot_at(polygons[idx].position[0],
                                  polygons[idx].position[1])
            else:
                if heroes and get_dis(
                        *heroes[0].position
                ) < 1000 and heroes[0].level - hero.level < 3:
                    idx = 0
                    self.accelerate_towards(heroes[idx].position[0],
                                            heroes[idx].position[1])
                    self.shoot_at(
                        heroes[idx].position[0] + random.uniform(-1, 1),
                        heroes[idx].position[1] + random.uniform(-1, 1),
                    )
                elif polygons:
                    idx = 0
                    if polygons[idx].max_health >= 200:
                        polygons.sort(key=cmp_to_key(cm_mhp))
                    if (self.clk % 50 < 10):
                        if (get_dis(*polygons[idx].position) > 3000
                                and polygons[idx].max_health < 200):
                            self.accelerate_towards(*polygons[idx].position)
                    self.shoot_at(polygons[idx].position[0],
                                  polygons[idx].position[1])


Client.main()
