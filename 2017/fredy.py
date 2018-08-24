from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'fredy'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        a = 0
        b = 0
        dis = 0
        dis2 = 0
        dist = []
        dist2 = []
        if hero.abilities.health_regen.level <= 2:
            self.level_up(0)
        if hero.abilities.body_damage.level < 8:
            self.level_up(2)

        self.level_up(4)
        if hero.abilities.movement_speed.level <= 3:
            self.level_up(1)
        if hero.abilities.movement_speed.level <= 3:
            self.level_up(7)
        if hero.abilities.bullet_penetration.level <= 3:
            self.level_up(6)
        if hero.abilities.reload.level == 8:
            self.level_up(5)
        if hero.abilities.bullet_damage.level == 8:
            self.level_up(3)
        if hero.abilities.bullet_speed.level == 8:
            for aa in range(0, 8):
                self.level_up(aa)
        for j in range(0, len(polygons)):
            if polygons:
                dist.append((polygons[j].position.x - hero.position.x)**2 +
                            (polygons[j].position.y - hero.position.y)**2)
        for k in range(0, len(heroes)):
            if heroes:
                dist2.append((heroes[k].position.x - hero.position.x)**2 +
                             (heroes[k].position.y - hero.position.y)**2)
        for l in range(0, len(dist)):
            if polygons:
                if dist[l] == min(dist):
                    a = l
        for m in range(0, len(dist2)):
            if heroes:
                if dist2[m] == min(dist2):
                    b = m
        print("-" * 79)
        if polygons:
            dis = (polygons[a].position.x - hero.position.x)**2 + (
                polygons[a].position.y - hero.position.y)**2
        if heroes:
            dis2 = (heroes[b].position.x - hero.position.x)**2 + (
                heroes[b].position.y - hero.position.y)**2
        if dis2 < 20 * hero.radius**2 and heroes:
            self.shoot_at(*heroes[b].position)
            self.accelerate_towards(
                2 * hero.position.x - 2 * heroes[b].position.x,
                2 * hero.position.y - 2 * heroes[b].position.y)
        elif dis < 50 * hero.radius**2 and polygons:
            self.accelerate_towards(hero.position.x - polygons[a].position.x,
                                    hero.position.y - polygons[a].position.y)
            self.shoot_at(*polygons[a].position)
        else:
            if polygons:
                self.shoot_at(*polygons[a].position)
                self.accelerate_towards(*polygons[a].position)
            if dis2 <= 500000:
                if heroes and hero.health > heroes[b].health and hero.level >= 20:
                    self.shoot_at(*heroes[b].position)
                    self.accelerate_towards(*heroes[b].position)
                if heroes and hero.health < heroes[b].health:
                    self.shoot_at(*heroes[b].position)
                    self.accelerate_towards(
                        2 * hero.position.x - 2 * heroes[b].position.x,
                        2 * hero.position.y - 2 * heroes[b].position.y)
                if heroes and hero.body_damage < heroes[b].body_damage:
                    self.accelerate_towards(
                        2 * hero.position.x - 2 * heroes[b].position.x,
                        2 * hero.position.y - 2 * heroes[b].position.y)
            if hero.position.x <= 1000 or hero.position.x >= 4000:
                self.accelerate_towards(2500, 2000)
            if hero.position.y <= 1000 or hero.position.y >= 3000:
                self.accelerate_towards(2500, 2000)


Client.main()
