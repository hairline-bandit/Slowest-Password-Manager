param ($file, $arg1, $arg2, $arg3, $arg4)

Start-Process "python" -ArgumentList "gloss.py $file $arg1 $arg2 $arg3 $arg4" -Wait -NoNewWindow
Start-Process "go" -ArgumentList "run 123123123123.go" -Wait -NoNewWindow

Remove-Item "123123123123.go"