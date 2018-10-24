/**
create table student(region STRING, distrito STRING, sid INT,nombre STRING,
  nivel STRING, sexo STRING, stid INT) row format delimited fields terminated by ',';
  **/

/**
create table escuela(region STRING, distrito STRING, municipio STRING,
eid INT, nombre STRING, nivel STRING, cid INT) row format delimited fields terminated by ',';
**/
/**Part 1**/
select e.region, e.municipio, count(*)
from student as s, escuela as e
where s.sid = e.eid
group by e.region, e.municipio;

/**Part 2**/
select municipio, nivel, count(*)
from escuela
group by municipio, nivel;

/**Part 3**/
select count(*)
from student as s, escuela as e
where e.eid = s.sid
and e.municipio = "Ponce"
and e.nivel = "Superior"
and s.sexo = "F";

/**Part 4**/
select e.region, e.distrito, e.municipio, count(*)
from student as s, escuela as e
where s.sid = e.eid and s.sexo = "M"
group by e.region, e.distrito, e.municipio;
