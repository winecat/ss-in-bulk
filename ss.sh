## ShadowsocksX 批量配置 by @cjli
# 如果没有 ss.xml 请在确保具有相应权限下先执行如下命令:
# cp ~/Library/Preferences/clowwindy.ShadowsocksX.plist ~/
# plutil -convert xml1 clowwindy.ShadowsocksX.plist -o ss.xml

# 1. 读取配置文件 servers.conf 生成新的 Base64 配置字符串并替换掉 ss.xml 中的 <data> 标签
php -f ss.php

# 2. 将新的 ss.xml 转换为 plist
plutil -convert binary1 ss.xml -o clowwindy.ShadowsocksX.plist

# 3. 用新的 plist 替换掉原来的 plist
defaults import clowwindy.ShadowsocksX clowwindy.ShadowsocksX.plist

# 4. 然后重新打开 ShadowsockX ( End )
