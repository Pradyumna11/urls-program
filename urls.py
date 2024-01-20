from GoogleNews import GoogleNews
Googlenews = GoogleNews()
Googlenews.set_time_range( '02/11/2023','20/01/2023')
Googlenews.search('World')
x = Googlenews.result()
print(x)