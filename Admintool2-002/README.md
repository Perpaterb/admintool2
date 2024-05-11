nano ~/.bashrc
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0

https://www.beekeeperstudio.io/blog/building-electron-windows-ubuntu-wsl2

npm install

to run 
npm run electron:serve