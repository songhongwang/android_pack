#从本地向FTP批量上传文档
#!/bin/sh
ftp -v -n qxu1649270087.my3w.com<<EOF
user qxu1649270087 shw286147206
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

 