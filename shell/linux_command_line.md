# 资料

https://billie66.github.io/TLCL/book/chap02.html
记得用简阅插件。

专业术语
* 因为 Linux 是以 Unix 家族的操作系统为模型写成的操作系统。
* Ubuntu 是一个基于 Debian 的 Linux 发行版。有很多Linux发行版。
* 命令行指的是 shell。shell 就是一个程序，它接受从键盘输入的命令， 然后把命令传递给操作系统去执行。几乎所有的 Linux 发行版都提供一个名为 bash 的 来自 GNU 项目的 shell 程序。“bash” 是 “Bourne Again SHell” 的首字母缩写， 是最初在 Unix 上由 Steve Bourne 写成 shell 程序 sh 的增强版。
* terminal emulator - 终端仿真器，它提供了一个图形界面，用来显示 shell 的输出， 并且接受来自键盘的输入。终端仿真器是一个图形程序，它运行在图形桌面环境中， 例如 GNOME 或 KDE。终端仿真器的图形界面被称为终端窗口。控制台和终端是同义词。



# 1. 常用命令

## 1.1. 命令格式

`command -options arguments`

eg. `ls -lt --reverse /home/bob` 


## 1.2. 基本命令
* `ls` - List directory contents
    - Filenames that begin with a period character are hidden. This only means that ls will not list them unless you say `ls -a`.
    - specify multiple directories. In this example we will list both the user’s home directory (symbolized by the “~” character) and the /usr directory. `ls ~ /usr`
    - 指定一个文件. eg `ls -lh temp.txt`.
    - `ls -lh` - long format, showing 
        - permissions The first character indicates the type of file. Among the different types, a leading dash means a regular file, while a “d” indicates a directory. The next three characters are the access rights for the file's owner, the next three are for members of the file's group, and the final three are for everyone else. ![](./101.png) see here for more: <https://billie66.github.io/TLCL/book/chap10.html>
        - the number of hard links that now exist for the file. Remember that a file will always have at least one link because the file’s name is created by a link.
        - Ownership, The user name of the file's owner and the group name of the file.
        - size(-h human readable), 
        - and time of last modification for each file.
* `cd` - Change directory
    - 相对路径: The “.” symbol refers to the working directory and the “..” symbol refers to the working directory’s parent directory. 
    - eg. `cd ..`
    - eg. `cd ./bin` = `cd bin `
    - `cd ~user_name`; Changes the working directory to the home directory of user_name. For example, `cd ~bob` will change the directory to the home directory of user “bob.”
    - `cd -`; Changes the working directory to the previous working directory.
* `file linux_command_line.md`  Determine file type
* ` less /etc/passwd` The less command is a program to view text files. 
    - G: Go to the end of the file.
    - g: Go to the beginning of the file.
    - /pattern: Search forward for the (N-th) matching line where pattern is a regular expression.
     - n: Repeat previous search (for N-th occurrence).
