with a as (
    select id,
           temperature,
           recordDate,
           LAG(recordDate) OVER (ORDER BY recordDate)  dat,
           LAG(temperature) OVER (ORDER BY recordDate) tmp
    from Weather)
select id
from a
where temperature > tmp
  and recordDate - dat = 1