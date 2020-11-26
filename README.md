## lol_event_api

	version 0.1.0

A samll crawler to wanplus.com, you can use this api to search all the teams and players information and performance in lol competitions, and this api is strictly prohibited for commercial use.

### Getting Started
installation via pip:

```
pip install loleventdata
```
### Functions
(1) search all the competitions
(2) search all the teams info
(3) search all the players info
(4) search all the team performance in special competition
(5) search all the players performance in special competition

### Notifications
The item is for entertainment only.

### Docs
#### get_competitions
Get all the competitions. Return a dict object.
Usages:
```
	import loleventdata
        competitions = loleventdata.get_competitions()
```
#### get_team_competition_info
Get all the teams in the specific Competition. Returns a dict object.
Params:

    eventname: the name of competition, you can get it from get_competitions

Usage:
```
	import loleventdata
	team_info = loleventdata.get_team_competition_info(eventname)
```

#### get_team_performance

Get all the team's data in the specific Competition. Returns a dict object.
Params:
```
	eventname: the name of competition, you can get it from get_competitions
```
Usage:
```
	import loleventdata
	team_performance = loleventdata.get_team_performance(eventname)
```
#### get_player_competition_info
Get all the players in the specific Competition. Returns a dict object.
Params:

	eventname: the name of competition, you can get it from get_competitions
	meta: default is all, you can input 'top','jun','mid','adc','sup'

Usage:

	import loleventdata
	player_info = loleventdata.get_player_competition_info(eventname,meta)


#### get_player_performance
Get all the player's data in the specific Competition. Returns a dict object.
Params:

	eventname: the name of competition, you can get it from get_competitions
	meta: default is all, you can input 'top','jun','mid','adc','sup'

Usage:

	import loleventdata
	player_performance = loleventdata.get_player_performance_info(eventname,meta)
