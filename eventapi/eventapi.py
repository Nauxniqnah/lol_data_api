import call_api

meta_dict = {'top': '上单', 'jun': '打野', 'adc': 'ADC', 'sup': '辅助', 'mid': '中单'}


def get_competitions():
    competitions = []
    data = call_api.send_team_post("2020NEST全国电子竞技大赛")
    temp = {'eid': '', 'name': '', 'eventtype': ''}
    for key in data['eventList'].keys():
        temp['eid'] = data['eventList'][key]['eid']
        temp['name'] = data['eventList'][key]['name']
        temp['eventtype'] = data['eventList'][key]['eventtype']
        competitions.append(temp)
    return competitions


def get_team_competition_info(event_name):
    competition_teams = []
    data = call_api.send_team_post(event_name)
    temp = {'eid': '', 'teamid': '', 'teamname': '', 'area': ''}
    for key in data['data']:
        temp['eid'] = key['eid']
        temp['teamid'] = key['teamid']
        temp['teamname'] = key['teamname']
        temp['area'] = key['area']
        competition_teams.append(temp)
    return competition_teams


def get_player_competition_info(event_name, meta='all'):
    competition_players = []
    data = call_api.send_player_post(event_name)
    temp = {'eid': '', 'teamid': '', 'teamname': '', 'playerid': '', 'playername': '', 'meta': ''}
    if meta == 'all':
        for key in data['data']:
            temp['eid'] = key['eid']
            temp['teamid'] = key['teamid']
            temp['teamname'] = key['teamname']
            temp['playerid'] = key['playerid']
            temp['playername'] = key['playername']
            temp['meta'] = key['meta']
            competition_players.append(temp)
        return competition_players
    elif meta == 'top' or 'mid' or 'jun' or 'adc' or 'sup':
        for key in data['data']:
            if key['meta'] == meta_dict[meta]:
                temp['eid'] = key['eid']
                temp['teamid'] = key['teamid']
                temp['teamname'] = key['teamname']
                temp['playerid'] = key['playerid']
                temp['playername'] = key['playername']
                temp['meta'] = key['meta']
                competition_players.append(temp)
        return competition_players


# print(get_player_competition_info("2015 LCS 欧洲春季资格赛", 'jun'))




