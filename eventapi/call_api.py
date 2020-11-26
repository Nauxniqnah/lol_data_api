import json

import requests

list_match_id = {1006, 1003, 996, 989, 985, 973, 971, 970, 969, 966, 965, 964, 963, 962, 961, 960, 959, 956, 949, 943,
                 939, 938, 927, 929, 925, 920, 913, 911, 919, 917, 916, 918, 908, 909, 907, 905, 898, 887, 870, 869,
                 861, 867, 863, 860, 862, 859, 830, 836, 829, 826, 822, 819, 820, 817, 815, 811, 808, 805, 803, 791,
                 761, 760, 762, 759, 758, 744, 750, 749, 747, 713, 717, 716, 711, 712, 709, 708, 707, 705, 660, 655,
                 658, 657, 648, 638, 643, 644, 645, 640, 626, 623, 616, 613, 589, 581, 572, 583, 580, 579, 573, 571,
                 569, 564, 565, 560, 535, 539, 532, 523, 528, 527, 529, 522, 509, 517, 510, 489, 486, 478, 485, 457,
                 466, 467, 460, 465, 463, 459, 454, 442, 439, 437, 430, 440, 400, 408, 347, 436, 432, 404, 350, 399,
                 423, 351, 348, 366, 349, 422, 345, 333, 311, 298, 303, 177, 250, 469, 230, 221, 217, 216, 218, 215,
                 178, 346, 176, 169, 170, 173, 165, 172, 164, 163, 154, 158, 152, 157, 136, 151, 150, 137, 144, 138,
                 139, 143, 140, 156, 41, 49, 126, 62, 63, 60, 29, 33, 40, 48, 61, 4, 7, 11, 12, 10, 15, 14, 18, 39,
                 47, 32, 58, 28, 31, 3, 6, 38, 46, 27, 30, 5, 2, 37, 45, 36, 17, 44, 167, 43, 35, 34, 42, 166, 13, 1,
                 265, 267}

