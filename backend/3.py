class StateMachine:
    def __init__(self):
        self.transitions = {}
        self.outputs = {}
        self.current_state = 0
        self.state_count = 1ello Google

    def add_word(self, word, output):
        current_state = 0
        for char in word:
            if (current_state, char) not in self.transitions:
                self.transitions[(current_state, char)] = self.state_count
                current_state = self.state_count
                self.state_count += 1
            else:
                current_state = self.transitions[(current_state, char)]
        
        # When we finish adding the word, store the output in the final state
        self.outputs[current_state] = output
        print(self.outputs)
        print(self.transitions)

    def next_state(self, current_state, char):
        return self.transitions.get((current_state, char), 0)

    def get_output(self, state):
        return self.outputs.get(state, None)

def search_text(text, state_machine):
    result = []
    state = 0
    i = 0

    while i < len(text):
        char = text[i]
        next_state = state_machine.next_state(state, char)

        if next_state:
            state = next_state
            output = state_machine.get_output(state)

            # Check if we have reached a final state with an output
            if output:
                result.append(output)
                # Move the index past the length of the matched word
                i += 1
                # Reset state to start looking for new matches
                state = 0
            else:
                i += 1
        else:
            # If no transition exists, reset state and move one character
            result.append(text[i])
            state = 0
            i += 1

    return ''.join(result)

# Example setup
state_machine = StateMachine()
state_machine.add_word("Google", "Google©")
state_machine.add_word("Fugro", "Fugro B.V.")
state_machine.add_word("Holland", "The Netherlands")


text = " We likeGoogle, and Holland."
converted_text = search_text(text, state_machine)
print(converted_text) 
