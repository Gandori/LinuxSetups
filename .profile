#.profile by gandori
# ~/

# bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

#set i3 config
if [ -f "$HOME/linux_setup/i3/config" ]; then
	exec i3 -c ~/linux_setup/i3/config
fi
