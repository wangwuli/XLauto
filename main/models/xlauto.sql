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
  `host_port` int(6) DEFAULT NULL,
  `host_type_key` varchar(50) NOT NULL,
  `host_project` varchar(50) DEFAULT NULL,
  `is_remove` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`host_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.host_instance 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `host_instance` DISABLE KEYS */;
INSERT INTO `host_instance` (`host_id`, `host_ip`, `host_name`, `host_port`, `host_type_key`, `host_project`, `is_remove`, `comment`) VALUES
	(1, '192.168.0.100', '测试主机', 22, 'docker', '1', NULL, NULL);
/*!40000 ALTER TABLE `host_instance` ENABLE KEYS */;

-- 导出  表 xlauto.host_users 结构
DROP TABLE IF EXISTS `host_users`;
CREATE TABLE IF NOT EXISTS `host_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_pass` varchar(50) NOT NULL,
  `user_role` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- 正在导出表  xlauto.host_users 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `host_users` DISABLE KEYS */;
INSERT INTO `host_users` (`user_id`, `host_id`, `user_name`, `user_pass`, `user_role`) VALUES
	(1, 1, 'root', '661602611BD6C5A7B531121B4BCC8535', 'root');
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
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` (`project_id`, `project_name`, `project_code`, `controller_ip`, `order_id`, `is_remove`, `create_time`, `modify_time`, `comments`) VALUES
	(1, '湖北hk机房', 'bq01', '19.25.6.7', NULL, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;

-- 导出  表 xlauto.server_software 结构
DROP TABLE IF EXISTS `server_software`;
CREATE TABLE IF NOT EXISTS `server_software` (
  `soft_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) DEFAULT NULL,
  `soft_type` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `soft_port` int(11) DEFAULT NULL,
  `start_soft_cmd` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `stop_soft_cmd` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `restart_soft_cmd` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `soft_log_path` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `is_remove` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `modify_time` datetime DEFAULT NULL,
  `comments` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`soft_id`),
  KEY `ix_server_software_host_id` (`host_id`),
  KEY `ix_server_software_soft_type` (`soft_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.server_software 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `server_software` DISABLE KEYS */;
/*!40000 ALTER TABLE `server_software` ENABLE KEYS */;

-- 导出  表 xlauto.sys_code 结构
DROP TABLE IF EXISTS `sys_code`;
CREATE TABLE IF NOT EXISTS `sys_code` (
  `code_id` int(11) NOT NULL AUTO_INCREMENT,
  `code_key` varchar(50) NOT NULL,
  `code_name` varchar(50) NOT NULL,
  `code_type` varchar(50) NOT NULL,
  `f_code` varchar(50) DEFAULT NULL,
  `order_queue` smallint(6) DEFAULT NULL,
  `comments` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`code_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.sys_code 的数据：~4 rows (大约)
/*!40000 ALTER TABLE `sys_code` DISABLE KEYS */;
INSERT INTO `sys_code` (`code_id`, `code_key`, `code_name`, `code_type`, `f_code`, `order_queue`, `comments`) VALUES
	(1, 'docker', '容器', 'host_type', NULL, NULL, NULL),
	(2, 'nginx', 'Nginx', 'host_type', NULL, NULL, NULL),
	(3, 'root', '管理员', 'user_role_type', NULL, NULL, NULL),
	(4, 'soft', '软件用户', 'user_role_type', NULL, NULL, NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- 正在导出表  xlauto.sys_menu 的数据：~5 rows (大约)
/*!40000 ALTER TABLE `sys_menu` DISABLE KEYS */;
INSERT INTO `sys_menu` (`id`, `parent_id`, `title`, `name`, `path`, `icon`, `statu`, `comments`) VALUES
	(1, NULL, '主页', 'home', NULL, 'el-icon-s-home', NULL, NULL),
	(2, NULL, '工具', 'instrument', NULL, 'el-icon-s-cooperation', NULL, NULL),
	(3, 2, '网络', 'network', '/network', 'el-icon-place', NULL, NULL),
	(4, 2, '主机', 'host_m', '/host_m', 'el-icon-place', NULL, NULL),
	(5, NULL, '部署', 'deploy', NULL, 'el-icon-s-claim', NULL, NULL),
	(6, NULL, '维护', 'info_record', NULL, 'el-icon-s-custom', NULL, NULL);
/*!40000 ALTER TABLE `sys_menu` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
