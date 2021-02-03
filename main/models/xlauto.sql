-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.21 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win32
-- HeidiSQL 版本:                  10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 xlauto 的数据库结构
DROP DATABASE IF EXISTS `xlauto`;
CREATE DATABASE IF NOT EXISTS `xlauto` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `xlauto`;

-- 导出  表 xlauto.host_instance 结构
DROP TABLE IF EXISTS `host_instance`;
CREATE TABLE IF NOT EXISTS `host_instance` (
  `host_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_ip` varchar(50) NOT NULL,
  `host_name` varchar(50) DEFAULT NULL,
  `host_port` int(11) DEFAULT NULL,
  `host_type_key` varchar(50) NOT NULL,
  `host_project` varchar(50) DEFAULT NULL,
  `is_remove` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`host_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.host_instance 的数据：~11 rows (大约)
DELETE FROM `host_instance`;
/*!40000 ALTER TABLE `host_instance` DISABLE KEYS */;
INSERT INTO `host_instance` (`host_id`, `host_ip`, `host_name`, `host_port`, `host_type_key`, `host_project`, `is_remove`, `comment`) VALUES
	(1, '192.168.10.134', '测试主机', 22, 'docker', '1', 1, NULL),
	(2, '192.168.10.133', NULL, 22, '', '', 1, NULL),
	(3, '192.168.10.134', NULL, 22, '', '', 1, NULL),
	(4, '192.168.10.135', NULL, 22, '', '', 1, NULL),
	(5, '192.168.154', NULL, 22, '', '', 1, NULL),
	(6, '192.168.155', NULL, 22, '', '', 1, NULL),
	(7, '192.168.156', NULL, 22, '', '', 1, NULL),
	(8, '192.168.10.154', NULL, 22, '', '', 1, NULL),
	(9, '192.168.10.133', '哦哦哦哦', 22, '', '1', NULL, NULL),
	(10, '192.168.10.156', NULL, 22, '', '', NULL, NULL),
	(11, '192.168.20.154', NULL, 22, '', '', NULL, NULL);
/*!40000 ALTER TABLE `host_instance` ENABLE KEYS */;

-- 导出  表 xlauto.host_server_software 结构
DROP TABLE IF EXISTS `host_server_software`;
CREATE TABLE IF NOT EXISTS `host_server_software` (
  `server_software_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) DEFAULT NULL,
  `soft_type` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `soft_port` int(11) DEFAULT NULL,
  `start_soft_cmd` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `stop_soft_cmd` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `restart_soft_cmd` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `soft_log_path` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `software_install_id` int(11) DEFAULT NULL,
  `is_remove` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `modify_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `comments` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`server_software_id`),
  KEY `ix_server_software_host_id` (`host_id`),
  KEY `ix_server_software_soft_type` (`soft_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.host_server_software 的数据：~0 rows (大约)
DELETE FROM `host_server_software`;
/*!40000 ALTER TABLE `host_server_software` DISABLE KEYS */;
/*!40000 ALTER TABLE `host_server_software` ENABLE KEYS */;

-- 导出  表 xlauto.host_users 结构
DROP TABLE IF EXISTS `host_users`;
CREATE TABLE IF NOT EXISTS `host_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_pass` varchar(50) NOT NULL,
  `user_role` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- 正在导出表  xlauto.host_users 的数据：~11 rows (大约)
