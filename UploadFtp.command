#从本地向FTP批量上传文档
#!/bin/sh
host=qxu1649270087.my3w.com
uname=qxu1649270087
upassword=shw286147206

ftp -v -n $host<<EOF
user $uname $upassword
binary
hash
cd myfolder/download
prompt
mdelete *

lcd `dirname $0`
lcd upload/
prompt
mput *

bye
#here document
EOF
echo "commit to ftp successfully"

 