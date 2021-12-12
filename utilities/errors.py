class IncorrectAnswer(Exception):
    def __init__(self, incorrect):
        self.message = f"\nIncorrect Answer: {incorrect}"
        super().__init__(self.message)


class KnownIncorrectAnswer(Exception):
    def __init__(self, incorrect):
        self.message = f"\nKnown Incorrect Answer: {incorrect}"
        super().__init__(self.message)


class NotJSONSerializable(Exception):
    def __init__(self, obj):
        self.message = f"\nUpdated cache is not JSON serializable:\n{obj}"
        super().__init__(self.message)


class SubmissionError(Exception):
    def __init__(self, incorrect):
        self.message = f"\nError Submitting: {incorrect}"
        super().__init__(self.message)


class WrongExampleAnswer(Exception):
    def __init__(self, incorrect, correct):
        self.message = f"\nYour answer for example input: {incorrect} \nCorrect answer for example input: {correct}"
        super().__init__(self.message)
