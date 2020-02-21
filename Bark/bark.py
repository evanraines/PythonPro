import commands
from collections import OrderedDict
import os

class Option:
    def __init__(self, name, command, prep_call = None):
        self.name = name
        self.command = command
        self.prep_call = prep_call
    
    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)
    
    def __str__(self):
        return self.name

def print_options(options):
    print()
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()

def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options

def get_option_choice(options):
    choice = input('Choose an option:')

    while not option_choice_is_valid(choice,options):
        print('Invalid Choice')
        choice = input('Choose an option:')

    return options[choice.upper()]

def get_user_intput(label, required = True):
    choice = input(f'Enter {label}:') or None
    if not choice and required:
        print('Choice Required')
        choice = input(f'Enter {label}:')
    return choice

def get_new_bookmark_data():
    return {
        'title': get_user_intput('Title'),
        'url': get_user_intput('URL'),
        'notes': get_user_intput('Notes', False)
        }

def get_bookmark_id_for_deletion():
    return get_user_intput('ID')


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)

def loop():

    options = OrderedDict({'A': Option('Add Bookmark', 
                                        commands.AddBookmarkCommand(),
                                        prep_call=get_new_bookmark_data),
                            'B': Option('List bookmarks by date', 
                                        commands.ListBookmarksCommand()),
                            'T': Option('List bookmarks by title',
                                        commands.ListBookmarksCommand(order_by='title')),
                                'D': Option('Delete a bookmark',
                                            commands.DeleteBookmarkCommand(),
                                            get_bookmark_id_for_deletion), 
                            'Q': Option('Quit', commands.QuitCommand())})

    clear_screen()
    print_options(options)

    choice = get_option_choice(options)

    clear_screen()
    choice.choose()

    _ = input('Press enter to return to main menu')

if __name__ == "__main__":
    commands.CreateBookmarksTableCommand().execute()

    while True:
        loop()
        
        



