## SS-In-Bulk

Mac OS X（现 macOS）下批量导入 ShadowsocksX 节点配置工具。

#### 1. 在 ss.cnf 中填写好节点配置信息，格式如下：

```
# !!! Make Sure that the Line Break Style is LF(UNIX)
# eg: IP|Domain Port Method Password Remarks

123.123.123.123 6789 aes-256-cfb PASSWORD 联通优先

usa.domain.tk 9999 chacha20 PASSWORD 洛杉矶-chacha20

# More Servers ...
```

#### 2. 运行 ss.sh

```
./ss.sh
```

#### Notice

- PHP Version: 5.4+。
- ss.cnf 文件需要使用 UNIX 换行风格，即 LF 。
- 使用 `#` 打头的行为注释行。
- 每行一个完整 shadowsocks 服务器配置。
- 每个配置项（服务器地址、端口、加密方式、密码、备注）之间只能使用一个空格隔开, 单个配置项内不能含有空格。
- 确保文件权限正确。

#### LICENSE
MIT.
