# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


from unittest.mock import patch

from pydolphinscheduler.tasks.shell import Shell


def test_shell_to_dict():
    code = "123"
    name = "test_shell_to_dict"
    command = "echo test shell"
    expect = {
        "code": code,
        "name": name,
        "version": 1,
        "description": None,
        "delayTime": 0,
        "taskType": "SHELL",
        "taskParams": {
            "resourceList": [],
            "localParams": [],
            "rawScript": command,
            "dependence": {},
            "conditionResult": {
                "successNode": [
                    ""
                ],
                "failedNode": [
                    ""
                ]
            },
            "waitStartTimeout": {}
        },
        "flag": "YES",
        "taskPriority": "MEDIUM",
        "workerGroup": "worker-group-pydolphin",
        "failRetryTimes": 0,
        "failRetryInterval": 1,
        "timeoutFlag": "CLOSE",
        "timeoutNotifyStrategy": None,
        "timeout": 0
    }
    with patch('pydolphinscheduler.core.task.Task.gen_code', return_value=code):
        shell = Shell(name, command)
        assert shell.to_dict() == expect
