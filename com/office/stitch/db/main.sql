/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : SQLite
 Source Server Version : 3008004
 Source Database       : main

 Target Server Type    : SQLite
 Target Server Version : 3008004
 File Encoding         : utf-8

 Date: 06/22/2016 09:13:30 AM
*/

PRAGMA foreign_keys = false;

-- ----------------------------
--  Table structure for keys
-- ----------------------------
DROP TABLE IF EXISTS "keys";
CREATE TABLE "keys" (
	 "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	 "keyword" text NOT NULL,
	 "status" integer NOT NULL
);

-- ----------------------------
--  Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS "result";
CREATE TABLE "result" (
	 "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	 "first" TEXT,
	 "second" TEXT,
	 "third" TEXT
);

PRAGMA foreign_keys = true;
