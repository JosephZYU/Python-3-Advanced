import datetime as dt

curr_weight = 175  # in lbs
goal_weight = 160  # in lbs

avg_lbs_week = 1.5  # in lbs

start_date = dt.date.today()  # start_date should be immutable!
end_date = start_date

while curr_weight > goal_weight:
    end_date += dt.timedelta(days=7)
    curr_weight -= avg_lbs_week

print(
    f'We can reach our goal in {(end_date - start_date).days//7} weeks')

print(end_date)
