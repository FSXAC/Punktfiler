alias l='ls -l'
alias la='ls -lA'

alias gits='git status'
alias gitc='git commit -m'
alias gitl='git log --all --decorate --oneline --graph'

# vscode shortcut
code () { VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;}

# ffmpeg shortcut
convert264() {
	if [ $# -eq 0 ]; then
		echo "Must provide the input file"
		exit 1
	fi
	filename=$(basename -- "$1")
	fname="${filename%.*}"
	echo "Converting $1 to $fname.mov"
	ffmpeg -i $1 -vcodec libx264 -crf 23 -c:a aac -pix_fmt yuv420p "./$fname.mov"
}
convert265() {
	if [ $# -eq 0]; then
		echo "Must provide the input file"
		exit 1
	fi
	filename=$(basename -- "$1")
	fname="${filename%.*}"
	echo "Converting $1 to $fname.mov"
	ffmpeg -i $1 -c:v libx265 -crf 23 -c:a aac -tag:v hvc1 -pix_fmt yuv420p "./$fname.mov"
}
fmcopy() {
	mv $2 "bk_$2"
	ffmpeg -i $1 -i "bk_$2" -map 1 -map_metadata 0 -c copy $2
}

# download youtube videos
alias ytd="youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'"
alias ytdmp3="youtube-dl -x --audio-format mp3"
alias ytdm4a="youtube-dl -x --audio-format m4a"

# python scripts
alias birthtime='python3 ~/.pyscripts/birthtime.py'
alias setbirthtime='python3 ~/.pyscripts/setbirthtime.py'
alias setbirthtimes='python3 ~/.pyscripts/groupsetbirthtime.py'

# running C programs
function runc() {
	printf "\033[2mRemoving old files\033[0m\n"
	if [[ -f "$1.o" ]]; then
		rm "$1.o"
	fi
	if [[ -f "$1.exe" ]]; then
		rm "$1.exe"
	fi

	if [[ -f "$1.c" ]]; then
		infile="$1.c"
	elif [[ -f "$1.cpp" ]]; then
		infile="$1.cpp"
	else
		printf "\033[91mCannot file specified file\033[0m\n"
		return 1
	fi

	printf "Building and running $1.c\n"
	gcc $infile -o "$1.exe" && printf "Build succesful.\n\033[0m" && ./"$1.exe"
	printf "\n\033[2mProgram terminated with exit code $?\n\033[0m"
}

# running C programs but for apsc160 (clear downloads folder before start)
alias PAUSE="read -p \"Press enter to continue . . .\""
function rc160() {
	rep=${2:-1}
	printf "CODE:\n\n"
	ccat "$1"
	printf "\n\nEND OF CODE\n"
	read
	gcc "$1" -o "$1.exe"
	rc=$?
	if [ $rc -eq 0 ]; then
		for (( i=0;i<$rep;i++ )); do ./"$1.exe"; done
		printf "\n\n\n"
		# rm -f *.c
		# rm -f *.cpp
		# rm -f *.exe
	else
		echo "Compilation Error"
	fi
}

# Turn on startup chime (set to %01 to turn off)
# sudo nvram StartupMute=%00
