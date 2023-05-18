
GTK_DEBUG=interactive GTK_INSPECTOR_DISPLAY=:1 ./a $@
#x11          :0    is ok
#broadway and :0    not visible
#broadway and x11:0 failed
#broadway and broadway:0 failed
