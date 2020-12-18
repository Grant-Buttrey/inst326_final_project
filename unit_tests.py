import fantasy_draft_rank as fdr
import mock_draft
import pandas as pd

data = pd.read_json("https://www.fantasyfootballdatapros.com/api/players/2019/all")
df = pd.DataFrame(data)
#Driver: William Navigator: Grant
def test_api():
    test_class = fdr.Rank(df)
    assert test_class.frame["player_name"][0] == "Christian McCaffrey", "API is not loading properly"
#Driver: Rachel Navigator: Sakib   
def test_player_dict():
    league_instance = fdr.League(df)
    assert league_instance.player_dict["Lamar Jackson"]["position"] == "QB"
#Driver: Grant  Navigator:  Rachel
def test_position_points():
    rank_instance = fdr.Rank(df)
    rank_instance.position_points()
    assert rank_instance.roster["Lamar Jackson"]["rank_points"] == 23
#Driver: Sakib Navigator: William
def test_draft_round():
    player_list = mock_draft.draft_round(df)
    assert player_list[0].player_name == "Christian McCaffrey"
    
test_api()
test_player_dict()
test_position_points()
test_draft_round()