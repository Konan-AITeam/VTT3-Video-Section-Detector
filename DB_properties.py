# DB 접속 정보

ip = ""
port = ""
dbname = ""
user = ""
password = ""

conn_string = "host=%s port=%s dbname =%s user=%s password=%s" % (ip, port, dbname, user, password)

sql_string = "SELECT * FROM vttm_catalogque_tb where status='wait' and (cancle_yn = 'n' or cancle_yn = 'N') ORDER BY videoid ASC limit 1"


# request 정보

web_ip = ""
web_port = ""
web_project = ""

base_url = "http://%s:%s/%s/" % (web_ip, web_port, web_project)
server_url = "http://%s:%s/%s/content/retry/catalog/" % (web_ip, web_port, web_project)
