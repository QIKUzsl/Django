from django.http import HttpResponse
from django.shortcuts import render
temp="""
<html>
    <body style="text-align: center;">
        <h1>绣春刀——无常簿</h1>
        
        <h2>findall--查看所有可疑员</h2>
        
        <h2>findgood--新增可疑人员</h2>
        
        <h2>findbad--删除可疑人员</h2>
    </body>
</html>
"""


def index(req):
    # return render(req, "index.html")
    return HttpResponse(temp)