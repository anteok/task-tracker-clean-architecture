from repositories.in_memory import InMemoryRepository
from views.command_pattern import CommandPatternFactory


class CommandLineHandler:

    def __init__(self):
        self._repository = InMemoryRepository()

        print(
            'Hello! You have no tasks.\n\n'
            'You are able to use such commands:\n'
            '- create task "<task name>"\n'
            '- move task <task id> to <in_backlog|prioritized|in_work|in_review|done>\n'
            '- what is <task id>\n'
            '- delete task <task id>\n'
            '\n'
            'Press Ctrl+C to finish.'
        )

    def run(self):
        while True:
            command = input()
            response = CommandPatternFactory.get_response(command, self._repository)
            print(response)


if __name__ == '__main__':
    CommandLineHandler().run()
