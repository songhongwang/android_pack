#从本地向FTP批量上传文档
#!/bin/sh
ftp -v -n xxx.xxx.xxx.xx<<EOF
user xx xxx
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

 