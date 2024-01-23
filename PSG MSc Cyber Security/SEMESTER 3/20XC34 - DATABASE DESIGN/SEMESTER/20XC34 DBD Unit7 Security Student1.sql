############################################################
# MySQL Sample Scripts
# PSG MSc Cyber Security - 21PC - 20XC34 Database Design
# Author: Ramesh  Date: 01-NOV-2022
############################################################

#################### MySQL Sample scripts - student1 #########################
select current_user();
show grants for 'student1'@'localhost';

use psg;

#Only select is granted
select * from accounts;
select * from employee;
create table account_std3(name varchar(10));

#INSERT
insert into accounts values ('AC005',100);
select * from accounts;

#UPDATE
select * from accounts;
update accounts set amount = 555 where accountno = 'AC003';
select * from accounts;

#Test grant option
grant select on psg.* to 'student3'@'localhost';

select * from student1;
insert into student1 values ('81MX02','Raja','Sekar',23,'Salem','9898989123');

#grant priviliege to other users
grant select on psg.student1 to 'student2'@'localhost';

select * from students2;

#################### End of the script #########################
