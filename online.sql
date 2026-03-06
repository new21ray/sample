create table course(
cid int,cname varchar(20),
ccateg varchar(20) check (ccateg in ('ns','ci&ml','acs')),
no_lect int,
no_ass int,
fee decimal(10,2)
);

create table faculty(

fid char(5) primary key check(substring(fid,1,1) in ('f') and substring(fid,2,1) in ('-') and substring(fid,3,3) between 000 and 999),
fname varchar(20),
faddr varchar(20),
qualif varchar(10) check(qualif in('b-tech','m-tech','phd')),
exp int,
mob bigint check(mob between 100000000 and 9999999999),
email varchar(50) check(email like '%@%')

);

create table course_info(
fid char(5) ,
cid int,
season varchar(20) check(season in ('w','s')),
year int,
primary key (fid,cid,season,year),
foreign key (fid) references faculty(fid) on update cascade on delete cascade,
foreign key (cid) references course(cid) on update cascade on delete cascade 
);