from mycroft import MycroftSkill, intent_file_handler


class BringEinkaufsliste(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('einkaufsliste.bring.intent')
    def handle_einkaufsliste_bring(self, message):
        self.speak_dialog('einkaufsliste.bring')


def create_skill():
    return BringEinkaufsliste()

