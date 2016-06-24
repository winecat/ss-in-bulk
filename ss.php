<?php

/**
 * ss.php
 * 批量导入 Shadowsocks 配置
 * by @cjli
 */

# 1. 先获得 Mac OS X 下 Shadowsocks 的配置的数组格式
// $ss_json = file_get_contents( 'test/ss.json' ) ;

// $ss_arr  = json_decode( $ss_json, true ) ;

// print_r( $ss_arr ) ;    // 通过数组查看默认配置规律

# 2. 处理基本配置文件并生成格式化的数组
$servers      = file_get_contents( 'ss.cnf' ) ;
$servers      = explode( "\n", $servers ) ;
$profiles     = array() ;
$default_node = 0 ;    // 默认节点

foreach ($servers as $k => $v) {
	if (!preg_match('/^#+/', $v) && !empty($v)) {
		# 判断有无配置默认节点
		if (preg_match('/ *default_node *= *\d */', $v)) {
			$default_node = explode('=', $v) ;
			$default_node = intval(trim($default_node[1])) ;
		} else {
			# 使用正则表达式检查配置文件每行格式是否正确
			// ...

			# 将每行配置拆分成几个数据项
			$server     = explode(' ', $v) ;
			/**
			 * !!! 不能直接在此循环中直接一次性添加到 $profiles 数组, 否则会报 illegal offset type error
			 * 错误的写法:
			 *          $profiles[] = array(
			 *          		['password']    => $server[3] ,
			 *          		['method']      => $server[2] ,
			 *          		['server_port'] => $server[1] ,
			 *          		['remarks']     => $server[4] ,
			 *          		['server']      => $server[0] ,
			 *	         ) ;
			 */
			$profiles[] = getFormattedArr($server) ;
		}
	}
}

$server_cnt    = count($profiles) ;    // 节点的个数

# 错误处理: 如果没有默认配置则提示
$selected = '' ;    // 保存默认选中的服务器信息
if ($server_cnt <= $default_node) {
	echo 'Notice: 默认配置无效' ;
	$default_node = 0 ;
	$selected     = $profiles[0] ;
} else {
	$selected     = $profiles[$default_node] ;
}

$new_arr       = array(
	'current'  => $default_node ,
	'profiles' => $profiles
	) ;

# 3. 将数组转化为 JSON 后使用 Base64 编码
// !!! 注意这里一定加上 JSON_UNESCAPED_UNICODE 参数(PHP Version > 5.4)来规避自动 UNICODE 转码问题导致的密码格式与配置文件不符合的问题
$ss_conf = base64_encode(json_encode($new_arr, JSON_UNESCAPED_UNICODE)) ;

# 4.1 将生成的 Base64 字符串保存到文件 (手动)
// date_default_timezone_set( 'Asia/Shanghai' ) ;
// file_put_contents( date('Y-m-d-His').'.ss.x'.$server_cnt, $ss_conf ) ;

# 4.2 将生成的 Base64 字符串替换掉 ss.xml 中 <data> 标签中的信息 (自动)
$pattern  = '/<data>\s*[\w|=|\+|\/]*\s*<\/data>/' ;
$subject  = file_get_contents( 'ss.xml' ) ;
$replace  = "<data>\n\t" ;
$replace .= $ss_conf ;
$replace .= "\n\t</data>" ;
$data     = preg_replace($pattern, $replace, $subject) ;

# 5. 将默认选中的配置保存到相应的标签组(如果有)
if (!empty($selected)) {
	# 替换默认加密方式
	$ptn_encry  = '/<key>proxy encryption<\/key>\s+<string>.*<\/string>/' ;
	$rpl_encry  = "<key>proxy encryption</key>\n\t<string>" ;
	$rpl_encry .= $selected['method'] ;
	$rpl_encry .= '</string>' ;
	// $data       = preg_replace($ptn_encry, $rpl_encry, $data) ;

	# 替换默认服务器地址
	$ptn_ip     = '/<key>proxy ip<\/key>\s+<string>.*<\/string>/' ;
	$rpl_ip     = "<key>proxy ip</key>\n\t<string>" ;
	$rpl_ip    .= $selected['server'] ;
	$rpl_ip    .= '</string>' ;
	// $data       = preg_replace($ptn_ip, $rpl_ip, $data) ;

	# 替换默认密码
	$ptn_pwd    = '/<key>proxy password<\/key>\s+<string>.*<\/string>/' ;
	$rpl_pwd    = "<key>proxy password</key>\n\t<string>" ;
	$rpl_pwd   .= $selected['password'] ;
	$rpl_pwd   .= '</string>' ;
	// $data       = preg_replace($ptn_pwd, $rpl_pwd, $data) ;

	# 替换默认端口
	$ptn_port   = '/<key>proxy port<\/key>\s+<string>.*<\/string>/' ;
	$rpl_port   = "<key>proxy port</key>\n\t<string>" ;
	$rpl_port  .= $selected['server_port'] ;
	$rpl_port  .= '</string>' ;

	$data       = preg_replace(
		array(
			$ptn_encry  ,
			$ptn_ip     ,
			$ptn_pwd    ,
			$ptn_port ) ,
		array(
			$rpl_encry  ,
			$rpl_ip     ,
			$rpl_pwd    ,
			$rpl_port ) ,

	$data) ;
}

# 6. 替换旧的 ss.xml
file_put_contents( 'ss.xml', $data) ;

/**
 * 重新获得一个格式化的数组
 * by @cjli
 */
function getFormattedArr($server) {
	$arr = array() ;

	$arr['password']    = $server[3] ;
    $arr['method']      = $server[2] ;
    $arr['server_port'] = $server[1] ;
    $arr['remarks']     = $server[4] ;
    $arr['server']      = $server[0] ;

	return $arr ;
}
