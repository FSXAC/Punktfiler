import aliases
import sys
import os

aliases_list = [getattr(aliases, obj_name) for obj_name in dir(aliases) if not obj_name.startswith('__')]
# print(aliases_list)

# Alias for various shell scripts
alias_format = {
    'bash': 'alias {0}=\'{1}\'',
    'csh': 'alias {0} \'{1}\'',
    'tsch': 'alias {0} \'{1}\'',
    'zsh': 'alias {0}=\'{1}\'',
}

# Ask the user for which shell to use
sh_sel = None
while sh_sel not in alias_format:
    sh_sel = input(f'Select a shell: (one of { ", ".join([ *alias_format.keys(), "or q to quit" ]) }): ')

    # Quit
    if sh_sel.lower() == 'q':
        sys.exit(0)

# Make output directory
if not os.path.exists('output'):
    os.makedirs('output')

# Generate file
out_fname = f'.{sh_sel}_aliases'

