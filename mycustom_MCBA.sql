-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: mycustombusinessapp.com    Database: mycustom_MCBA
-- ------------------------------------------------------
-- Server version	5.7.23-23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `_id` int(11) NOT NULL AUTO_INCREMENT,
  `id_domain_only` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Fully qualified Domain Name',
  `name` text COLLATE utf8_unicode_ci NOT NULL,
  `baseURL` text COLLATE utf8_unicode_ci NOT NULL COMMENT 'include trailing "/"',
  `MCBA_Dir` text COLLATE utf8_unicode_ci NOT NULL,
  `Shop_Dir` text COLLATE utf8_unicode_ci NOT NULL,
  `url` text COLLATE utf8_unicode_ci NOT NULL,
  `gcm_project` text COLLATE utf8_unicode_ci,
  `gcm_api_key` text COLLATE utf8_unicode_ci,
  `active` int(11) NOT NULL DEFAULT '0',
  `update_count` int(11) NOT NULL,
  `promo_count` int(11) NOT NULL,
  `company_name` text COLLATE utf8_unicode_ci NOT NULL,
  `request_upgrade` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`_id`)
) ENGINE=MyISAM AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (6,'','Millers Tree Care','http://millerstreecare.com/','wp-content/plugins/MCBA-Wordpress/','','http://millerstreecare.com/wp-content/plugins/MCBA-Wordpress/','294283586502','AAAARISrK8Y:APA91bGfftTMVFV3KukvnC6WtDZcMmdsOVv5YER4Y7VypPRVXmkE_dxY2MWjoDbRJz0p_2n_JHZkeDe7E6gXGyGtCfe3OG_n5dF0wbuM0Ffw8BKssSz1iwkDH847HoasFjoXS7NmzG8F',0,0,0,'Tree Care By Robert Miller',0),(7,'','Zounds','','wp-content/plugins/MCBA-Wordpress/','','http://zoundsspringsflorida.com/wp-content/plugins/MCBA-Wordpress/','256348019034','AIzaSyBlIWOaSnawD_ux2i0XXyF1Sbrf6Gh2TNI',0,0,0,'Zounds Springs Florida',0),(8,'','Johnston Sasser','','wp-content/plugins/MCBA-Wordpress/','','http://johnstonandsasser.com/wp-content/plugins/MCBA-Wordpress/','687361076749','AIzaSyDMpvmFSH8G3D-l-E9wV3gylx6jem0pvUw',1,0,0,'Johnston And Sasser',0),(12,'','JonDavis Tree','','wp-content/plugins/MCBA-Wordpress/','','http://jondavistreeservice.com/wp-content/plugins/MCBA-Wordpress/','151808707034','AIzaSyB3ubNjkH2NsBJMf7ySw9fK0hNUsKi9AWk',1,0,0,'Jon Davis Tree Service',0),(14,'','A+ Realty','','wp-content/plugins/MCBA-Wordpress/','','http://aplusrealtymanagement.com/wp-content/plugins/MCBA-Wordpress/','149399793924','AIzaSyCPvJIeyWdrpU2zsEVmnGnvrrqBeCWmjBU',1,0,0,'A+ Realty Management',0),(15,'','SellersAreUs','','wp-content/plugins/MCBA-Wordpress/','','http://sellersareusclub.com/wp-content/plugins/MCBA-Wordpress/\n','822439285786','AIzaSyBjmN0OsomRiqOk9RVDErdzlXdmbmkKh2c',1,0,0,'Sellers Are Us Club',0),(16,'','The Red Room Salon','https://theredroomsalon.com/','wp-content/plugins/MCBA-Wordpress/','','https://theredroomsalon.com/wp-content/plugins/MCBA-Wordpress/','1018953753323','AAAA7T5gYus:APA91bGbLYWUkCyDL4TggmoaomZpHvXiXPY96vjGlgm71-hVeJhZplo9Ow2UpDQeuo_h1muEaDw1Skl_Oj7rp02LGZqQU-6Lyu1o9dGbgBW8NjhYPa30Bnekk3VEoAJ0biSmbkI4D7VE',0,0,0,'Red Room Salon',0),(24,'','Anchor Dental','http://anchordentalcare.com/','wp-content/plugins/MCBA-Wordpress/','','http://anchordentalcare.com/wp-content/plugins/MCBA-Wordpress/','397729063747','AAAAXJp_40M:APA91bH4OXNHMxr2nneMWvQ6iEQHKfGIbjX3uI2kZ9ydB8ZygmtiA7-dCJzZzSiy7qjW3HGKwn3qexHrAkw8W24eLpTJxQ2gRB1xnT58Q0jvahuKa1A4ukcmV8i-WKFAQdaZX7u_iYB6',1,0,0,'Anchor Dental Care',0),(25,'','Suncoast CPA','http://suncoastcpagroup.com/','wp-content/plugins/MCBA-Wordpress/','','http://suncoastcpagroup.com/wp-content/plugins/MCBA-Wordpress/','790812851426','AAAAuCAefOI:APA91bFjCySVy5SUsZnjcVJk3qLajMVl6Orq4_72htL7Umw7bn9xHsc3-gC4zMbdDCoDfon12tpN_5kTxAjpjqdubjfr-X3BUPuTidog2qWI3O6jWC_iUkPkngsA9e1nTBgtJBuFdPh6hMJlZsFSHqxr1K_1zXZ52g',0,0,0,'Suncoast CPA',0),(28,'','NatureCoast TV','','wp-content/plugins/MCBA-Wordpress/','','http://naturecoast.tv/wp-content/plugins/MCBA-Wordpress/',NULL,NULL,0,0,0,'',0),(1,'','MCBA Master','https://mycustombusinessapp.com/','wp-content/plugins/MCBA-Wordpress/','shop/shop/','https://mycustombusinessapp.com/wp-content/plugins/MCBA-Wordpress/','1153728140','AAAAAETEfow:APA91bHVzVU_S8h7x7E4cYQSoKdPY3NGVw2yNnCg2iTm8Zc9vzc0TQozx7EipSkYlc5k1uqCC0jMgJqwIaWJ1oXZ3UGxfHjqhayOiPd_ZrRDw6jJ8MQt1EXPimgCQ9adRGChvlXtCufm',1,0,0,'MCBA',0),(30,'collectiondebtlawyer.com','Elkin-Peck','http://collectiondebtlawyer.com/','wp-content/plugins/MCBA-Wordpress/','','http://collectiondebtlawyer.com/wp-content/plugins/MCBA-Wordpress/','754761497287','AAAAr7tKesc:APA91bGSYRhVhUoa81y5D42x4z0TwV8h8XBBu_ndgjAeSbHN9K8K_y33PT86QvRR3yVUCbEUcNh90uza-Lxg2bHSJp7hg7eNrLC9AQ_9Ge-Vi_bIAUZSAotPdCux9Bfq81ewg73nfa5qyMc2RlWE6L0UlFqAPavE5w',1,0,0,'',0),(32,'','ProLine Tile','http://prolinetilesh.com/','wp-content/plugins/MCBA-Wordpress/','','http://prolinetilesh.com/wp-content/plugins/MCBA-Wordpress/','822295112240','AAAAv3SbqjA:APA91bG7QxsgVD1zbNHoeRAhZL8O29syOEKKsKP_Skrra1Y9Fgx7eSx_wnnGgyXIrbcF1HXrjOmiSIFOKv9VAvq7id5xjvC97SWW9NS3ujnIAbWhFGG4_Wq-j_7kH2JoF2h9yJeRguA6Qp0jxIM85KI1V6CNF2UvdA',1,0,0,'',0),(39,'','Butash and Donovan','http://butashdonovan.com/','wp-content/plugins/MCBA-Wordpress/','','http://butashdonovan.com/wp-content/plugins/MCBA-Wordpress/','659559225962','AAAAmZDLGmo:APA91bGhIdDU35r83MsEvcrioOz4NeetMEyvtokZAYGmUE2DoFcPyrA6DHQ4VFDht8VuLPiOPygoEhM7z02OOQPd1uEJ7kmzFXdxdu0UIETJAXHI6-s_HF6dUxfeYw7EhKXjVxAhWjDmjs8Cxpta_51bgP3SX41H8A',1,0,0,'',0),(34,'','Diver City','','wp-content/plugins/MCBA-Wordpress/','','http://divercityaquavertical.com/wp-content/plugins/MCBA-Wordpress/','826749552786','AIzaSyBHx-Z1-SfCADRJNNEeUX77B2h2Vgnw6jQ',1,0,0,'',0),(35,'','Amdrill Inc','http://amdrillinc.com/','wp-content/plugins/MCBA-Wordpress/','','http://amdrillinc.com/wp-content/plugins/MCBA-Wordpress/','822034773566','AAAAv2UXNj4:APA91bHah9oT0BpINopdvxyQA7FZ22rUCFh2JIv4dFKSYV-Rm6ncIPBZwqughezCq0aEuoN8YyFd3IRPJ-L4vs9jcWBRZBqFqZ6QOLh2CcO1GwNwv7Ysr9trhisRYhy3JZl3ovx8_4MR',1,0,0,'Amdrill Inc',0),(36,'','Vivify by Vacare','','wp-content/plugins/MCBA-Wordpress/','','http://vivifybyvacare.com/wp-content/plugins/MCBA-Wordpress/','835116541862','AIzaSyB0imG9ZMK_qKRM4gN_H-cmisduVCXTDHo',1,0,0,'',0),(42,'','1 Team Christian','','wp-content/plugins/MCBA-Wordpress/','','http://1teamchristian.com/wp-content/plugins/MCBA-Wordpress/','19251368638','AAAABHt4kr4:APA91bGQSzVpBLBRQeDkGyNcRWjNeTbu_mIDnDhWBUeT76-ofdkUQyzzoCE3s_SnIeJyXlHQy_T2bu440_WhJJFyy_G5q3DBuCPoG1KdQwY_MV_KQ14suW6OkS-OUaLUvlDGuydn5FUo',1,0,0,'',0),(43,'','Prestige Air','http://prestigeaireandheat.com/','wp-content/plugins/MCBA-Wordpress/','shop/','http://prestigeairandheat.com/wp-content/plugins/MCBA-Wordpress/','528666457077','AAAAexb58_U:APA91bH9XL4RvQ8WkKftBtlckNFIBWtril0YoZDAJSCjdI4kV14A6IY02HyaMZLnEYSu1TktKaG2d8Og9PT3aNjrRIxs0GwqEBG9RFu1OA96hRYkrjcJywGw1bwx2Hl7P7G-BSLHzU8j',1,0,0,'',0),(44,'','Tarpon Furniture','http://articles.tarponfurniture.net/','wp-content/plugins/MCBA-Wordpress/','','http://articles.tarponfurniture.net/wp-content/plugins/MCBA-Wordpress/','758726486676','AAAAsKefapQ:APA91bGNLpVFf3EKJ07BB2T7fk3NCROKJPaSuCWpEfF7TcEwsta9hztWqxs1lOVkh-VA9NC069Yy1URCiYEpv1EzsZdefZjmr95B7NoIwFwoRO1cqrreIUsTCgGQBx6W6gRV9fSoCrto',1,0,0,'Tarpon Furniture',0),(45,'','Zest Medical','','wp-content/plugins/MCBA-Wordpress/','','http://zestmedicalrejuvenation.com/wp-content/plugins/MCBA-Wordpress/','199253530168','AAAALmRvljg:APA91bG8RR_1a_mzyHEiQvvr8BDm5xtOfRVQPZccxhck7DUSkdV91-4dPtRb7f86uZ-sMzxIUtSzfJLbgD_AJ8HQ92s0oeOfzcPK3bjTGwwe7JI__26FGjENjpk0HjqCN6KXBYNNMulz',1,0,0,'',0),(48,'','BaySide Medical Group','','wp-content/plugins/MCBA-Wordpress/','shop/','http://baysidemedicalgroup.net/wp-content/plugins/MCBA-Wordpress/','530194146481','AAAAe3IIpLE:APA91bGzKsJlW3L1HQvfqsG2uzlE8YOqkZFc_0PfUb5jOalewoRAx18jKr7QDYYKtVR64DgOZdYgIripILoTqC9oLuRLNNL8GUoPFL8w-j_p6VnbTbym-21MECTDGL71xznbmPlyTL01',1,0,0,'',0),(49,'','Serv-U #1','http://servu1.com/','wp-content/plugins/MCBA-Wordpress/','shop/','http://servu1.com/wp-content/plugins/MCBA-Wordpress/','145214408729','AAAAIc90CBk:APA91bGt5kKwbmtko6M-aM5V9Zqr6znzjRyPhYE9Av5BCgfUledqUB8YgdvzG09K0aBXL96kEfRHWS9luUZdqYEcAXvxIP2VTz0u6-yo567a_W5YJDLAVgMEpolzHojkw21IpMoI1qzM',1,0,0,'Servu1',0),(50,'','Shutter Professionals','http://shutterprofessionals.com/','wp-content/plugins/MCBA-Wordpress/','shop/','http://shutterprofessionals.com/wp-content/plugins/MCBA-Wordpress/','175156878616','AAAAKMgp3Rg:APA91bGctptXP8D1NI-zG8m3ZeRj9apYVHfq7v4Z95b8fC5vFEwNDaQGZn0msxxn7rPqX95KExUKoAyYi1YOUdHuVvpWM4NUGeG0H14TYgE6XwQDZX1cQ-LCw1hlALGGBGHCSo1Skj5E',1,0,0,'ShutterProfessionals',0),(51,'','All Safe Mobile Locksmith','http://allsafemobilelocksmith.com/','wp-content/plugins/MCBA-Wordpress/','shop/','http://allsafemobilelocksmith.com/wp-content/plugins/MCBA-Wordpress/','16721129628','AAAAA-SoMJw:APA91bEuMcwV1UXiDLs5tzunhh_K9-sovqu1YyNs5-L68AHYoDLDnq2MG0DDsYtkmoa3nyTEuMPQJ9AHcLuYPrTgjj83y-k-wjLZI6GKzQROJ8DIv9xXEcC85eYjntNkb1QvgqAkC60r',1,0,0,'AllSafeMobileLocksmith',0),(52,'','The Melendez Law Office','http://melendezlawoffice.com/','wp-content/plugins/MCBA-Wordpress/','','http://melendezlawoffice.com/wp-content/plugins/MCBA-Wordpress/','920997875656','AAAA1m_AT8g:APA91bFIDQCV3u1KgJ1Z49xI-SaVnHZZVISy4DnTU0FuhvWcMvFTlFAgnh68jKqzsMVNpm0FGNEX4CU99m-3jpca47wt9AtVjTww9lcPRuLKMaiKm4Bp-rJcXEo3f5vc7L1RrdFCjbmD',1,0,0,'The Melendez Law Office',0),(53,'','Laser AC and Heating INC','https://laseracrepairspringhill.com/','wp-content/plugins/MCBA-Wordpress/','shop/','https://laseracrepairspringhill.com/wp-content/plugins/MCBA-Wordpress/','443025456897','AAAAZyZf_wE:APA91bESpaCsZDu9Dpnrd24jDdi1V1uO92P16-j6S6EUlGhuDRhFeJAf3z07XrB_3HyOcGgZab_QbrOIpHIFCrn7ztpTdySOrFb8DyF8nlFGgBSB0Qu_wkUTABuxo0TCQ8hmR_Cs22Rn',1,0,0,'Laser Air Conditioning & Heating INC',0),(54,'','Dreamscapes Irrigation Inc','https://dreamscapesirr.com/','wp-content/plugins/MCBA-Wordpress/','shop/','https://dreamscapesirr.com/wp-content/plugins/MCBA-Wordpress/','282575758379','AAAAQcrT5Cs:APA91bF8I7EZ5RuRVteTN8XUjuChpuP4x15PuY93Wo8WYY--PpA-CxVhZdG_vZ2tsvyj0JqWS4FPVuqsyz0Rth4dx_qCZXgBwJMx1tthgkYYtTM5ikhtqsM_z_rpJoFeLo--LWUkr74t',1,0,0,'Dreamscapes Irrigation Inc\r\n',0),(55,'','Florida Car Wash','https://floridascarwash.com/','wp-content/plugins/MCBA-Wordpress/','shop/','https://floridascarwash.com//wp-content/plugins/MCBA-Wordpress/','1059615166197','AAAA9rX8TvU:APA91bG-NQaei9Kx94y6N9p2cWOg4PxStTQ-yWG9mtsqgBtzIyZX1M3r1StEKqNtFR5S6rxCZpE_LZpkIUYVXRhOKN4s6UqF5qaMtpbPwuwk6wOCr-L77po-Ab_kwbDmHgRSCfSY38kD',1,0,0,'Florida Car Wash',0);
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `debug_log`
--

DROP TABLE IF EXISTS `debug_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `debug_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(50) NOT NULL,
  `class_method` varchar(50) CHARACTER SET utf8 NOT NULL,
  `message` text CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `debug_log`
--

LOCK TABLES `debug_log` WRITE;
/*!40000 ALTER TABLE `debug_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `debug_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `_id` int(11) NOT NULL AUTO_INCREMENT,
  `mcba_id` int(11) NOT NULL,
  `first_name` text COLLATE utf8_unicode_ci NOT NULL,
  `last_name` text COLLATE utf8_unicode_ci NOT NULL,
  `push_id` text COLLATE utf8_unicode_ci NOT NULL,
  `device` text COLLATE utf8_unicode_ci NOT NULL,
  `DateReg` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,1,'Erik','Madison','e_m8QYJLTMk:APA91bFMHlFE2V2en2zhm67Am2kipgmJ3YdLSyxW3DsTYiBGO54g9bqkamqaAwADKHgBLRj9MWSwTkYhCM8Y2_8YOxgrHNnLb8ixoD_iClhaAQnUMM7u2J4GhlUTFLRzTCcwgeuNlzXi','Huawei Nexus 6P','2017-05-05 22:16:40');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-09 20:05:54
