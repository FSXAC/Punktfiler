shell_aliases = {
    '__desc__': 'Aliases for most shells',

    # List directories
    'l': 'ls -lh',

    # Disk utilization
    'du0': 'du -sh',
    'du1': 'du -h -d 1',
}

git_aliases = {
    '__desc__': 'Git alias commands',

    'gog': 'git log --oneline --decorate --graph',
    'gst': 'git status'
}

youtube_aliases = {
    '__desc__': 'Aliases to download content from YouTube (NOTE: must have \'youtube-dl\' installed!)',

    'ytd': 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bet[ext=mp4]/best"',
    'ytdm4a': 'youtube-dl -x --audio-format m4a'
}

tmux_aliases = {
    '__desc__': 'Terminal multiplexer (TMUX) aliases (NOTE: must have \'tmux\' installed!)',

    'tls': 'tmux ls',
    'tns': 'tmux new -s',
    'tks': 'tmux kill-session -t',
    'ta': 'tmux a -t'
}

cd_aliases = {
    '__desc__': 'For quickly going to often visited paths (for personal use)',

    'elec400m': r'cd ~/Documents/2020\ UBC/ELEC\ 400M/',
    'apsc450': r'cd ~/Documents/2020\ UBC/APSC\ 450/',
    'ubc': r'cd ~/Documents/2021\ UBC/',
    'fsxac': 'cd ~/Programming/FSXAC.github.io'
}

ssh_aliases = {
    '__desc__': 'For quickly connecting to SSH servers (for personal use)',

    'sshece': 'ssh mhe@ssh.ece.ubc.ca',
    'sshecesoc': 'ssh mhe@ssh-soc.ece.ubc.ca'
}

elec402_aliases = {
    '__desc__': 'Command aliases for running CAD tools related to UBC ELEC 402 (NOTE: requires user to be on UBC ECE\'s SSH-SOC server!)',

    'new_proj': 'source /CMC/kits/AMSKIT616_GPDK/underg_install.csh',
    'setup_local': 'source setup_local.csh',
    'sl': 'source setup_local.csh',
    'modelsim': 'source /CMC/scripts/mentor.modelsim.10.7c.csh && vsim',
    'modelsim64': 'source /CMC/scripts/mentor.modelsim.10.7c.csh && vsim -64'
}

macos_aliases = {
    '__desc__': 'Aliases exclusive for macOS terminal (NOTE: requires macOS!)',

    # Find file by name in current directory
    'f': 'find . -name',

    # mouse acceleration
    'mouse_acc_off': 'defaults write -g com.apple.mouse.scaling -1',
    'mouse_acc_on': 'defaults write -g com.apple.mouse.scaling 2.5',

    # Startup chime
    'start_chime_off': 'sudo nvram StartupMute=%01',
    'start_chime_on': 'sudo nvram StartupMute=%00'
}

macos_app_aliases = {
    '__desc__': 'Aliases for launching apps on macOS (NOTE: requires macOS and the corresponding applications already installed!)',

    'typora': 'open -a Typora'
}

# ====================

# aliases = {
#     **shell_aliases,
#     **git_aliases,
#     **youtube_aliases,
#     **tmux_aliases,
#     **cd_aliases,
#     **ssh_aliases,
#     **elec402_aliases,
#     **macos_aliases
# }