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

# Ask the user which aliases to include
aliases_stage = dict()
for idx, aliases_set in enumerate(aliases_list):
    # print('\n\n\n')
    print(f'SET {idx + 1} out of {len(aliases_list)}')
    print(f'Do you wish to include: {aliases_set["__desc__"]}?')
    
    print()
    for alias in aliases_set:
        if not alias.startswith('__'):
            print(' ‣  {:12}: {}'.format(alias, aliases_set[alias]))
    print()

    if input('y/n: ') == 'y':
        aliases_stage.update(aliases_set)
    
    print('\n\n')

# Make output directory
print('Ouputing to \'output/\' folder . . .')
if not os.path.exists('output'):
    os.makedirs('output')

# Generate file
print(f'Generating file for {sh_sel} . . .')
out_fname = f'output/.{sh_sel}_aliases'
with open(out_fname, 'w', encoding='utf-8') as outfile:
    for alias in aliases_stage:
        if not alias.startswith('__'):
            outfile.write(alias_format[sh_sel].format(alias, aliases_stage[alias]))
            outfile.write('\n')

print('Done!')