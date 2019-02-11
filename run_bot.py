from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig
from custominterpreter import CustomInterpreter
from bot_server_channel import BotServerInputChannel


def load_agent():
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load(path='./models/dialogue', action_endpoint=action_endpoint)
    agent.interpreter = CustomInterpreter
    return agent


def main_server():
    agent = load_agent()
    channel = BotServerInputChannel(agent, port=5005)
    agent.handle_channels([channel], http_port=5005)


main_server()
