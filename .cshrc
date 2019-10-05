# Common .cshrc  will source the common which then sources your .cshrc.$Arch (e.g. .linux)
# Your .cshrc gets sourced for every terminal, your .login gets sourced once per login session.
#  Look under /usr/common for more details.
source /usr/common/Cshrc

# apply aliases
source ~/.csh_aliases

# apply custom prompt
set prompt = '[%T](%M) %~: '
