class Context:
    pass


class ElectionStep:
    message_type: str

    def __init__(self) -> None:
        self.next_step = None

    def skip_message(self, message_type: str):
        return self.message_type != message_type

    def process_message(self, message_type: str, message: dict, context: Context):
        raise NotImplementedError()


class Wrapper:
    context: Context
    step: ElectionStep

    def __init__(self, context: Context, step: ElectionStep) -> None:
        self.context = context
        self.step = step

    def skip_message(self, message_type: str) -> bool:
        return self.step.skip_message(message_type)

    def process_message(self, message_type: str, message: dict) -> dict:
        if self.step.skip_message(message_type):
            return

        result = self.step.process_message(message_type, message, self.context)

        if self.step.next_step:
            self.step = self.step.next_step

        return result
