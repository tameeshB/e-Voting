-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: evoting
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add bucket',1,'add_bucket'),(2,'Can change bucket',1,'change_bucket'),(3,'Can delete bucket',1,'delete_bucket'),(4,'Can view bucket',1,'view_bucket'),(5,'Can add candidate',2,'add_candidate'),(6,'Can change candidate',2,'change_candidate'),(7,'Can delete candidate',2,'delete_candidate'),(8,'Can view candidate',2,'view_candidate'),(9,'Can add config vars',3,'add_configvars'),(10,'Can change config vars',3,'change_configvars'),(11,'Can delete config vars',3,'delete_configvars'),(12,'Can view config vars',3,'view_configvars'),(13,'Can add positions',4,'add_positions'),(14,'Can change positions',4,'change_positions'),(15,'Can delete positions',4,'delete_positions'),(16,'Can view positions',4,'view_positions'),(17,'Can add token id',5,'add_tokenid'),(18,'Can change token id',5,'change_tokenid'),(19,'Can delete token id',5,'delete_tokenid'),(20,'Can view token id',5,'view_tokenid'),(21,'Can add token no',6,'add_tokenno'),(22,'Can change token no',6,'change_tokenno'),(23,'Can delete token no',6,'delete_tokenno'),(24,'Can view token no',6,'view_tokenno'),(25,'Can add voters',7,'add_voters'),(26,'Can change voters',7,'change_voters'),(27,'Can delete voters',7,'delete_voters'),(28,'Can view voters',7,'view_voters'),(29,'Can add votes1',8,'add_votes1'),(30,'Can change votes1',8,'change_votes1'),(31,'Can delete votes1',8,'delete_votes1'),(32,'Can view votes1',8,'view_votes1'),(33,'Can add Token Dashboard',6,'add_tokendash'),(34,'Can change Token Dashboard',6,'change_tokendash'),(35,'Can delete Token Dashboard',6,'delete_tokendash'),(36,'Can view Token Dashboard',6,'view_tokendash'),(37,'Can add log entry',10,'add_logentry'),(38,'Can change log entry',10,'change_logentry'),(39,'Can delete log entry',10,'delete_logentry'),(40,'Can view log entry',10,'view_logentry'),(41,'Can add permission',11,'add_permission'),(42,'Can change permission',11,'change_permission'),(43,'Can delete permission',11,'delete_permission'),(44,'Can view permission',11,'view_permission'),(45,'Can add group',12,'add_group'),(46,'Can change group',12,'change_group'),(47,'Can delete group',12,'delete_group'),(48,'Can view group',12,'view_group'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add content type',14,'add_contenttype'),(54,'Can change content type',14,'change_contenttype'),(55,'Can delete content type',14,'delete_contenttype'),(56,'Can view content type',14,'view_contenttype'),(57,'Can add session',15,'add_session'),(58,'Can change session',15,'change_session'),(59,'Can delete session',15,'delete_session'),(60,'Can view session',15,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$CkvuPt4uJa1H$rEzT38jcxNTEhLHFRT6zk3p3vTMe7S+pKR69cvkw1xg=','2018-11-06 20:37:44.471054',1,'tameeshb','','','me@tameesh.in',1,1,'2018-11-06 20:32:27.016107');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-06 21:38:57.255033','publish','ConfigVars object (publish)',2,'[{\"changed\": {\"fields\": [\"varKey\"]}}]',3,1),(2,'2018-11-06 21:39:07.375773','1','ConfigVars object (1)',3,'',3,1),(3,'2018-11-06 21:49:42.323520','1','BTech-2rdYr-Boys',1,'[{\"added\": {}}]',1,1),(4,'2018-11-06 21:49:57.020664','2','BTech-3rdYr-Boys',1,'[{\"added\": {}}]',1,1),(5,'2018-11-06 21:50:19.602834','3','BTech-3rdYr-Girls',1,'[{\"added\": {}}]',1,1),(6,'2018-11-06 21:50:36.004564','4','BTech-2rdYr-Girls',1,'[{\"added\": {}}]',1,1),(7,'2018-11-06 21:51:18.913906','Vice-President','Vice-President',1,'[{\"added\": {}}]',4,1),(8,'2018-11-06 21:51:56.566932','Tech-Sec-3rd-Year','Tech-Sec-3rd-Year',1,'[{\"added\": {}}]',4,1),(9,'2018-11-06 21:52:13.248977','Tech-Sec-2rd-Year','Tech-Sec-2rd-Year',1,'[{\"added\": {}}]',4,1),(10,'2018-11-06 21:52:37.016963','1','Parth Kulkarni:Vice-President',1,'[{\"added\": {}}]',2,1),(11,'2018-11-06 21:52:49.151860','2','Parth Kulkarni:Tech-Sec-3rd-Year',1,'[{\"added\": {}}]',2,1),(12,'2018-11-06 21:53:14.456099','3','Anushree Jain:Tech-Sec-3rd-Year',1,'[{\"added\": {}}]',2,1),(13,'2018-11-06 21:53:27.059394','4','Manish Kumar:Vice-President',1,'[{\"added\": {}}]',2,1),(14,'2018-11-06 21:54:22.380704','5','Zena Foster:Tech-Sec-3rd-Year',1,'[{\"added\": {}}]',2,1),(15,'2018-11-06 21:54:35.177147','6','Alexandre Carney:Vice-President',1,'[{\"added\": {}}]',2,1),(16,'2018-11-06 21:55:10.842758','4','Enrique Shaffer:Vice-President',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',2,1),(17,'2018-11-06 21:55:32.134666','3','Anushree JainVernon Gates:Tech-Sec-3rd-Year',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',2,1),(18,'2018-11-06 21:55:53.871992','2','Skylar Bautista:Tech-Sec-3rd-Year',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',2,1),(19,'2018-11-06 21:56:01.518982','3','Vernon Gates:Tech-Sec-3rd-Year',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',2,1),(20,'2018-11-06 21:56:07.562819','1','Skylar Bautista:Vice-President',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (10,'admin','logentry'),(12,'auth','group'),(11,'auth','permission'),(13,'auth','user'),(14,'contenttypes','contenttype'),(1,'polls','bucket'),(2,'polls','candidate'),(3,'polls','configvars'),(4,'polls','positions'),(9,'polls','tokendash'),(5,'polls','tokenid'),(6,'polls','tokenno'),(7,'polls','voters'),(8,'polls','votes1'),(15,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-06 20:28:21.777384'),(2,'auth','0001_initial','2018-11-06 20:28:22.077538'),(3,'admin','0001_initial','2018-11-06 20:28:22.172031'),(4,'admin','0002_logentry_remove_auto_add','2018-11-06 20:28:22.186605'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-06 20:28:22.204365'),(6,'contenttypes','0002_remove_content_type_name','2018-11-06 20:28:22.293933'),(7,'auth','0002_alter_permission_name_max_length','2018-11-06 20:28:22.332459'),(8,'auth','0003_alter_user_email_max_length','2018-11-06 20:28:22.371939'),(9,'auth','0004_alter_user_username_opts','2018-11-06 20:28:22.390240'),(10,'auth','0005_alter_user_last_login_null','2018-11-06 20:28:22.440925'),(11,'auth','0006_require_contenttypes_0002','2018-11-06 20:28:22.444574'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-06 20:28:22.465812'),(13,'auth','0008_alter_user_username_max_length','2018-11-06 20:28:22.523449'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-06 20:28:22.577728'),(15,'polls','0001_initial','2018-11-06 20:28:22.848153'),(16,'sessions','0001_initial','2018-11-06 20:28:22.873812');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('foxnp9eqx6fqm7i08rnw8mo0pzcqyi3x','MTMzMzExODgwYWJmYjc5MjM1OTExZjMwMTZhMGMxYWE0MmQ1MjczNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNzRiNzYwNWE5NTE1MzYzOTM2ODA4ODEwYTBhODA3NWZlZDZmZDU0In0=','2018-11-20 20:37:44.475612');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_bucket`
--

DROP TABLE IF EXISTS `polls_bucket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_bucket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bucketName` varchar(200) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `hostel` varchar(3) NOT NULL,
  `year` int(11) NOT NULL,
  `course` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_bucket`
--

LOCK TABLES `polls_bucket` WRITE;
/*!40000 ALTER TABLE `polls_bucket` DISABLE KEYS */;
INSERT INTO `polls_bucket` VALUES (1,'BTech-2rdYr-Boys','M','BH1',17,'B'),(2,'BTech-3rdYr-Boys','M','BH1',16,'B'),(3,'BTech-3rdYr-Girls','F','GH1',16,'B'),(4,'BTech-2rdYr-Girls','F','GH1',17,'B');
/*!40000 ALTER TABLE `polls_bucket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_candidate`
--

DROP TABLE IF EXISTS `polls_candidate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_candidate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `votes` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `agendaURL` varchar(1000) DEFAULT NULL,
  `position_id` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_candidate_position_id_b6efa2b5_fk_polls_positions_posID` (`position_id`),
  CONSTRAINT `polls_candidate_position_id_b6efa2b5_fk_polls_positions_posID` FOREIGN KEY (`position_id`) REFERENCES `polls_positions` (`posid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_candidate`
--

LOCK TABLES `polls_candidate` WRITE;
/*!40000 ALTER TABLE `polls_candidate` DISABLE KEYS */;
INSERT INTO `polls_candidate` VALUES (1,0,'Skylar Bautista','https://iitp.ac.in/','Vice-President'),(2,0,'Skylar Bautista','https://iitp.ac.in/','Tech-Sec-3rd-Year'),(3,0,'Vernon Gates','https://iitp.ac.in/','Tech-Sec-3rd-Year'),(4,0,'Enrique Shaffer','https://iitp.ac.in/','Vice-President'),(5,0,'Zena Foster','https://iitp.ac.in/','Tech-Sec-3rd-Year'),(6,0,'Alexandre Carney','https://iitp.ac.in/','Vice-President');
/*!40000 ALTER TABLE `polls_candidate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_configvars`
--

DROP TABLE IF EXISTS `polls_configvars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_configvars` (
  `varKey` varchar(10) NOT NULL,
  `varVal` int(11) NOT NULL,
  PRIMARY KEY (`varKey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_configvars`
--

LOCK TABLES `polls_configvars` WRITE;
/*!40000 ALTER TABLE `polls_configvars` DISABLE KEYS */;
INSERT INTO `polls_configvars` VALUES ('ongoing',0),('publish',1);
/*!40000 ALTER TABLE `polls_configvars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_positions`
--

DROP TABLE IF EXISTS `polls_positions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_positions` (
  `posID` varchar(200) NOT NULL,
  `posName` varchar(200) NOT NULL,
  PRIMARY KEY (`posID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_positions`
--

LOCK TABLES `polls_positions` WRITE;
/*!40000 ALTER TABLE `polls_positions` DISABLE KEYS */;
INSERT INTO `polls_positions` VALUES ('Tech-Sec-2rd-Year','Tech Sec, 2rd Year'),('Tech-Sec-3rd-Year','Tech Sec, 3rd Year'),('Vice-President','Vice President');
/*!40000 ALTER TABLE `polls_positions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_positions_buckets`
--

DROP TABLE IF EXISTS `polls_positions_buckets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_positions_buckets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `positions_id` varchar(200) NOT NULL,
  `bucket_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `polls_positions_buckets_positions_id_bucket_id_e74a2bf3_uniq` (`positions_id`,`bucket_id`),
  KEY `polls_positions_buckets_bucket_id_c1b92358_fk_polls_bucket_id` (`bucket_id`),
  CONSTRAINT `polls_positions_buck_positions_id_70340fee_fk_polls_pos` FOREIGN KEY (`positions_id`) REFERENCES `polls_positions` (`posid`),
  CONSTRAINT `polls_positions_buckets_bucket_id_c1b92358_fk_polls_bucket_id` FOREIGN KEY (`bucket_id`) REFERENCES `polls_bucket` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_positions_buckets`
--

LOCK TABLES `polls_positions_buckets` WRITE;
/*!40000 ALTER TABLE `polls_positions_buckets` DISABLE KEYS */;
INSERT INTO `polls_positions_buckets` VALUES (7,'Tech-Sec-2rd-Year',1),(8,'Tech-Sec-2rd-Year',4),(5,'Tech-Sec-3rd-Year',2),(6,'Tech-Sec-3rd-Year',3),(1,'Vice-President',1),(2,'Vice-President',2),(3,'Vice-President',3),(4,'Vice-President',4);
/*!40000 ALTER TABLE `polls_positions_buckets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_tokenid`
--

DROP TABLE IF EXISTS `polls_tokenid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_tokenid` (
  `tokenID` varchar(5) NOT NULL,
  `used` tinyint(1) NOT NULL,
  PRIMARY KEY (`tokenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_tokenid`
--

LOCK TABLES `polls_tokenid` WRITE;
/*!40000 ALTER TABLE `polls_tokenid` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_tokenid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_tokenno`
--

DROP TABLE IF EXISTS `polls_tokenno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_tokenno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tokenNo` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_tokenno`
--

LOCK TABLES `polls_tokenno` WRITE;
/*!40000 ALTER TABLE `polls_tokenno` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_tokenno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_voters`
--

DROP TABLE IF EXISTS `polls_voters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_voters` (
  `voterID` varchar(200) NOT NULL,
  `hasVoted` tinyint(1) NOT NULL,
  PRIMARY KEY (`voterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_voters`
--

LOCK TABLES `polls_voters` WRITE;
/*!40000 ALTER TABLE `polls_voters` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_voters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_votes1`
--

DROP TABLE IF EXISTS `polls_votes1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `polls_votes1` (
  `tokenID` varchar(5) NOT NULL,
  `voteJSON` varchar(1000) NOT NULL,
  `signature` varchar(100) NOT NULL,
  PRIMARY KEY (`tokenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_votes1`
--

LOCK TABLES `polls_votes1` WRITE;
/*!40000 ALTER TABLE `polls_votes1` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_votes1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-07  3:38:06
