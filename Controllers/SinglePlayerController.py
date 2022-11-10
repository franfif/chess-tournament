from Views.PlayerView import PlayerView
from Views.BaseView import BaseView
from Models.Player import Player
from Models.Option import Option


class SinglePlayerController:
    def __init__(self, player=None):
        self.view = PlayerView()
        self.base_view = BaseView()
        if player is not None:
            self.player = player
        else:
            self.player = Player(*self.get_player_info())

    def get_player_info(self):
        first_name = self.view.prompt_for_first_name()
        last_name = self.view.prompt_for_last_name()
        date_of_birth = self.view.prompt_for_date_of_birth()
        gender = self.view.prompt_for_gender()
        ranking = self.view.prompt_for_ranking()
        return first_name, last_name, date_of_birth, gender, ranking

    def display_player(self):
        self.view.show_player(self)

    def edit_player(self):
        next_action = None
        while next_action is None:
            menu = self.edit_player_options()
            menu_names = list(map(lambda x: x.name, menu))
            to_do = self.base_view.select_from_list(menu_names)
            next_action = menu[to_do].function()
        return

    def edit_player_options(self):
        options = [Option('Change first name', self.update_first_name),
                   Option('Change last name', self.update_last_name),
                   Option('Change date of birth', self.update_date_of_birth),
                   Option('Change gender', self.update_gender),
                   Option('Change ranking', self.update_ranking),
                   Option('Save and go back', self.exit)]
        return options

    def update_first_name(self):
        new_first_name = self.view.get_new_first_name(self.player.get_full_name())
        self.player.first_name = new_first_name

    def update_last_name(self):
        new_last_name = self.view.get_new_last_name(self.player.get_full_name())
        self.player.last_name = new_last_name

    def update_date_of_birth(self):
        new_date_of_birth = self.view.get_new_date_of_birth(self.player.get_full_name(), self.player.date_of_birth)
        self.player.date_of_birth = new_date_of_birth

    def update_gender(self):
        new_gender = self.view.get_new_gender(self.player.get_full_name(), self.player.gender)
        self.player.gender = new_gender

    def update_ranking(self):
        new_ranking = self.view.get_new_ranking(self.player.ranking, self.player.get_full_name())
        self.player.ranking = new_ranking

    def exit(self):
        return True
