#!/usr/bin/env python
# coding: utf-8

# In[ ]:


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
accum = 0
count = 0
sum_ = 0
for item in week_temps_f.split(','):
    count += 1
    sum_ = sum_ + float(item)
    accum = sum_/len(week_temps_f.split(',')) # count can be used instead of len(week_temps_f.split(',')) 
    
print(sum_)    
print(accum)

