from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import warnings

import ruamel.yaml

warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy

logger = logging.getLogger(__name__)

# this will catch predictions the model isn't very certain about
# there is a threshold for the NLU predictions as well as the action predictions
fallback = FallbackPolicy(fallback_action_name="utter_unclear",
                          core_threshold=0.15,
                          nlu_threshold=0.1)


def train_dialogue():
    agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])
    training_data = agent.load_data('stories.md')

    agent.train(
        training_data)

    agent.persist('models/dialogue')
    return agent


# def run_weather_bot():
#     nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
#     agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter)
#
#     # rasa_core.run.serve_application(agent ,channel='cmdline')
#
#     return agent


if __name__ == '__main__':
    train_dialogue()
    # run_weather_bot()
