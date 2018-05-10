批量打包流程

1> 把需要批量打包的文件放入info目录中，格式如info/channel_template.txt

2> 执行脚本开始打包：双击 MultiChannelBuildTool.command 或者在终端中运行 python MultiChannelBuildTool.py

3> 执行脚本开始上传ftp：双击 UploadFtp.command 或者终端中运行 sh UploadFtp.sh

4> 登录ftp看下文件文件数量是否正确，是否有遗漏的（可能网络异常脚本跳过某个文件）

>祝好运