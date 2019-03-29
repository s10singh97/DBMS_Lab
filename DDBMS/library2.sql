-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2018 at 06:40 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library2`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` varchar(128) NOT NULL,
  `Pass` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `Pass`) VALUES
('123', '12fa7bdf45ab1241476fb0f0f3d628be'),
('Ashish', '90389074c3753fa7cce569f2ea027719');

-- --------------------------------------------------------

--
-- Table structure for table `authorbook`
--

CREATE TABLE `authorbook` (
  `a_id` varchar(20) NOT NULL,
  `b_id` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authorbook`
--

INSERT INTO `authorbook` (`a_id`, `b_id`) VALUES
('1', 103),
('2', 107),
('4', 102),
('5', 101),
('6', 101),
('7', 104),
('7', 107),
('8', 105);

-- --------------------------------------------------------

--
-- Table structure for table `authorcat`
--

CREATE TABLE `authorcat` (
  `a_id` varchar(20) NOT NULL,
  `category` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `authorcat`
--

INSERT INTO `authorcat` (`a_id`, `category`) VALUES
('1', 'Technical'),
('10', 'Optics'),
('2', 'Social'),
('3', 'Detective'),
('3', 'Technical'),
('3', 'Thrill'),
('4', 'Computer'),
('4', 'Programming'),
('5', 'Database'),
('6', 'Database'),
('7', 'Theoretical'),
('8', 'Drama'),
('8', 'Non-fiction'),
('9', 'Physics');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` bigint(10) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  `publisher_id` bigint(20) DEFAULT NULL,
  `genre` varchar(128) DEFAULT NULL,
  `edition` int(10) DEFAULT NULL,
  `pages` bigint(20) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `isbn_no` bigint(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `name`, `publisher_id`, `genre`, `edition`, `pages`, `price`, `isbn_no`) VALUES
(101, 'DBMS', 1010, 'Study', 3, 898, 1000, 3123123233214),
(102, 'C_plus_plus', 1001, 'Tech', 7, 918, 700, 1231278474892),
(103, 'C++', 1001, 'Study', 879, 999, 1000, 1231238192139),
(104, 'Number_theory', 1001, 'Think', 5, 800, 1000, 7897987283219),
(105, 'Game', 1010, 'Plan', 5, 198, 300, 1231231234313),
(107, 'PoliticsAround', 1002, 'Knowledge', 7, 665, 400, 1235437397465);

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `borrower_id` int(11) NOT NULL,
  `book_id` bigint(10) NOT NULL,
  `date_of_issue` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`borrower_id`, `book_id`, `date_of_issue`) VALUES
(9011, 101, '2018-10-04'),
(9011, 102, '2018-11-02'),
(9011, 105, '2018-11-13'),
(9011, 107, '2018-11-13'),
(9013, 103, '2018-09-14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `authorbook`
--
ALTER TABLE `authorbook`
  ADD PRIMARY KEY (`a_id`,`b_id`),
  ADD KEY `authorbook_ibfk_3` (`b_id`);

--
-- Indexes for table `authorcat`
--
ALTER TABLE `authorcat`
  ADD PRIMARY KEY (`a_id`,`category`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `publisher_id` (`publisher_id`);

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`borrower_id`,`book_id`),
  ADD KEY `book_id` (`book_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
