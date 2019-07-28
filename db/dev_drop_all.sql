use whale;

set foreign_key_checks = false;
drop table whale.app_session;
drop table whale.friendship;
drop table whale.game;
drop table whale.game_session;
drop table whale.user;

-- Checking:
select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA = "whale";