* cp Copy files and directories. 
    - `cp -r source_directory destination_directory` **Recursively** copy directories and their contents. This option (or the -a option) is required when copying directories.
    - `cp -i source destination` - -i option will cause cp to prompt before overwriting an existing destination file. **If this option is not specified, cp will silently overwrite files.** **interactive**
    - `cp -a source_directory destination_directory` -a option will cause cp to preserve all file attributes, including ownerships and permissions, and also preserve any symlinks that might exist. Normally, copies take on the default attributes of the user performing the copy. **archive**
    - '`cp -u source destination` When copying files from one directory to another, only copy files that either don’t exist or are newer than the existing corresponding files in the destination directory. **update**
    - eg. [copy实例](https://billie66.github.io/TLCL/book/chap05.html)
    - cp -r dir1 dir2. dir2存在时，dir1会被复制到dir2下的dir1下。
    - cp dir1/* dir2. dir2存在时，dir1下的文件会被复制到dir2下。

* mv  Move/rename files and directories.
    - `mv file1 file2` - Rename file1 to file2. 与`cp file1 file2`不同的是，`mv`不会保留原文件。
    - `mv file1 file2 directory`
    - `mv directory1 directory2`, directory2存在时，directory1会被复制到directory2下的directory1下。
    - `mv directory1/* directory2`, directory2存在时，directory1下的文件会被复制到directory2下。注意与前者的区别。

* mkdir  Create directories. `mkdir directory...
`
* rm  Remove files and directories
    - `rm -i file` - -i option will cause rm to prompt before removing each file. 
    - `rm -r directory`
    - `rm -f file` - -f option will cause rm to continue even if the file cannot be removed. 
    - Here is a useful tip. Whenever you use wildcards with rm (besides carefully checking your typing!), test the wildcard first with ls. This will let you see the files that will be deleted. Then press the up arrow key to recall the command and replace the ls with rm.
* `ln` Create hard and symbolic links. 
    - `ln doc1 doc1-hardlink` 每一个硬链接都指向一个包含文件内容的索引节点(inode number),  `ls -li`展示的第一串数字就是索引节点，索引节点相同，代表它们指向同一个文件.Hard links cannot reference directories, only files.
    - `ln -s doc1 doc1-symlink` 软链接是一个特殊的文件，它包含了另一个文件的路径名。软链接可以指向目录。
    - One thing to remember about symbolic links is that most file operations are carried out on the link’s target, not the link itself. `rm` is an exception. When you delete a link, it is the link that is deleted, not the target.
* `touch file` - Create an empty file eg. `touch file1 file2 file3`

## 1.3. 命令行通配符
Wildcards can be used with any command that accepts filenames as arguments. 
* `*` - Matches any characters
* `?` - Matches any single character
* `[characters]` - Matches any character that is a member of the set characters.
* `[!characters]` - Matches any character that is not a member of the set characters.
* `[class]` - Matches any character that is a member of the specified class below:
    - `[:alnum:]` - Alphanumeric characters. 匹配任意一个字母或数字
    - `[:alpha:]` - Alphabetic characters. 匹配任意一个字母
    - `[:digit:]` - Numerals. 匹配任意一个数字
    - `[:lower:]` - Lowercase letters. 匹配任意一个小写字母
    - `[:upper:]` - Uppercase letters. 匹配任意一个大写字母
    - `[:space:]` - Space characters (such as space, tab, and formfeed, to name a few). 匹配任意一个空白字符
    - `[:punct:]` - Punctuation characters (such as period, comma, and semicolon, to name a few). 匹配任意一个标点符号
    -  ls [![:digit:]]* - 列出不以数字开头的文件

## 1.4. 查询命令

* `type command` - Display information about command type. eg. `type ls`; `type cp`; `type type`
* `which`  only works for executable programs, not builtins nor aliases that are substitutes for actual executable programs. To determine the exact location of a given executable.
* `help` - bash has a built-in help facility available for each of the **shell builtins**. To use it, type “help” followed by the name of the shell builtin. eg. `help cd`; `help help`
* `--help` - Many **executable programs** support a `--help` option that will display a brief summary of how the command is used, including a list of all available options. 
* `man command` Man pages, however, do not usually include examples, and are intended as a reference, not a tutorial.  `man section command`, 定位到command manual的第五section.
* `apropos keyword` - Search the manual database for strings that contain keyword. eg. `apropos copy`, 输出所有包含"copy"的man page的命令以及队员的section number。
* `whatis command` - Display a very brief description of command. eg. `whatis bash`
* `alias name='command1; command2'` - Create an alias named name for command. eg. `alias name='cd ..;ls'`. 注意，name和=之间不能有空格。
    - `unalias name` - Remove alias named name.
    - 创建别名前，可以用`type name`查看name是否已经被占用。


## 1.5. 查找文件

### locate 依据文件名来查找文件

在基于 Debian 的系统（如 Ubuntu）上，locate 命令包含在 mlocate 包中。你可以使用以下命令来安装它：

`sudo apt-get update; sudo apt-get install mlocate`

locate 数据库由另一个叫做 updatedb 的程序创建。通常，这个程序作为一个定时任务（jobs）周期性运转；也就是说，一个任务 在特定的时间间隔内被 cron 守护进程执行。大多数装有 locate 的系统会每隔一天运行一回 updatedb 程序。因为数据库不能被持续地更新，所以当使用 locate 时，你会发现 目前最新的文件不会出现。为了克服这个问题，安装完成后，你需要运行 updatedb 命令来更新 locate 命令使用的数据库：`sudo updatedb`.

locate 程序会执行一次快速的路径名数据库搜索，并且输出每个与给定子字符串相匹配的路径名。`locate pathname`


* locate -i /bin/*zip - 搜索所有以zip结尾的文件，忽略大小写
* locate zip | grep bin - 搜索所有包含zip,bin的文件

### find 查找文件的复杂方式
`find [path...] [expression]` 在path下搜索，如果path为空，则默认为当前目录。




test测试条件
* `-type d` - 搜索所有目录（directory
* `-type f` - 搜索file
* `-name "*.jpg"` - 搜索*.jpg的文件. 
    - 为什么要有双引号？如果没有双引号，shell会把*.jpg展开为当前目录下所有以.jpg结尾的文件，然后再传递给find命令。如果当前目录下没有以.jpg结尾的文件，那么find命令就会报错。
* `-iname "*.jpg"` 不区分大小写
* `-size +1M`, 搜索超过(+)1M的。`-1M`，小于。`1M`正好1M. 单位有`k`,`M`,`G`etc
* 还有更多的test限制，见manual


操作符
* `-and`, `-or`, `-not` - 逻辑操作符
* `()` - 优先级操作符
* `find ~ \( -type f \and -not -perm 0600 \) -or \( -type d \and -not -perm 0700 \)` - 搜索home目录下，所有不是0600权限的文件，或者不是0700权限的目录。
    - 因为圆括号字符对于 shell 来说有特殊含义，所以在命令行中使用它们的时候，它们必须 用引号引起来，才能作为实参传递给 find 命令。通常反斜杠字符被用来转义圆括号字符。
    - 上例`\and`可以被删除，因它是默认使用的。


执行的操作

* `-print` - 打印出搜索到的文件名
* `-ls` - 打印出搜索到的文件的详细信息，类似于ls -l
* `-delete` - 删除搜索到的文件
* 例如，`find ~ -type f -name '*.BAK' -delete` - 删除home目录下，所有以.BAK结尾的文件. 
* 注意，`find ~ -type f -and -name '*.BAK' -and -print` 与`find ~ -print -and -type f -and -name '*.BAK`的区别。前者只打印出以.BAK结尾的文件，后者打印出所有文件。（-print的位置不同）
* `-exec command {}`， 除了预定义的行为之外，我们也可以调用任意的命令。例如`find ~ -type f -name '*.BAK' -delete`可以改写为`find ~ -type f -name '*.BAK' -exec rm {} \;`。`{}`是一个特殊的字符串，它会被替换为搜索到的文件名。`-exec`选项的最后一个参数必须是一个分号字符，它告诉 find 命令，-exec 选项的参数到此为止了。因为分号字符对于 shell 来说有特殊含义，所以在命令行中使用它们的时候，它们必须用引号引起来，才能作为实参传递给 find 命令。通常反斜杠字符被用来转义分号字符。
    - 注意格式。`-exec command {} ';'`, -exec后有三个参数，command, {}, ';'.
* `-ok command {}` - 与`-exec`类似，但是会询问是否执行该命令。eg. `find ~ -type f -name '*.BAK' -ok rm {} \;`
* `find ~ -type f -name 'foo*' -exec ls -l '{}' +`, 一次性执行多个命令，而不是每个文件执行一次命令。`{}`必须放在`+`之前。
    - `find ~ -type f -name 'foo*' -print | xargs ls -l`的效果等价，用到了xargs命令， xargs 命令会执行一个有趣的函数。它从标准输入接受输入，并把输入转换为一个特定命令的 参数列表。



## 1.6. 压缩和解压缩文件

gzip，无损压缩
* `gzip file` - 压缩文件，生成file.gz文件，原文件被删除。
* `gunzip file.gz` - 解压缩文件，生成file文件，原file.gz文件被删除。
* `gzip -r directory` - 压缩目录下的文件（包括子目录下的文件），在相同位置生成file.gz文件，原文件被删除。
* `gunzip -r directory` - 解压缩目录下的所有文件(不能压缩目录)，生成file文件，原file.gz文件被删除。
* `-c` 把输出写入到标准输出，并且保留原始文件。`gunzip -c foo.txt.gz | less`, 读取压缩文件的内容，不改变压缩文件本身。


`ls -l /etc | gzip > file.gz`中，`ls -l /etc`的标准输出管道到gzip程序压缩，压缩后的输出重定向为file.gz文件中。`gzip`接受标准输入，和`less`类似。



## 1.7 归档（achieve）

归档就是收集许多文件，并把它们 捆绑成一个大文件的过程。

`tar` 是 tape archive 的简称，揭示了它的根源，它是一款制作磁带备份的工具。而它仍然被用来完成传统任务， 它也同样适用于其它的存储设备。我们经常看到扩展名为 .tar 或者 .tgz 的文件，它们各自表示“普通” 的 tar 包和被 gzip 程序压缩过的 tar 包。一个 tar 包可以由一组独立的文件，一个或者多个目录，或者 两者混合体组成。

tar 命令的基本格式如下：
`tar [options] [archive-file] [file or directory to be archived]`

* `tar -cf archive.tar file` - 创建一个名为 archive.tar 的 tar 包，它包含了 foo 文件。选项 -c 告诉 tar 创建一个新的 tar 包。选项 -f 告诉 tar，后面紧跟着的是 tar 包的名字。
* `tar tf archive.tar` - 选项 -t 告诉 tar 列出 tar 包中的文件。
* `tar tvf playground.tar` - 选项 -v 告诉 tar显示每个文件的详细信息。
* `tar xf playground.tar` - 选项 -x 告诉 tar 从 tar 包中提取文件。
* 绝对路径。







## 快捷键

注明：为什么有些快捷键组合在vscode中不起作用？Note: 可能已被GUI占用。Some of the key sequences below (particularly those which use the Alt key) may be intercepted by the GUI for other functions. All of the key sequences should work properly when using a virtual console.

* `Ctrl + a` - 移动光标到行首
* `Ctrl + e` - 移动光标到行尾
* `Ctrl + l` - 清屏，等效于`clear`命令
* 自动补全，`Tab`键. 
* 历史命令，`↑`键. `history`命令查看历史命令列表。该记录保存在`~/.bash_history`文件中。`history`命令可查看。
    - 例如，我们想找历史记录中包含`less`的命令，可用`history | grep less`. 发现第88条命令是所需的，可用`!88`执行该命令。
    - `Ctrl + r` - search the history list incrementally. 再次输入`Ctrl + r`查找下一个；找到后，`ctrl + J`（vscode中右方向键复制有效）到命令行上（但不执行）；按`Enter`键执行该命令；`ctrl + g`退出搜索。




# 重定向

一个程序的输出会流入到几个带编号的文件中。这些文件的前 三个称作标准输入、标准输出和标准错误输出，shell 内部分别将其称为文件描述符 0、1 和 2。默认情况下，标准输入是键盘，标准输出和标准错误输出都是屏幕。重定向就是改变这些默认的文件描述符的目的地。
    
### 重定向输出
* `command > file` - Redirect standard output of command to **file**. If file does not exist, it is created; otherwise, it is overwritten. eg. `ls -l > ls-output.txt`
    - `> ls-output.txt`. Simply using the redirection operator with no command preceding it will truncate an existing file or create a new, empty file.
    - `command 2> file` - Redirect standard error of command to file. eg `ls fdfe 2> error.txt`
* `command >> file` - Append standard output of command to file. 
*  `command &> ls-output.txt` - Redirect both standard output and standard error of command to file.
    - `command >>& file` - Append both standard output and standard error of command to file.
* suppress output. `command > /dev/null`. `/dev/null` is a special device file that is similar to a bottomless pit. Anything sent to this file is discarded.

### 重定向输入

* `command < file` - Redirect standard input to come from file. eg. `sort < mylist.txt` 

### pipeline

* `command1 | command2` - Pipe the output of **command1** to the input of **command2**. eg. `ls -l . | less`; 注意比较与`ls -l . > less`的区别。

# 2. 展开

## 2.1. 通配符展开

`echo *` - 显示当前目录下的所有文件和目录名。展开是由shell完成的，而不是由命令完成的。

## 2.2. 表达式展开 $((expression))

`$((expression))`,eg. `echo $((2+2))`

## 2.3. 花括号展开 {pattern1,pattern2,...}

`echo {001..010}` - 001 002 003 004 005 006 007 008 009 010

`echo front{A,B,C}back` - frontAback frontBback frontCback

`echo {Z..A}` - Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

 `echo a{A{1,2},B{3,4}}b` - aA1b aA2b aB3b aB4b 嵌套结构

 应用实例：
    mkdir Photos;
    cd Photos;
    mkdir {2007..2009}-{01..12};
    ls;


## 2.4. 变量展开 $variable

`printenv | less` - 查看所有环境变量. 可以查找到`USER`变量；`echo $USER` - 查看`USER`变量的值。

## 2.5. 命令展开 $(command)

`ls -l $(which cp)`,  getting the listing of the cp program without having to know its full pathname.

请注意参数和标准输入的区别。`less test.txt`中，test.txt是参数，而不是标准输入。`ls -l . | less`中，是把ls的标准输出作为less的标准输入。

`ls -l $(which cp)`可以写作`which cp | ls -l`吗？不可以！因为`which cp`将标准输出`/bin/cp`传递给后面的命令，但是`ls -l`命令不需要用到这个输出，`ls`命令不需要用到标准输入。它的参数部分空白，因此实际效果是`ls -l` = `which cp | ls -l`.

Up to now, we haven’t encountered any commands that make use of standard input, except for one: `less`.


## 2.6. 双引号 和 单引号 和 转义字符

如果你把文本放在双引号中， shell使用的特殊字符，除了$，\ （反斜杠），和 `（倒引号），其余都失去它们的特殊含义，被当作普通字符来看待。 

`echo "$USER $((2+2)) $(cal)"` 没有被双引号抑制

`echo "{1..5}    多个空格被压缩为一个空格  ~ 波浪线被抑制"`

 `echo $(cal)` 与 `echo "$(cal)"` 的区别. In the first instance, the unquoted command substitution resulted in a command line containing 38 arguments. In the second, it resulted in a command line with one argument that includes the embedded spaces and newlines.

单引号的作用是抑制所有特殊字符的特殊含义，使其成为普通字符。

转义字符：`\` - 使其后的字符失去特殊含义，变成普通字符。eg. `echo "The balance for user $USER is: \$5.00"`

转义字符除了抑制特殊字符的特殊含义，还可以用来表示一些特殊字符。eg. `\n`。`echo -e "Time's up\n"`. `-e`选项告诉echo命令去解释转义字符。



    # 权限

* `id` - Display the user and group names and numeric IDs.
* `chmod`  - Change a file’s mode. eg. `chmod u=rwx,g=rx,o=r myfile`. 可用八进制来改变mode(permission), 6(八进制) = 110 = rw-, 那么，`chmod u=rwx,g=rx,o=r myfile` = `chmod 754 myfile`.前者是符号表示法，后者是八进制表示法。
* `su -l username` - Switch user. eg. `su -l bob`. `-l`选项告诉shell切换到新用户的环境。如果不加`-l`选项，shell会保留当前用户的环境。如果username没有指定，shell会默认为root用户。结束su会话，输入`exit`。
    - `su -l` - Switch to root user.
    - `su -c 'command'` - Execute command as another user. eg. `su -c 'ls -l /root' bob`. `-c`选项告诉shell执行完command后，退出su会话。command用单引号括起来，as we do not want expansion to occur in our shell, but rather in the new shell.
* `sudo`. 
    - su 命令允许你假定为另一个用户的身份，以这个用户的 ID启动一个新的 shell 会话，或者是以这个用户的身份来发布一个命令。sudo 命令允许一个管理员设置一个叫做 /etc/sudoers 的配置文件，并且定义了一些具体命令，允许变身用户执行这些命令。
    - 另一个重要差异是 sudo 命令不要求超级用户的密码。使用 sudo 命令时，用户使用他 / 她自己的密码来认证。
    - sudo 不会重新启动一个 shell，也不会加载另一个用户的 shell 运行环境。这意味者命令不必用单引号引起来。
    - `sudo -i`, 打开sudo的对话。
* `chown [owner][:[group]] file...`, Change a file’s owner and group. eg. `chown bob myfile` - 只改变文件的owner，不改变group。`chown :staff myfile` - 只改变文件的group，不改变owner。`chown bob: myfile` - 改变文件的owner，and changes the group owner to the login group of user bob.
* 创建共享音乐夹的实例。<https://billie66.github.io/TLCL/book/chap10.html>
* `passwd` - Change a user’s password. eg. `passwd bob` - 改变bob的密码(需要有superuser的权限)。`passwd` - 改变当前用户的密码。


# 进程
* `ps` - Report a snapshot of the current processes. 
* `jobs` - List active jobs（列出从我们终端中启动了的任务）. eg. `sleep 100 &` - sleep 100 seconds in the background. 
* `ctrl + Z` 停止stop进程，但不是终止它，该进程被移入后台。
* `ctrl + C` 终止进程。
* `command &` - 让前台的命令在后台执行，Run command in the background. eg. `sleep 100 &` - sleep 100 seconds in the background.
* `fg %jobspec`命令将进程移回前台(foreground前台)。eg. `fg %1` - 将job1移回前台.
* `bg %jobspec`or 让后台停止的命令继续执行。
* 注明：任务在前台总是running的，在后台可以stopped or running。
* `kill %jobspec` - 终止后台的进程。eg. `kill %1` - 终止job1。
* 信号：Signals are one of several
ways that the operating system communicates with programs. We have already seen signals in action with the use of Ctrl-c and Ctrl-z. When the terminal receives one of these keystrokes, it sends a signal to the program in the foreground. In the case of Ctrl-c, a signal called INT (Interrupt) is sent; with Ctrl-z, a signal called TSTP(Terminal Stop.) Programs, in turn, “listen” for signals and may act upon them as they are received. The fact that a program can listen and act upon signals allows a program to do things like save work in progress when it is sent a termination signal.你必须是进程所有者or superuser才能给该进程发送信号。可以通过`kill`指令发送信号，eg `kill -20 1234` - 给进程1234发送TSTP信号, 等价于 给进程1234按下`ctrl + z`。TSTP 终端终止信号由目标进程接收，且可能被忽略，效果是让进程stop，移入后台。


# 环境变量和配置

当我们登录系统后， bash 程序启动，并且会读取一系列称为启动文件的配置脚本， 这些文件定义了默认的可供所有用户共享的 shell 环境。然后是读取更于当前用户自己家目录中 的启动文件，这些启动文件定义了用户个人的 shell 环境。

我们知道了启动文件所在的位置和它们所包含的内容，我们就可以用文本编辑器修改它们来定制自己的 shell 环境。

例如，我们可以编辑 ~/.bashrc 文件，添加一行 `alias ll='ls -l'`，这样我们就可以用 `ll` 命令来代替 `ls -l` 命令了。

我们对于文件 .bashrc 的修改不会生效，直到我们关闭终端会话，再重新启动一个新的会话，因为 .bashrc 文件只是在刚开始启动终端会话时读取。然而，我们可以强迫 bash 重新读取修改过的.bashrc 文件，通过命令：`source ~/.bashrc`。





* `printenv` - Print all or part of environment variables. eg. `printenv | less` - 查看所有环境变量以及其值. 
* 查找某个环境变量的值。
    - `echo $USER` - 查看`USER`变量的值。
    - `printenv USER`.
    - `PATH` 常用的环境变量`PATH`，PATH由冒号分开的目录列表，当你输入可执行程序名后，会搜索这个目录列表。
* `set` The set command, when used without options or arguments, will display both the shell and environment variables, as well as any defined shell functions.
* `alias` - 查看所有别名。eg. `alias | less`



## Vim

`vim filename` - 用vim编辑文件，如果该文件不存在，则创建一个新文件再打开。

vi 是一个模式编辑器。vi 启动后会直接进入 普通模式(normal mode)。这种模式下，可以复制粘贴，删除，移动光标，搜索等等。

为了在文件中添加文本，按下”i” 键进入插入模式。按下”Esc” 键退出插入模式(insert mode)，回到普通模式。

在普通模式下输入`:`，进入命令模式(command mode)。在命令模式下，我们可以输入各种命令，例如保存文件、退出 vi 等等。输入完命令后，按下”Enter” 键执行命令，然后回到普通模式。

在普通模式下，按`v`进入可视模式，可视模式下，可以选择文本，然后按`y`复制，按`d`删除.


### 普通模式下，移动光标
* 字符级：
    - `h` - 左移；
    - `j` - 下移；
    - `k` - 上移； 
    - `l` - 右移。（可用方向键替代） 
    - `4h` - 左移4个字符
* 单词级：
    - `w` - 移动到下一个单词的开头；
    - `b` - 移动到上一个单词的开头。
* 行级：
    - `0` - 移动到行首；
    - `$` - 移动到行尾。
    - `numberG` - 移动到第number行。eg. `10G` or `:10` - 移动到第10行。
    - `G` - 移动到文件最后一行；
    - `gg` or `1G` - 移动到文件开头一行。

* 段落级：
    - `ctrl + u` - 上翻半屏；
    - `ctrl + d` - 下翻半屏；
    - `ctrl + b` - 上翻一屏；
    - `ctrl + f` - 下翻一屏。

* 基于文本对象的移动：
    - `f character` - Move the cursor to the next occurrence of **one** character on the current line. eg. `fa`, `;`继续搜索。注意，`f`命令只能在当前行搜索，不能跨行搜索.
    - `/ pattern` - Search forward for the (N-th) matching line where pattern is a regular expression. `n`继续搜索下一个匹配行。

### 普通模式下，复制粘贴删除（操作后接范围）and else

* `y` - 复制(yank)
    - `yj` - 复制当前行
    - `y4j` - 复制当前行及其下面4行
    - `yw` - 复制光标到当前单词结尾的内容
    - `y$` - 复制光标所在位置到行尾的所有字符
    - `yfr` - 复制光标所在位置到下一个r的所有字符
* `d` - 删除(delete)
    - `dj` - 删除当前行
    - `d4j` - 删除当前行及其下面4行
    - `dw` - 删除光标到当前单词结尾的内容
    - `d$` - 删除光标所在位置到行尾的所有字符
    - `dfr` - 删除光标所在位置到下一个r的所有字符
    - `dG` - 删除光标所在位置到文件末尾的所有字符
    - `d1G` - 删除光标所在位置到文件开头的所有字符
    - 注明：`d`命令不仅删除，还会把删除的内容放入剪贴板，可以用`p`命令粘贴。
* `x` - 删除光标所在位置的字符
* `p` - 粘贴
* `u` - 撤销上一次操作
* `J` - Join the current line with the next line. 
* 替换查找操作，略
* 编辑多个文件,略



### 命令模式
* `:w` - 保存文件
* `:q` - 退出
* `:wq` - 保存并退出,等价于`ZZ`



### b站某大神总结

vim普通模式的理念是：移动和操作

移动：就是光标移动，快速定位光标

操作:操作后接范围，这个范围
* ①以当前光标为起点，以一次移动为终点。
* ②可以以文本对象作为范围。文本对象：官方定义为双引号“”，单引号''，大括号{}小括号【】等里面的内容。文本对象才是能极大提高编辑速度的关键。

我们首先要搞清楚vim可以解决的文件编辑问题:一个文件对于操作系统是最小的单位，对于里面的字符却是最大的单位。

我们可以将整个文件逐级分割来更准确的编辑:屏幕、段落、行、单词、字符。我们的上下左右/hjkl对应的是字符级。e，w，b对应单词级。$，0，f对应行级。{}对应段落级。反正随你怎么分，只要能理解这些都是文本对象就好，文本对象可以确定操作范围。


# shell提示符

`PS1` - shell提示符 “prompt string one”。eg. `PS1='\u@\h:\w\$ '` - 用户名@主机名:当前工作目录`$`结尾。`\u` - 用户名；`\h` - 主机名；`\w` - 当前工作目录；`\$` - $符号。

尝试以下例子：
* `PS1= `  无提示符
* `PS1="\$ "` $符号
* ` PS1="\a\$ "` $符号，且有声音提示. 
* 注：PS1命令接受转义字符和转义序列。



# 包管理系统

Package management systems usually consist of two types of tools: low-level tools which handle tasks such as installing and removing package files, and high-level tools that perform metadata searching and dependency resolution.

注意，以下命令只是支持Dedian风格的发行版。

## 查找包仓库中的软件包(high-level)

`sudo apt-get update; apt-cache search search_string` - 搜索包含search_string的包。
* apt-cache queries and displays available information about installed and installable packages. apt-cache is a low-level tool that is used by Dedian style.
* `sudo apt-get update`这个命令会从你在 /etc/apt/sources.list 文件中定义的源（source）下载最新的软件包信息，包括软件包的版本和依赖关系等。这样，当你使用 apt-get install 命令安装软件包时，APT（Advanced Package Tool）就能知道软件包的最新版本和需要安装的依赖。

## 从包仓库中安装软件包(high-level)

`sudo apt-get update; apt-get install package_name` 上层工具允许从一个包仓库中下载一个软件包，并经过完全依赖解析来安装它。

## 通过软件包文件来安装软件(low-level)

通过软件包文件(.deb)来安装软件
如果从某处而不是从包仓库中下载了一个软件包文件，可以使用底层工具来直接（不经过依赖解析）安装它。

`dpkg --install package_file.deb
`

## 从包仓库中删除软件包(high-level or low-level)

`apt-get remove package_name` (high-level) 

`dpkg --remove package_name` (low-level)

## 经过包仓库来更新软件包(high-level)

`apt-get update; apt-get upgrade` 更新所有已安装的软件包。

## 通过软件包文件来更新软件包(low-level)

dpkg does not have a specific option for upgrading a package versus installing one.

`dpkg --install package_file.deb` - 安装一个新版本的软件包，如果已经安装了旧版本的软件包，那么旧版本的软件包将被新版本的软件包替换。

## 列出所安装的软件包

`dpkg --list` - 列出所有已安装的软件包。

## 软件包信息

`dpkg --status package_name` - 显示软件包的信息。(low-level)
`apt-cache show package_name
` - 显示软件包的信息。(high-level)



# 网络系统

参考资料：
* <https://zhuanlan.zhihu.com/p/420047286>
* 计算机速成课笔记
* [端口科普](https://zhuanlan.zhihu.com/p/225777212)


* `ping baidu.com` ping 命令发送一个特殊的网络数据包，叫做 ICMP ECHO_REQUEST，到 一台指定的主机。大多数接收这个包的网络设备将会回复它，来允许网络连接验证。
    - 注明：网络限制：所有 Azure 虚拟机的入站 ICMP 数据包都被阻止，因此 ping 或 traceroute 命令可能无法工作。这意味着，如果你在 GitHub Actions 的工作流中使用这些命令，可能会看到它们失败或不返回预期的结果。

# 编译源码包

 gcc (GNU C Compiler)

 /src source code

 Most programs build with a simple, two-command sequence:
    
        ./configure 
        make

Since configure is not located where the shell normally expects programs to be located, we must explicitly tell the shell its location by prefixing the command with ./ to indicate that the program is located in the current working directory.

We see configure created several new files in our source directory. The most impor- tant one is Makefile. Makefile is a configuration file that instructs the make program exactly how to build the program. Without it, make will refuse to run. makefile 文件 描述了包括最终完成的程序的各组件之间的关系和依赖性。 

The make program will run, using the contents of Makefile to guide its actions. 

 make 程序:
 * 它保持目标文件是最新的。make 坚持目标文件要新于它们的依赖文件。 (如果目标文件比依赖文件旧，那么 make 将会重新构建它。)
 * make 程序只构建所需要构建的内容.(少什么内容才构建什么内容)


 Well-packaged source code will often include a special make target called install. This target will install the final product in a system directory for use. Usually, this directory is /usr/local/bin, the traditional location for locally built software. However, this directory is not normally writable by ordinary users, so we must become the superuser to perform the installation:
    
            sudo make install



# shell脚本

Shell 有些独特，因为它不仅是一个功能强大的命令行接口,也是一个脚本语言解释器。

            #!/bin/bash
            # This is our first script.
            echo 'Hello World!'

* #!字符序列是一种特殊的结构叫做 shebang。 这个 shebang 被用来告诉操作系统将执行此脚本所用的解释器的名字。每个 shell 脚本都应该把这一文本行 作为它的第一行。
* 需要赋予脚本可执行权限。对于脚本文件，有两个常见的权限设置；权限为755的脚本，则每个人都能执行，和权限为700的 脚本，只有文件所有者能够执行。注意为了能够执行脚本，脚本必须是可读的。`chmod 755 script.sh` - 赋予脚本可执行权限。
* 运行脚本。`./script.sh`
* 查看`$PATH`,将该脚本放置到对应路径下，即可直接运行脚本`script.sh`. 
    - 个人用的脚本： ~/bin 
    - 系统中每个用户都可用的脚本： /usr/local/bin
    - 系统中只有超级用户可用的脚本： /usr/local/sbin
    - In most cases, locally supplied software, whether scripts or compiled programs, should be placed in the `/usr/local` hierarchy and not in /bin or /usr/bin.
    - 若$PATH下不包含相关目录，可以 `locate bashrc`,在对应bashrc文件末尾添加export PATH=~/bin:"$PATH"