DELETE FROM `host_users`;
/*!40000 ALTER TABLE `host_users` DISABLE KEYS */;
INSERT INTO `host_users` (`user_id`, `host_id`, `user_name`, `user_pass`, `user_role`) VALUES
	(1, 1, 'root', '661602611BD6C5A7B531121B4BCC8535', 'root'),
	(2, 2, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(3, 3, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(4, 4, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(5, 5, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(6, 6, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(7, 7, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(8, 8, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(9, 9, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(10, 10, 'root', 'C717530F41F320757B4AA1BFAF11C42E', 'root'),
	(11, 11, 'root', 'B64F565CC75C7E036777C13B854A76BB', 'root');
/*!40000 ALTER TABLE `host_users` ENABLE KEYS */;

-- 导出  表 xlauto.projects 结构
DROP TABLE IF EXISTS `projects`;
CREATE TABLE IF NOT EXISTS `projects` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(50) DEFAULT NULL,
  `project_code` varchar(50) DEFAULT NULL,
  `controller_ip` varchar(50) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `is_remove` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `modify_time` datetime DEFAULT NULL,
  `comments` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.projects 的数据：~0 rows (大约)
DELETE FROM `projects`;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` (`project_id`, `project_name`, `project_code`, `controller_ip`, `order_id`, `is_remove`, `create_time`, `modify_time`, `comments`) VALUES
	(1, '湖北hk机房', 'CBH', '19.25.6.7', NULL, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;

-- 导出  表 xlauto.script_file_cabinet 结构
DROP TABLE IF EXISTS `script_file_cabinet`;
CREATE TABLE IF NOT EXISTS `script_file_cabinet` (
  `script_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `script_file_path` varchar(300) DEFAULT NULL,
  `script_file_name` varchar(50) DEFAULT NULL,
  `script_file_group` varchar(50) DEFAULT NULL,
  `script_file_type` varchar(50) DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `modify_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `comment` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`script_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='脚本主表';

-- 正在导出表  xlauto.script_file_cabinet 的数据：~0 rows (大约)
DELETE FROM `script_file_cabinet`;
/*!40000 ALTER TABLE `script_file_cabinet` DISABLE KEYS */;
INSERT INTO `script_file_cabinet` (`script_file_id`, `script_file_path`, `script_file_name`, `script_file_group`, `script_file_type`, `create_time`, `modify_time`, `comment`) VALUES
	(1, 'C:\\Users\\Kk\\Desktop\\开发代码\\XLauto\\main\\src/data\\scriptfiles\\b2c98548-9894-11ea-a689-001a7dda7113', 'test.sh', 'favorites', 'python', '2020-05-18 07:18:21', '2020-05-18 17:29:11', NULL);
/*!40000 ALTER TABLE `script_file_cabinet` ENABLE KEYS */;

-- 导出  表 xlauto.script_file_execute_event 结构
DROP TABLE IF EXISTS `script_file_execute_event`;
CREATE TABLE IF NOT EXISTS `script_file_execute_event` (
  `script_file_execute_event_id` int(11) NOT NULL AUTO_INCREMENT,
  `script_execute_event_batch_id` varchar(50) DEFAULT NULL,
  `script_file_id` int(11) DEFAULT NULL,
  `execute_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `execute_end_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `execute_result` tinyint(4) DEFAULT NULL COMMENT 'sys_code.script_file_execute_result_ype   1为成功，0为失败',
  `script_file_content` mediumtext,
  `host_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`script_file_execute_event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=latin1 COMMENT='脚本执行事件表';

-- 正在导出表  xlauto.script_file_execute_event 的数据：~26 rows (大约)
DELETE FROM `script_file_execute_event`;
/*!40000 ALTER TABLE `script_file_execute_event` DISABLE KEYS */;
INSERT INTO `script_file_execute_event` (`script_file_execute_event_id`, `script_execute_event_batch_id`, `script_file_id`, `execute_time`, `execute_end_time`, `execute_result`, `script_file_content`, `host_id`) VALUES
	(46, '2bae8300-a63c-11ea-9a7b-38d547addffb', 0, '2020-06-04 16:20:27', '2020-06-04 16:20:27', -1, 'sh: /tmp2bbb24a4-a63c-11ea-b699-38d547addffb: No such file or directory', 1),
	(47, '1b9077d0-a63d-11ea-a8c1-38d547addffb', 0, '2020-06-04 16:27:11', '2020-06-04 16:27:11', -1, 'sh: /tmp1b97509c-a63d-11ea-a4fd-38d547addffb: No such file or directory', 1),
	(48, '58775d92-a63d-11ea-acf2-38d547addffb', 0, '2020-06-04 16:28:50', '2020-06-04 16:28:50', 0, '', 1),
	(49, 'bbb8986e-a63d-11ea-9842-38d547addffb', 0, '2020-06-04 16:31:36', '2020-06-04 16:31:36', -1, 'sh: /tmpbbca181c-a63d-11ea-8f6c-38d547addffb: No such file or directory', 1),
	(50, 'fe239e64-a63d-11ea-95dd-38d547addffb', 0, '2020-06-04 16:33:28', '2020-06-04 16:33:48', -1, 'sh: /tmpfe3066c8-a63d-11ea-aef1-38d547addffb: No such file or directory', 1),
	(51, '49007c36-a63e-11ea-9214-38d547addffb', 0, '2020-06-04 16:35:33', '2020-06-04 16:35:33', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(52, 'fda7261c-aa21-11ea-aafa-38d547addffb', 0, '2020-06-09 15:23:06', '2020-06-09 15:23:06', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(53, 'af80bce2-aa26-11ea-8008-38d547addffb', 0, '2020-06-09 15:56:42', '2020-06-09 15:56:42', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(54, 'caca4ba6-aa26-11ea-b807-38d547addffb', 0, '2020-06-09 15:57:28', '2020-06-09 15:57:38', 1, 'PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.64 bytes from 192.168.1.1: icmp_seq=1 ttl=127 time=0.403 ms64 bytes from 192.168.1.1: icmp_seq=2 ttl=127 time=0.249 ms64 bytes from 192.168.1.1: icmp_seq=3 ttl=127 time=0.972 ms64 bytes from 192.168.1.1: icmp_seq=4 ttl=127 time=0.363 ms64 bytes from 192.168.1.1: icmp_seq=5 ttl=127 time=0.399 ms64 bytes from 192.168.1.1: icmp_seq=6 ttl=127 time=0.351 ms64 bytes from 192.168.1.1: icmp_seq=7 ttl=127 time=0.652 ms64 bytes from 192.168.1.1: icmp_seq=8 ttl=127 time=0.292 ms64 bytes from 192.168.1.1: icmp_seq=9 ttl=127 time=0.421 ms64 bytes from 192.168.1.1: icmp_seq=10 ttl=127 time=0.347 ms64 bytes from 192.168.1.1: icmp_seq=11 ttl=127 time=0.293 ms64 bytes from 192.168.1.1: icmp_seq=12 ttl=127 time=0.995 ms64 bytes from 192.168.1.1: icmp_seq=13 ttl=127 time=4.07 ms64 bytes from 192.168.1.1: icmp_seq=14 ttl=127 time=5.70 ms64 bytes from 192.168.1.1: icmp_seq=15 ttl=127 time=1.39 ms64 bytes from 192.168.1.1: icmp_seq=16 ttl=127 time=0.345 ms64 bytes from 192.168.1.1: icmp_seq=17 ttl=127 time=1.33 ms64 bytes from 192.168.1.1: icmp_seq=18 ttl=127 time=1.54 ms64 bytes from 192.168.1.1: icmp_seq=19 ttl=127 time=7.64 ms64 bytes from 192.168.1.1: icmp_seq=20 ttl=127 time=0.794 ms--- 192.168.1.1 ping statistics ---20 packets transmitted, 20 received, 0% packet loss, time 19012msrtt min/avg/max/mdev = 0.249/1.428/7.645/1.963 ms', 1),
	(55, 'b8b65e24-aa27-11ea-8dce-38d547addffb', 0, '2020-06-09 16:04:07', '2020-06-09 16:05:38', 1, 'PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.64 bytes from 192.168.1.1: icmp_seq=1 ttl=127 time=0.415 ms64 bytes from 192.168.1.1: icmp_seq=2 ttl=127 time=0.250 ms64 bytes from 192.168.1.1: icmp_seq=3 ttl=127 time=0.251 ms64 bytes from 192.168.1.1: icmp_seq=4 ttl=127 time=1.72 ms64 bytes from 192.168.1.1: icmp_seq=5 ttl=127 time=6.67 ms64 bytes from 192.168.1.1: icmp_seq=6 ttl=127 time=2.50 ms64 bytes from 192.168.1.1: icmp_seq=7 ttl=127 time=2.57 ms64 bytes from 192.168.1.1: icmp_seq=8 ttl=127 time=0.251 ms64 bytes from 192.168.1.1: icmp_seq=9 ttl=127 time=1.50 ms64 bytes from 192.168.1.1: icmp_seq=10 ttl=127 time=1.92 ms64 bytes from 192.168.1.1: icmp_seq=11 ttl=127 time=0.309 ms64 bytes from 192.168.1.1: icmp_seq=12 ttl=127 time=0.277 ms64 bytes from 192.168.1.1: icmp_seq=13 ttl=127 time=0.314 ms64 bytes from 192.168.1.1: icmp_seq=14 ttl=127 time=0.381 ms64 bytes from 192.168.1.1: icmp_seq=15 ttl=127 time=0.346 ms64 bytes from 192.168.1.1: icmp_seq=16 ttl=127 time=0.336 ms64 bytes from 192.168.1.1: icmp_seq=17 ttl=127 time=0.334 ms64 bytes from 192.168.1.1: icmp_seq=18 ttl=127 time=10.1 ms64 bytes from 192.168.1.1: icmp_seq=19 ttl=127 time=0.285 ms64 bytes from 192.168.1.1: icmp_seq=20 ttl=127 time=0.316 ms64 bytes from 192.168.1.1: icmp_seq=21 ttl=127 time=0.266 ms64 bytes from 192.168.1.1: icmp_seq=22 ttl=127 time=1.43 ms64 bytes from 192.168.1.1: icmp_seq=23 ttl=127 time=0.468 ms64 bytes from 192.168.1.1: icmp_seq=24 ttl=127 time=0.289 ms64 bytes from 192.168.1.1: icmp_seq=25 ttl=127 time=0.300 ms64 bytes from 192.168.1.1: icmp_seq=26 ttl=127 time=0.585 ms64 bytes from 192.168.1.1: icmp_seq=27 ttl=127 time=0.289 ms64 bytes from 192.168.1.1: icmp_seq=28 ttl=127 time=0.313 ms64 bytes from 192.168.1.1: icmp_seq=29 ttl=127 time=0.591 ms64 bytes from 192.168.1.1: icmp_seq=30 ttl=127 time=0.257 ms64 bytes from 192.168.1.1: icmp_seq=31 ttl=127 time=0.651 ms64 bytes from 192.168.1.1: icmp_seq=32 ttl=127 time=0.274 ms64 bytes from 192.168.1.1: icmp_seq=33 ttl=127 time=0.300 ms64 bytes from 192.168.1.1: icmp_seq=34 ttl=127 time=0.359 ms64 bytes from 192.168.1.1: icmp_seq=35 ttl=127 time=0.334 ms64 bytes from 192.168.1.1: icmp_seq=36 ttl=127 time=0.475 ms64 bytes from 192.168.1.1: icmp_seq=37 ttl=127 time=0.312 ms64 bytes from 192.168.1.1: icmp_seq=38 ttl=127 time=0.322 ms64 bytes from 192.168.1.1: icmp_seq=39 ttl=127 time=0.307 ms64 bytes from 192.168.1.1: icmp_seq=40 ttl=127 time=7.75 ms64 bytes from 192.168.1.1: icmp_seq=41 ttl=127 time=7.50 ms64 bytes from 192.168.1.1: icmp_seq=42 ttl=127 time=1.51 ms64 bytes from 192.168.1.1: icmp_seq=43 ttl=127 time=0.447 ms64 bytes from 192.168.1.1: icmp_seq=44 ttl=127 time=0.293 ms64 bytes from 192.168.1.1: icmp_seq=45 ttl=127 time=0.287 ms64 bytes from 192.168.1.1: icmp_seq=46 ttl=127 time=0.363 ms64 bytes from 192.168.1.1: icmp_seq=47 ttl=127 time=0.275 ms64 bytes from 192.168.1.1: icmp_seq=48 ttl=127 time=0.289 ms64 bytes from 192.168.1.1: icmp_seq=49 ttl=127 time=0.278 ms64 bytes from 192.168.1.1: icmp_seq=50 ttl=127 time=0.402 ms64 bytes from 192.168.1.1: icmp_seq=51 ttl=127 time=0.334 ms64 bytes from 192.168.1.1: icmp_seq=52 ttl=127 time=0.653 ms64 bytes from 192.168.1.1: icmp_seq=53 ttl=127 time=0.384 ms64 bytes from 192.168.1.1: icmp_seq=54 ttl=127 time=0.317 ms64 bytes from 192.168.1.1: icmp_seq=55 ttl=127 time=0.425 ms64 bytes from 192.168.1.1: icmp_seq=56 ttl=127 time=4.35 ms64 bytes from 192.168.1.1: icmp_seq=57 ttl=127 time=0.576 ms64 bytes from 192.168.1.1: icmp_seq=58 ttl=127 time=0.294 ms64 bytes from 192.168.1.1: icmp_seq=59 ttl=127 time=0.312 ms64 bytes from 192.168.1.1: icmp_seq=60 ttl=127 time=0.285 ms64 bytes from 192.168.1.1: icmp_seq=61 ttl=127 time=0.308 ms64 bytes from 192.168.1.1: icmp_seq=62 ttl=127 time=0.268 ms64 bytes from 192.168.1.1: icmp_seq=63 ttl=127 time=0.276 ms64 bytes from 192.168.1.1: icmp_seq=64 ttl=127 time=0.289 ms64 bytes from 192.168.1.1: icmp_seq=65 ttl=127 time=2.03 ms64 bytes from 192.168.1.1: icmp_seq=66 ttl=127 time=5.50 ms64 bytes from 192.168.1.1: icmp_seq=67 ttl=127 time=2.74 ms64 bytes from 192.168.1.1: icmp_seq=68 ttl=127 time=5.73 ms64 bytes from 192.168.1.1: icmp_seq=69 ttl=127 time=0.602 ms64 bytes from 192.168.1.1: icmp_seq=70 ttl=127 time=1.92 ms64 bytes from 192.168.1.1: icmp_seq=71 ttl=127 time=0.848 ms64 bytes from 192.168.1.1: icmp_seq=72 ttl=127 time=0.408 ms64 bytes from 192.168.1.1: icmp_seq=73 ttl=127 time=0.316 ms64 bytes from 192.168.1.1: icmp_seq=74 ttl=127 time=0.315 ms64 bytes from 192.168.1.1: icmp_seq=75 ttl=127 time=4.07 ms64 bytes from 192.168.1.1: icmp_seq=76 ttl=127 time=0.343 ms64 bytes from 192.168.1.1: icmp_seq=77 ttl=127 time=0.285 ms64 bytes from 192.168.1.1: icmp_seq=78 ttl=127 time=0.286 ms64 bytes from 192.168.1.1: icmp_seq=79 ttl=127 time=10.2 ms64 bytes from 192.168.1.1: icmp_seq=80 ttl=127 time=1.02 ms64 bytes from 192.168.1.1: icmp_seq=81 ttl=127 time=0.272 ms64 bytes from 192.168.1.1: icmp_seq=82 ttl=127 time=0.298 ms64 bytes from 192.168.1.1: icmp_seq=83 ttl=127 time=8.47 ms64 bytes from 192.168.1.1: icmp_seq=84 ttl=127 time=6.57 ms64 bytes from 192.168.1.1: icmp_seq=85 ttl=127 time=0.367 ms64 bytes from 192.168.1.1: icmp_seq=86 ttl=127 time=7.87 ms64 bytes from 192.168.1.1: icmp_seq=87 ttl=127 time=0.298 ms64 bytes from 192.168.1.1: icmp_seq=88 ttl=127 time=5.99 ms64 bytes from 192.168.1.1: icmp_seq=89 ttl=127 time=1.16 ms64 bytes from 192.168.1.1: icmp_seq=90 ttl=127 time=8.22 ms64 bytes from 192.168.1.1: icmp_seq=91 ttl=127 time=4.44 ms64 bytes from 192.168.1.1: icmp_seq=92 ttl=127 time=0.376 ms64 bytes from 192.168.1.1: icmp_seq=93 ttl=127 time=2.79 ms64 bytes from 192.168.1.1: icmp_seq=94 ttl=127 time=0.257 ms64 bytes from 192.168.1.1: icmp_seq=95 ttl=127 time=0.580 ms64 bytes from 192.168.1.1: icmp_seq=96 ttl=127 time=0.367 ms64 bytes from 192.168.1.1: icmp_seq=97 ttl=127 time=0.467 ms64 bytes from 192.168.1.1: icmp_seq=98 ttl=127 time=0.390 ms64 bytes from 192.168.1.1: icmp_seq=99 ttl=127 time=0.962 ms64 bytes from 192.168.1.1: icmp_seq=100 ttl=127 time=3.34 ms--- 192.168.1.1 ping statistics ---100 packets transmitted, 100 received, 0% packet loss, time 99050msrtt min/avg/max/mdev = 0.250/1.578/10.220/2.432 ms', 1),
	(56, 'cd7c3324-aa37-11ea-95dc-38d547addffb', 0, '2020-06-09 17:59:14', '2020-06-09 17:59:14', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(57, '051ad9ee-aa38-11ea-aed8-38d547addffb', 0, '2020-06-09 18:00:47', '2020-06-09 18:00:47', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(58, '233b4d62-aa38-11ea-97f5-38d547addffb', 0, '2020-06-09 18:01:38', '2020-06-09 18:01:38', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(59, 'f7d810cc-aba1-11ea-99f2-38d547addffb', 0, '2020-06-11 13:11:42', '2020-06-11 13:11:42', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(60, '2038a93a-aba2-11ea-9d33-38d547addffb', 0, '2020-06-11 13:12:50', '2020-06-11 13:12:50', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(61, '4311d8a2-aba3-11ea-998e-38d547addffb', 0, '2020-06-11 13:20:58', '2020-06-11 13:20:58', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(62, 'db65089e-aba4-11ea-b8cb-38d547addffb', 0, '2020-06-11 13:32:23', '2020-06-11 13:32:23', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(63, 'ef39b092-aba6-11ea-a597-38d547addffb', 0, '2020-06-11 13:47:15', '2020-06-11 13:47:15', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(64, 'e73c0864-abb0-11ea-a26d-38d547addffb', 0, '2020-06-11 14:58:37', '2020-06-11 14:58:37', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(65, 'b9cb38c2-abb5-11ea-9ae1-38d547addffb', 0, '2020-06-11 15:33:08', '2020-06-11 15:33:08', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(66, '89ecd1f0-abb6-11ea-a871-38d547addffb', 0, '2020-06-11 15:38:57', '2020-06-11 15:38:57', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(67, '36d317d2-abb7-11ea-84c6-38d547addffb', 0, '2020-06-11 15:43:48', '2020-06-11 15:43:48', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(68, 'd35e19f4-abb7-11ea-9eee-38d547addffb', 0, '2020-06-11 15:48:10', '2020-06-11 15:48:10', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(69, 'd306fa74-abb8-11ea-ac85-38d547addffb', 0, '2020-06-11 15:55:19', '2020-06-11 15:55:19', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(70, '610a2ea2-af66-11ea-8a1f-001a7dda7113', 3, '2020-06-16 08:15:14', '2020-06-16 08:15:14', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1),
	(71, '82c582ee-af66-11ea-a231-001a7dda7113', 3, '2020-06-16 08:16:11', '2020-06-16 08:16:11', 1, 'anaconda-ks.cfgens_messageheaderens_util_logos_info.json', 1);
/*!40000 ALTER TABLE `script_file_execute_event` ENABLE KEYS */;

-- 导出  表 xlauto.software_conf 结构
DROP TABLE IF EXISTS `software_conf`;
CREATE TABLE IF NOT EXISTS `software_conf` (
  `software_conf_id` int(11) NOT NULL AUTO_INCREMENT,
  `software_package_id` int(11) NOT NULL,
  `software_conf_name` varchar(50) DEFAULT NULL,
  `software_conf_type` varchar(50) DEFAULT NULL COMMENT 'sys_code.software_conf__type',
  `software_conf_path` varchar(500) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`software_conf_id`),
  KEY `software_package_id` (`software_package_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COMMENT='软件配置文件，配置模板，待替换参数的配置文件';

-- 正在导出表  xlauto.software_conf 的数据：~2 rows (大约)
DELETE FROM `software_conf`;
/*!40000 ALTER TABLE `software_conf` DISABLE KEYS */;
INSERT INTO `software_conf` (`software_conf_id`, `software_package_id`, `software_conf_name`, `software_conf_type`, `software_conf_path`, `comment`) VALUES
	(5, 2, 'ansible.zip', NULL, 'C:/Users/Kk/Desktop/开发代码/XLauto/main/package/software/111/1111/ansible.zip', NULL),
	(8, 1, 'ansible.zip', NULL, 'C:/Users/Kk/Desktop/开发代码/XLauto/main/package/software/4.4.0/zabbix/ansible.zip', NULL);
/*!40000 ALTER TABLE `software_conf` ENABLE KEYS */;

-- 导出  表 xlauto.software_conf_parameter 结构
DROP TABLE IF EXISTS `software_conf_parameter`;
CREATE TABLE IF NOT EXISTS `software_conf_parameter` (
  `software_conf_parameter_id` int(11) NOT NULL AUTO_INCREMENT,
  `software_conf_id` int(11) NOT NULL COMMENT 'software_conf.software_conf_id',
  `replacement_entry` varchar(50) NOT NULL COMMENT '参数',
  `default_value` varchar(50) NOT NULL COMMENT '默认值',
  `comment` varchar(50) NOT NULL,
  PRIMARY KEY (`software_conf_parameter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='配置文件参数替换';

-- 正在导出表  xlauto.software_conf_parameter 的数据：~0 rows (大约)
DELETE FROM `software_conf_parameter`;
/*!40000 ALTER TABLE `software_conf_parameter` DISABLE KEYS */;
/*!40000 ALTER TABLE `software_conf_parameter` ENABLE KEYS */;

-- 导出  表 xlauto.software_conf_parameter_replace 结构
DROP TABLE IF EXISTS `software_conf_parameter_replace`;
CREATE TABLE IF NOT EXISTS `software_conf_parameter_replace` (
  `software_conf_parameter_replace_id` int(11) NOT NULL AUTO_INCREMENT,
  `software_conf_parameter_id` int(11) NOT NULL COMMENT 'software_conf.software_conf_id',
  `replacement_value` varchar(50) NOT NULL,
  `comment` varchar(50) NOT NULL,
  PRIMARY KEY (`software_conf_parameter_replace_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='配置文件参数替换';

-- 正在导出表  xlauto.software_conf_parameter_replace 的数据：~0 rows (大约)
DELETE FROM `software_conf_parameter_replace`;
/*!40000 ALTER TABLE `software_conf_parameter_replace` DISABLE KEYS */;
/*!40000 ALTER TABLE `software_conf_parameter_replace` ENABLE KEYS */;

-- 导出  表 xlauto.software_package 结构
DROP TABLE IF EXISTS `software_package`;
CREATE TABLE IF NOT EXISTS `software_package` (
  `software_package_id` int(11) NOT NULL AUTO_INCREMENT,
  `software_name` varchar(50) DEFAULT NULL COMMENT '软件名称 会下/package/software/下创建一个软件目录',
  `software_versions` varchar(50) DEFAULT NULL,
  `package_path` varchar(200) DEFAULT NULL COMMENT '安装包位置，项目/package/software/{{software_versions}}/{{software_name}}下面',
  `software_package_zip_type` varchar(50) DEFAULT NULL COMMENT 'sys_code.sys_type=software_package_zip_type',
  `package_storage_type` varchar(50) DEFAULT NULL COMMENT 'sys_code.sys_type=package_storage_type',
  `comment` varchar(50) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`software_package_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COMMENT='软件安装表';

-- 正在导出表  xlauto.software_package 的数据：~5 rows (大约)
DELETE FROM `software_package`;
/*!40000 ALTER TABLE `software_package` DISABLE KEYS */;
INSERT INTO `software_package` (`software_package_id`, `software_name`, `software_versions`, `package_path`, `software_package_zip_type`, `package_storage_type`, `comment`) VALUES
	(10, 'nginx', '1.19.6', 'C:\\Users\\Kk\\Desktop\\开发代码\\XLauto\\main\\package\\software\\nginx\\1.19.6', 'tgz', 'local', NULL);
/*!40000 ALTER TABLE `software_package` ENABLE KEYS */;

-- 导出  表 xlauto.software_package_install_event 结构
DROP TABLE IF EXISTS `software_package_install_event`;
CREATE TABLE IF NOT EXISTS `software_package_install_event` (
  `software_package_install_event_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) NOT NULL COMMENT 'host_instance.host_id',
  `software_package_id` int(11) DEFAULT NULL COMMENT 'software_package.software_package_id',
  `execute_result` varchar(1000) DEFAULT NULL COMMENT '执行结果收集',
  `server_software_action_type` char(50) DEFAULT NULL COMMENT '执行动作 code_key：sys_code.code_type=server_software_action_type',
  `execute_status` char(50) DEFAULT NULL COMMENT '执行动作 code_key：sys_code.code_type=tandard_execution_results',
  `execute_time` char(50) DEFAULT NULL COMMENT '第一次执行时间',
  `re_execute_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次执行时间',
  PRIMARY KEY (`software_package_install_event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.software_package_install_event 的数据：~0 rows (大约)
DELETE FROM `software_package_install_event`;
/*!40000 ALTER TABLE `software_package_install_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `software_package_install_event` ENABLE KEYS */;

-- 导出  表 xlauto.system_function 结构
DROP TABLE IF EXISTS `system_function`;
CREATE TABLE IF NOT EXISTS `system_function` (
  `system_function_id` int(11) NOT NULL AUTO_INCREMENT,
  `system_name` varchar(50) NOT NULL COMMENT '操作系统名称',
  `system_version` varchar(50) NOT NULL COMMENT '系统版本',
  `function_type` varchar(50) NOT NULL COMMENT '文件新增、文件内容追加、指定内容替换、执行命令',
  `system_content` mediumtext NOT NULL COMMENT '操作文本内容',
  `system_content_file` varchar(200) DEFAULT NULL COMMENT '文件文本路径',
  `system_action` varchar(50) NOT NULL COMMENT '动作归类',
  `system_action_name` varchar(50) DEFAULT NULL COMMENT '动作归类名',
  `action_service_switch` tinyint(4) DEFAULT NULL COMMENT '服务类动作，启动，停止标记。1启动，2停止',
  `force` tinyint(4) DEFAULT NULL COMMENT '标记为码值，禁止全部删除',
  `order_by` int(11) DEFAULT NULL COMMENT '排序',
  `comment` varchar(100) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`system_function_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COMMENT='系统命令表';

-- 正在导出表  xlauto.system_function 的数据：~15 rows (大约)
DELETE FROM `system_function`;
/*!40000 ALTER TABLE `system_function` DISABLE KEYS */;
INSERT INTO `system_function` (`system_function_id`, `system_name`, `system_version`, `function_type`, `system_content`, `system_content_file`, `system_action`, `system_action_name`, `action_service_switch`, `force`, `order_by`, `comment`) VALUES
	(1, 'centos', '8', 'cmd', 'systemctl start firewalld', '', 'firewalld_control', '', 1, 1, 100, NULL),
	(2, 'centos', '8', 'cmd', 'systemctl stop firewalld ', '', 'firewalld_control', '', 0, 1, 100, NULL),
	(3, 'centos', '8', 'cmd', 'sed -i "s/^SELINUX\\=.*/SELINUX\\=disabled/g" /etc/selinux/config ;setenforce 0', '', 'selinux_control', '', 0, 1, 100, NULL),
	(4, 'centos', '8', 'cmd', 'sed -i "s/^SELINUX\\=.*/SELINUX\\=enforcing/g" /etc/selinux/config ;setenforce 1', '', 'selinux_control', '', 1, 1, 100, NULL),
	(5, 'centos', '8', 'cmd', 'sed -i "s/^SELINUX\\=.*/SELINUX\\=permissive/g" /etc/selinux/config; ;setenforce Permissive', '', 'selinux_control', '', 2, 1, 100, NULL),
	(6, 'centos', '8', 'addfile', '[kuebrnetes]\nname=Kubernetes Repository\nbaseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/\nenabled=1\ngpgcheck=0', '/etc/yum.repos.d/Kubernetes_Repository.repo', 'kubernetes_repository', 'Aliyun-Centos8', NULL, 1, 99, NULL),
	(7, 'centos', '8', 'addfile', '[kuebrnetes]\nname=Kubernetes Repository\nbaseurl=https://packages.cloud.google.com/yum/repos/kuebrnetes-el7-x86_64/\nenabled=1\ngpgcheck=0', '/etc/yum.repos.d/Kubernetes_Repository.repo', 'kubernetes_repository', '官方-Centos8', NULL, 1, 99, NULL),
	(8, 'centos', '8', 'cmd', 'yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes', '', 'yum_install_kubelet', 'kubelet安装', NULL, 1, 98, NULL),
	(9, 'centos', '8', 'cmd', 'systemctl enable docker', '', 'enable_docker', 'docker开机启动', 1, NULL, 97, NULL),
	(10, 'centos', '8', 'cmd', 'systemctl start docker', '', 'start_docker', 'docker服务启动', 1, NULL, 97, NULL),
	(11, 'centos', '8', 'cmd', 'systemctl enable kubelet', '', 'enable_kubelet', 'kubelet开机启动', 1, NULL, 97, NULL),
	(12, 'centos', '8', 'cmd', 'systemctl start kubelet', '', 'start_kubelet', 'kubelet服务启动', 1, NULL, 97, NULL),
	(14, 'centos', '8', 'cmdp', 'find {{ directory }} -mtime +{{ day }} -name "{{ filename }}" -exec rm -rf {} \\;', '', 'rm_day_file', '删除多少天前的文件', NULL, NULL, 0, NULL),
	(15, 'centos', '8', 'addfile', '[docker-ce-stable]\r\nname=Docker CE Stable - $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/$basearch/stable\r\nenabled=1\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-stable-debuginfo]\r\nname=Docker CE Stable - Debuginfo $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/debug-$basearch/stable\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-stable-source]\r\nname=Docker CE Stable - Sources\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/source/stable\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-edge]\r\nname=Docker CE Edge - $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/$basearch/edge\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-edge-debuginfo]\r\nname=Docker CE Edge - Debuginfo $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/debug-$basearch/edge\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-edge-source]\r\nname=Docker CE Edge - Sources\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/source/edge\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-test]\r\nname=Docker CE Test - $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/$basearch/test\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-test-debuginfo]\r\nname=Docker CE Test - Debuginfo $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/debug-$basearch/test\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-test-source]\r\nname=Docker CE Test - Sources\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/source/test\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-nightly]\r\nname=Docker CE Nightly - $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/$basearch/nightly\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-nightly-debuginfo]\r\nname=Docker CE Nightly - Debuginfo $basearch\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/debug-$basearch/nightly\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n\r\n[docker-ce-nightly-source]\r\nname=Docker CE Nightly - Sources\r\nbaseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/source/nightly\r\nenabled=0\r\ngpgcheck=1\r\ngpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/gpg\r\n', '/etc/yum.repos.d/docker-ce.repo', 'docker_repository', 'docker-Aliyun-Centos8', NULL, NULL, 99, NULL),
	(16, 'centos', '8', 'cmd', 'yum install https://download.docker.com/linux/fedora/30/x86_64/stable/Packages/containerd.io-1.2.6-3.3.fc30.x86_64.rpm -y; yum install docker-ce -y', '', 'yum_install_docker', 'docker安装', NULL, NULL, 98, NULL);
/*!40000 ALTER TABLE `system_function` ENABLE KEYS */;

-- 导出  表 xlauto.sys_code 结构
DROP TABLE IF EXISTS `sys_code`;
CREATE TABLE IF NOT EXISTS `sys_code` (
  `code_id` int(11) NOT NULL AUTO_INCREMENT,
  `code_key` varchar(500) DEFAULT NULL,
  `code_name` varchar(50) NOT NULL,
  `code_type` varchar(50) NOT NULL,
  `f_code` varchar(50) DEFAULT NULL,
  `order_queue` smallint(6) DEFAULT NULL,
  `comments` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`code_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.sys_code 的数据：~28 rows (大约)
DELETE FROM `sys_code`;
/*!40000 ALTER TABLE `sys_code` DISABLE KEYS */;
INSERT INTO `sys_code` (`code_id`, `code_key`, `code_name`, `code_type`, `f_code`, `order_queue`, `comments`) VALUES
	(1, 'docker', '容器', 'host_type', NULL, NULL, NULL),
	(2, 'nginx', 'Nginx', 'host_type', NULL, NULL, NULL),
	(3, 'root', '管理员', 'user_role_type', NULL, NULL, NULL),
	(4, 'soft', '软件用户', 'user_role_type', NULL, NULL, NULL),
	(5, NULL, '全部组', 'execute_script_group', NULL, NULL, NULL),
	(6, NULL, '全部类型', 'execute_script_type', NULL, NULL, NULL),
	(7, 'python', 'Python脚本', 'execute_script_type', NULL, NULL, NULL),
	(8, 'shell', 'Shell脚本', 'execute_script_type', NULL, NULL, NULL),
	(9, 'favorites', '收藏', 'execute_script_group', NULL, NULL, NULL),
	(10, '1', '成功', 'standard_execution_results', NULL, NULL, NULL),
	(11, '-1', '失败', 'standard_execution_results', NULL, NULL, NULL),
	(12, '2', '警告', 'standard_execution_results', NULL, NULL, NULL),
	(15, 'Zabbix_agentd', 'Zabbix客户端', 'server_software_type', NULL, NULL, NULL),
	(16, 'install', '安装', 'server_software_action_type', NULL, NULL, NULL),
	(17, 'uninstall', '卸载', 'server_software_action_type', NULL, NULL, NULL),
	(18, 'reinstall', '覆盖安装', 'server_software_action_type', NULL, NULL, NULL),
	(19, 'rpm', 'RPM', 'software_install_type', NULL, NULL, NULL),
	(20, 'make', 'Make', 'software_install_type', NULL, NULL, NULL),
	(21, 'unzip', 'Unzip', 'software_install_type', NULL, NULL, NULL),
	(22, 'zip', 'zip', 'software_package_zip_type', NULL, NULL, NULL),
	(23, 'gz', 'gz', 'software_package_zip_type', NULL, NULL, NULL),
	(24, 'tgz', 'tgz', 'software_package_zip_type', NULL, NULL, NULL),
	(25, 'tar', 'tar', 'software_package_zip_type', NULL, NULL, NULL),
	(26, 'local', '本地', 'package_storage_type', NULL, NULL, NULL),
	(27, 'repository', 'URL仓库', 'package_storage_type', NULL, NULL, NULL),
	(28, 'conf', 'conf', 'software_conf_type', NULL, NULL, NULL),
	(29, 'xml', 'xml', 'software_conf_type', NULL, NULL, NULL),
	(30, 'template', '模板', 'software_conf_type', NULL, NULL, NULL);
/*!40000 ALTER TABLE `sys_code` ENABLE KEYS */;

-- 导出  表 xlauto.sys_menu 结构
DROP TABLE IF EXISTS `sys_menu`;
CREATE TABLE IF NOT EXISTS `sys_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `path` varchar(50) DEFAULT NULL,
  `icon` varchar(50) DEFAULT NULL,
  `statu` int(11) DEFAULT NULL,
  `comments` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.sys_menu 的数据：~11 rows (大约)
DELETE FROM `sys_menu`;
/*!40000 ALTER TABLE `sys_menu` DISABLE KEYS */;
INSERT INTO `sys_menu` (`id`, `parent_id`, `title`, `name`, `path`, `icon`, `statu`, `comments`) VALUES
	(1, NULL, '主页', 'home', NULL, 'el-icon-s-home', NULL, NULL),
	(2, NULL, '工具', 'instrument', NULL, 'el-icon-s-cooperation', NULL, NULL),
	(3, 2, '网络', 'network', '/network', 'el-icon-place', NULL, NULL),
	(4, 2, '主机', 'host_m', '/host_m', 'el-icon-place', NULL, NULL),
	(5, NULL, '部署', 'deploy', NULL, 'el-icon-s-claim', NULL, NULL),
	(7, 5, '软件部署', 'soft_d', '/soft_d', 'el-icon-s-claim', NULL, NULL),
	(8, NULL, '管理', 'manage', NULL, 'el-icon-s-claim', NULL, NULL),
	(9, 8, 'Zabbix', 'zabbix', '/zabbix', 'el-icon-s-claim', NULL, NULL),
	(10, 8, '软件配置', 'soft_s', '/soft_s', 'el-icon-s-claim', NULL, NULL),
	(100, NULL, '维护', 'info_record', NULL, 'el-icon-s-custom', NULL, NULL),
	(101, 100, '配置', 'setting', '/setting', 'el-icon-s-custom', NULL, NULL);
/*!40000 ALTER TABLE `sys_menu` ENABLE KEYS */;

-- 导出  表 xlauto.zabbix_agent 结构
DROP TABLE IF EXISTS `zabbix_agent`;
CREATE TABLE IF NOT EXISTS `zabbix_agent` (
  `zabbix_install_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) DEFAULT NULL COMMENT 'host_instance.host_id',
  `install_info` mediumtext,
  `execute_result` tinyint(4) DEFAULT NULL COMMENT '-1错误、1成功、2警告、3未知',
  `zabbix_host_name` varchar(50) DEFAULT NULL COMMENT '主机名',
  `zabbix_hostid` varchar(100) DEFAULT NULL,
  `zabbix_groupids` varchar(100) DEFAULT NULL COMMENT '主机组',
  `zabbix_templateids` varchar(100) DEFAULT NULL COMMENT '关联模板',
  `monitored_by_proxy_id` varchar(50) DEFAULT NULL COMMENT '代理ID',
  `operate_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`zabbix_install_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- 正在导出表  xlauto.zabbix_agent 的数据：~0 rows (大约)
DELETE FROM `zabbix_agent`;
/*!40000 ALTER TABLE `zabbix_agent` DISABLE KEYS */;
INSERT INTO `zabbix_agent` (`zabbix_install_id`, `host_id`, `install_info`, `execute_result`, `zabbix_host_name`, `zabbix_hostid`, `zabbix_groupids`, `zabbix_templateids`, `monitored_by_proxy_id`, `operate_time`) VALUES
	(11, 9, NULL, NULL, '192.168.10.133.CBH', '11857', '40', '10074', '0', '2020-12-10 10:28:17');
/*!40000 ALTER TABLE `zabbix_agent` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
