
-- 创建测试库
CREATE DATABASE `app1` DEFAULT CHARACTER SET UTF8 DEFAULT COLLATE utf8_general_ci;

-- 创建测试表
CREATE TABLE `app1`.`user`(
	uid VARCHAR(13) PRIMARY KEY,
	phone_number VARCHAR(13)
);

-- 创建修改手机号的存储过程
DELIMITER $$

CREATE PROCEDURE `app1`.`update_phone_number_by_uid`(
	IN p_uid VARCHAR(13),
	IN p_old_phone_number VARCHAR(13),
	IN p_new_phone_number VARCHAR(13)
)
BEGIN
    UPDATE `app1`.`user` SET phone_number=p_new_phone_number WHERE uid=p_uid AND phone_number=p_old_phone_number;
END$$

DELIMITER ;


-- 创建修改银行卡的存储过程
DELIMITER $$

CREATE PROCEDURE `app1`.`update_bank_card_number_by_uid`(
	IN p_uid VARCHAR(13),
	IN p_old_bank_card_number VARCHAR(13),
	IN p_new_bank_card_number VARCHAR(13)
)
BEGIN
    UPDATE `app1`.`user` SET phone_number=p_new_phone_number WHERE uid=p_uid AND phone_number=p_old_phone_number;
END$$

DELIMITER ;


/*

-- 手动调用测试
CALL `app1`.`update_phone_number_by_uid`('1', '11122223333', '00000000000');

-- 查看创建的存储过程信息
SELECT db,name,type,body_utf8 FROM `mysql`.`proc` WHERE db='app1' AND type='procedure'\G

*/