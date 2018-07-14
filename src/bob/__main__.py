import os
from pathlib import Path

import click
from dotenv import load_dotenv

from .services.hermes import Client
from .__about__ import __version__
from .services.logger import Logger


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__)
@click.option('-q', '--quiet', is_flag=True, help="no output")
@click.option('-v', '--verbose', count=True, help="verbosity level")
def main(quiet, verbose):
    """Bob is a fuckin' bitch. Slap it. 🐟"""
    Logger.prepare('main', 1000 if quiet else 50 - verbose * 10)
    # configure app
    load_dotenv(dotenv_path=Path('.') / '.env')


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print('CONNECTED')
    print(client)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("hermes/intent/#")
    client.subscribe("hermes/nlu/#")
    client.subscribe("hermes/asr/#")
    client.subscribe("hermes/dialogueManager/#")


@main.command('run')
def run():
    print(os.getenv('SPOTIFY_EMAIL'))
    print("coucou")
    client = Client(mqtt_host=os.getenv('MQTT_HOST'),
                    mqtt_port=os.getenv('MQTT_PORT'))
    client.on_connect = on_connect
    client.connect()
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
    # loop_start / loop_stop for threaded loop


if __name__ == '__main__':
    main()
