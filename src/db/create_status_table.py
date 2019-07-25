from sqlalchemy import MetaData, Table, Column, Integer
from sqlalchemy.dialects.mysql import TINYINT, SMALLINT

meta = MetaData()

Table(
    'status', meta,
    Column('account_id', Integer, primary_key=True, autoincrement=False),
    Column('hp', SMALLINT, nullable=False, server_default='30'),
    Column('weapon_id', SMALLINT, nullable=False, server_default='1'),
    Column('weapon_lv', TINYINT, nullable=False, server_default='0'),
    Column('armor_id', SMALLINT, nullable=False, server_default='1'),
    Column('armor_lv', TINYINT, nullable=False, server_default='0'),
    Column('magic_id', SMALLINT, nullable=False, server_default='1'),
    Column('magic_lv', TINYINT, nullable=False, server_default='0'),
)

Table(
    'status_2', meta,
    Column('account_id', Integer, primary_key=True, autoincrement=False),
    Column('hp', SMALLINT, nullable=False, server_default='30'),
    Column('weapon_id', SMALLINT, nullable=False, server_default='1'),
    Column('weapon_lv', TINYINT, nullable=False, server_default='0'),
    Column('armor_id', SMALLINT, nullable=False, server_default='1'),
    Column('armor_lv', TINYINT, nullable=False, server_default='0'),
    Column('magic_id', SMALLINT, nullable=False, server_default='1'),
    Column('magic_lv', TINYINT, nullable=False, server_default='0'),
)

Table(
    'status_3', meta,
    Column('account_id', Integer, primary_key=True, autoincrement=False),
    Column('hp', SMALLINT, nullable=False, server_default='30'),
    Column('weapon_id', SMALLINT, nullable=False, server_default='1'),
    Column('weapon_lv', TINYINT, nullable=False, server_default='0'),
    Column('armor_id', SMALLINT, nullable=False, server_default='1'),
    Column('armor_lv', TINYINT, nullable=False, server_default='0'),
    Column('magic_id', SMALLINT, nullable=False, server_default='1'),
    Column('magic_lv', TINYINT, nullable=False, server_default='0'),
)
