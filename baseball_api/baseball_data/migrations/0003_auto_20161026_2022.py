# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 20:22
from __future__ import unicode_literals

from django.db import migrations
import csv


def add_master_batting_fielding_pitching(apps, schema_editor):
    Master = apps.get_model("baseball_data", "Master")
    Batting = apps.get_model("baseball_data", "Batting")
    Pitching = apps.get_model("baseball_data", "Pitching")
    Fielding = apps.get_model("baseball_data", "Fielding")


    with open('master.csv') as infile:
        contents = csv.DictReader(infile)
        for row in contents:
            print(row)
            Master.objects.create(player_code=row["playerID"], birth_year=row["birthYear"], birth_day=row["birthDay"],
                                  birth_country=row["birthCountry"], birth_state=row["birthState"],
                                  birth_city=row["birthCity"], death_year=row["deathYear"], death_month=row["deathMonth"],
                                  death_day=row["deathDay"], death_country=row["deathCountry"], death_state=row["deathState"],
                                  death_city=row["deathCity"], name_first=row["nameFirst"], name_last=row["nameLast"],
                                  name_given=row["nameGiven"], weight=row["weight"], height=row["height"], bats=row["bats"],
                                  throws=row["throws"], debut=row["debut"], final_game=row["finalGame"], retro_code=row["retroID"],
                                  bbref_code=row["bbrefID"])

    with open('batting.csv') as infile:
        contents = csv.DictReader(infile)
        for row in contents:
            print(row)
            player_code = Master.objects.get(player_code=row["playerID"])
            Batting.objects.create(player_code=player_code, year_code=row["yearID"], stint=row["stint"], team_code=row["teamID"],
                                   league_code=row["lgID"], games=row["G"], at_bats=row["AB"], runs=row["R"], hits=row["H"], doubles=row["2B"], triples=row["3B"], homeruns=row["HR"],
                                   rbis=row["RBI"], stolen_base=row["SB"], caught_stealing=row["CS"], base_on_balls=row["BB"], strikeouts=row["SO"],
                                   intent_walk=row["IBB"], hit_by_pitch=row["HBP"], sacrifice_hits=row["SH"], sacrifice_fly=row["SF"], ground_double_play=row["GIDP"])

    with open('pitching.csv') as infile:
        contents = csv.DictReader(infile)
        for row in contents:
            print(row)
            player_code = Master.objects.get(player_code=row["playerID"])
            Pitching.objects.create(player_code=player_code, year_code=row["yearID"], stint=row["stint"], team_code=row["teamID"],
                                    league_code=row["lgID"], wins=row["W"], losses=row["L"], games=row["G"], games_started=row["GS"],
                                    complete_games=row["CG"], shutouts=row["SHO"], saves=row["SV"], outs_pitched=row["IPouts"],
                                    hits=row["H"], earned_runs=row["ER"], homeruns=row["HR"], walks=row["BB"], strikeouts=row["SO"],
                                    opponent_batting_avg=row["BAOpp"], earned_run_avg=row["ERA"], intentional_walks=row["IBB"],
                                    wild_pitch=row["WP"], batter_hit_by_pitch=row["HBP"], balks=row["BK"], batter_faced_by_pitcher=row["BFP"],
                                    games_finished=row["GF"], runs_allowed=row["R"], sacrifice_opp_batter=row["SH"], sacrifice_fly_opp_batter=row["SF"],
                                    ground_double_play_opp_batter=row["GIDP"])

    with open('fielding.csv') as infile:
        contents = csv.DictReader(infile)
        for row in contents:
            print(row)
            player_code = Master.objects.get(player_code=row["playerID"])
            Fielding.objects.create(player_code=player_code, year_code=row["yearID"], stint=row["stint"], team_code=row["teamID"],
                                    league_code=row["lgID"], position=row["POS"], games=row["G"], games_started=row["GS"],
                                    time_in_field=row["InnOuts"], putouts=row["PO"], assists=row["A"], errors=row["E"],
                                    double_plays=row["DP"], passed_balls=row["PB"], wild_pitches=row["WP"], opp_stolen_bases=row["SB"],
                                    opp_caught_stealing=row["CS"], zone_rating=row["ZR"])

    # raise Exception("STINKY FEEEETTTTTT!")


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_data', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_master_batting_fielding_pitching)
    ]