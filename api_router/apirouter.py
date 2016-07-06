from api_store import api_item1 # Ny times API call
from cleaner import api_result_cleaner # cleanup API results











'''----------------------------------------------
    Divert the results from the API Clean up
------------------------------------------------'''
def api_result_cleaner(result):












'''----------------------------------------------
    Send the
------------------------------------------------'''





'''---------------------------------------------
    Call APIs from all the news sources.
------------------------------------------------'''
def api_router(query):
    qu_results= api_item1.api_item1(query)
    api_result_cleaner(qu_results)



