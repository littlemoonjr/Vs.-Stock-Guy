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

    "Sheldon Cooper (Young)" : {
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

        self.Folder = Library["assets"]["Characters"][CharacterName]

        self.Stances = {
            "Idle" : self.Folder["Back View.png"].convert_alpha(),
        }


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