def get_team_performance(event_name):
    team_performance = []
    data = call_api.send_team_post(event_name)
    temp = {
        "eid": "",
        "teamid": "",
        "teamname": "",
        "area": "",
        "appearedTimes": "",
        "kda": "",
        "fstbloodpercentage": "",
        "proAppearedTimes": "",
        "totalKills": "",
        "totalDeaths": "",
        "totalAssists": "",
        "totalLasthit": "",
        "totalGolds": "",
        "totalDamagetohero": "",
        "totalDamagetaken": "",
        "totalWardsplaced": "",
        "totalWardskilled": "",
        "totalDuration": "",
        "totalBarons": "",
        "totalDragon": "",
        "totalTowerTaken": "",
        "totalTowerDeath": "",
        "totalHeronum": "",
        "goldsPermin": "",
        "lasthitPermin": "",
        "damagetoheroPermin": "",
        "wardsplacedpermin": "",
        "wardskilledpermin": "",
        "killsPergame": "",
        "deathsPergame": "",
        "assistsPergame": "",
        "damagetoheropermatch": "",
        "goldpermatch": "",
        "lasthitpermatch": "",
        "damagetakenpermatch": "",
        "baronkillsPergame": "",
        "dragonkillsPergame": "",
        "towertakensPergame": "",
        "towerdeathsPergame": "",
        "wardsplacedPergame": "",
        "wardskilledPergame": "",
        "highestgoldpermin": "",
        "dragonkillspercentage": "",
        "baronkillspercentage": "",
        "wardskilledrate": "",
        "avgDuration": "",
        "heroFrequencyWinrate": "",
        "banHero": "",
        "pickHero": "",
        "winrate": "",
        "teamWinrate": "",
        "bo3Rate": "",
        "fsttowerpercentage": "",
        "goldearnedLead": "",
        "fstbloodwinPercentage": "",
        "firsttowerwinPercentage": "",
        "firstbaronwinPercentage": "",
        "baronbenefitPerkill": "",
        "order": ""
            }

    for key in data['data']:
        temp["eid"] = key['eid']
        temp["teamid"] = key['teamid']
        temp["teamname"] = key['teamname']
        temp["area"] = key['area']
        temp["appearedTimes"] = key['appearedTimes']
        temp["kda"] = key['kda']
        temp["fstbloodpercentage"] = key['fstbloodpercentage']
        temp["proAppearedTimes"] = key['proAppearedTimes']
        temp["totalKills"] = key['totalKills']
        temp["totalDeaths"] = key['totalDeaths']
        temp["totalAssists"] = key['totalAssists']
        temp["totalLasthit"] = key['totalLasthit']
        temp["totalGolds"] = key['totalGolds']
        temp["totalDamagetohero"] = key['totalDamagetohero']
        temp["totalDamagetaken"] = key['totalDamagetaken']
        temp["totalWardsplaced"] = key['totalWardsplaced']
        temp["totalWardskilled"] = key['totalWardskilled']
        temp["totalDuration"] = key['totalDuration']
        temp["totalBarons"] = key['totalBarons']
        temp["totalDragon"] = key['totalDragon']
        temp["totalTowerTaken"] = key['totalTowerTaken']
        temp["totalTowerDeath"] = key['totalTowerDeath']
        temp["totalHeronum"] = key['totalHeronum']
        temp["goldsPermin"] = key['goldsPermin']
        temp["lasthitPermin"] = key['lasthitPermin']
        temp["damagetoheroPermin"] = key['damagetoheroPermin']
        temp["wardsplacedpermin"] = key['wardsplacedpermin']
        temp["wardskilledpermin"] = key['wardskilledpermin']
        temp["killsPergame"] = key['killsPergame']
        temp["deathsPergame"] = key['deathsPergame']
        temp["assistsPergame"] = key['assistsPergame']
        temp["damagetoheropermatch"] = key['damagetoheropermatch']
        temp["goldpermatch"] = key['goldpermatch']
        temp["lasthitpermatch"] = key['lasthitpermatch']
        temp["damagetakenpermatch"] = key['damagetakenpermatch']
        temp["baronkillsPergame"] = key['baronkillsPergame']
        temp["dragonkillsPergame"] = key['dragonkillsPergame']
        temp["towertakensPergame"] = key['towertakensPergame']
        temp["towerdeathsPergame"] = key['towerdeathsPergame']
        temp["wardsplacedPergame"] = key['wardsplacedPergame']
        temp["wardskilledPergame"] = key['wardskilledPergame']
        temp["highestgoldpermin"] = key['highestgoldpermin']
        temp["dragonkillspercentage"] = key['dragonkillspercentage']
        temp["baronkillspercentage"] = key['baronkillspercentage']
        temp["wardskilledrate"] = key['wardskilledrate']
        temp["avgDuration"] = key['avgDuration']
        temp["heroFrequencyWinrate"] = key['heroFrequencyWinrate']
        temp["banHero"] = key['banHero']
        temp["pickHero"] = key['pickHero']
        temp["winrate"] = key['winrate']
        temp["teamWinrate"] = key['teamWinrate']
        temp["bo3Rate"] = key['bo3Rate']
        temp["fsttowerpercentage"] = key['fsttowerpercentage']
        temp["goldearnedLead"] = key['goldearnedLead']
        temp["fstbloodwinPercentage"] = key['fstbloodwinPercentage']
        temp["firsttowerwinPercentage"] = key['firsttowerwinPercentage']
        temp["firstbaronwinPercentage"] = key['firstbaronwinPercentage']
        temp["baronbenefitPerkill"] = key['baronbenefitPerkill']
        temp["order"] = key['order']
        team_performance.append(temp)
    return team_performance


