# /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
# and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).

PATH="/usr/local/bin:/usr/bin:/bin"
EDITOR="/bin/vi"			# needed for packages like cron
test -z "$TERM" && TERM="vt100"	# Basic terminal capab. For screen etc.

if [ ! -e /etc/localtime -a ! -e /etc/TZ ]; then
	TZ="UTC"		# Time Zone. Look at http://theory.uwinnipeg.ca/gnu/glibc/libc_303.html 
				# for an explanation of how to set this to your local timezone.
	export TZ
fi

if [ "$HOME" = "/home/root" ]; then
   PATH=$PATH:/usr/local/sbin:/usr/sbin:/sbin
fi
if [ "$PS1" ]; then
# works for bash and ash (no other shells known to be in use here)
   PS1='\u@\h:\w\$ '
fi

if [ -d /etc/profile.d ]; then
  for i in /etc/profile.d/* ; do
    . $i
  done
  unset i
fi

if [ -x /usr/bin/resize ];then
  /usr/bin/resize >/dev/null
fi

export PATH PS1 OPIEDIR QPEDIR QTDIR EDITOR TERM


export JAVA_HOME=/jdk1.8.0_151
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export BUILDID=L3.14.28_201803_ST_PIDS_V005
export BUILDBOARD=imx6solosabresd

umask 022

