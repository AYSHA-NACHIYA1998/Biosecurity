-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2024 at 07:36 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hetro_pd`
--

-- --------------------------------------------------------

--
-- Table structure for table `horticulturepests`
--

CREATE TABLE `horticulturepests` (
  `ID` int(11) NOT NULL,
  `CommonName` varchar(255) DEFAULT NULL,
  `ScientificName` varchar(255) DEFAULT NULL,
  `PresenceInNZ` tinyint(1) DEFAULT NULL,
  `PrimaryImageURL` varchar(2000) DEFAULT NULL,
  `KeyCharacteristics` text DEFAULT NULL,
  `BiologyDescription` text DEFAULT NULL,
  `Impacts` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `horticulturepests`
--

INSERT INTO `horticulturepests` (`ID`, `CommonName`, `ScientificName`, `PresenceInNZ`, `PrimaryImageURL`, `KeyCharacteristics`, `BiologyDescription`, `Impacts`) VALUES
(2, 'null', 'null', 1, 'https://www.efsa.europa.eu/sites/default/files/styles/sm_col_12_16x9_fallback/public/news/Japanese%20beetle.jpg.jpeg?itok=PlFQ3Wea', 'null', 'null', 'null'),
(3, 'null', 'null', 0, 'https://geckopestservices.com/wp-content/uploads/2016/08/nemchem-international-pest-control-pests-1.jpg', 'null', 'null', 'null');

--
-- Triggers `horticulturepests`
--
DELIMITER $$
CREATE TRIGGER `after_horticulturepests_delete` AFTER DELETE ON `horticulturepests` FOR EACH ROW BEGIN
    INSERT INTO trig (fid, action, timestamp)
    VALUES (OLD.id, 'delete', NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_horticulturepests_insert` AFTER INSERT ON `horticulturepests` FOR EACH ROW BEGIN
    INSERT INTO trig (fid, action, timestamp)
    VALUES (NEW.id, 'insert', NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_horticulturepests_update` AFTER UPDATE ON `horticulturepests` FOR EACH ROW BEGIN
    INSERT INTO trig (fid, action, timestamp)
    VALUES (NEW.id, 'update', NOW());
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `rid` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `active` varchar(50) NOT NULL,
  `phonenumber` varchar(12) NOT NULL,
  `address` varchar(50) NOT NULL,
  `dateofjoind` datetime NOT NULL DEFAULT current_timestamp(),
  `lastname` varchar(30) NOT NULL,
  `password` varchar(500) NOT NULL,
  `uid` int(10) NOT NULL DEFAULT 3
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`rid`, `firstname`, `email`, `active`, `phonenumber`, `address`, `dateofjoind`, `lastname`, `password`, `uid`) VALUES
(20, 'aysha', 'aysha@hetro.com', '1', '908017754233', 'some where', '2024-03-22 00:00:00', '', 'fa1de4364cfd94d75e7bda5d0583bcb136d6437c88a36dc06bcd64566a3530ae', 3);

--
-- Triggers `register`
--
DELIMITER $$
CREATE TRIGGER `deletion` BEFORE DELETE ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,OLD.rid,'FARMER DELETED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `insertion` AFTER INSERT ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.rid,'Farmer Inserted',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `updation` AFTER UPDATE ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.rid,'FARMER UPDATED',NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `trig`
--

CREATE TABLE `trig` (
  `id` int(11) NOT NULL,
  `fid` varchar(50) NOT NULL,
  `action` varchar(50) NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trig`
--

INSERT INTO `trig` (`id`, `fid`, `action`, `timestamp`) VALUES
(86, '20', 'FARMER UPDATED', '2024-03-14 01:05:55'),
(87, '20', 'FARMER UPDATED', '2024-03-14 01:05:59'),
(88, '20', 'FARMER UPDATED', '2024-03-14 01:06:21'),
(89, '20', 'FARMER UPDATED', '2024-03-14 01:07:26'),
(90, '20', 'FARMER UPDATED', '2024-03-14 01:07:48'),
(91, '20', 'FARMER UPDATED', '2024-03-14 01:07:54'),
(92, '5', 'insert', '2024-03-14 22:31:07'),
(93, '5', 'delete', '2024-03-15 00:06:39');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL,
  `uid` int(2) NOT NULL COMMENT '1 - admin , 2 - staff ,3 hetro',
  `lastname` varchar(30) NOT NULL,
  `phone` int(20) NOT NULL,
  `hiredate` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `firstname`, `email`, `password`, `uid`, `lastname`, `phone`, `hiredate`) VALUES
(5, 'aysha', 'aysha@admin.com', 'fa1de4364cfd94d75e7bda5d0583bcb136d6437c88a36dc06bcd64566a3530ae', 1, 'm', 2147483647, '2024-03-14 18:30:00'),
(6, 'aysha@staff', 'aysha@staff.com', 'fa1de4364cfd94d75e7bda5d0583bcb136d6437c88a36dc06bcd64566a3530ae', 2, '', 2147483647, '2024-03-21 18:30:00');

--
-- Triggers `user`
--
DELIMITER $$
CREATE TRIGGER `after_user_delete` AFTER DELETE ON `user` FOR EACH ROW BEGIN
    INSERT INTO trig (fid, action, timestamp)
    VALUES (OLD.id, 'delete', NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_user_insert` AFTER INSERT ON `user` FOR EACH ROW BEGIN
    INSERT INTO trig (fid, action, timestamp)
    VALUES (NEW.id, 'insert', NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_user_update` AFTER UPDATE ON `user` FOR EACH ROW BEGIN
    INSERT INTO trig (fid, action, timestamp)
    VALUES (NEW.id, 'update', NOW());
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `horticulturepests`
--
ALTER TABLE `horticulturepests`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `trig`
--
ALTER TABLE `trig`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `horticulturepests`
--
ALTER TABLE `horticulturepests`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `trig`
--
ALTER TABLE `trig`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
