def count_pages(string):
    count = 0
    y = string.split(',')
    for page in y:
        if '-' in page:
            start, end = map(int, page.split('-'))
            if end > start:
              count += end - start + 1
            else:
                count += start - end + 1
       
    print(count)

# Test
count_pages('2-5, 7')
count_pages('12-18, 20-20')
count_pages('18-12, 20-20, 5-6')

