# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests tools.validators.instance_validator.instance_validator"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl.testing import absltest
from validate import handler

_TESTCASE_PATH = os.path.join('.', 'tests', 'fake_instances')

class HandlerTest(absltest.TestCase):

  def testValidateOneBuildingExist(self):
    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD',
                                'good_building_type.yaml')
      args = ['--input', input_file]
      instance_handler = handler.ValidationHelper(args)
      instance_handler.Validate()
    except SyntaxError:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testValidateOneBuildingExistFails(self):
    with self.assertRaises(SyntaxError):
      # there is missing building type in the test file
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'good_links.yaml')
      args = ['--input', input_file]
      instance_handler = handler.ValidationHelper(args)
      instance_handler.Validate()

  def testTelemetryArgsBothSetSuccess(self):
    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD',
                                'good_building_type.yaml')
      args = ['--input', input_file, '--service-account', 'file',
              '--subscription', 'some-subscription']
      handler.ValidationHelper(args)
    except SystemExit:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testTelemetryArgsMissingSubscription(self):
    with self.assertRaises(SystemExit):
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD',
                                'good_building_type.yaml')
      args = ['--input', input_file, '--service-account', 'file']
      handler.ValidationHelper(args)

  def testTelemetryArgsMissingServiceAccount(self):
    with self.assertRaises(SystemExit):
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD',
                                'good_building_type.yaml')
      args = ['--input', input_file, '--subscription', 'some-subscription']
      handler.ValidationHelper(args)


if __name__ == '__main__':
  absltest.main()