list_match_name = ["2020NEST全国电子竞技大赛", "2020 S10全球总决赛", "2020 S10全球总决赛 入围赛", "2020 LCK S10 资格赛", "2020 LPL S10 资格赛",
                   "2020 LCL 夏季赛", "2020 LLA 闭幕赛", "2020 PCS 夏季赛", "2020 VCS 夏季赛", "2020 LCK 夏季赛", "2020 LJL 夏季赛",
                   "2020 LCS 夏季赛", "2020 LEC 夏季赛", "2020 LDL 夏季赛", "2020 CBLOL 第二阶段", "2020 TCL 夏季赛",
                   "2020 OPL 第二阶段",
                   "2020 LPL 夏季赛", "2020 英雄联盟 季中杯", "2020 LCK 夏季升降级赛", "2020 LDL 春季赛", "2020 LDL 公开训练赛",
                   "2020 LPL 公开训练赛", "2020 LCL 春季赛", "2020 LLA 开幕赛", "2020 LJL 春季赛", "2020 PCS 春季赛", "2020 LCK 春季赛",
                   "2020 TCL 冬季赛", "2020 OPL 第一阶段", "2020 VCS 春季赛", "2020 CBLOL 第一阶段", "2020 LCS 春季赛",
                   "2020 LEC 春季赛",
                   "2020 LPL 春季赛", "KeSPA杯2019", "2019德玛西亚杯", "2019LPL全明星周末", "2019 S9全球总决赛", "2019 S9全球总决赛 入围赛",
                   "2019 LEC S9资格赛", "2020 LCK 春季升降级赛", "2019 LPL S9资格赛", "2019 LCS S9资格赛", "2019 LMS S9资格赛",
                   "2019 LCK S9资格赛", "2019 亚洲对抗赛", "2019 欧美对抗赛", "2019 LDL 夏季赛", "2019 LMS 夏季赛", "2019 LEC 夏季赛",
                   "2019 LCK 夏季赛", "2019 LCS 夏季赛", "2019 LPL 夏季赛", "2019NESTOB全国电子竞技大赛", "2019 MSI 季中冠军赛",
                   "2019 MSI 入围赛", "2019NEST全国电子竞技大赛", "2019LCK春季升降级赛", "2019 LDL 春季赛", "2019 LCS 春季赛",
                   "2019 LEC 春季赛",
                   "2019 LMS 春季赛", "2019 LCK 春季赛", "2019 LPL 春季赛", "2018 德玛西亚杯西安站", "2018 韩国电竞协会杯",
                   "2018 全明星1v1淘汰赛",
                   "2018 全明星赛", "2018 NEST 全国电子竞技大赛", "2018 S8全球总决赛", "2018 S8全球总决赛 入围赛", "2018 LMS S8资格赛",
                   "2019 LCK 夏季升降级赛", "2018 LPL S8资格赛", "2018 LCS欧洲S8资格赛", "2018 LCS北美S8资格赛", "2018 LCK S8资格赛",
                   "2018 欧美对抗赛", "2018 亚洲对抗赛", "LOL亚运会", "2018 LDL 夏季赛", "2018 LMS 夏季赛", "2018 LCS 北美夏季赛",
                   "2018 LCS 欧洲夏季赛", "2018 LCK夏季赛", "2018 LPL夏季赛", "德玛西亚杯珠海站", "2018 MSI 季中冠军赛", "2018 MSI 入围赛",
                   "2018 LCK 升降级赛", "UZI 2000杀", "2018 LDL春季赛", "2018 LCS 欧洲春季赛", "2018 LCS 北美春季赛", "2018 LMS 春季赛",
                   "2018 LCK春季赛", "2018 LPL春季赛", "德玛西亚杯青岛站", "春节联欢晚会集中讨论吐槽", "2017NESO总决赛", "2017全明星赛",
                   "2017全明星赛SOLO赛",
                   "2017韩国电竞协会杯", "2017 全球总决赛", "WUCG 世界大学生电子竞技联赛", "2017 全球总决赛 入围赛", "2018 LCK 春季升降级赛",
                   "2017 LCS NA S7资格赛", "2017 LCS EU S7资格赛", "NEST2017全国电子竞技大赛", "2017 LPL S7资格赛", "2017LCK S7资格赛",
                   "2017 LMS S7资格赛", "2018 EU LCS 春季升降级赛", "2017俄土对抗赛", "2017南美对抗赛", "2017欧美对抗赛", "2017太平洋对抗赛",
                   "2017亚洲对抗赛", "2017 LPL 夏季赛", "2017 LSPL 夏季赛", "2017 LCS 北美夏季赛", "2017 LMS 港澳台夏季赛",
                   "2017 LCS 欧洲夏季赛",
                   "2017 LCK 韩国夏季赛", "德玛西亚杯长沙站", "2017 MSI 季中冠军赛", "2017 MSI 入围赛", "2017 LCK 升降级赛", "2017 LPL 升降级赛",
                   "2017 GPL 东南亚 春季赛", "2017 IEM 卡托维兹站", "2017 LCL 独联体 春季赛", "2017 LMS 港澳台春季联赛", "2017 TCL 土耳其冬季赛",
                   "2017 OPL 春季赛", "2017 CBL 巴西夏季赛", "2017 LCS 北美春季赛", "2017 LJL 春季赛", "2017 CLS 南拉丁美洲 春季赛",
                   "2017 LCS 欧洲春季赛", "2017 LPL 春季赛", "2017 LSPL 春季赛", "2017 LCK 韩国春季赛", "2017 LLN 北拉丁美洲 春季赛",
                   "2016无锡中韩电竞对抗赛", "2016 IEM 京畿道站", "2016 IEM 奥克兰站", "NEST2016全国电子竞技大赛", "2016年韩国电竞协会杯",
                   "2016全球总决赛",
                   "2016 S6 世界总决赛LPL预选赛", "2017 LPL 春季升降级赛", "2016德玛西亚杯—苏州武汉", "2016 LMS 港澳台夏季联赛", "2016 LCS 北美夏季赛",
                   "2016 LCS 欧洲夏季赛", "2016 LPL 夏季赛", "2016 LCK 韩国夏季赛", "2016 MSI 季中冠军赛", "2016 LPL 夏季赛资格赛",
                   "2016 IEM 卡托维兹站", "2016 LCS 北美春季赛", "2016 LCS 欧洲春季赛", "2016 LMS 港澳台春季联赛", "2016 LPL 春季赛",
                   "2016 LCK 韩国春季赛", "2015 IEM 科隆站", "WCA 2015 LOL 全球总决赛", "NEST2015全国电子竞技大赛", "2015 德玛西亚杯—武汉",
                   "2015IEM圣何塞站", "2015年韩国电竞协会杯", "2015全球总决赛", "2016 LCS 北美赛区春季赛资格赛", "2016 LCS 欧洲赛区春季赛资格赛",
                   "2015 S5 LPL 预选赛", "2015 S5 LCK韩国赛区预选赛", "2015 S5 LCS北美赛区预选赛", "2015 S5 LCS欧洲赛区预选赛",
                   "S5赛季世界总决赛外卡赛",
                   "2015 S5 港澳台地区预选赛", "2015 LJL 日本联赛总决赛", "2015 LCS 北美夏季赛", "2015 LCS 欧洲夏季赛", "2015 德玛西亚杯—北京",
                   "2015 LPL 夏季赛", "2015 LMS 港澳台区夏季赛", "2015 LCK 韩国夏季赛", "2015 LCK 夏季资格赛", "2015 MSI 季中邀请赛",
                   "2015 LCS 北美夏季资格赛", "2015 LCS 欧洲夏季资格赛", "2015 LPL 夏季资格赛", "2015 LCS 北美春季赛", "2015 LCS 欧洲春季赛",
                   "2015 LPL 春季赛", "2015 LMS 港澳台春季联赛", "2015 LCK 韩国春季赛", "2015 欧洲扩展赛", "2015 北美扩展赛",
                   "2014 S4 全球总决赛",
                   "2015 LCS 北美春季资格赛", "2015 LCS 欧洲春季资格赛", "2014 S4 世界总决赛LPL预选赛", "S4世界总决赛韩国地区预选赛", "2014 OGN 夏季赛",
                   "2014 LPL 夏季赛", "2014 LCS 北美夏季赛", "2014 LCS 欧洲夏季赛", "2014 LCS 北美夏季资格赛", "2014 LCS 欧洲夏季资格赛",
                   "2014 OGN 春季赛", "2014 LPL 春季赛", "2014 LCS 欧洲春季赛", "2014 LCS 北美春季赛", "2014 LCS 北美春季资格赛",
                   "2014 LCS 欧洲春季资格赛", "2013 S3 全球总决赛 北美预选赛", "2013全球总决赛", "2013 S3 全球总决赛 欧洲预选赛", "2013 LPL 夏季赛",
                   "2013 LCS 欧洲夏季常规赛", "2013 LCS 北美夏季赛", "2013 LCS 北美夏季资格赛", "2013 LCS 欧洲夏季资格赛", "2013 LPL 春季赛",
                   "2013 LCS 欧洲春季赛", "2013 LCS 北美春季赛", "S2赛季世界总决赛", "S1世界总决赛"]

