import paho.mqtt.client as mqtt

from src.bob.services.logger import Logger


class Client(mqtt.Client):
    __mqtt_host = None
    __mqtt_port = None
    __logger = None
    on_asr = None
    on_intent = None
    on_intent_not_parsed = None
    on_intent_not_recognized = None
    on_nlu = None
    on_dialogue_manager = None

    def __init__(self, mqtt_host: str, mqtt_port: int) -> None:
        self.__mqtt_host = mqtt_host
        self.__mqtt_port = mqtt_port
        self.__logger = Logger.get('main.hermes.Client')

    def connect(self, **kwargs) -> None:
        super(Client, self).connect(self.__mqtt_host, self.__mqtt_port, 60)
        self.message_callback_add(sub='hermes/asr/#', callback=self.__on_asr)
        self.message_callback_add(sub='hermes/intent/#',
                                  callback=self.__on_intent)
        self.message_callback_add(sub='hermes/nlu/intentNotParsed',
                                  callback=self.__on_intent_not_parsed)
        self.message_callback_add(sub='hermes/nlu/intentNotRecognized',
                                  callback=self.__on_intent_not_recognized)
        self.message_callback_add(sub='hermes/nlu/#', callback=self.__on_nlu)
        self.message_callback_add(sub='hermes/dialogueManager/#',
                                  callback=self.__on_dialogue_manager)

    def __on_asr(self, user_data, message) -> None:
        if self.on_asr is not None:
            self.on_asr(self, user_data, message)
        else:
            self.__event_not_implemented('on_asr')

    def __on_intent(self, user_data, message) -> None:
        if self.on_intent is not None:
            self.on_intent(self, user_data, message)
        else:
            self.__event_not_implemented('on_intent')

    def __on_intent_not_parsed(self, user_data, message) -> None:
        if self.on_intent_not_parsed is not None:
            self.on_intent_not_parsed(self, user_data, message)
        else:
            self.__event_not_implemented('on_intent_not_parsed')

    def __on_intent_not_recognized(self, user_data, message) -> None:
        if self.on_intent_not_recognized is not None:
            self.on_intent_not_recognized(self, user_data, message)
        else:
            self.__event_not_implemented('on_intent_not_recognized')

    def __on_nlu(self, user_data, message) -> None:
        if self.on_nlu is not None:
            self.on_nlu(self, user_data, message)
        else:
            self.__event_not_implemented('on_nlu')

    def __on_dialogue_manager(self, user_data, message) -> None:
        if self.on_dialogue_manager is not None:
            self.on_dialogue_manager(self, user_data, message)
        else:
            self.__event_not_implemented('on_dialogue_manager')

    def __event_not_implemented(self, event: str) -> None:
        self.__logger.debug(f'"{event}" event received but not implemented')
