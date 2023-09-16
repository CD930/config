[[ $- != *i* ]] && return

# General Aliases
alias vi="vis"
alias ls="ls -A --color=auto"
alias top="btop"

# Xbps Aliases
alias xu="doas xbps-install -Su"
alias xi="doas xbps-install"
alias xr="doas xbps-remove -R"
alias xq="xbps-query -Rs"
alias xl="xbps-query -l"

# Aesthetic
PS1='[\u@\h \W]\$ '
