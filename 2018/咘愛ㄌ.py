from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import random
import math


def destination(a, b):
    return ((a.position[0] - b.position[0])**2 +
            (a.position[1] - b.position[1])**2)**0.5


def win_hero(h, e):
    return h.health / (e.body_damage + e.bullet_damage) > e.health / (
        h.body_damage + h.bullet_damage)


def win_polygon(h, p):
    return h.health / p.body_damage > p.health / h.body_damage


def arc(h, e):
    if h.position[1] == e.position[1]:
        if e.position[0] > h.position[0]:
            return 0
        else:
            return math.pi
    elif e.position[1] < h.position[1]:
        return 720 * math.pi / math.atan(e.position[1] - h.position[1]) / (
            e.position[0] - h.position[0])
    else:
        return math.pi * 2 - 720 * math.pi / math.atan(
            e.position[1] - h.position[1]) / (e.position[0] - h.position[0])


class Client(HeadlessClient):
    def init(self):
        self.name = '咘愛ㄌ'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print('-' * 79)

        is_moving = False

        # Ability
        if hero.health_regen_level < 6 and hero.body_damage_level < 6:
            if hero.body_damage_level < hero.health_regen_level:
                self.level_up(Ability.BodyDamage)
            else:
                self.level_up(Ability.HealthRegen)
        elif hero.max_health_level < 4 and hero.movement_speed_level < 4:
            if hero.max_health_level < hero.movement_speed_level:
                self.level_up(Ability.MaxHealth)
            else:
                self.level_up(Ability.MovementSpeed)
        elif hero.reload_level < 4 and hero.bullet_speed_level < 4:
            if hero.reload_level < hero.bullet_speed_level:
                self.level_up(Ability.Reload)
            else:
                self.level_up(Ability.BulletSpeed)
        else:
            self.level_up(Ability.BodyDamage)
            self.level_up(Ability.HealthRegen)
            self.level_up(Ability.BulletPenetration)
            self.level_up(Ability.BulletDamage)
            self.level_up(Ability.MovementSpeed)
            self.level_up(Ability.Reload)
            self.level_up(Ability.BulletSpeed)
            self.level_up(Ability.MaxHealth)

        # if shooted
        if bullets:
            enemy = None
            for h in heroes:
                if destination(hero, h) < hero.radius:
                    enemy = h
                    break
            if not enemy:
                for b in bullets:
                    if destination(hero, b) < hero.radius:
                        enemy = heroes[0]
                        for h in heroes:
                            if destination(hero, h) < enemy.radius:
                                enemy = h
            if enemy:
                if win_hero(hero, enemy):
                    self.accelerate(arc(hero, enemy))
                else:
                    self.accelerate(
                        (arc(hero, enemy) + math.pi / 2) % (math.pi * 2))
                self.shoot_at(*enemy.position)
                print('enemy', enemy.name, enemy.position)
                is_moving = True
        # enemy around
        if heroes and not is_moving:
            loser = None
            for h in heroes:
                if win_hero(hero, h):
                    if (
                            not loser
                    ) or h.rewarding_experience > loser.rewarding_experience:
                        loser = h
            if loser:
                self.accelerate_towards(*loser.position)
                self.shoot_at(*loser.position)
                print('loser(x, y): ', int(loser.position[0]),
                      int(loser.position[1]), 'health: ', loser.health,
                      hero.health)
                is_moving = True
        # Polygons around
        elif polygons and not is_moving:
            target = None
            for p in polygons:
                if win_polygon(hero, p):
                    if (
                            not target
                    ) or p.rewarding_experience > target.rewarding_experience:
                        target = p
            if target:
                self.accelerate_towards(*target.position)
                self.shoot_at(*target.position)
                print('polygons', target.position)
            else:
                if destination(hero, polygons[0]) < 1.5 * hero.radius:
                    self.accelerate_towards(*polygons[0].position)
                self.shoot_at(*polygons[0].position)
            is_moving = True

        if not is_moving:
            a = random.randint(0, 6)
            x = random.randint(0, 300)
            y = random.randint(0, 300)

            print('no')
            self.accelerate(a)
            self.shoot_at(x, y)


Client.main()
