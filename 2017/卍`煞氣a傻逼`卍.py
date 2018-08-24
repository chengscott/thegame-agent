from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '卍`煞氣a傻逼`卍'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        '''
        if bullets:
            for q in range(0,len(bullets)):
                self.accelerate_towards(5000-bullets[q].position[0],4000-bullets[q].position[0])
        '''
        if polygons:
            '''
            if hero.health>=hero.abilities.max_health.value/2:   
                if hero.abilities.health_regen.level<4:
                    i=0
                    while polygons[i].body_damage>20:
                        self.accelerate_towards(polygons[i].position[0],polygons[i].position[0])
                        i=i+1
                else:
                    for t in range(0,len(polygons)):
                        if polygons[t].body_damage>19:
                            self.accelerate_towards(polygons[t].position[0],polygons[t].position[0])
            '''

            self.shoot_at(polygons[0].position[0], polygons[0].position[1])
            if polygons[0].health < hero.health:
                if hero.health >= hero.abilities.max_health.value / 2:
                    self.accelerate_towards(*polygons[0].position)
                else:
                    self.shoot_at(polygons[0].position[0],
                                  polygons[0].position[1])
            else:
                self.shoot_at(polygons[4].position[0], polygons[4].position[1])

        if hero.level >= 15:
            if heroes:
                self.shoot_at(heroes[0].position[0], heroes[0].position[1])
                if heroes[0].health < hero.health:
                    self.accelerate_towards(*heroes[0].position)
                else:
                    self.accelerate_towards(5000 - heroes[0].position[0],
                                            4000 - heroes[0].position[1])
        else:
            if heroes:
                self.shoot_at(heroes[0].position[0], heroes[0].position[1])
                self.accelerate_towards(5000 - heroes[0].position[0],
                                        4000 - heroes[0].position[1])

        if hero.abilities.health_regen.level != 8:
            self.level_up(Ability.HealthRegen)
        else:
            if hero.abilities.health_regen.level == 8:
                self.level_up(Ability.MaxHealth)
                if hero.abilities.max_health.level == 8:
                    self.level_up(Ability.Reload)
                    if hero.abilities.reload.level == 8:
                        self.level_up(Ability.BodyDamage)
                        if hero.abilities.body_damage.level == 8:
                            if hero.abilities.movement_speed.level <= 5:
                                self.level_up(Ability.MovementSpeed)
                            else:
                                self.level_up(Ability.BulletDamage)
                                if hero.abilities.bullet_damage.level == 8:
                                    self.level_up(Ability.BulletSpeed)
                                    if hero.abilities.bullet_speed.level == 8:
                                        self.level_up(
                                            Ability.BulletPenetration)


Client.main()
