# custom user alias
alias ll='ls -l'
alias la='ls -lA'
alias l='ls -CF'
alias gits='git status -uno'
alias gitc='git commit -m'
alias gitl='git log --all --decorate --oneline --graph'

function runc() {
    printf "Removing old files"
    rm "$1.exe"
    printf "Building and running $1.c\n\n"
    gcc --version
    gcc -v "$1.c" -o "$1.exe" && printf "Build successful.\n\n" && ./"$1.exe"

    printf "\n\n\nProgram terminated with exit code $?\n"
}


