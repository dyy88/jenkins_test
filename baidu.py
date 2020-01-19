import requests

a=requests.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&rsv_pq=99d7bdee0005ccaf&rsv_t=8bbdv0yL8hqh690ZWMuYkD02DNmbDoUG5cwA4EASIALdDnG8z66xAMgyj%2Fk&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=9&rsv_sug1=9&rsv_sug7=101&inputT=3498&rsv_sug4=3990&rsv_sug=1')

print (a.status_code)


