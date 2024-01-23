############################################################
# MySQL Sample Scripts
# PSG MSc Cyber Security - 21PC - 20XC34 Database Design
# Author: Ramesh  Date: 01-NOV-2022
############################################################

####################MySQL Sample scripts - Security #########################
select current_user();
use psg;

create user 'hod'@'localhost' identified by 'ramesh';

create user 'staff1'@'localhost' identified by 'ramesh';
create user 'staff2'@'localhost' identified by 'ramesh';

create user 'student1'@'localhost' identified by 'ramesh';
create user 'student2'@'localhost' identified by 'ramesh';
create user 'student3'@'localhost' identified by 'ramesh';
create user 'student4'@'localhost' identified by 'ramesh';

drop user 'hod'@'localhost';

drop user 'staff1'@'localhost';
drop user 'staff2'@'localhost';

drop user 'student1'@'localhost';
drop user 'student2'@'localhost';
drop user 'student3'@'localhost';
drop user 'student4'@'localhost';

select * from mysql.user where user like 'student%';

show grants for 'hod'@'localhost';

show grants for 'staff1'@'localhost';
show grants for 'staff2'@'localhost';

show grants for 'student1'@'localhost';
show grants for 'student2'@'localhost';
show grants for 'student3'@'localhost';

select * from student;
insert into psg.student values ('15CS04','Ramesh','1990-01-01','MSCCS',1100,'Chennai');

grant select, insert, update on psg.student to 'hod'@'localhost';
grant select, update on psg.student to 'staff1'@'localhost';
grant select on psg.student to 'student1'@'localhost';

revoke select, insert, update on psg.student from 'hod'@'localhost';
revoke select, update on psg.student from 'staff1'@'localhost';
revoke select on psg.student from 'student1'@'localhost';


grant alter, drop, insert, update, delete on psg.accounts to 'student1'@'localhost';
revoke alter, drop, insert, update, delete on psg.accounts from 'student1'@'localhost';

grant create on psg to 'student1'@'localhost';
revoke create on psg from 'student1'@'localhost';

grant all privileges on psg.* to 'student1'@'localhost';
revoke all privileges on psg.* from 'student1'@'localhost';

grant select on psg.* to 'student2'@'localhost' with grant option;
revoke select on psg.* from 'student2'@'localhost';

grant all privileges on psg.* to 'student2'@'localhost' with grant option;
revoke all privileges on psg.* from 'student2'@'localhost';

show grants for 'student1'@'localhost';
show grants for 'student2'@'localhost';
show grants for 'student3'@'localhost';
show grants for 'student4'@'localhost';

grant select on psg.* to 'student1'@'localhost';
revoke select on psg.* from 'student1'@'localhost';

grant insert on psg.accounts to 'student1'@'localhost';
grant update on psg.accounts to 'student1'@'localhost';
revoke insert, update on psg.accounts from 'student1'@'localhost';

grant alter, drop, insert, update, delete on psg.accounts to 'student1'@'localhost';
revoke alter, drop, insert, update, delete on psg.accounts from 'student1'@'localhost';

grant create on psg to 'student1'@'localhost';
revoke create on psg from 'student1'@'localhost';

grant all privileges on psg.* to 'student1'@'localhost';
revoke all privileges on psg.* from 'student1'@'localhost';

grant select on psg.* to 'student2'@'localhost' with grant option;
revoke select on psg.* from 'student2'@'localhost';

grant all privileges on psg.* to 'student2'@'localhost' with grant option;
revoke all privileges on psg.* from 'student2'@'localhost';

#Run immediately after a CREATE USER or GRANT statement in order to reload the grant tables 
#to ensure that the new privileges are put into effect:
FLUSH PRIVILEGES; 



# create role RBAC
create role student;
drop role student;

grant select on psg.student to student;
show grants for student;

grant student to 'student4'@'localhost';
revoke student from 'student4'@'localhost';


show grants for 'student1'@'localhost';

create role 'developer';
grant select, alter, drop, insert, update, delete on psg.students2 to 'developer';
grant 'developer' to 'student1'@'localhost';
revoke 'developer' from 'student1'@'localhost';
FLUSH PRIVILEGES; 

#################### End of the script #########################