from fetcher import head
from storage import jsonData
he=head()
res_data=he.get_data()
js=jsonData
js.load_data(res_data)