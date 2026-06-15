# Main Script
```lua
getgenv().Nixus = {
    autoskip = false,
    SellAllTower = false,
    AtWave = 50,
    Modifiers = {"Glass", "HiddenEnemies", "ExplodingEnemies", "Limitation", "Commited"},
    AutoAbilities = true,
    AutoRewards = false,
    macroURL = "https://raw.githubusercontent.com/QuangN123/tds/refs/heads/main/strat.txt",
    Webhook = "",
    replay = true,
    Gamemode = "Survival",
    Map = "U-Turn",
    Difficulty = "Frost",
    Loadout = {"Cowboy", "Engineer", "EvolvedJuggernaut", "DJ Booth", "Hacker"}
}
loadstring(game:HttpGet("https://raw.githubusercontent.com/2xrW/returnhub-output/refs/heads/main/TDS"))()
```
> [!Note]
> You have to upgrade juggernaut and hacker manually once there are 2 paths otherwise it'll skip the upgrades.
> Top path juggernaut for flying detection and bottom path hacker for 2 min dupe. 
> You also have to clone towers yourself. Clone 2 engi first, then once cd ends clone juggernaut and an engi.
> You can skip waves 20-40 (28/29 is risky)

> [!Warning]
> Skip wave 6 at :25 or you will lose
