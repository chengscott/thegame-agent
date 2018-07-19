from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):

    def init(self):
        self.name = '456789' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):

        import random

        if hero.abilities.bullet_speed.level < 4 :
            self.accelerate_towards(0,400)
            if polygons:
                self.shoot_at(*polygons[0].position)
            
            if heroes:
                self.shoot_at(*heroes[0].position)


            if hero.abilities.health_regen.level <=4:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.bullet_damage.level <= 4:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.bullet_speed.level <= 4:
                self.level_up(Ability.BulletSpeed)
            elif hero.abilities.body_damage.level <= 6:
                self.level_up(Ability.BodyDamage)
            elif hero.abilities.reload.level <= 4:
                self.level_up(Ability.Reload)
            elif hero.abilities.max_health.level <= 4:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.movement_speed.level <= 4:
                self.level_up(Ability.MovementSpeed)
            elif hero.abilities.bullet_penetration.level <= 4:
                self.level_up(Ability.BulletPenetration)
            else:
                self.level_up(Ability.HealthRegen)
                self.level_up(Ability.BulletSpeed)
                self.level_up(Ability.MaxHealth)
                self.level_up(Ability.BulletDamage)
                self.level_up(Ability.BodyDamage)
                self.level_up(Ability.MovementSpeed)
                self.level_up(Ability.BulletPenetration)
                self.level_up(Ability.Reload)

        else:
        
        
            if hero.abilities.health_regen.level <=4:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.body_damage.level <= 3:
                self.level_up(Ability.BodyDamage)
            elif hero.abilities.bullet_damage.level <= 4:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.bullet_speed.level <= 4:
                self.level_up(Ability.BulletSpeed)
            elif hero.abilities.reload.level <= 4:
                self.level_up(Ability.Reload)
            elif hero.abilities.body_damage.level <= 6:
                self.level_up(Ability.BodyDamage)
            elif hero.abilities.bullet_penetration.level <= 4:
                self.level_up(Ability.BulletPenetration)
            elif hero.abilities.max_health.level <= 4:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.movement_speed.level <= 4:
                self.level_up(Ability.MovementSpeed)
            else:
                self.level_up(Ability.HealthRegen)
                self.level_up(Ability.BulletSpeed)
                self.level_up(Ability.MaxHealth)
                self.level_up(Ability.BulletDamage)
                self.level_up(Ability.BodyDamage)
                self.level_up(Ability.MovementSpeed)
                self.level_up(Ability.BulletPenetration)
                self.level_up(Ability.Reload)





            if heroes:
                self.shoot_at(*heroes[0].position)

                if heroes[0].abilities.bullet_damage.value > hero.abilities.bullet_damage.value:
                    self.accelerate_towards(5000,4000)
                else:
                    for x in range (0,100):
                        self.shoot_at(*heroes[0].position)
                        self.accelerate_towards(*heroes[0].position)


            else:
                for x in range (0,15):
                    self.shoot_at(*polygons[0].position)















Client.main()
