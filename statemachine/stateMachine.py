import json


class StateMachine:
    currentState = None
    states = []
    inputs = []
    actions = []

    def __init__(self, conf_file):

        with open(conf_file) as json_file:
            data = json.load(json_file)
            for state in data["STATES"]:
                self.states.append(state)
            for inp in data["INPUTS"]:
                self.inputs.append(inp)
        print(f'Loading states -> ', self.states)
        print(f'Loading inputs -> ', self.inputs)

    def possible_state_transitions(self):
        pass




if __name__ == '__main__':
    t = StateMachine
    t('record.json')
