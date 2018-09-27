.open 'class.db'

/* Find average comments for videos in common */
select CAvideos.category_id, avg(CAvideos.comment_count) as cnt
from CAvideos
inner join USvideos on USvideos.video_id = CAvideos.video_id
inner join DEvideos on DEvideos.video_id = CAvideos.video_id
inner join FRvideos on FRvideos.video_id = CAvideos.video_id
inner join GBvideos on GBvideos.video_id = CAvideos.video_id
group by CAvideos.category_id
order by cnt DESC;
