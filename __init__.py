from mycroft import MycroftSkill, intent_file_handler


class Mosquitto(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mosquitto.intent')
    def handle_mosquitto(self, message):
        self.speak_dialog('mosquitto')


def create_skill():
    return Mosquitto()

