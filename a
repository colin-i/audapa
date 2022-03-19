
if [ -n "$1" ]; then
z=$1
else
z="python"
fi

if [ -n "$2" ]; then
x=$2
else
x=0
fi

if [ -z "$GTK_DEBUG" ]; then
if [ -n "$3" ]; then
GDK_BACKEND=broadway BROADWAY_DISPLAY=:$x GTK_DEBUG=$3 $z -m audapa.main
exit
fi
fi

if [ -n "$3" ]; then
GTK_DEBUG+=",$3"
fi
GDK_BACKEND=broadway BROADWAY_DISPLAY=:$x $z -m audapa.main