dic = dict(map(lambda x,y:[x,y], list_match_name, list_match_id))

headers = {
    'authority': 'm.wanplus.com',
    'method': 'POST',
    'path': '/ajax/stats/list',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '4718',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'wanplus_token=ca5c9886e44b030e6a72b616db11c999; wanplus_storage=lf4m67eka3o; wanplus_sid=b91cbc70de5d5852aac738d23d238b6f; wanplus_csrf=_csrf_tk_717215530; gameType=2; UM_distinctid=175fd2cc56933-021e75472229c2-c791e37-13c680-175fd2cc56a23c; wp_pvid=4036787096; wp_info=ssid=s3914832348; Hm_lvt_f69cb5ec253c6012b2aa449fb925c1c2=1606270372; Hm_lpvt_f69cb5ec253c6012b2aa449fb925c1c2=1606270585; CNZZDATA1275078652=1900053009-1606265507-%7C1606276334; wanplus_token=6d828b7bbfbd6254bc3a4b37acd51388; wanplus_storage=lf4m67eka3o; wanplus_sid=14951c1e109604192bfb362d68e84f28',
    'origin': 'https://m.wanplus.com',
    'referer': 'https://m.wanplus.com/lol/teamstats',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
    'x-csrf-token': '784324394',
    'x-requested-with': 'XMLHttpRequest'
}


