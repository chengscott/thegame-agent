from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient

import math
import collections
import random
import itertools
import bisect


class Client(GuiClient):

    skills_to_learn = [
        (1, [Ability.HealthRegen]),
        (4, [Ability.Reload]),
        (2, [Ability.BulletSpeed]),
        (8, [Ability.Reload]),
        (4, [Ability.BulletSpeed]),
        (2, [Ability.MaxHealth]),
        (8, [Ability.BulletDamage, Ability.HealthRegen, Ability.BulletPenetration]),
        (8, range(8))
    ]

    def level_skill(self, hero):
        for target_level, skills in self.skills_to_learn:
            skill = min(skills, key=lambda s: hero.abilities[s].level)
            if hero.abilities[skill].level < target_level:
                self.level_up(skill)
                break

    def init(self):
        self.name = 'Jerry'
        self.shots = collections.Counter()
        self.last_shot = 0
        self.last_count = 0
        self.last_target_shots = 1

    def distance(self, d):
        x, y = d.position
        return math.hypot(self._hero.position.x - x, self._hero.position.y - y)

    def shoot_object(self, target):
        hero = self._hero
        x = target.position.x - hero.position.x
        y = target.position.y - hero.position.y
        phi = math.atan2(target.velocity.y, target.velocity.x) - math.atan2(y, x)
        u = math.hypot(target.velocity.y, target.velocity.x)
        v = hero.bullet_speed
        if u < v:
            theta0 = math.asin(u/v*math.sin(phi))
            theta1 = -math.asin(u/v*math.sin(phi))+math.pi
            self.shoot(math.atan2(y, x)+theta0)

    def shots_to_kill(self, target):
        damaging_ticks = math.ceil(
            self._hero.bullet_penetration / target.body_damage)
        damage_per_bullet = self._hero.bullet_damage * damaging_ticks
        return math.ceil(target.health / damage_per_bullet)

    def ticks_to_kill(self, target):
        ticks_to_kill = self.shots_to_kill(target) * self._hero.reload
        travel_ticks = self.distance(target) / self._hero.bullet_speed
        return travel_ticks + ticks_to_kill

    def cp(self, target):
        ttk = self.ticks_to_kill(target)
        if ttk > 600:
            return 0
        return target.rewarding_experience / self.ticks_to_kill(target)

    def get_shoot_target(self, hero, polygons, heroes, bullets):
        heroes = [h for h in heroes if math.hypot(h.velocity.y, h.velocity.x) < hero.bullet_speed * 0.9]
        bullets = [b for b in bullets if b.owner_id != hero.id]

        targets = sorted(
            itertools.chain(
                # polygons,
                heroes,
                bullets
            ),
            key=self.distance
        )
        if targets and self.distance(targets[0]) < 200:
            return targets[0]

        targets = sorted(
            itertools.chain(heroes, polygons),
            key=self.cp,
            reverse=True,
        )
        for target in targets:
            if self.last_shot == target.id:
                if self.last_count < self.last_target_shots:
                    self.last_count += not hero.cooldown
                    if not hero.cooldown:
                        print(self.last_count, self.last_target_shots)
                    return target
            else:
                self.last_target_shots = self.shots_to_kill(target)
                self.last_shot = target.id
                self.last_count = not hero.cooldown
                if not hero.cooldown:
                    print(self.last_count, self.last_target_shots)
                return target

    def move(self, hero, polygons, heroes, bullets):
        objects = sorted(
            itertools.chain(
                heroes,
                polygons,
                (bullet for bullet in bullets if bullet.owner_id != hero.id),
            ),
            key=self.distance
        )

    def action(self, hero, polygons, heroes, bullets):

        self.x, self.y = hero.position

        def distance(p):
            px, py = p.position
            hx, hy = hero.position
            return math.hypot(px - hx, py - hy)

        shoot_at = self.get_shoot_target(hero, polygons, heroes, bullets)
        if shoot_at is not None:
            self.shoot_object(shoot_at)

        self.level_skill(hero)


        if polygons:
            shoosss = min(polygons, key = lambda s : math.hypot(s.position.x - hero.position.x, s.position.y - hero.position.y))
            if(shoosss.edges != 5):
                if hero.health > (hero.max_health)/2:
                    self.accelerate_towards(*shoosss.position)
            else:
                self.accelerate_towards(random.randint(0,5000), random.randint(0,4000))
        else:
            self.accelerate_towards(random.randint(0,5000), random.randint(0,4000))

        if heroes:
            hero_short = min(heroes, key = lambda s : math.hypot(s.position.x - hero.position.x, s.position.y - hero.position.y))
            pos = (hero_short.position.x - hero.position.x, hero_short.position.y - hero.position.y)
            if hero_short.score <= hero.score - 500 and hero.health - 500 > hero_short.health:
                self.accelerate_towards(*hero_short.position)
            else:
                self.accelerate(math.atan2(pos[1], pos[0])+math.pi*0.7)

Client.main()
