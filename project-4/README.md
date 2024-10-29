# HW4 - Report
### Chris Skeens
### Due Date: 10/27/24

## Q1: Analyze Datetimes of Mementos

![Scatter-plot](https://github.com/odu-cs432-websci/fall24-cskee004/raw/main/HW4/HW4/Q1/scatter-plot.png)

I reused my 'parse_maps()` method from HW3 with the alterations to get the difference in time from the collection date and the earliest memento date for the given timemap.
```
collection_date = datetime.strptime('2024-10-16', '%Y-%m-%d')

def parse_maps():
        for name in os.listdir(r"./time-maps"):
        file_path = os.path.join(r"./time-maps", name)
        file_size = os.path.getsize(file_path)
        if file_size > 0:
            temp_list = []
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)
                for memento in data['mementos']['list']:
                    memento_datetime = datetime.strptime(memento['datetime'], '%Y-%m-%dT%H:%M:%SZ')
                    temp_list.append(memento_datetime)       
            num_mementos = len(temp_list)
            if num_mementos > 0:
                earliest_memento = min(temp_list)
                age = (collection_date - earliest_memento).days
                ages.append(age)
                mementos_count.append(num_mementos)
```

### Q: *What can you say about the relationship between the age of a URI-R and the number of its mementos?*
### Answer:
Besides some outlyers, the age of URI-R does not always mean a higher number of memento compared to younger URI-Rs.  

### Q: *What URI-R had the oldest memento? Did that surprise you?*
### Answer:
Yahoo had the oldest memento I found. These results were as expected becasue of the amount of time Yahoo has been around.

### Q: *How many URI-Rs had an age of < 1 week, meaning that their first memento was captured the same week you collected the data?*
### Answer:
0

## Q2: Explore Conifer and ReplayWeb.Page

### Q: *Why did you choose this particular topic?*
### Answer: 
I decided to capture websites around Legos becasue I think its interesting to see what sets were around for this time period. 

### Q: *Did you have any issues in archiving the webpages?*
### Answer: 
Yes. Most websites I tried to capture would begin to reload constantly giving 404 errors.

### Q: *Do the archived webpages look like the original webpages?*
### Answer:
The majority of the archived webpages did look like the original ones.

[Screenshot1](https://github.com/odu-cs432-websci/fall24-cskee004/raw/main/HW4/HW4/Q2/ss1.pdf)

[Screenshot2](https://github.com/odu-cs432-websci/fall24-cskee004/raw/main/HW4/HW4/Q2/ss2.pdf)

### Q: *How many URLs were archived in the WARC file? How does this compare to the number of Pages?* 
### Answer: 

![Graph](https://github.com/odu-cs432-websci/fall24-cskee004/raw/main/HW4/HW4/Q2/bar-chart.png)

23 URLS in the WARC file and 10,504 captured resources found in the WARC file.

- HTML = 308
- Images = 9404
- Audio/visual = 7
- PDF = 0
- Javascript = 369
- CSS = 249 
- Fonts = 69
- Plaintext = 5
- JSON = 93
- DASH/HLS = 0

### Q: *Which file type had the most URLs? Were you surprised by this?*
Images had the majority of the captured resources. I wasnt surprised because images make up a lot of what a website is and how it functions.
