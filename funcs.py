app_funcs = {
    'code': 'VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;',
}

ffmpeg_funcs = {
    'ffmpegcopy': 'ffmpeg -i $1 -vcodec copy -acodec copy $2',
    'ffmpegcopy2': 'ffmpeg -i $1 -c:v libx264 -c:a libvo_aacenc -b:a 128k $2',
    'ffmpegcopy3': 'ffmpeg -i $1 -c:v libx264 $2'
}