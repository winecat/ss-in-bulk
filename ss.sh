## ShadowsocksX 批量配置 by @cjli
# 如果没有 ss.xml 请在确保具有相应权限下先执行如下命令:
# cp ~/Library/Preferences/clowwindy.ShadowsocksX.plist ~/
# plutil -convert xml1 clowwindy.ShadowsocksX.plist -o ss.xml

date +%T-%Y/%m/%d

# 切换路径
filepath=$(cd "$(dirname "$0")"; pwd)
cd $filepath

# 0. 从MianVPN获取免费的SS账号 写入到配置文件
# python getFreeSs.py > ss.cnf
python proxyGetFreeSs.py > ss.cnf

# 0. 判断获取到的SS账号,如果未获取到中止运行
if [ "`md5 ss.cnf`" == 'MD5 (ss.cnf) = 68b329da9893e34099c7d8ad5cb9c940' ]; then
    exit 1
fi

# 0. 计算MD5 如果一致就不做更新 不一致保存新的MD5
#if [ "`md5 ss.cnf`" == "`cat md5.txt`" ]; then  
#	exit 1  
#fi
#md5 ss.cnf > md5.txt

# 1. 读取配置文件 servers.conf 生成新的 Base64 配置字符串并替换掉 ss.xml 中的 <data> 标签
php -f ss.php

# 2. 将新的 ss.xml 转换为 plist
plutil -convert binary1 ss.xml -o clowwindy.ShadowsocksX.plist

# 3. 用新的 plist 替换掉原来的 plist
defaults import clowwindy.ShadowsocksX clowwindy.ShadowsocksX.plist

# 4. 然后重新打开 ShadowsockX ( End )
killall ShadowsocksX 1>/dev/null 2>/dev/null
sleep 1s
open /Applications/ShadowsocksX.app/

# 返回路径
cd - >/dev/null
