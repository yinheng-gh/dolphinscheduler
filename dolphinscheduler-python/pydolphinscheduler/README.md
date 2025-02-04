<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

# pydolphinscheduler

pydolphinscheduler is python API for Apache DolphinScheduler, which allow you definition
your workflow by python code, aka workflow-as-codes.

## Quick Start

> **_Notice:_** For now, due to pydolphinscheduler without release to any binary tarball or [PyPI][pypi], you 
> have to clone Apache DolphinScheduler code from GitHub to ensure quick start setup

Here we show you how to install and run a simple example of pydolphinscheduler

### Prepare

```shell
# Clone code from github
git clone git@github.com:apache/dolphinscheduler.git

# Install pydolphinscheduler from source
cd dolphinscheduler-python/pydolphinscheduler
pip setup.py install
```

### Start Server And Run Example

Before you run an example, you have to start backend server. You could follow [development setup][dev-setup]
section "DolphinScheduler Standalone Quick Start" to set up developer environment. You have to start backend
and frontend server in this step, which mean that you could view DolphinScheduler UI in your browser with URL
http://localhost:12345/dolphinscheduler

After backend server is being start, all requests from `pydolphinscheduler` would be sends to backend server.
And for now we could run a simple example by:

```shell
cd dolphinscheduler-python/pydolphinscheduler
python example/tutorial.py
```

> **_NOTICE:_** Since Apache DolphinScheduler's tenant is requests while running command, you might need to change
> tenant value in `example/tutorial.py`. For now the value is `tenant_exists`, please change it to username exists
> in you environment. 

After command execute, you could see a new project with single process definition named *tutorial* in the [UI][ui-project].

Until now, we finish quick start by an example of pydolphinscheduler and run it. If you want to inspect or join
pydolphinscheduler develop, you could take a look at [develop](#develop)

## Develop

pydolphinscheduler is python API for Apache DolphinScheduler, it just defines what workflow look like instead of
store or execute it. We here use [py4j][py4j] to dynamically access Java Virtual Machine.

### Setup Develop Environment

We already clone the code in [quick start](#quick-start), so next step we have to open pydolphinscheduler project
in you editor. We recommend you use [pycharm][pycharm] instead of [IntelliJ IDEA][idea] to open it. And you could
just open directory `dolphinscheduler-python/pydolphinscheduler` instead of `dolphinscheduler-python`.

### Brief Concept

Apache DolphinScheduler is design to define workflow by UI, and pydolphinscheduler try to define it by code. When
define by code, user usually do not care user, tanant, or queue exists or not. All user care about is create
a new workflow by the code his/her definition. So we have some **side object** in `pydolphinscheduler/side`
directory, their only check object exists or not, and create them if not exists. 

#### Process Definition

pydolphinscheduler workflow object name, process definition is also same name as Java object(maybe would be change to
other word for more simple).

#### Tasks

pydolphinscheduler tasks object, we use tasks to define exact job we want DolphinScheduler do for us. For now,
we only support `shell` task to execute shell task. [This link][all-task] list all tasks support in DolphinScheduler
and would be implement in the further.


[pypi]: https://pypi.org/
[dev-setup]: https://dolphinscheduler.apache.org/en-us/development/development-environment-setup.html
[ui-project]: http://8.142.34.29:12345/dolphinscheduler/ui/#/projects/list
[py4j]: https://www.py4j.org/index.html
[pycharm]: https://www.jetbrains.com/pycharm
[idea]: https://www.jetbrains.com/idea/
[all-task]: https://dolphinscheduler.apache.org/en-us/docs/dev/user_doc/guide/task/shell.html
