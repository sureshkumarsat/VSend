############################################################
# MySQL Sample Scripts
# PSG MSc Cyber Security - 21PC - 20XC34 Database Design
# Author: Ramesh  Date: 01-NOV-2022
############################################################

#################### MySQL Sample scripts - student2 #########################
select current_user();
show grants for 'student2'@'localhost';

use psg;

#Only select is granted
select * from accounts;

create table account_std5(name varchar(10));

#now grant to another user student3
grant select on psg.* to 'student3'@'localhost' with grant option;
revoke select on psg.* from 'student3'@'localhost';

#################### End of the script #########################