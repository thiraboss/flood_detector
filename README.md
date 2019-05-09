# Flood_detector
_This API will give the information of the dam whether it has flood or not and there are 3 levels(low, high and very high) to determine how much risk of having flood._

```
/flood_detector/{location}
```
coming_data = {'name':"flood_detector",'status':very high, 'percentage':100, 'location':'thirawat'}

## Table

| Header        | type          | information |
| ------------- | ------------- |------------   
|name  | string  |project name|
| status  | string  |the levels of water (low, high and very high)
|percentage|string|percentage of the risk of having flood (eg.100%)
|location|string|thirawat
