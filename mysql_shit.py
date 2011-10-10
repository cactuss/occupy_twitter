"""

CREATE TABLE  `ows`.`hash_tags` (
`id` INT NOT NULL AUTO_INCREMENT ,
`hash_tag` VARCHAR( 140 ) NOT NULL ,
`count` INT NOT NULL ,
PRIMARY KEY (  `id` ) ,
UNIQUE (
`hash_tag`
)
) ENGINE = MYISAM ;

"""

import MySQLdb
try:
  import mysql_config
  host = mysql_config.host
  user = mysql_config.user
  passwd = mysql_config.passwd
  db = mysql_config.db
except Exception:
  host = 'localhost'
  user = 'user'
  passwd = 'passwd'
  db = 'ows'


mysql_client = MySQLdb.Connect(host=host,user=user,
         passwd=passwd,db=db)
mysql_client.select_db(db)

def update_hash_tag(name, value):
    name = mysql_client.escape_string(name)
    value = mysql_client.escape_string(str(value))
    query = "INSERT INTO `ows`.`hash_tags` (`id`, `hash_tag`, `count`) VALUES (NULL, '"+name+"', '"+value+"') on duplicate key update count=count+"+value+";"
    mysql_client.query(query)