def send_team_post(event_name):

    url = "https://m.wanplus.com/ajax/stats/list"

    team_payload = {"_gtk": "784324394", "draw": 12, "columns[0][data]": "order", "columns[0][name]": "",
                    "columns[0][searchable]": True, "columns[0][orderable]": False, "columns[0][search][value]": "",
                    "columns[0][search][regex]": False, "columns[1][data]": "teamname", "columns[1][name]": "",
                    "columns[1][searchable]": True, "columns[1][orderable]": False, "columns[1][search][value]": "",
                    "columns[1][search][regex]": False, "columns[2][data]": "kda", "columns[2][name]": "",
                    "columns[2][searchable]": True, "columns[2][orderable]": True, "columns[2][search][value]": "",
                    "columns[2][search][regex]": False, "columns[3][data]": "killsPergame", "columns[3][name]": "",
                    "columns[3][searchable]": True, "columns[3][orderable]": True, "columns[3][search][value]": "",
                    "columns[3][search][regex]": False, "columns[4][data]": "deathsPergame", "columns[4][name]": "",
                    "columns[4][searchable]": True, "columns[4][orderable]": True, "columns[4][search][value]": "",
                    "columns[4][search][regex]": False, "columns[5][data]": "damagetoheroPermin",
                    "columns[5][name]": "", "columns[5][searchable]": True, "columns[5][orderable]": True,
                    "columns[5][search][value]": "", "columns[5][search][regex]": False,
                    "columns[6][data]": "fstbloodpercentage", "columns[6][name]": "", "columns[6][searchable]": True,
                    "columns[6][orderable]": True, "columns[6][search][value]": "", "columns[6][search][regex]": False,
                    "columns[7][data]": "avgDuration", "columns[7][name]": "", "columns[7][searchable]": True,
                    "columns[7][orderable]": True, "columns[7][search][value]": "", "columns[7][search][regex]": False,
                    "columns[8][data]": "goldpermatch", "columns[8][name]": "", "columns[8][searchable]": True,
                    "columns[8][orderable]": True, "columns[8][search][value]": "", "columns[8][search][regex]": False,
                    "columns[9][data]": "goldsPermin", "columns[9][name]": "", "columns[9][searchable]": True,
                    "columns[9][orderable]": True, "columns[9][search][value]": "", "columns[9][search][regex]": False,
                    "columns[10][data]": "lasthitPermin", "columns[10][name]": "", "columns[10][searchable]": True,
                    "columns[10][orderable]": True, "columns[10][search][value]": "",
                    "columns[10][search][regex]": False, "columns[11][data]": "dragonkillsPergame",
                    "columns[11][name]": "", "columns[11][searchable]": True, "columns[11][orderable]": True,
                    "columns[11][search][value]": "", "columns[11][search][regex]": False,
                    "columns[12][data]": "dragonkillspercentage", "columns[12][name]": "",
                    "columns[12][searchable]": True, "columns[12][orderable]": True, "columns[12][search][value]": "",
                    "columns[12][search][regex]": False, "columns[13][data]": "baronkillsPergame",
                    "columns[13][name]": "", "columns[13][searchable]": True, "columns[13][orderable]": True,
                    "columns[13][search][value]": "", "columns[13][search][regex]": False,
                    "columns[14][data]": "baronkillspercentage", "columns[14][name]": "",
                    "columns[14][searchable]": True, "columns[14][orderable]": True, "columns[14][search][value]": "",
                    "columns[14][search][regex]": False, "columns[15][data]": "wardsplacedpermin",
                    "columns[15][name]": "", "columns[15][searchable]": True, "columns[15][orderable]": True,
                    "columns[15][search][value]": "", "columns[15][search][regex]": False,
                    "columns[16][data]": "wardskilledpermin", "columns[16][name]": "", "columns[16][searchable]": True,
                    "columns[16][orderable]": True, "columns[16][search][value]": "",
                    "columns[16][search][regex]": False, "columns[17][data]": "wardskilledrate",
                    "columns[17][name]": "", "columns[17][searchable]": True, "columns[17][orderable]": True,
                    "columns[17][search][value]": "", "columns[17][search][regex]": False,
                    "columns[18][data]": "towertakensPergame", "columns[18][name]": "", "columns[18][searchable]": True,
                    "columns[18][orderable]": True, "columns[18][search][value]": "",
                    "columns[18][search][regex]": False, "columns[19][data]": "towerdeathsPergamev",
                    "columns[19][name]": "", "columns[19][searchable]": True, "columns[19][orderable]": True,
                    "columns[19][search][value]": "", "columns[19][search][regex]": False, "order[0][column]": 2,
                    "order[0][dir]": "desc", "start": 0, "length": 20, "search[value]": "", "search[regex]": False,
                    "area": "", "type": "team", "gametype": 2, "filter": "{\"team\":{},\"player\":{},\"meta\":{}}",
                    'eid': dic[event_name]}

    response = requests.request(method='POST', url=url, headers=headers, data=team_payload)
    content = response.content.decode()
    data = json.loads(content)
    return data


