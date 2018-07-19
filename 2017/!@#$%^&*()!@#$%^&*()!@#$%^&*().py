from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
from math import atan2, sin, cos
import random


class Client(GuiClient):

    def init(self):
        self.name = "!@#$%^&*()!@#$%^&*()!@#$%^&*()"
        #self.name = "t1"
        #self.name = "Dark Souls IV"
        #self.upgrade_order = [1, 1, 1, 1, 5, 5, 5, 6, 6, 6, 1, 1, 1, 1, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 3, 3, 3, 3, 3, 3, 3, 3]
        #self.upgrade_order = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 7, 7, 7, 7, 2, 2, 2, 2, 7, 7, 7, 7, 5, 5, 6, 6, 5, 5, 6, 6]
        self.upgrade_order = [
        {
        7 : 2,
        }, {
        0 : 4,
        1 : 4,
        2 : 6,
        }, {
        0 : 8,
        1 : 8,
        2 : 8,
        7 : 8,
        }, {
        6 : 8,
        }, {
        5 : 8,
        }, {
        4 : 8,
        }, {
        0 : 8,
        1 : 8,
        2 : 8,
        3 : 8,
        4 : 8,
        5 : 8,
        6 : 8,
        7 : 8,
        }]
        self.aggressive = 1
        self.coward = 0
        self.mode = 0 # 0->poly, 1->tank, 2->bullet, 3->pri
        self.count = 0
        self.force = 0
        self.lastforcedir = [0, 0]
        self.polynear = 0
        self.regenerating = 1
        self.prehealth = 0

    def get_level(self, hero):
        level = 1
        level += hero.health_regen_level
        level += hero.max_health_level
        level += hero.body_damage_level
        level += hero.bullet_speed_level
        level += hero.bullet_penetration_level
        level += hero.bullet_damage_level
        level += hero.reload_level
        level += hero.movement_speed_level
        return level

    def get_dis_and_safe(self, hero, target, delta):
        dis = self.get_dis(hero, target)
        safedis = dis - hero.radius - target.radius
        if safedis < 0:
            safedis = 0
        return [dis, safedis - delta]

    def get_vec(self, hero, target):
        dx = target.position[0] - hero.position[0]
        dy = target.position[1] - hero.position[1]
        return [dx, dy]

    def get_dis(self, hero, target):
        vec = self.get_vec(hero, target)
        dis = (vec[0]**2 + vec[1]**2)**0.5
        return dis

    def action(self, hero, heroes, polygons, bullets):
        '''
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        '''
        # self.count += 1
        hx = hero.position[0]
        hy = hero.position[1]
        self.regenerating = 0
        self.prehealth = hero.health
        #Change Mood
        if hero.level < 20:
            if hero.health < hero.max_health // 2:
                self.aggressive = 0
            else:
                self.aggressive = 1
        else:
            if hero.health < hero.max_health // 2: # no need to poly
                self.aggressive = 0
            else:
                self.aggressive = 1
        #Upgrade
        if hero.skill_points:
            for upgrade_list in self.upgrade_order:
                out = 0
                for key in upgrade_list.keys():
                    if hero.abilities[Ability(key)].level < upgrade_list[key]:
                        print('lv up:', Ability(key))
                        self.level_up(Ability(key))
                        out = 1
                        break
                if out:
                    break
        #Wait
        if self.force:
            self.force -= 1
            print('force:', self.force, ',f:', self.lastforcedir)
            self.accelerate_towards(*self.lastforcedir)
            return
        #Shoot
        target_poly = None
        target_tank = None
        target_bullet = None
        #init
        self.coward = 0
        self.polynear = 0
        ## Heroes
        if heroes:
            nearest_powdis = 100000000
            nearest_lhp = heroes[0]
            health_delta = 40
            for h in heroes:
                dx = h.position[0] - hx
                dy = h.position[1] - hy
                powdis = dx**2 + dy**2
                if powdis + h.health * health_delta < nearest_powdis:
                    nearest_powdis = powdis + h.health * health_delta
                    nearest_lhp = h
            target_tank = nearest_lhp
            if hero.level > 20:
                if hero.health < hero.max_health // 2 or hero.health < target_tank.health or hero.body_damage_level < target_tank.body_damage_level:
                    self.coward = 1
                elif hero.level > target_tank.level - 2:
                    self.coward = 0
                else:
                    self.coward = 1
            else:
                if hero.health < hero.max_health / 3 * 2 or hero.health < target_tank.health or hero.body_damage_level < target_tank.body_damage_level:
                    self.coward = 1
                elif hero.level > target_tank.level + 2:
                    self.coward = 0
                else:
                    self.coward = 1
            if self.coward:
                self.shoot_at(*target_tank.position)
            else:
                vec = self.get_vec(hero, target_tank)
                self.shoot_at(hx - vec[0], hy - vec[1])
        ## Polygons
        if polygons:
            nearest_powdis = 100000000
            nearest_lhp = polygons[0]
            health_delta = 40
            for p in polygons:
                dx = p.position[0] - hx
                dy = p.position[1] - hy
                powdis = dx**2 + dy**2
                if powdis + p.health * health_delta < nearest_powdis:
                    nearest_powdis = powdis + p.health * health_delta
                    nearest_lhp = p
            if target_tank == None:
                target_poly = nearest_lhp
                self.shoot_at(*target_poly.position)
            elif nearest_lhp and (nearest_powdis - nearest_lhp.health * health_delta) ** 0.5 < nearest_lhp.radius + hero.radius + 20:
                target_poly = nearest_lhp
                #self.polynear = 1 #Bug??
        ## Bullets
        if bullets:
            if hero.level < 20:
                nearest_powdis = 100000000
                nearest_hhp = None
                for b in bullets:
                    vx = b.velocity[0]
                    vy = b.velocity[1]
                    powvel = vx**2 + vy**2
                    hvx = hero.velocity[0]
                    hvy = hero.velocity[1]
                    powhvel = hvx**2+hvy**2
                    if b.owner_id == hero.id or powvel < powhvel:
                        continue
                    health_delta = 40
                    dx = hx - b.position[0]
                    dy = hy - b.position[1]
                    # print(atan2(dy, dx), atan2(b.velocity.y, b.velocity.x))
                    ddd = abs(atan2(dy, dx) - atan2(b.velocity.y, b.velocity.x))
                    if ddd > 3.14159:
                        ddd = 6.283 - ddd
                    if ddd < 10 * 3.14159 / 180:
                        powdis = dx**2 + dy**2
                        if powdis < nearest_powdis - b.body_damage * health_delta:
                            nearest_powdis = nearest_powdis - b.body_damage * health_delta
                            nearest_hhp = b
                target_bullet = nearest_hhp
        #Move
        prioritized = [0, 0]
        if hero.position.x < 200 + random.randint(0, 20):
            prioritized[0] = 1
        if hero.position.y < 200 + random.randint(0, 20):
            prioritized[1] = 1
        if hero.position.x > 4800 + random.randint(-20, 0):
            prioritized[0] = -1
        if hero.position.y > 3800 + random.randint(-20, 0):
            prioritized[1] = -1
        if (self.coward or self.regenerating) and prioritized[0] != 0 or prioritized[1] != 0:
            #if self.mode != 3:
            #    self.mode = 3
            print(self.count, 'pri mode')
            self.force = 60
            self.lastforcedir = [hx + prioritized[0] * 1000, hy + prioritized[1] * 1000]
            self.accelerate_towards(*self.lastforcedir)
        elif (self.coward or self.regenerating) and target_bullet:
            if self.mode != 2:
                self.mode = 2
                print(self.count, 'bullet mode')
                # print(target_bullet.body_damage)
            vec = self.get_vec(hero, target_bullet)
            bvec = target_bullet.velocity
            orientation = atan2(vec[1], vec[0])
            normal = orientation + 90 / 180 * 3.14159
            print(normal * 180 / 3.14159)
            self.accelerate_towards(cos(normal) * 1000, sin(normal) * 1000)
            # if(hero.position[1] > 2000 + random.randint(-100, 100) and bvec[0] > 0):
                # self.accelerate_towards(hx + bvec[1], hy - bvec[0])
            # else:
                # self.accelerate_towards(hx - bvec[1], hy + bvec[0])
        else:
            if target_tank:
                #if self.mode != 1:
                #    self.mode = 1
                print(self.count, 'tank mode:', self.coward)
                vec = self.get_vec(hero, target_tank)
                if self.coward or self.regenerating:
                    self.accelerate_towards(hx - vec[0], hy - vec[1])
                elif target_tank.bullet_damage_level > hero.level / 5:
                    tx = hx + vec[0]
                    ty = hy + vec[1]
                    dis = (vec[0]**2 + vec[1]**2) ** 0.5
                    ddd = atan2(vec[1], vec[0])
                    if ddd > 3.14159:
                        ddd = 6.283 - ddd
                    orientation = ddd - 30 / 180 * 3.14159
                    self.accelerate_towards(dis * cos(orientation), dis * sin(orientation))
                else:
                    self.accelerate_towards(hx + vec[0], hy + vec[1])
            elif target_poly:
                #if self.mode != 0:
                #    self.mode = 0
                print(self.count, 'poly mode:', self.aggressive)
                dis_and_safe = self.get_dis_and_safe(hero, target_poly, 5)
                vec = self.get_vec(hero, target_poly)
                if self.aggressive and not self.regenerating:
                    # vec[0] *= dis_and_safe[1] / dis_and_safe[0]
                    # vec[1] *= dis_and_safe[1] / dis_and_safe[0]
                    self.accelerate_towards(hx + vec[0], hy + vec[1])
                else:
                    self.accelerate_towards(hx - vec[0], hy - vec[1])
        # Dodge Bullet when Cowarding
        '''
        if (self.coward or not self.aggressive) and self.polynear:
            if target_tank:
                vec = self.get_vec(hero, target_tank)
                orientation = atan2(vec[1], vec[0])
                vec = self.get_vec(target_poly, hero)
                orientation2 = atan2(vec[1], vec[0])
                ddd = abs(orientation - orientation2)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                print('dodge poly if:', ddd * 180 / 3.14159)
                if ddd > 3.14159:
                    ddd = 6.283 - ddd
                if ddd > 20 / 180 * 3.14159:
                    print ('dodge poly when avoiding t')
                    self.accelerate_towards(hx - vec[0], hy - vec[1])
                    '''


Client.main()