def get_player_performance(eventname, meta='all'):
    player_performance = []
    data = call_api.send_player_post(eventname)
    temp = {
            "eid": "",
            "teamid": "",
            "teamname": "",
            "playerid": "",
            "playername": "",
            "meta": "",
            "kills": "",
            "deaths": "",
            "assists": "",
            "lasthit": "",
            "golds": "",
            "damagetohero": "",
            "damagetaken": "",
            "wardsplaced": "",
            "wardskilled": "",
            "totalKills": "",
            "totalDeaths": "",
            "totalAssists": "",
            "totalLasthit": "",
            "totalGolds": "",
            "totalDamagetohero": "",
            "totalDamagetaken": "",
            "totalWardsplaced": "",
            "totalWardskilled": "",
            "appearedTimes": "",
            "proAppearedTimes": "",
            "duration": "",
            "killsPergame": "",
            "deathsPergame": "",
            "assistsPergame": "",
            "goldsPermin": "",
            "lasthitPermin": "",
            "damagetakenPermin": "",
            "damagetoheroPermin": "",
            "wardsplacedPergame": "",
            "wardskilledPergame": "",
            "goldsPercent": "",
            "damagetakenPercent": "",
            "damagetoheroPercent": "",
            "heronum": "",
            "heroFrequencyWinratejson" :"",
            "pretenLasthit": "",
            "pretwnLasthit": "",
            "lasthitPergame": "",
            "pretenLasthitDiff": "",
            "wardsplacedPermin": "",
            "wardskilledPermin": "",
            "mostassists": "",
            "mostdeaths": "",
            "mostkills": "",
            "kda": "",
            "attendrate": "",
            "winnum": "",
            "losenum": "",
            "damagePergame": "",
            "prefifteenLasthitDiff": "",
            "singleKillsNum": "",
            "damagetoheroConversionRate": "",
            "lasthitPergameDiff": "",
            "metaGoldsLead": "",
            "order": ""
    }
    if meta == 'all':
        for key in data['data']:
            temp["eid"] = key["eid"]
            temp["teamid"] = key["teamid"]
            temp["teamname"] = key["teamname"]
            temp["playerid"] = key["playerid"]
            temp["playername"] = key["playername"]
            temp["meta"] = key["meta"]
            temp["kills"] = key["kills"]
            temp["deaths"] = key["deaths"]
            temp["assists"] = key["assists"]
            temp["lasthit"] = key["lasthit"]
            temp["golds"] = key["golds"]
            temp["damagetohero"] = key["damagetohero"]
            temp["damagetaken"] = key["damagetaken"]
            temp["wardsplaced"] = key["wardsplaced"]
            temp["wardskilled"] = key["wardskilled"]
            temp["totalKills"] = key["totalKills"]
            temp["totalDeaths"] = key["totalDeaths"]
            temp["totalAssists"] = key["totalAssists"]
            temp["totalLasthit"] = key["totalLasthit"]
            temp["totalGolds"] = key["totalGolds"]
            temp["totalDamagetohero"] = key["totalDamagetohero"]
            temp["totalDamagetaken"] = key["totalDamagetaken"]
            temp["totalWardsplaced"] = key["totalWardsplaced"]
            temp["totalWardskilled"] = key["totalWardskilled"]
            temp["appearedTimes"] = key["appearedTimes"]
            temp["proAppearedTimes"] = key["proAppearedTimes"]
            temp["duration"] = key["duration"]
            temp["killsPergame"] = key["killsPergame"]
            temp["deathsPergame"] = key["deathsPergame"]
            temp["assistsPergame"] = key["assistsPergame"]
            temp["goldsPermin"] = key["goldsPermin"]
            temp["lasthitPermin"] = key["lasthitPermin"]
            temp["damagetakenPermin"] = key["damagetakenPermin"]
            temp["damagetoheroPermin"] = key["damagetoheroPermin"]
            temp["wardsplacedPergame"] = key["wardsplacedPergame"]
            temp["wardskilledPergame"] = key["wardskilledPergame"]
            temp["goldsPercent"] = key["goldsPercent"]
            temp["damagetakenPercent"] = key["damagetakenPercent"]
            temp["damagetoheroPercent"] = key["damagetoheroPercent"]
            temp["heronum"] = key["heronum"]
            temp["heroFrequencyWinratejson"] = key["heroFrequencyWinratejson"]
            temp["pretenLasthit"] = key["pretenLasthit"]
            temp["pretwnLasthit"] = key["pretwnLasthit"]
            temp["lasthitPergame"] = key["lasthitPergame"]
            temp["pretenLasthitDiff"] = key["pretenLasthitDiff"]
            temp["wardsplacedPermin"] = key["wardsplacedPermin"]
            temp["wardskilledPermin"] = key["wardskilledPermin"]
            temp["mostassists"] = key["mostassists"]
            temp["mostdeaths"] = key["mostdeaths"]
            temp["mostkills"] = key["mostkills"]
            temp["kda"] = key["kda"]
            temp["attendrate"] = key["attendrate"]
            temp["winnum"] = key["winnum"]
            temp["losenum"] = key["losenum"]
            temp["damagePergame"] = key["damagePergame"]
            temp["prefifteenLasthitDiff"] = key["prefifteenLasthitDiff"]
            temp["singleKillsNum"] = key["singleKillsNum"]
            temp["damagetoheroConversionRate"] = key["damagetoheroConversionRate"]
            temp["lasthitPergameDiff"] = key["lasthitPergameDiff"]
            temp["metaGoldsLead"] = key["metaGoldsLead"]
            temp["order"] = key["order"]
            player_performance.append(temp)
        return player_performance
    elif meta == 'top' or 'mid' or 'jun' or 'adc' or 'sup':
        for key in data['data']:
            if key['meta'] == meta_dict[meta]:
                temp["eid"] = key["eid"]
                temp["teamid"] = key["teamid"]
                temp["teamname"] = key["teamname"]
                temp["playerid"] = key["playerid"]
                temp["playername"] = key["playername"]
                temp["meta"] = key["meta"]
                temp["kills"] = key["kills"]
                temp["deaths"] = key["deaths"]
                temp["assists"] = key["assists"]
                temp["lasthit"] = key["lasthit"]
                temp["golds"] = key["golds"]
                temp["damagetohero"] = key["damagetohero"]
                temp["damagetaken"] = key["damagetaken"]
                temp["wardsplaced"] = key["wardsplaced"]
                temp["wardskilled"] = key["wardskilled"]
                temp["totalKills"] = key["totalKills"]
                temp["totalDeaths"] = key["totalDeaths"]
                temp["totalAssists"] = key["totalAssists"]
                temp["totalLasthit"] = key["totalLasthit"]
                temp["totalGolds"] = key["totalGolds"]
                temp["totalDamagetohero"] = key["totalDamagetohero"]
                temp["totalDamagetaken"] = key["totalDamagetaken"]
                temp["totalWardsplaced"] = key["totalWardsplaced"]
                temp["totalWardskilled"] = key["totalWardskilled"]
                temp["appearedTimes"] = key["appearedTimes"]
                temp["proAppearedTimes"] = key["proAppearedTimes"]
                temp["duration"] = key["duration"]
                temp["killsPergame"] = key["killsPergame"]
                temp["deathsPergame"] = key["deathsPergame"]
                temp["assistsPergame"] = key["assistsPergame"]
                temp["goldsPermin"] = key["goldsPermin"]
                temp["lasthitPermin"] = key["lasthitPermin"]
                temp["damagetakenPermin"] = key["damagetakenPermin"]
                temp["damagetoheroPermin"] = key["damagetoheroPermin"]
                temp["wardsplacedPergame"] = key["wardsplacedPergame"]
                temp["wardskilledPergame"] = key["wardskilledPergame"]
                temp["goldsPercent"] = key["goldsPercent"]
                temp["damagetakenPercent"] = key["damagetakenPercent"]
                temp["damagetoheroPercent"] = key["damagetoheroPercent"]
                temp["heronum"] = key["heronum"]
                temp["heroFrequencyWinratejson"] = key["heroFrequencyWinratejson"]
                temp["pretenLasthit"] = key["pretenLasthit"]
                temp["pretwnLasthit"] = key["pretwnLasthit"]
                temp["lasthitPergame"] = key["lasthitPergame"]
                temp["pretenLasthitDiff"] = key["pretenLasthitDiff"]
                temp["wardsplacedPermin"] = key["wardsplacedPermin"]
                temp["wardskilledPermin"] = key["wardskilledPermin"]
                temp["mostassists"] = key["mostassists"]
                temp["mostdeaths"] = key["mostdeaths"]
                temp["mostkills"] = key["mostkills"]
                temp["kda"] = key["kda"]
                temp["attendrate"] = key["attendrate"]
                temp["winnum"] = key["winnum"]
                temp["losenum"] = key["losenum"]
                temp["damagePergame"] = key["damagePergame"]
                temp["prefifteenLasthitDiff"] = key["prefifteenLasthitDiff"]
                temp["singleKillsNum"] = key["singleKillsNum"]
                temp["damagetoheroConversionRate"] = key["damagetoheroConversionRate"]
                temp["lasthitPergameDiff"] = key["lasthitPergameDiff"]
                temp["metaGoldsLead"] = key["metaGoldsLead"]
                temp["order"] = key["order"]
                player_performance.append(temp)
        return player_performance