def send_player_post(event_name):

    url = "https://m.wanplus.com/ajax/stats/list"

    player_payload = {"_gtk": "784324394", "draw": 12, "columns[0][data]": "order", "columns[0][name]": "",
                      "columns[0][searchable]": True, "columns[0][orderable]": False, "columns[0][search][value]": "",
                      "columns[0][search][regex]": False, "columns[1][data]": "playername", "columns[1][name]": "",
                      "columns[1][searchable]": True, "columns[1][orderable]": False, "columns[1][search][value]": "",
                      "columns[1][search][regex]": False, "columns[2][data]": "teamname", "columns[2][name]": "",
                      "columns[2][searchable]": True, "columns[2][orderable]": False, "columns[2][search][value]": "",
                      "columns[2][search][regex]": False, "columns[3][data]": "meta", "columns[3][name]": "",
                      "columns[3][searchable]": True, "columns[3][orderable]": False, "columns[3][search][value]": "",
                      "columns[3][search][regex]": False, "columns[4][data]": "appearedTimes", "columns[4][name]": "",
                      "columns[4][searchable]": True, "columns[4][orderable]": True, "columns[4][search][value]": "",
                      "columns[4][search][regex]": False, "columns[5][data]": "kda", "columns[5][name]": "",
                      "columns[5][searchable]": True, "columns[5][orderable]": True, "columns[5][search][value]": "",
                      "columns[5][search][regex]": False, "columns[6][data]": "attendrate", "columns[6][name]": "",
                      "columns[6][searchable]": True, "columns[6][orderable]": True, "columns[6][search][value]": "",
                      "columns[6][search][regex]": False, "columns[7][data]": "killsPergame", "columns[7][name]": "",
                      "columns[7][searchable]": True, "columns[7][orderable]": True, "columns[7][search][value]": "",
                      "columns[7][search][regex]": False, "columns[8][data]": "mostkills", "columns[8][name]": "",
                      "columns[8][searchable]": True, "columns[8][orderable]": True, "columns[8][search][value]": "",
                      "columns[8][search][regex]": False, "columns[9][data]": "deathsPergame", "columns[9][name]": "",
                      "columns[9][searchable]": True, "columns[9][orderable]": True, "columns[9][search][value]": "",
                      "columns[9][search][regex]": False, "columns[10][data]": "mostdeaths", "columns[10][name]": "",
                      "columns[10][searchable]": True, "columns[10][orderable]": True, "columns[10][search][value]": "",
                      "columns[10][search][regex]": False, "columns[11][data]": "assistsPergame",
                      "columns[11][name]": "", "columns[11][searchable]": True, "columns[11][orderable]": True,
                      "columns[11][search][value]": "", "columns[11][search][regex]": False,
                      "columns[12][data]": "mostassists", "columns[12][name]": "", "columns[12][searchable]": True,
                      "columns[12][orderable]": True, "columns[12][search][value]": "",
                      "columns[12][search][regex]": False, "columns[13][data]": "goldsPermin", "columns[13][name]": "",
                      "columns[13][searchable]": True, "columns[13][orderable]": True, "columns[13][search][value]": "",
                      "columns[13][search][regex]": False, "columns[14][data]": "lasthitPermin",
                      "columns[14][name]": "", "columns[14][searchable]": True, "columns[14][orderable]": True,
                      "columns[14][search][value]": "", "columns[14][search][regex]": False,
                      "columns[15][data]": "damagetoheroPermin", "columns[15][name]": "",
                      "columns[15][searchable]": True, "columns[15][orderable]": True, "columns[15][search][value]": "",
                      "columns[15][search][regex]": False, "columns[16][data]": "damagetoheroPercent",
                      "columns[16][name]": "", "columns[16][searchable]": True, "columns[16][orderable]": True,
                      "columns[16][search][value]": "", "columns[16][search][regex]": False,
                      "columns[17][data]": "damagetakenPermin", "columns[17][name]": "",
                      "columns[17][searchable]": True, "columns[17][orderable]": True, "columns[17][search][value]": "",
                      "columns[17][search][regex]": False, "columns[18][data]": "damagetakenPercent",
                      "columns[18][name]": "", "columns[18][searchable]": True, "columns[18][orderable]": True,
                      "columns[18][search][value]": "", "columns[18][search][regex]": False,
                      "columns[19][data]": "wardsplacedPermin", "columns[19][name]": "",
                      "columns[19][searchable]": True, "columns[19][orderable]": True, "columns[19][search][value]": "",
                      "columns[19][search][regex]": False, "columns[20][data]": "wardskilledPermin",
                      "columns[20][name]": "", "columns[20][searchable]": True, "columns[20][orderable]": True,
                      "columns[20][search][value]": "", "columns[20][search][regex]": False, "order[0][column]": 4,
                      "order[0][dir]": "desc", "start": 0, "length": 20, "search[value]": "", "search[regex]": False,
                      "area": "", "type": "player", "gametype": 2, "filter": "{\"team\":{},\"player\":{},\"meta\":{}}",
                      'eid': dic[event_name]}

    response = requests.request(method='POST', url=url, headers=headers, data=player_payload)
    content = response.content.decode()
    data = json.loads(content)
    return data


