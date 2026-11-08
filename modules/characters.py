from modules.library import Library

Characters = {
    "Mr. White" : {
        "Coins" : 100,
        "Health" : 100,

        "Attacks" : {
            "THE ONE WHO KNOCKS" : {
                "Type" : "Normal",
                "CD" : 0
            },
        }
    },

    "Sheldon (Young)" : {
        "Coins" : 0,
        "Health" : 25,

        "Attacks" : {
            "The Ultimate Weapon" : {
                "Type" : "Normal",
                "CD" : 1
            },

            "you dawg" : {
                "Type" : "Normal",
                "CD" : 0
            }
        }
    }
}



class Player_Character:
    def __init__(self, CharacterName : str):
        if not CharacterName in Characters: 
            print(f"Invalid Character : {CharacterName}")
            return

        Character = Characters[CharacterName]

        self.Name = CharacterName
        self.Health = Character["Health"]
        self.MaxHealth = Character["Health"]
        self.Attacks = Character["Attacks"]

        self.Icon = Library["assets"]["Characters"][CharacterName]["PFP.png"].convert_alpha()
        self.Drawing = Library["assets"]["Characters"][CharacterName]["Back View.png"].convert_alpha()
        self.HealthIcon = Library["assets"]["UI"]["HP.png"].convert_alpha()

        self.OriginActionWheel = Library["assets"]["UI"]["Action Wheel.png"].convert_alpha()
        self.ActionWheel = self.OriginActionWheel

        self.Folder = Library["assets"]["Characters"][CharacterName]

        self.Stances = {
            "Idle" : self.Folder["Back View.png"].convert_alpha(),
        }
        
        self.WheelTarget = "Attack"

    def TakeDamage(self, Damage : int):
        self.Health -= Damage

        if self.Health < 0:
            self.Health = 0


class Stock_Guy:
    def __init__(self):
        self.Name = "Stock Guy"
        self.Health = 100
        self.MaxHealth = 100

        self.Drawing = Library["assets"]["Stock Guy"]["Idle.png"].convert_alpha()
        self.Attacks = {
            "Stock Market Crash" : {
                "Type" : "Normal",
                "CD" : 0
            }
        }

        self.Folder = Library["assets"]["Stock Guy"]
                
        self.Stances = {
            "Idle" : self.Folder["Idle.png"].convert_alpha(),
        }
