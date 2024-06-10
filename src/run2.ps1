param ($mode, $text)

Start-Process "javac" -ArgumentList "Hash.java" -Wait -NoNewWindow
Start-Process "java" -ArgumentList "Hash $mode $text" -Wait -NoNewWindow

Remove-Item "Bitwise.class"
Remove-Item "Hash.class"
Remove-Item "Primes.class"