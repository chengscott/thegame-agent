from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import random


class Client(HeadlessClient):
    def init(self):
        self.name = '~ ~ ~'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        #print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        #print("I'm surrounded by these polygons:", polygons)
        #print("I'm surrounded by these heroes:", heroes)
        #print("I'm surrounded by these bullets:", bullets)
        #print('-' * 79)
        print("my health = ", hero.health)

        if hero.level < 18:
            self.bullet_(hero, heroes, polygons, bullets)
            self.upgrate_(hero, heroes, polygons, bullets)
            if hero.health <= 200:
                self.enemy_(hero, heroes, polygons, bullets)
            else:
                self.polygons_(hero, heroes, polygons, bullets)
        if hero.level >= 18:
            self.bullet_(hero, heroes, polygons, bullets)
            self.upgrate_(hero, heroes, polygons, bullets)
            if hero.health <= 500:
                self.enemy_(hero, heroes, polygons, bullets)
            else:
                self.polygons_(hero, heroes, polygons, bullets)

    #def move_(self, hero, heroes, polygons, bullets):

    def bullet_(self, hero, heroes, polygons, bullets):
        bulldis = []
        bulldisapp = []

        for a in range(0, len(bullets)):
            if bullets[a].owner_id != hero.name and bullets[a].body_damage > 10:
                for i in range(0, len(bullets)):
                    bulldis.append(0)
                for j in range(0, len(bullets)):
                    bulldis[j] = (
                        (bullets[j].position[0] - hero.position[0])**2 +
                        (bullets[j].position[1] - hero.position[1])**2)**0.5
                for k in range(0, len(bullets)):
                    if bulldis[k] <= 400:
                        bulldisapp.append(k)
        for b in range(0, len(bulldisapp)):
            self.accelerate_towards(
                hero.position[0] + (hero.position[0] - bullets[k].position[0]),
                hero.position[1] + (hero.position[1] - bullets[k].position[1]))

    def polygons_(self, hero, heroes, polygons, bullets):
        polyhealth = []
        polydis = []
        enemydis = []
        enemylv = []
        enemyhealth = []

        for e in range(0, len(polygons)):
            polyhealth.append(0)
        for f in range(0, len(polygons)):
            polyhealth[f] = polygons[f].health
        minpolyhealth = min(polyhealth)
        for g in range(0, len(polygons)):
            if polyhealth[g] == minpolyhealth:
                break

        for i in range(0, len(polygons)):
            polydis.append(0)
        for j in range(0, len(polygons)):
            polydis[j] = ((polygons[j].position[0] - hero.position[0])**2 +
                          (polygons[j].position[1] - hero.position[1])**2)**0.5
        minpolydis = min(polydis)
        for k in range(0, len(polygons)):
            if polydis[k] == minpolydis:
                break

        for l in range(0, len(heroes)):
            enemydis.append(0)
        for m in range(0, len(heroes)):
            enemydis[m] = ((heroes[m].position[0] - hero.position[0])**2 +
                           (heroes[m].position[1] - hero.position[1])**2)**0.5
        minenemydis = min(enemydis)
        for n in range(0, len(heroes)):
            if enemydis[n] == minenemydis:
                break

        for p in range(0, len(heroes)):
            enemylv.append(0)
        for q in range(0, len(heroes)):
            enemylv[q] = heroes[q].level
        maxenemylv = max(enemylv)
        minenemylv = min(enemylv)
        for r in range(0, len(heroes)):
            if enemylv[r] == maxenemylv:
                break
        for s in range(0, len(heroes)):
            if enemylv[s] == minenemylv:
                break

        for t in range(0, len(heroes)):
            enemyhealth.append(0)
        for u in range(0, len(heroes)):
            enemyhealth[u] = heroes[u].health
        minenemyhealth = min(enemyhealth)
        for v in range(0, len(heroes)):
            if enemyhealth[v] == minenemyhealth:
                break

        #if minpolyhealth < 10 and minenemyhealth >= 10:
        #    if minenemydis < 100:
        #        self.accelerate_towards(hero.position[0] + (hero.position[0] - heroes[n].position[0]),hero.position[1] + (hero.position[1] - heroes[n].position[1]))
        #        self.shoot_at(*heroes[n].position)
        #    elif minpolydis < 100:
        #        self.accelerate_towards(hero.position[0] + (hero.position[0] - polygons[k].position[0]),hero.position[1] + (hero.position[1] - polygons[k].position[1]))
        #        self.shoot_at(*polygons[k].position)
        #    else:
        #        self.accelerate_towards(*polygons[g].position)
        #        self.shoot_at(*polygons[g].position)
        #if minenemyhealth < 10 and minenemyhealth >= 10:
        #    if minenemydis < 100:
        #        self.accelerate_towards(hero.position[0] + (hero.position[0] - heroes[n].position[0]),hero.position[1] + (hero.position[1] - heroes[n].position[1]))
        #        self.shoot_at(*heroes[n].position)
        #    elif minpolydis < 100:
        #        self.accelerate_towards(hero.position[0] + (hero.position[0] - polygons[k].position[0]),hero.position[1] + (hero.position[1] - polygons[k].position[1]))
        #        self.shoot_at(*polygons[k].position)
        #    else:
        #        self.accelerate_towards(*heroes[v].position)
        #        self.shoot_at(*heroes[v].position)
        #if minenemyhealth >= 10 and minenemyhealth >= 10:
        if minenemydis < 500:
            self.accelerate_towards(
                hero.position[0] + (hero.position[0] - heroes[n].position[0]),
                hero.position[1] + (hero.position[1] - heroes[n].position[1]))
            self.shoot_at(*heroes[n].position)
        if minpolydis >= 150:
            self.accelerate_towards(*polygons[k].position)
            self.shoot_at(*polygons[k].position)
        if minpolydis < 150:
            self.accelerate_towards(
                hero.position[0] +
                (hero.position[0] - polygons[k].position[0]), hero.position[1]
                + (hero.position[1] - polygons[k].position[1]))
            self.shoot_at(*polygons[k].position)

    def enemy_(self, hero, heroes, polygons, bullets):
        polyhealth = []
        polydis = []
        enemydis = []
        enemylv = []
        enemyhealth = []

        for e in range(0, len(polygons)):
            polyhealth.append(0)
        for f in range(0, len(polygons)):
            polyhealth[f] = polygons[f].health
        minpolyhealth = min(polyhealth)
        for g in range(0, len(polygons)):
            if polyhealth[g] == minpolyhealth:
                break

        for i in range(0, len(polygons)):
            polydis.append(0)
        for j in range(0, len(polygons)):
            polydis[j] = ((polygons[j].position[0] - hero.position[0])**2 +
                          (polygons[j].position[1] - hero.position[1])**2)**0.5
        minpolydis = min(polydis)
        for k in range(0, len(polygons)):
            if polydis[k] == minpolydis:
                break

        for l in range(0, len(heroes)):
            enemydis.append(0)
        for m in range(0, len(heroes)):
            enemydis[m] = ((heroes[m].position[0] - hero.position[0])**2 +
                           (heroes[m].position[1] - hero.position[1])**2)**0.5
        minenemydis = min(enemydis)
        for n in range(0, len(heroes)):
            if enemydis[n] == minenemydis:
                break

        for p in range(0, len(heroes)):
            enemylv.append(0)
        for q in range(0, len(heroes)):
            enemylv[q] = heroes[q].level
        maxenemylv = max(enemylv)
        minenemylv = min(enemylv)
        for r in range(0, len(heroes)):
            if enemylv[r] == maxenemylv:
                break
        for s in range(0, len(heroes)):
            if enemylv[s] == minenemylv:
                break

        for t in range(0, len(heroes)):
            enemyhealth.append(0)
        for u in range(0, len(heroes)):
            enemyhealth[u] = heroes[u].health
        minenemyhealth = min(enemyhealth)
        for v in range(0, len(heroes)):
            if enemyhealth[v] == minenemyhealth:
                break

        if minpolyhealth < 30 and minenemyhealth >= 30:
            if minenemydis < 500:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - heroes[n].position[0]),
                    hero.position[1] +
                    (hero.position[1] - heroes[n].position[1]))
                self.shoot_at(*heroes[n].position)
            elif minpolydis < 150:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - polygons[k].position[0]),
                    hero.position[1] +
                    (hero.position[1] - polygons[k].position[1]))
                self.shoot_at(*polygons[k].position)
            else:
                self.accelerate_towards(*polygons[g].position)
                self.shoot_at(*polygons[g].position)
        if minenemyhealth < 30 and minpolyhealth >= 30:
            if minenemydis < 500:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - heroes[n].position[0]),
                    hero.position[1] +
                    (hero.position[1] - heroes[n].position[1]))
                self.shoot_at(*heroes[n].position)
            elif minpolydis < 150:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - polygons[k].position[0]),
                    hero.position[1] +
                    (hero.position[1] - polygons[k].position[1]))
                self.shoot_at(*polygons[k].position)
            else:
                self.accelerate_towards(*heroes[v].position)
                self.shoot_at(*heroes[v].position)
        if minenemyhealth >= 30 and minenemyhealth >= 30:
            if minenemydis < 500:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - heroes[n].position[0]),
                    hero.position[1] +
                    (hero.position[1] - heroes[n].position[1]))
                self.shoot_at(*heroes[n].position)
            if (maxenemylv - hero.level) >= 5:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - heroes[r].position[0]),
                    hero.position[1] +
                    (hero.position[1] - heroes[r].position[1]))
                self.shoot_at(*heroes[r].position)
            if (maxenemylv - hero.level) < 5:
                self.accelerate_towards(*heroes[r].position)
                self.shoot_at(*heroes[r].position)
            if minpolydis >= 150:
                self.accelerate_towards(*polygons[k].position)
                self.shoot_at(*polygons[k].position)
            if minpolydis < 150:
                self.accelerate_towards(
                    hero.position[0] +
                    (hero.position[0] - polygons[k].position[0]),
                    hero.position[1] +
                    (hero.position[1] - polygons[k].position[1]))
                self.shoot_at(*heroes[s].position)

    def upgrate_(self, hero, heroes, polygons, bullets):
        if hero.abilities.max_health.level == hero.abilities.health_regen.level:
            a = random.randint(0, 1)
            if a == 0:
                self.level_up(Ability.MaxHealth)
            elif a == 1:
                self.level_up(Ability.HealthRegen)
        if hero.abilities.max_health.level < hero.abilities.health_regen.level:
            self.level_up(Ability.MaxHealth)
        if hero.abilities.max_health.level > hero.abilities.health_regen.level:
            self.level_up(Ability.HealthRegen)
        if hero.abilities.max_health.level == 8 and hero.abilities.health_regen.level == 8:
            if hero.abilities.movement_speed.level == hero.abilities.reload.level:
                b = random.randint(0, 1)
                if b == 0:
                    self.level_up(Ability.MovementSpeed)
                elif b == 1:
                    self.level_up(Ability.Reload)
            if hero.abilities.movement_speed.level < hero.abilities.reload.level:
                self.level_up(Ability.MovementSpeed)
            if hero.abilities.movement_speed.level > hero.abilities.reload.level:
                self.level_up(Ability.Reload)
        if hero.abilities.movement_speed.level == 8 and hero.abilities.reload.level == 8:
            if hero.abilities.bullet_speed.level == hero.abilities.bullet_damage.level:
                c = random.randint(0, 1)
                if c == 0:
                    self.level_up(Ability.BulletSpeed)
                elif c == 1:
                    self.level_up(Ability.BulletDamage)
            if hero.abilities.bullet_speed.level < hero.abilities.bullet_damage.level:
                self.level_up(Ability.BulletSpeed)
            if hero.abilities.bullet_speed.level > hero.abilities.bullet_damage.level:
                self.level_up(Ability.BulletDamage)
        if hero.abilities.bullet_speed.level == 8 and hero.abilities.bullet_damage.level == 8:
            if hero.abilities.body_damage.level == hero.abilities.bullet_penetration.level:
                d = random.randint(0, 1)
                if d == 0:
                    self.level_up(Ability.BodyDamage)
                elif d == 1:
                    self.level_up(Ability.BulletPenetration)
            if hero.abilities.body_damage.level < hero.abilities.bullet_penetration.level:
                self.level_up(Ability.BodyDamage)
            if hero.abilities.body_damage.level > hero.abilities.bullet_penetration.level:
                self.level_up(Ability.BulletPenetration)
        #if hero.abilities.reload.level == 4 and hero.abilities.bullet_penetration.level == 4:
        #    e = random.randint(0,7)
        #    if e == 0:
        #        self.level_up(Ability.HealthRegen)
        #    if e == 1:
        #        self.level_up(Ability.MaxHealth)
        #    if e == 2:
        #        self.level_up(Ability.BodyDamage)
        #    if e == 3:
        #        self.level_up(Ability.BulletSpeed)
        #    if e == 4:
        #        self.level_up(Ability.BulletPenetration)
        #    if e == 5:
        #        self.level_up(Ability.BulletDamage)
        #    if e == 6:
        #        self.level_up(Ability.Reload)
        #    if e == 7:
        #        self.level_up(Ability.MovementSpeed)


Client.main()
