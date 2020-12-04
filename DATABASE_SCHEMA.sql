-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: eaf
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chemical_compositon`
--

DROP TABLE IF EXISTS `chemical_compositon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chemical_compositon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `element_id` int DEFAULT NULL,
  `percentage` int DEFAULT NULL,
  `commodity_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `commidity_property_fk_idx` (`commodity_id`),
  KEY `element_id_fk_idx` (`element_id`),
  CONSTRAINT `commidity_property_fk` FOREIGN KEY (`commodity_id`) REFERENCES `commodity_properties` (`id`),
  CONSTRAINT `element_id_fk` FOREIGN KEY (`element_id`) REFERENCES `chemical_element` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chemical_compositon`
--

LOCK TABLES `chemical_compositon` WRITE;
/*!40000 ALTER TABLE `chemical_compositon` DISABLE KEYS */;
INSERT INTO `chemical_compositon` VALUES (1,1,10,3),(2,2,10,4),(4,3,50,6),(28,6,50,6);
/*!40000 ALTER TABLE `chemical_compositon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chemical_element`
--

DROP TABLE IF EXISTS `chemical_element`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chemical_element` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chemical_element`
--

LOCK TABLES `chemical_element` WRITE;
/*!40000 ALTER TABLE `chemical_element` DISABLE KEYS */;
INSERT INTO `chemical_element` VALUES (1,'G'),(2,'P'),(3,'T'),(4,'M'),(5,'W'),(6,'unknown');
/*!40000 ALTER TABLE `chemical_element` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity_properties`
--

DROP TABLE IF EXISTS `commodity_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commodity_properties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `inventory` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity_properties`
--

LOCK TABLES `commodity_properties` WRITE;
/*!40000 ALTER TABLE `commodity_properties` DISABLE KEYS */;
INSERT INTO `commodity_properties` VALUES (1,'Plate & Structural','200.5','1234.5'),(2,'Plate & Structural','200.5','1234.5'),(3,'Plate','300','1234.5'),(4,'Structural','200.5','1234.5'),(5,'Plate & Structural','200.5','1234.5'),(6,'yyyy','200.5','1000');
/*!40000 ALTER TABLE `commodity_properties` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-04  9:01:30
