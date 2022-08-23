[[ $- != *i* ]] && return

# General Aliases
alias vi="nvim"
alias ls="ls --color=auto"
alias top="btop"

# Xbps Aliases
alias xu="doas xbps-install -Su"
alias xi="doas xbps-install"
alias xr="doas xbps-remove -R"
alias xq="xbps-query -Rs"
alias xl="xbps-query -l"

# Looking
PS1='[\u@\h \W]\$ '
