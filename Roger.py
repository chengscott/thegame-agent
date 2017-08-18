from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient

import math
import cmath
import itertools
from thegame.entity import Vector


class VirtualEnemy:
    body_damage = float('inf')
    health = float('inf')
    rewarding_experience = 0
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)


class Client(HeadlessClient):

    skills_to_learn = [
        (4, [Ability.HealthRegen]),
        (2, [Ability.BodyDamage, Ability.MovementSpeed, Ability.MaxHealth]),
        (8, [Ability.HealthRegen]),
        (8, [Ability.MovementSpeed]),
        (8, [Ability.BodyDamage, Ability.MaxHealth]),
        (8, Ability)
    ]

    def init(self):
        self.name = 'Roger'

    def virtual_enemies(self):
        for x in range(-200, 5401, 400):
            yield VirtualEnemy(x, -200)
            yield VirtualEnemy(x, 4200)
        for y in range(0, 4200, 400):
            yield VirtualEnemy(-200, y)
            yield VirtualEnemy(5200, y)

    def tick_to_arrival(self, target):
        x, y = target.position
        dx = x - self._hero.position.x
        dy = y - self._hero.position.y
        theta = math.atan2(dy, dx)
        vtx = self._hero.movement_speed * math.cos(theta)
        vty = self._hero.movement_speed * math.sin(theta)
        vcx, vcy = self._hero.velocity
        return (math.hypot(dx, dy) + math.hypot(
            vcx - vtx, vcy - vty) * 10) / self._hero.movement_speed

    def tick_to_recover(self, target):
        if not self._hero.health_regen:
            return 0
        tick_to_kill = math.ceil(target.health / self._hero.body_damage)
        received_damage = tick_to_kill * target.body_damage
        return math.ceil(received_damage / self._hero.health_regen)

    def ncp(self, target):
        return -target.rewarding_experience / (
            self.tick_to_arrival(target) + self.tick_to_recover(target) + 0.1)

    def level_skill(self, hero):
        for target_level, skills in self.skills_to_learn:
            skill = min(skills, key=lambda s: hero.abilities[s].level)
            if hero.abilities[skill].level < target_level:
                self.level_up(skill)
                break

    def accelerate_to(self, x, y):
        hx, hy = self._hero.position
        vx, vy = self._hero.velocity
        angle = math.atan2(y - hy, x - hx)
        vangle = math.atan2(vy, vx)
        mult = -math.sin(vangle - angle)
        ang = math.atan2(
                mult * math.sin(angle + math.pi / 2) + math.sin(angle),
                mult * math.cos(angle + math.pi / 2) + math.cos(angle),
        )
        self.accelerate(ang)
        self.shoot(ang + math.pi)

    def action(self, hero, polygons, heroes, bullets):

        def distance(p):
            px, py = p.position
            hx, hy = hero.position
            return math.hypot(px - hx, py - hy)
        target = min([h for h in heroes if h.health * h.body_damage < (hero.health - hero.max_health * 0.3) * hero.body_damage], default=None, key=self.ncp)
        if target is None and polygons:
            target = min([h for h in polygons if h.health * h.body_damage < (hero.health - hero.max_health * 0.3) * hero.body_damage], default=None, key=self.ncp)
        aggressive = False
        if target is not None:
            if (hero.health > hero.max_health * 0.8 or
                (hero.health > hero.max_health * 0.3 and hero.health_regen_cooldown)
            ):
                self.accelerate_to(*target.position)
                aggressive = True
            else:
                self.shoot_at(*target.position)
        def angle(p):
            px, py = p.position
            hx, hy = hero.position
            return math.atan2(py - hy, px - hx)
        if not aggressive:
            enemies = sorted(
                itertools.chain(
                    heroes,
                    [b for b in bullets if b.owner_id != hero.id],
                    polygons,
                    # self.virtual_enemies(),
                ),
                key=distance
            )
            if not enemies:
                self.accelerate_to(2500, 2000)
            else:
                first, *remaining = enemies
                firstd = distance(first)
                ecount = 1
                eangle = angle(first)
                for enemy in remaining:
                    if distance(enemy) < firstd * 1.2:
                        ecount += 1
                        eangle += 2
                    else:
                        break
            for enemy in enemies:
                if distance(enemy) > 400:
                    break
                ecount += 1
                eangle += angle(enemy)
                self.accelerate(eangle / ecount + math.pi)

        self.level_skill(hero)



Client.main()
