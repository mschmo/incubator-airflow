# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from mock import MagicMock

from airflow.contrib.operators.mysql_to_gcs import \
    MySqlToGoogleCloudStorageOperator


class MySqlToGoogleCloudStorageOperatorTest(unittest.TestCase):

    def test_write_local_data_files(self):

        # Configure
        task_id = "some_test_id"
        sql = "some_sql"
        bucket = "some_bucket"
        filename = "some_filename"
        schema = "some_schema"
        description_list = [['col_integer'], ['col_byte']]
        row_iter = [[1, b'byte_str_1'], [2, b'byte_str_2']]

        op = MySqlToGoogleCloudStorageOperator(
            task_id=task_id,
            sql=sql,
            bucket=bucket,
            filename=filename,
            schema=schema)

        cursor_mock = MagicMock()
        cursor_mock.description = description_list
        cursor_mock.__iter__.return_value = row_iter

        # Run
        op._write_local_data_files(cursor_mock)
