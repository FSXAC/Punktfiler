shell_aliases = {

    # List directories
    'l': 'ls -lh',

    # Disk utilization
    'du0': 'du -sh',
    'du1': 'du -h -d 1',

    # Find file by name in current directory
    'f': 'find . -name'
}

git_aliases = {
    'gog': 'git log --oneline --decorate --graph',
    'gst': 'git status'
}

youtube_aliases = {
    'ytd': 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bet[ext=mp4]/best"',
    'ytdm4a': 'youtube-dl -x --audio-format m4a'
}

tmux_aliases = {
    'tls': 'tmux ls',
    'tns': 'tmux new -s',
    'tks': 'tmux kill-session -t',
    'ta': 'tmux a -t'
}

cd_aliases = {
    'elec400m': r'cd ~/Documents/2020\ UBC/ELEC\ 400M/',
    'apsc450': r'cd ~/Documents/2020\ UBC/APSC\ 450/',
    'ubc': r'cd ~/Documents/2021\ UBC/',
    'fsxac': 'cd ~/Programming/FSXAC.github.io'
}

ssh_aliases = {
    'sshece': 'ssh mhe@ssh.ece.ubc.ca',
    'sshecesoc': 'ssh mhe@ssh-soc.ece.ubc.ca'
}

elec402_aliases = {
    'new_proj': 'source /CMC/kits/AMSKIT616_GPDK/underg_install.csh',
    'setup_local': 'source setup_local.csh',
    'sl': 'source setup_local.csh',
    'modelsim': 'source /CMC/scripts/mentor.modelsim.10.7c.csh && vsim',
    'modelsim64': 'source /CMC/scripts/mentor.modelsim.10.7c.csh && vsim -64'
}

# ====================

aliases = {
    **shell_aliases,
    **git_aliases,
    **youtube_aliases,
    **tmux_aliases,
    **cd_aliases,
    **ssh_aliases,
    **elec402_aliases
}