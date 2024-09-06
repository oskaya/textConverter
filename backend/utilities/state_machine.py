class StateMachine:
    def __init__(self):
        self.transitions = {}
        self.outputs = {}
        self.state_count = 1  # State 0 is the initial state

    def add_word(self, word, output):
        current_state = 0
        for char in word:
            if (current_state, char) not in self.transitions:
                self.transitions[(current_state, char)] = self.state_count
                current_state = self.state_count
                self.state_count += 1
            else:
                current_state = self.transitions[(current_state, char)]
        self.outputs[current_state] = output

    def next_state(self, current_state, char):
        return self.transitions.get((current_state, char), 0)

    def get_output(self, state):
        return self.outputs.get(state, None)